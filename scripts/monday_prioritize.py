#!/usr/bin/env python3
"""
Monday.com Morning Workload Prioritizer
Run this each morning to fetch and rank open items by due date,
priority column, and status, then write the ranked order back
to a "Priority Order" number column on the board.

Usage:
    python monday_prioritize.py

Required env vars (set once in a .env file or your shell profile):
    MONDAY_API_KEY   – your Monday.com API v2 token
    MONDAY_BOARD_ID  – numeric ID of the board to prioritize
    MONDAY_USER_NAME – name (or partial name) of the person whose
                       items to filter; leave blank to include all items

Optional env vars:
    MONDAY_DRY_RUN   – set to "true" to print the ranked list without
                       writing anything back to Monday.com
    MONDAY_PRIORITY_COLUMN_ID – ID of the column that holds the text
                       priority label (e.g. "priority4" or "status").
                       Defaults to "priority".
    MONDAY_ORDER_COLUMN_ID    – ID of a Number column where the script
                       writes the computed rank (1 = do first).
                       Leave blank to skip writing back.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, date

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_KEY = os.environ.get("MONDAY_API_KEY", "")
BOARD_ID = os.environ.get("MONDAY_BOARD_ID", "")
USER_NAME_FILTER = os.environ.get("MONDAY_USER_NAME", "").strip().lower()
DRY_RUN = os.environ.get("MONDAY_DRY_RUN", "false").lower() == "true"
PRIORITY_COL = os.environ.get("MONDAY_PRIORITY_COLUMN_ID", "priority")
ORDER_COL = os.environ.get("MONDAY_ORDER_COLUMN_ID", "")

API_URL = "https://api.monday.com/v2"

# Priority label → sort weight (lower = more urgent)
PRIORITY_WEIGHTS = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
    "": 4,
}

# Status labels that mean "done" – these are skipped
DONE_STATUSES = {"done", "complete", "completed", "closed", "cancelled", "canceled"}


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------
def gql(query: str, variables: dict | None = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": API_KEY,
            "API-Version": "2024-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        sys.exit(f"Monday.com API error {exc.code}: {exc.read().decode()}")
    if "errors" in body:
        sys.exit(f"GraphQL error: {body['errors']}")
    return body["data"]


def fetch_items(board_id: str) -> list[dict]:
    """Fetch all non-done items from a board (handles pagination)."""
    items = []
    cursor = None

    query = """
    query($board: ID!, $cursor: String) {
      boards(ids: [$board]) {
        items_page(limit: 100, cursor: $cursor) {
          cursor
          items {
            id
            name
            state
            column_values {
              id
              text
              value
            }
          }
        }
      }
    }
    """

    while True:
        data = gql(query, {"board": board_id, "cursor": cursor})
        page = data["boards"][0]["items_page"]
        items.extend(page["items"])
        cursor = page.get("cursor")
        if not cursor:
            break

    return items


def update_number_column(board_id: str, item_id: str, col_id: str, value: int):
    mutation = """
    mutation($board: ID!, $item: ID!, $col: String!, $val: JSON!) {
      change_column_value(board_id: $board, item_id: $item,
                          column_id: $col, value: $val) { id }
    }
    """
    gql(mutation, {
        "board": board_id,
        "item": item_id,
        "col": col_id,
        "val": json.dumps(value),
    })


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------
def parse_date(text: str) -> date | None:
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(text.strip(), fmt).date()
        except ValueError:
            continue
    return None


def score_item(item: dict) -> tuple:
    """Return a sort key (priority_weight, days_until_due, name)."""
    col_map = {cv["id"]: cv["text"].strip().lower() for cv in item["column_values"]}

    # Priority weight
    priority_label = col_map.get(PRIORITY_COL, "")
    weight = PRIORITY_WEIGHTS.get(priority_label, PRIORITY_WEIGHTS[""])

    # Due date distance (None → pushed to the end)
    due_text = col_map.get("date", "") or col_map.get("due_date", "") or col_map.get("timeline", "")
    due = parse_date(due_text) if due_text else None
    today = date.today()
    days_out = (due - today).days if due else 9999

    return (weight, days_out, item["name"].lower())


def is_done(item: dict) -> bool:
    if item.get("state", "").lower() == "done":
        return True
    for cv in item["column_values"]:
        if cv["id"] == "status" and cv["text"].strip().lower() in DONE_STATUSES:
            return True
    return False


def matches_user(item: dict) -> bool:
    if not USER_NAME_FILTER:
        return True
    for cv in item["column_values"]:
        if cv["id"] in ("person", "people", "assignee", "owner"):
            if USER_NAME_FILTER in cv["text"].strip().lower():
                return True
    return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    if not API_KEY:
        sys.exit("ERROR: MONDAY_API_KEY is not set.")
    if not BOARD_ID:
        sys.exit("ERROR: MONDAY_BOARD_ID is not set.")

    today_str = datetime.now(timezone.utc).strftime("%A, %B %-d %Y")
    print(f"\n{'='*60}")
    print(f"  Monday.com Workload Prioritization  —  {today_str}")
    print(f"{'='*60}\n")

    print("Fetching items from board…")
    all_items = fetch_items(BOARD_ID)
    print(f"  Found {len(all_items)} total items.")

    # Filter
    open_items = [i for i in all_items if not is_done(i) and matches_user(i)]
    print(f"  {len(open_items)} open item(s) assigned to "
          f"{'anyone' if not USER_NAME_FILTER else USER_NAME_FILTER}.\n")

    if not open_items:
        print("Nothing to do — enjoy your morning! ☕")
        return

    # Sort
    open_items.sort(key=score_item)

    # Display
    print(f"{'Rank':<5} {'Priority':<10} {'Due':<12} {'Item'}")
    print("-" * 60)
    for rank, item in enumerate(open_items, start=1):
        col_map = {cv["id"]: cv["text"].strip() for cv in item["column_values"]}
        priority = col_map.get(PRIORITY_COL, "-") or "-"
        due = (col_map.get("date") or col_map.get("due_date")
               or col_map.get("timeline") or "-")
        print(f"  {rank:<3} {priority:<10} {due:<12} {item['name']}")

    # Write back
    if ORDER_COL and not DRY_RUN:
        print(f"\nWriting rank to column '{ORDER_COL}'…")
        for rank, item in enumerate(open_items, start=1):
            update_number_column(BOARD_ID, item["id"], ORDER_COL, rank)
            print(f"  #{rank} → {item['name'][:50]}")
        print("Done! Board updated.")
    elif DRY_RUN:
        print("\n[DRY RUN] Board not updated.")
    else:
        print("\nTip: set MONDAY_ORDER_COLUMN_ID to auto-write ranks back to the board.")

    print()


if __name__ == "__main__":
    main()
