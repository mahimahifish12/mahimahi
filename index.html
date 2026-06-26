"""
1-on-1 Code Lessons — Signup App
Run:  pip install flask
      python app.py
Then open: http://localhost:5000
"""

import json
import os
import re
from datetime import datetime
from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "change-this-to-something-secret"

SIGNUPS_FILE = "signups.json"

# ── Helpers ───────────────────────────────────────────────────────────────────

def load_signups():
    if not os.path.exists(SIGNUPS_FILE):
        return {}
    with open(SIGNUPS_FILE) as f:
        return json.load(f)

def save_signup(name, email):
    signups = load_signups()
    signups[email.lower()] = {
        "name":  name,
        "email": email,
        "date":  datetime.utcnow().isoformat()
    }
    with open(SIGNUPS_FILE, "w") as f:
        json.dump(signups, f, indent=2)

def already_signed_up():
    """Check if the current browser session has already signed up."""
    email = session.get("signed_up_email")
    if not email:
        return None
    signups = load_signups()
    return signups.get(email.lower())

def valid_email(email):
    return bool(re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email))

# ── Shared CSS ────────────────────────────────────────────────────────────────

BASE_STYLE = """
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --bg:      #0f1117;
    --surface: #1a1d27;
    --card:    #22263a;
    --accent:  #6c63ff;
    --accent2: #a78bfa;
    --text:    #e8eaf0;
    --muted:   #8b90a7;
    --success: #34d399;
    --error:   #f87171;
    --border:  #2e3250;
  }
  body {
    font-family: 'Segoe UI', system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
  }
  a { color: var(--accent2); text-decoration: none; }

  /* ── Landing ── */
  .hero {
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 80px 24px 60px; text-align: center;
    position: relative; overflow: hidden;
  }
  .hero::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% -10%, rgba(108,99,255,0.22), transparent);
    pointer-events: none;
  }
  .badge {
    display: inline-block;
    background: rgba(108,99,255,0.15);
    border: 1px solid rgba(108,99,255,0.4);
    color: var(--accent2); font-size: 12px; font-weight: 700;
    letter-spacing: 1.2px; text-transform: uppercase;
    padding: 6px 18px; border-radius: 999px; margin-bottom: 28px;
  }
  .hero h1 {
    font-size: clamp(2rem, 5vw, 3.4rem); font-weight: 800;
    line-height: 1.15; max-width: 700px; margin-bottom: 24px;
    background: linear-gradient(135deg, #fff 40%, var(--accent2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .hero-pitch {
    font-size: clamp(1rem, 1.8vw, 1.15rem); color: var(--muted);
    max-width: 620px; line-height: 1.9; margin-bottom: 52px;
  }
  .hero-pitch strong { color: var(--text); }
  .features {
    display: flex; flex-wrap: wrap; gap: 16px;
    justify-content: center; max-width: 740px; margin-bottom: 64px;
  }
  .feature-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 14px; padding: 22px 24px; width: 210px; text-align: left;
  }
  .feature-card .icon { font-size: 26px; margin-bottom: 10px; }
  .feature-card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
  .feature-card p  { font-size: 13px; color: var(--muted); line-height: 1.6; }
  .scroll-hint {
    display: flex; flex-direction: column; align-items: center;
    gap: 8px; color: var(--muted); font-size: 13px;
    animation: bob 2s ease-in-out infinite;
  }
  @keyframes bob {
    0%, 100% { transform: translateY(0); }
    50%       { transform: translateY(7px); }
  }
  .cta-section {
    padding: 80px 24px; display: flex; flex-direction: column;
    align-items: center; text-align: center;
    border-top: 1px solid var(--border); background: var(--surface);
  }
  .cta-section h2 { font-size: clamp(1.4rem, 3vw, 2rem); font-weight: 700; margin-bottom: 12px; }
  .cta-section p  { color: var(--muted); max-width: 460px; margin-bottom: 32px; font-size: 15px; line-height: 1.7; }

  /* ── Step cards ── */
  .step-page {
    min-height: 100vh; display: flex;
    align-items: center; justify-content: center;
    padding: 24px; position: relative;
  }
  .step-page::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(ellipse 60% 40% at 50% 0%, rgba(108,99,255,0.1), transparent);
    pointer-events: none;
  }
  .step-card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 20px; padding: 48px 40px;
    width: 100%; max-width: 460px; position: relative;
  }
  .progress-dots { display: flex; gap: 6px; margin-bottom: 32px; }
  .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--border); }
  .dot.active { background: var(--accent); transform: scale(1.3); }
  .dot.done   { background: var(--success); }
  .step-num {
    display: inline-flex; align-items: center; justify-content: center;
    width: 36px; height: 36px;
    background: rgba(108,99,255,0.15); border: 1px solid rgba(108,99,255,0.35);
    border-radius: 50%; font-size: 14px; font-weight: 700;
    color: var(--accent2); margin-bottom: 20px;
  }
  .step-card h2 { font-size: 1.55rem; font-weight: 800; margin-bottom: 8px; }
  .step-card .sub { color: var(--muted); font-size: 14px; line-height: 1.65; margin-bottom: 32px; }
  .form-group { margin-bottom: 20px; }
  .form-group label {
    display: block; font-size: 12px; font-weight: 700;
    color: var(--muted); text-transform: uppercase;
    letter-spacing: 0.6px; margin-bottom: 8px;
  }
  .form-group input {
    width: 100%; padding: 14px 16px;
    background: var(--card); border: 1.5px solid var(--border);
    border-radius: 10px; color: var(--text); font-size: 15px; outline: none;
  }
  .form-group input.error { border-color: var(--error); }
  .err-msg { color: var(--error); font-size: 13px; margin-top: 6px; }

  /* ── Buttons ── */
  .btn {
    display: inline-flex; align-items: center; justify-content: center;
    gap: 8px; padding: 14px 28px; border-radius: 12px;
    font-size: 15px; font-weight: 700; cursor: pointer;
    border: none; width: 100%; margin-top: 8px; text-decoration: none;
  }
  .btn-primary { background: var(--accent); color: #fff; }
  .btn-ghost {
    background: transparent; color: var(--muted);
    border: 1.5px solid var(--border); margin-top: 12px;
  }

  /* ── Success / already ── */
  .success-icon {
    width: 72px; height: 72px;
    background: rgba(52,211,153,0.1); border: 2px solid var(--success);
    border-radius: 50%; display: flex; align-items: center;
    justify-content: center; font-size: 30px; margin: 0 auto 24px;
  }
  .info-box {
    background: rgba(108,99,255,0.08); border: 1px solid rgba(108,99,255,0.25);
    border-radius: 10px; padding: 14px 16px;
    font-size: 14px; color: var(--muted); line-height: 1.65; margin-top: 20px;
  }
  .info-box strong { color: var(--text); }
</style>
"""

