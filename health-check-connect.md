---
layout: layout.njk
title: "Connect Your Books"
eyebrow: "Bookkeeping Health Check · Next step"
heroTitle: "Payment done. Now let's securely connect your"
heroTitleEm: "books"
heroLead: "Thank you for booking your Bookkeeping Health Check. Please use your accounting software's own invitation process to give The Bookkeepers Solution access. Never email or message us your password."
description: "Secure next steps for connecting Xero, MYOB or QuickBooks for your Bookkeeping Health Check."
permalink: /health-check-connect/
hideCTA: true
---

<div class="hc-hero-cta reveal">
  <p class="hc-assurance"><strong>Important:</strong> Never send us your Xero, MYOB or QuickBooks password.</p>
</div>

## Choose your accounting software

<div class="hc-checks-grid reveal">
  <div class="hc-check-card">
    <span class="hc-check-num">X</span>
    <h3>Xero</h3>
    <p>Open your organisation's user settings and use Xero's invitation process to add The Bookkeepers Solution. We will confirm the exact email address and access level required for the review.</p>
  </div>
  <div class="hc-check-card">
    <span class="hc-check-num">M</span>
    <h3>MYOB</h3>
    <p>Use MYOB's user-management or adviser invitation process rather than sharing your login. We will confirm the exact email address and permissions required for your file.</p>
  </div>
  <div class="hc-check-card">
    <span class="hc-check-num">Q</span>
    <h3>QuickBooks</h3>
    <p>Use QuickBooks' accountant or user invitation process to grant access. We will confirm the exact email address and access level required for the Health Check.</p>
  </div>
</div>

## What happens next

<div class="hc-deliverables reveal">
  <div class="hc-del-card"><h3>1. We confirm your booking</h3><p>We'll match your payment with the details you supplied at checkout.</p></div>
  <div class="hc-del-card"><h3>2. You grant access securely</h3><p>We'll confirm the invitation details for your accounting platform. You remain in control of your file and can remove access afterwards.</p></div>
  <div class="hc-del-card"><h3>3. We review the file</h3><p>We'll work through the Health Check areas and flag what looks healthy, what needs watching and what needs attention.</p></div>
  <div class="hc-del-card"><h3>4. You receive your report</h3><p>You'll receive practical findings and recommendations. Any clean-up or ongoing bookkeeping work is completely optional and quoted separately.</p></div>
</div>

## Tell us when you're ready

<p>Complete this short step so we can match your access invitation to your payment and start the right file. Your email address is used for your Health Check service. Marketing updates are optional.</p>

<form name="health-check-onboarding" method="POST" data-netlify="true" netlify-honeypot="company-website" action="/health-check-connect/?submitted=true" class="contact-form reveal">
  <input type="hidden" name="form-name" value="health-check-onboarding">
  <input type="hidden" name="checkout_session_id" id="checkout-session-id" value="">
  <p style="display:none;">
    <label>Leave this field empty: <input name="company-website"></label>
  </p>

  <div class="form-field">
    <label for="hc-name">Your name</label>
    <input id="hc-name" name="name" type="text" autocomplete="name" required>
  </div>

  <div class="form-field">
    <label for="hc-business">Business name</label>
    <input id="hc-business" name="business" type="text" autocomplete="organization" required>
  </div>

  <div class="form-field">
    <label for="hc-email">Email used at checkout</label>
    <input id="hc-email" name="email" type="email" autocomplete="email" required>
  </div>

  <div class="form-field">
    <label for="hc-software">Accounting software</label>
    <select id="hc-software" name="software" required>
      <option value="">Choose one</option>
      <option value="Xero">Xero</option>
      <option value="MYOB">MYOB</option>
      <option value="QuickBooks">QuickBooks</option>
      <option value="Other">Other</option>
    </select>
  </div>

  <div class="form-field">
    <label for="hc-access">Access status</label>
    <select id="hc-access" name="access_status" required>
      <option value="">Choose one</option>
      <option value="Need invitation details">I need the invitation details first</option>
      <option value="Invitation sent">I've sent the access invitation</option>
      <option value="Need help">I need help connecting my file</option>
    </select>
  </div>

  <div class="form-field">
    <label style="display:flex; gap:.65rem; align-items:flex-start; font-weight:400;">
      <input type="checkbox" name="marketing_opt_in" value="yes" style="width:auto; margin-top:.3rem;">
      <span>Yes, I'd also like occasional bookkeeping tips, updates and offers from The Bookkeepers Solution. I can unsubscribe at any time.</span>
    </label>
  </div>

  <button type="submit" class="btn btn-primary btn-lg">Finish my Health Check setup</button>
</form>

<script>
(function () {
  var params = new URLSearchParams(window.location.search);
  var sessionId = params.get('session_id');
  var field = document.getElementById('checkout-session-id');
  if (sessionId && field) field.value = sessionId;
})();
</script>

## Before granting access

Please make sure the organisation or company file you invite us to is the **correct business file**. If you have more than one entity, wait for our confirmation before granting access so we review the right one.

This Health Check is a focused, high-level bookkeeping review. It is not an audit, assurance engagement, tax advice or financial advice, and it cannot guarantee every error or compliance issue will be identified.

<div class="hc-final-cta reveal">
  <h2 style="border:none; padding:0; margin:0 0 0.5rem;">You're booked in.</h2>
  <p>Keep an eye on your email for the secure access details and next steps from The Bookkeepers Solution.</p>
  <a href="/" class="btn btn-white btn-lg">Back to The Bookkeepers Solution</a>
</div>
