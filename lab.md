---
layout: layout.njk
title: "The Bookkeepers Lab"
eyebrow: "Innovation hub"
heroTitle: "The Bookkeepers"
heroTitleEm: "Lab"
heroLead: "Where we experiment, build and share. AI tools, automation ideas, business tips and practical resources — all tested in our own practice before we recommend them to yours."
description: "The Bookkeepers Lab — AI experiments, automation ideas, free resources and practical tools from The Bookkeepers Solution. Innovation for small business bookkeeping."
permalink: /lab/
---

<div class="lab-intro reveal">
  <p>Most bookkeeping firms do the work and send the invoice. We do that too — but we also spend time figuring out how to do it <strong>better</strong>. The Bookkeepers Lab is where we share what we learn: the tools we're testing, the automations we're building, and the ideas that actually work for small business.</p>
</div>

<div class="lab-grid reveal">

  <div class="lab-card">
    <div class="lab-card-badge">AI</div>
    <div class="lab-card-icon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a4 4 0 0 1 4 4v2a4 4 0 0 1-8 0V6a4 4 0 0 1 4-4z"/><path d="M16 14a4 4 0 0 1 4 4v2H4v-2a4 4 0 0 1 4-4"/><circle cx="12" cy="6" r="2"/></svg>
    </div>
    <h3>AI for Small Business</h3>
    <p>We test AI tools so you don't have to. Practical guides on using AI for invoicing, receipt capture, cashflow forecasting and client communication — written for real business owners, not tech people.</p>
  </div>

  <div class="lab-card">
    <div class="lab-card-badge">Tools</div>
    <div class="lab-card-icon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
    </div>
    <h3>Practical Tools</h3>
    <p>Spreadsheets, templates and checklists built from our own workflows. Every tool in the <a href="/shop/">shop</a> started life here — tested on real clients before we packaged it up.</p>
  </div>

  <div class="lab-card">
    <div class="lab-card-badge">Automation</div>
    <div class="lab-card-icon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
    </div>
    <h3>Automation Ideas</h3>
    <p>How we connect Xero, Dext, bank feeds and reporting tools to eliminate manual work. Step-by-step walkthroughs you can replicate in your own business.</p>
  </div>

  <div class="lab-card">
    <div class="lab-card-badge">Tips</div>
    <div class="lab-card-icon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
    </div>
    <h3>Business Tips</h3>
    <p>Short, actionable advice on cashflow, compliance, pricing and growth — from a bookkeeper who works with small businesses every day, not a textbook.</p>
  </div>

  <div class="lab-card">
    <div class="lab-card-badge">Updates</div>
    <div class="lab-card-icon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
    </div>
    <h3>Product Updates</h3>
    <p>What we're building, what we've shipped, and what's coming next. Follow along as we develop tools like Receivables Rescue and the Bookkeepers Vault.</p>
  </div>

  <div class="lab-card">
    <div class="lab-card-badge">Free</div>
    <div class="lab-card-icon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
    </div>
    <h3>Free Resources</h3>
    <p>Not everything has a price tag. Free checklists, guides and downloads to help you run a tighter business — no email required for most of them.</p>
  </div>

</div>

## Coming soon

We're just getting started. The Lab will grow with regular posts, tool reviews, downloadable resources and behind-the-scenes content. Want to know when something new drops?

<div class="lab-cta reveal">
  <a href="/#newsletter" class="btn btn-primary">Join the newsletter</a>
  <a href="/shop/" class="btn btn-outline">Browse the shop</a>
</div>

<style>
.lab-intro {
  max-width: 720px;
  margin: 0 auto 3rem;
  text-align: center;
  font-size: 1.05rem;
}
.lab-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0 3rem;
}
.lab-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 2rem;
  box-shadow: var(--shadow-sm);
  transition: transform 0.25s, box-shadow 0.25s;
  position: relative;
}
.lab-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }
.lab-card-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(43,123,217,0.1);
  color: var(--color-primary);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.3rem 0.65rem;
  border-radius: 6px;
}
.lab-card-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: rgba(43,123,217,0.12);
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
}
.lab-card h3 { font-family: 'Playfair Display', serif; margin: 0 0 0.75rem; font-size: 1.1rem; }
.lab-card p { margin: 0; font-size: 0.95rem; color: var(--color-text-muted); }
.lab-cta { display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap; margin: 2rem 0; }
</style>