# ── Templates ─────────────────────────────────────────────────────────────────

LANDING_HTML = BASE_STYLE + """
<section class="hero">
  <div class="badge">🎓 Limited Spots Available</div>
  <h1>Learn to Code with a Personal Mentor, Not a Video</h1>
  <p class="hero-pitch">
    Most people trying to learn to code get stuck watching tutorials they barely follow,
    copying code they don't understand, and quitting before they ever build anything real.
    <br><br>
    <strong>That ends here.</strong> In a 1-on-1 lesson you get a real person who looks
    at <em>your</em> code, answers <em>your</em> questions, and teaches at <em>your</em> pace.
    No pre-recorded fluff — just focused, personal teaching that gets you from confused to confident, fast.
    <br><br>
    Whether you're a complete beginner or someone stuck at the same level for months,
    a single session will move you further than weeks of solo grinding.
  </p>
  <div class="features">
    <div class="feature-card">
      <div class="icon">🎯</div>
      <h3>Tailored to You</h3>
      <p>Lessons built around your goals, your level, and your learning style.</p>
    </div>
    <div class="feature-card">
      <div class="icon">💬</div>
      <h3>Ask Anything</h3>
      <p>No dumb questions. Real answers in real time from a real person.</p>
    </div>
    <div class="feature-card">
      <div class="icon">⚡</div>
      <h3>Learn Faster</h3>
      <p>Progress faster than self-teaching with direct expert feedback.</p>
    </div>
  </div>
  <div class="scroll-hint">
    <span>Scroll down to sign up</span>
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M12 5v14M5 12l7 7 7-7"/>
    </svg>
  </div>
</section>

<section class="cta-section">
  <h2>Ready to actually learn?</h2>
  <p>Sign up takes under a minute. We'll get your first session scheduled right away.</p>
  <a href="/name" class="btn btn-primary" style="width:auto;padding:14px 36px">
    Get Started →
  </a>
</section>
"""

