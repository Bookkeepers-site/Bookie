---
layout: layout.njk
title: "Contact"
eyebrow: "Get in touch"
heroTitle: "Let's have a"
heroTitleEm: "chat"
heroLead: "Ready to talk to a real bookkeeper? We'd love to hear from you — there's no obligation and no jargon."
description: "Get in touch with The Bookkeepers Solution. Phone, email, or use our contact form — serving Perth's Northern Suburbs and Australia-wide remotely."
permalink: /contact/
hideCTA: true
---

<div class="contact-grid reveal">

  <div class="contact-cards">
    <div class="contact-card">
      <div class="contact-card-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 1h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 8.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      </div>
      <div>
        <div class="contact-card-label">Phone</div>
        <div class="contact-card-value"><a href="tel:+61419143150">+61 419 143 150</a></div>
      </div>
    </div>

    <div class="contact-card">
      <div class="contact-card-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
      </div>
      <div>
        <div class="contact-card-label">Email</div>
        <div class="contact-card-value"><a href="mailto:admin@thebookkeeperssolution.com">admin@thebookkeeperssolution.com</a></div>
      </div>
    </div>

    <div class="contact-card">
      <div class="contact-card-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
      </div>
      <div>
        <div class="contact-card-label">Service Area</div>
        <div class="contact-card-value">Perth Northern Suburbs, Bindoon &amp; Chittering Valley — and Australia-wide remotely</div>
      </div>
    </div>

    <div class="contact-card">
      <div class="contact-card-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
      </div>
      <div>
        <div class="contact-card-label">Hours</div>
        <div class="contact-card-value">Monday – Friday, 8:30am – 5:00pm AWST</div>
      </div>
    </div>
  </div>

  <div class="contact-form-card">
    <h3>Send us a message</h3>
    <p>Fill in the form and we'll get back to you within one business day.</p>
    <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="styled-form" action="/thanks.html">
      <input type="hidden" name="form-name" value="contact" />
      <p style="display:none;"><label>Don't fill this out: <input name="bot-field" /></label></p>
      <label>
        Your name
        <input type="text" name="name" required autocomplete="name" placeholder="Jane Smith" />
      </label>
      <label>
        Email address
        <input type="email" name="email" required autocomplete="email" placeholder="you@business.com.au" />
      </label>
      <label>
        Phone (optional)
        <input type="tel" name="phone" autocomplete="tel" placeholder="+61 4xx xxx xxx" />
      </label>
      <label>
        What can we help with?
        <select name="topic">
          <option>General enquiry</option>
          <option>New client — day-to-day bookkeeping</option>
          <option>Payroll support</option>
          <option>BAS &amp; GST reporting</option>
          <option>Software setup / training</option>
          <option>Strategic advisory</option>
        </select>
      </label>
      <label>
        Message
        <textarea name="message" rows="5" required placeholder="Tell us a bit about your business and what you're after…"></textarea>
      </label>
      <button type="submit" class="btn btn-primary">Send message</button>
    </form>
  </div>

</div>
