# Monday.com Morning Prioritizer — Setup

## What it does
Runs each morning to pull every open item assigned to you from a Monday.com
board, ranks them by **priority label + due date**, prints a numbered list,
and (optionally) writes the rank number back to a column on the board.

## Requirements
- Python 3.10+ (no extra packages needed — uses only stdlib)
- A Monday.com API token

## One-time setup

### 1. Get your API token
Monday.com → click your avatar → **Developers** → **My Access Tokens** →
copy the token.

### 2. Find your Board ID
Open the board in a browser. The URL looks like:
`https://yourcompany.monday.com/boards/1234567890`
The number at the end is the Board ID.

### 3. Create a `.env` file (keep it out of git)
```
MONDAY_API_KEY=your_token_here
MONDAY_BOARD_ID=1234567890
MONDAY_USER_NAME=Heidi          # partial match, case-insensitive
```

Load it before running:
```bash
export $(cat .env | xargs)
```

### 4. (Optional) Write ranks back to the board
Add a **Numbers** column to your board (e.g. "Priority Order"), then set:
```
MONDAY_ORDER_COLUMN_ID=numbers   # replace with the actual column ID
```
To find a column's ID: open the board → click the column menu (⋮) →
**Column settings** → the ID is shown at the bottom.

### 5. (Optional) Dry-run mode
```
MONDAY_DRY_RUN=true
```
Prints the ranked list without touching the board.

## Running manually
```bash
python scripts/monday_prioritize.py
```

## Scheduling it every morning (Mac/Linux)
```bash
crontab -e
```
Add a line (runs at 8 AM Mon–Fri):
```
0 8 * * 1-5 cd /path/to/project && export $(cat .env | xargs) && python scripts/monday_prioritize.py >> ~/monday_log.txt 2>&1
```

## Priority column labels
The script maps these labels to sort weights (lower = do first):

| Label    | Weight |
|----------|--------|
| Critical | 0      |
| High     | 1      |
| Medium   | 2      |
| Low      | 3      |
| (blank)  | 4      |

Within the same priority level, items are sorted by due date (soonest first).