NAME_HTML = BASE_STYLE + """
<div class="step-page">
  <div class="step-card">
    <div class="progress-dots">
      <div class="dot active"></div>
      <div class="dot"></div>
    </div>
    <div class="step-num">1</div>
    <h2>What's your name?</h2>
    <p class="sub">We'll use this to personalise your experience.</p>

    {% if error %}
      <p class="err-msg" style="margin-bottom:12px">{{ error }}</p>
    {% endif %}

    <form method="POST" action="/name">
      <div class="form-group">
        <label for="name">Full Name</label>
        <input id="name" name="name" type="text"
               placeholder="e.g. Alex Johnson" autocomplete="name"
               value="{{ prefill }}" class="{{ 'error' if error else '' }}"/>
      </div>
      <button type="submit" class="btn btn-primary">Continue →</button>
    </form>
  </div>
</div>
"""

EMAIL_HTML = BASE_STYLE + """
<div class="step-page">
  <div class="step-card">
    <div class="progress-dots">
      <div class="dot done"></div>
      <div class="dot active"></div>
    </div>
    <div class="step-num">2</div>
    <h2>What's your email?</h2>
    <p class="sub">Hey {{ first_name }}! Where should we send your session details?</p>

    {% if error %}
      <p class="err-msg" style="margin-bottom:12px">{{ error }}</p>
    {% endif %}

    <form method="POST" action="/email">
      <div class="form-group">
        <label for="email">Email Address</label>
        <input id="email" name="email" type="email"
               placeholder="you@example.com" autocomplete="email"
               value="{{ prefill }}" class="{{ 'error' if error else '' }}"/>
      </div>
      <button type="submit" class="btn btn-primary">Complete Sign Up →</button>
    </form>
  </div>
</div>
"""

SUCCESS_HTML = BASE_STYLE + """
<div class="step-page">
  <div class="step-card" style="text-align:center">
    <div class="success-icon">✓</div>
    <h2>You're in!</h2>
    <p class="sub">
      Welcome, {{ first_name }}! We'll reach out to <strong>{{ email }}</strong>
      soon to schedule your first lesson. 🎉
    </p>
  </div>
</div>
"""

ALREADY_HTML = BASE_STYLE + """
<div class="step-page">
  <div class="step-card" style="text-align:center">
    <div style="font-size:48px;margin-bottom:16px">👋</div>
    <h2>Welcome back!</h2>
    <p class="sub">You've already signed up — we haven't forgotten about you!</p>
    <div class="info-box">
      Signed up as <strong>{{ name }}</strong> with email <strong>{{ email }}</strong>.
    </div>
    <a href="/restart" class="btn btn-ghost">Use a different account</a>
  </div>
</div>
"""

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def landing():
    user = already_signed_up()
    if user:
        return redirect(url_for("already"))
    return render_template_string(LANDING_HTML)


@app.route("/name", methods=["GET", "POST"])
def name_step():
    user = already_signed_up()
    if user:
        return redirect(url_for("already"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        parts = [p for p in name.split() if p]

        if len(parts) < 2:
            return render_template_string(
                NAME_HTML,
                error="Please enter your first and last name.",
                prefill=name
            )

        session["signup_name"] = name
        return redirect(url_for("email_step"))

    return render_template_string(NAME_HTML, error=None, prefill="")


@app.route("/email", methods=["GET", "POST"])
def email_step():
    user = already_signed_up()
    if user:
        return redirect(url_for("already"))

    name = session.get("signup_name")
    if not name:
        return redirect(url_for("name_step"))

    first_name = name.split()[0]

    if request.method == "POST":
        email = request.form.get("email", "").strip()

        if not valid_email(email):
            return render_template_string(
                EMAIL_HTML,
                error="Please enter a valid email address.",
                prefill=email,
                first_name=first_name
            )

        save_signup(name, email)
        session["signed_up_email"] = email.lower()
        session.pop("signup_name", None)
        return redirect(url_for("success"))

    return render_template_string(EMAIL_HTML, error=None, prefill="", first_name=first_name)


@app.route("/success")
def success():
    email = session.get("signed_up_email")
    if not email:
        return redirect(url_for("landing"))
    signups = load_signups()
    user = signups.get(email)
    if not user:
        return redirect(url_for("landing"))
    return render_template_string(
        SUCCESS_HTML,
        first_name=user["name"].split()[0],
        email=user["email"]
    )


@app.route("/already")
def already():
    user = already_signed_up()
    if not user:
        return redirect(url_for("landing"))
    return render_template_string(ALREADY_HTML, name=user["name"], email=user["email"])


@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("landing"))


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Starting server at http://localhost:5000")
    app.run(debug=True)
