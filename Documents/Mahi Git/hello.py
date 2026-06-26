<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>1-on-1 Code Lessons</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg: #0f1117; --surface: #1a1d27; --card: #22263a;
      --accent: #6c63ff; --accent2: #a78bfa; --text: #e8eaf0;
      --muted: #8b90a7; --success: #34d399; --error: #f87171; --border: #2e3250;
    }
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; }
    .page { display: none; }
    .page.active { display: block; }
    #page-landing { min-height: 100vh; display: flex; flex-direction: column; }
    .hero { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 80px 24px 60px; text-align: center; position: relative; }
    .hero::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 80% 60% at 50% -10%, rgba(108,99,255,0.22), transparent); pointer-events: none; }
    .badge { display: inline-block; background: rgba(108,99,255,0.15); border: 1px solid rgba(108,99,255,0.4); color: var(--accent2); font-size: 12px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; padding: 6px 18px; border-radius: 999px; margin-bottom: 28px; }
    .hero h1 { font-size: clamp(2rem, 5vw, 3.4rem); font-weight: 800; line-height: 1.15; max-width: 700px; margin-bottom: 24px; background: linear-gradient(135deg, #fff 40%, var(--accent2)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .hero-pitch { font-size: clamp(1rem, 1.8vw, 1.15rem); color: var(--muted); max-width: 620px; line-height: 1.9; margin-bottom: 52px; }
    .hero-pitch strong { color: var(--text); }
    .features { display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; max-width: 740px; margin-bottom: 64px; }
    .feature-card { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 22px 24px; width: 210px; text-align: left; }
    .feature-card .icon { font-size: 26px; margin-bottom: 10px; }
    .feature-card h3 { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
    .feature-card p { font-size: 13px; color: var(--muted); line-height: 1.6; }
    .scroll-hint { display: flex; flex-direction: column; align-items: center; gap: 8px; color: var(--muted); font-size: 13px; animation: bob 2s ease-in-out infinite; }
    @keyframes bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(7px); } }
    .cta-section { padding: 80px 24px; display: flex; flex-direction: column; align-items: center; text-align: center; border-top: 1px solid var(--border); background: var(--surface); }
    .cta-section h2 { font-size: clamp(1.4rem, 3vw, 2rem); font-weight: 700; margin-bottom: 12px; }
    .cta-section p { color: var(--muted); max-width: 460px; margin-bottom: 32px; font-size: 15px; line-height: 1.7; }
    .step-page { min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 24px; position: relative; }
    .step-page::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 60% 40% at 50% 0%, rgba(108,99,255,0.1), transparent); pointer-events: none; }
    .step-card { background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 48px 40px; width: 100%; max-width: 460px; position: relative; }
    .progress-dots { display: flex; gap: 6px; margin-bottom: 32px; }
    .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--border); transition: background 0.3s, transform 0.3s; }
    .dot.active { background: var(--accent); transform: scale(1.3); }
    .dot.done { background: var(--success); }
    .step-num { display: inline-flex; align-items: center; justify-content: center; width: 36px; height: 36px; background: rgba(108,99,255,0.15); border: 1px solid rgba(108,99,255,0.35); border-radius: 50%; font-size: 14px; font-weight: 700; color: var(--accent2); margin-bottom: 20px; }
    .step-card h2 { font-size: 1.55rem; font-weight: 800; margin-bottom: 8px; }
    .step-card .sub { color: var(--muted); font-size: 14px; line-height: 1.65; margin-bottom: 32px; }
    .form-group { margin-bottom: 20px; }
    .form-group label { display: block; font-size: 12px; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 8px; }
    .form-group input { width: 100%; padding: 14px 16px; background: var(--card); border: 1.5px solid var(--border); border-radius: 10px; color: var(--text); font-size: 15px; outline: none; transition: border-color 0.2s, box-shadow 0.2s; }
    .form-group input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(108,99,255,0.15); }
    .form-group input.error { border-color: var(--error); }
    .err-msg { color: var(--error); font-size: 13px; margin-top: 6px; display: none; }
    .err-msg.show { display: block; }
    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 14px 28px; border-radius: 12px; font-size: 15px; font-weight: 700; cursor: pointer; border: none; transition: all 0.2s; width: 100%; margin-top: 8px; }
    .btn-primary { background: var(--accent); color: #fff; }
    .btn-primary:hover { background: #5a52e0; transform: translateY(-2px); box-shadow: 0 8px 24px rgba(108,99,255,0.3); }
    .btn-ghost { background: transparent; color: var(--muted); border: 1.5px solid var(--border); margin-top: 12px; }
    .btn-ghost:hover { border-color: var(--accent2); color: var(--accent2); }
    .success-icon { width: 72px; height: 72px; background: rgba(52,211,153,0.1); border: 2px solid var(--success); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 30px; margin: 0 auto 24px; }
    .info-box { background: rgba(108,99,255,0.08); border: 1px solid rgba(108,99,255,0.25); border-radius: 10px; padding: 14px 16px; font-size: 14px; color: var(--muted); line-height: 1.65; margin-top: 20px; }
    .info-box strong { color: var(--text); }
  </style>
</head>
<body>

<div id="page-landing" class="page active">
  <section class="hero">
    <div class="badge">Limited Spots Available</div>
    <h1>Learn to Code with a Personal Mentor, Not a Video</h1>
    <p class="hero-pitch">
      Most people trying to learn to code get stuck watching tutorials they barely follow,
      copying code they don't understand, and quitting before they ever build anything real.
      <br><br>
      <strong>That ends here.</strong> In a 1-on-1 lesson you get a real person who looks
      at <em>your</em> code, answers <em>your</em> questions, and teaches at <em>your</em> pace.
      No pre-recorded fluff — just focused, personal teaching that gets you from confused to confident, fast.
      <br><br>
      Whether you are a complete beginner or someone stuck at the same level for months,
      a single session will move you further than weeks of solo grinding.
    </p>
    <div class="features">
      <div class="feature-card"><div class="icon">&#127919;</div><h3>Tailored to You</h3><p>Lessons built around your goals, your level, and your learning style.</p></div>
      <div class="feature-card"><div class="icon">&#128172;</div><h3>Ask Anything</h3><p>No dumb questions. Real answers in real time from a real person.</p></div>
      <div class="feature-card"><div class="icon">&#9889;</div><h3>Learn Faster</h3><p>Progress faster than self-teaching with direct expert feedback.</p></div>
    </div>
    <div class="scroll-hint">
      <span>Scroll down to sign up</span>
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
    </div>
  </section>
  <section class="cta-section">
    <h2>Ready to actually learn?</h2>
    <p>Sign up takes under a minute. We'll get your first session scheduled right away.</p>
    <button class="btn btn-primary" style="width:auto;padding:14px 36px" onclick="show('name')">Get Started &rarr;</button>
  </section>
</div>

<div id="page-name" class="page">
  <div class="step-page"><div class="step-card">
    <div class="progress-dots"><div class="dot active"></div><div class="dot"></div></div>
    <div class="step-num">1</div>
    <h2>What's your name?</h2>
    <p class="sub">We'll use this to personalise your experience.</p>
    <div class="form-group">
      <label for="inp-name">Full Name</label>
      <input id="inp-name" type="text" placeholder="e.g. Alex Johnson" autocomplete="name"/>
      <div class="err-msg" id="err-name">Please enter your first and last name.</div>
    </div>
    <button class="btn btn-primary" onclick="submitName()">Continue &rarr;</button>
  </div></div>
</div>

<div id="page-email" class="page">
  <div class="step-page"><div class="step-card">
    <div class="progress-dots"><div class="dot done"></div><div class="dot active"></div></div>
    <div class="step-num">2</div>
    <h2>What's your email?</h2>
    <p class="sub" id="email-sub">We'll send your session details here.</p>
    <div class="form-group">
      <label for="inp-email">Email Address</label>
      <input id="inp-email" type="email" placeholder="you@example.com" autocomplete="email"/>
      <div class="err-msg" id="err-email">Please enter a valid email address.</div>
    </div>
    <button class="btn btn-primary" onclick="submitEmail()">Complete Sign Up &rarr;</button>
  </div></div>
</div>

<div id="page-success" class="page">
  <div class="step-page"><div class="step-card" style="text-align:center">
    <div class="success-icon">&#10003;</div>
    <h2>You're in!</h2>
    <p class="sub" id="success-msg">We'll be in touch soon to get your first lesson scheduled.</p>
  </div></div>
</div>

<div id="page-already" class="page">
  <div class="step-page"><div class="step-card" style="text-align:center">
    <div style="font-size:48px;margin-bottom:16px">&#128075;</div>
    <h2>Welcome back!</h2>
    <p class="sub">You've already signed up — we haven't forgotten about you!</p>
    <div class="info-box" id="already-info"></div>
    <button class="btn btn-ghost" onclick="restart()">Use a different account</button>
  </div></div>
</div>

<script>
  const STORAGE_KEY = 'codeLesson_v1';
  let name = '', email = '';

  window.addEventListener('DOMContentLoaded', () => {
    const saved = getSaved();
    if (saved) {
      document.getElementById('already-info').innerHTML = 'Signed up as <strong>' + saved.name + '</strong> with email <strong>' + saved.email + '</strong>.';
      show('already');
    } else {
      show('landing');
    }
  });

  function getSaved() {
    try {
      const d = JSON.parse(localStorage.getItem(STORAGE_KEY));
      return (d && d.name && d.email) ? d : null;
    } catch(e) { return null; }
  }

  function show(page) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.getElementById('page-' + page).classList.add('active');
    window.scrollTo(0, 0);
  }

  function submitName() {
    const inp = document.getElementById('inp-name');
    const err = document.getElementById('err-name');
    const val = inp.value.trim();
    if (val.split(/\s+/).filter(Boolean).length < 2) {
      inp.classList.add('error'); err.classList.add('show'); return;
    }
    inp.classList.remove('error'); err.classList.remove('show');
    name = val;
    document.getElementById('email-sub').textContent = 'Hey ' + val.split(' ')[0] + '! Where should we send your session details?';
    show('email');
  }

  function submitEmail() {
    const inp = document.getElementById('inp-email');
    const err = document.getElementById('err-email');
    const val = inp.value.trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) {
      inp.classList.add('error'); err.classList.add('show'); return;
    }
    inp.classList.remove('error'); err.classList.remove('show');
    email = val;
    localStorage.setItem(STORAGE_KEY, JSON.stringify({ name: name, email: email, date: new Date().toISOString() }));
    document.getElementById('success-msg').textContent = 'Welcome, ' + name.split(' ')[0] + '! We will reach out to ' + email + ' soon to schedule your first lesson.';
    show('success');
  }

  function restart() {
    localStorage.removeItem(STORAGE_KEY);
    document.getElementById('inp-name').value = '';
    document.getElementById('inp-email').value = '';
    name = ''; email = '';
    show('landing');
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('inp-name').addEventListener('keydown', function(e) { if (e.key === 'Enter') submitName(); });
    document.getElementById('inp-email').addEventListener('keydown', function(e) { if (e.key === 'Enter') submitEmail(); });
  });
</script>
</body>
</html>
