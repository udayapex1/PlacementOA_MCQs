import { CHEATSHEETS } from './cheatsheets.js';

const SUBJECTS = [
  {
    id: 'oops',
    name: 'Object-Oriented Programming',
    shortName: 'OOPs',
    icon: '01',
    accent: '#56a8ff',
    file: './OOPS/questionBank.json',
    description: 'Classes, inheritance, polymorphism, design patterns, and language-specific concepts.',
    topics: 'C++  ·  Java  ·  Python',
  },
  {
    id: 'cn',
    name: 'Computer Networks',
    shortName: 'Computer Networks',
    icon: '02',
    accent: '#51d6a4',
    file: './CN/questionBank.json',
    description: 'Network layers, protocols, routing, addressing, security, and distributed systems.',
    topics: 'OSI  ·  TCP/IP  ·  Routing',
  },
  {
    id: 'os',
    name: 'Operating Systems',
    shortName: 'Operating Systems',
    icon: '03',
    accent: '#ffc45c',
    file: './OS/questionBank.json',
    description: 'Processes, memory, scheduling, file systems, concurrency, and Linux fundamentals.',
    topics: 'Processes  ·  Memory  ·  Linux',
  },
  {
    id: 'sql',
    name: 'SQL',
    shortName: 'SQL',
    icon: '04',
    accent: '#c88cff',
    file: './SQL/questionBank.json',
    description: 'Queries, joins, normalization, transactions, indexing, security, and database design.',
    topics: 'Queries  ·  Joins  ·  Databases',
  },
];

const state = {
  banks: {},
  subject: null,
  questions: [],
  current: 0,
  answers: {},
  marked: new Set(),
  finished: false,
  snippets: new Map(),
};

const app = document.querySelector('#app');
const letters = ['A', 'B', 'C', 'D', 'E', 'F'];

function escapeHTML(value) {
  return String(value ?? '').replace(/[&<>'"]/g, (character) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;',
  }[character]));
}

function subjectById(id) {
  return SUBJECTS.find((subject) => subject.id === id);
}

function cheatsheetById(id) {
  return CHEATSHEETS.find((sheet) => sheet.id === id);
}

function renderLoading() {
  app.innerHTML = '<div class="loading"><div class="spinner"></div><p>Loading your question banks…</p></div>';
}

function renderError(message) {
  app.innerHTML = `<div class="error-state"><span class="eyebrow">Question bank unavailable</span><h1>Could not load the practice set</h1><p>${escapeHTML(message)}</p><p>Open this folder through a local web server so the JSON files can be fetched.</p></div>`;
}

async function loadBanks() {
  renderLoading();
  try {
    const responses = await Promise.all(SUBJECTS.map(async (subject) => {
      const response = await fetch(subject.file);
      if (!response.ok) throw new Error(`${subject.file} returned ${response.status}`);
      return [subject.id, await response.json()];
    }));
    state.banks = Object.fromEntries(responses);
    handleRoute();
  } catch (error) {
    console.error(error);
    renderError(error.message);
  }
}

function renderHome() {
  app.className = 'page-content home-page';
  app.innerHTML = `
    <section class="hero">
      <div class="eyebrow">Your next interview starts here</div>
      <h1>Practice with intent.<br /><em>Perform with confidence.</em></h1>
      <p>Choose a subject, work through every question in the bank, and see exactly where you stand. No distractions — just a clean test loop built for placement preparation.</p>
      <div class="hero-actions"><a class="button primary" href="#test/oops">Start practicing <span>→</span></a><a class="inline-link" href="#cheatsheets/oops">Browse cheat sheets <span>↗</span></a></div>
    </section>
    <section class="subject-section" aria-labelledby="subject-heading">
      <div class="section-heading">
        <h2 id="subject-heading">Choose your subject</h2>
        <p>Each test includes the complete 250-question bank</p>
      </div>
      <div class="subject-grid">
        ${SUBJECTS.map((subject) => `
          <article class="subject-card" style="--accent: ${subject.accent}">
            <div class="subject-card-top"><span class="subject-icon">${subject.icon}</span><span class="subject-count">${state.banks[subject.id].length} MCQs</span></div>
            <h3>${escapeHTML(subject.name)}</h3>
            <p>${escapeHTML(subject.description)}</p>
            <div class="subject-topics">${escapeHTML(subject.topics)}</div>
            <a class="start-link" href="#test/${subject.id}">Start full test <span>→</span></a>
          </article>
        `).join('')}
      </div>
    </section>
    <section class="cheat-callout" aria-labelledby="cheat-heading">
      <div class="cheat-callout-mark">CS</div>
      <div class="cheat-callout-copy"><div class="eyebrow">Revision module</div><h2 id="cheat-heading">Cheat sheets for the final review</h2><p>Quick-reference concepts, interview comparisons, and copyable code snippets for OOPs, OS, DBMS, and SQL.</p></div>
      <a class="button secondary" href="#cheatsheets/oops">Open cheat sheets <span>→</span></a>
    </section>
    <div class="home-note"><span class="status-dot"></span><span><strong>1,000 MCQs loaded</strong> across 4 core placement subjects</span></div>
  `;
}

function renderCheatsheets(id = 'oops') {
  const active = cheatsheetById(id) || CHEATSHEETS[0];
  state.snippets = new Map();
  app.className = 'page-content cheatsheet-page';
  app.style.setProperty('--accent', active.accent);

  app.innerHTML = `
    <div class="cheat-head">
      <div><a class="back-link" href="#home">← PlacementPrep home</a><div class="cheat-title"><span class="pill" style="color:${active.accent}">QUICK REF</span><h1>Core subject cheat sheets</h1></div><p class="cheat-intro">A compact last-mile revision guide. Scan the concepts, then copy a pattern into your own notes or editor.</p></div>
      <div class="cheat-meta"><strong>04</strong> subjects covered</div>
    </div>
    <nav class="cheat-tabs" aria-label="Cheat sheet subjects">
      ${CHEATSHEETS.map((sheet) => `<a class="cheat-tab ${sheet.id === active.id ? 'active' : ''}" style="--tab-accent:${sheet.accent}" href="#cheatsheets/${sheet.id}"><span>${sheet.name}</span><small>${sheet.sections.length} sections</small></a>`).join('')}
    </nav>
    <section class="cheat-overview" style="--accent:${active.accent}"><div class="cheat-overview-icon">${active.name.slice(0, 2).toUpperCase()}</div><div><div class="eyebrow">${escapeHTML(active.name)} / study mode</div><h2>${escapeHTML(active.subtitle)}</h2></div></section>
    <div class="cheat-sections">
      ${active.sections.map((section, sectionIndex) => `
        <section class="cheat-section">
          <div class="cheat-section-heading"><span class="section-number">${String(sectionIndex + 1).padStart(2, '0')}</span><h2>${escapeHTML(section.title)}</h2></div>
          ${section.items ? `<div class="cheat-items">${section.items.map((item) => `<article class="cheat-item"><h3>${escapeHTML(item.term)}</h3><p>${escapeHTML(item.detail)}</p></article>`).join('')}</div>` : ''}
          ${section.snippets ? `<div class="snippet-grid">${section.snippets.map((item, snippetIndex) => {
            const key = `${active.id}-${sectionIndex}-${snippetIndex}`;
            state.snippets.set(key, item.code);
            return `<article class="snippet-card code-window"><div class="code-window-chrome"><div class="traffic-lights" aria-hidden="true"><span></span><span></span><span></span></div><button class="copy-button" data-copy="${key}">Copy</button></div><div class="snippet-head"><span class="snippet-language">${escapeHTML(item.language)}</span><strong>${escapeHTML(item.title)}</strong></div><pre><code>${escapeHTML(item.code)}</code></pre></article>`;
          }).join('')}</div>` : ''}
        </section>
      `).join('')}
    </div>
  `;

  document.querySelectorAll('[data-copy]').forEach((button) => button.addEventListener('click', async () => {
    const code = state.snippets.get(button.dataset.copy);
    try {
      await navigator.clipboard.writeText(code);
    } catch {
      const textarea = document.createElement('textarea');
      textarea.value = code;
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      textarea.remove();
    }
    const original = button.textContent;
    button.textContent = 'Copied';
    window.setTimeout(() => { button.textContent = original; }, 1300);
  }));
}

function startTest(id) {
  const subject = subjectById(id);
  if (!subject || !state.banks[id]) return renderHome();
  state.subject = subject;
  state.questions = state.banks[id];
  state.current = 0;
  state.answers = {};
  state.marked = new Set();
  state.finished = false;
  renderQuiz();
}

function difficultyClass(difficulty) {
  return String(difficulty || '').toLowerCase();
}

function renderQuiz() {
  const subject = state.subject;
  const question = state.questions[state.current];
  const answeredCount = Object.keys(state.answers).length;
  const progress = ((state.current + 1) / state.questions.length) * 100;
  const selected = state.answers[question.id];
  const marked = state.marked.has(question.id);

  app.className = 'page-content quiz-page';
  app.style.setProperty('--accent', subject.accent);
  app.innerHTML = `
    <div class="quiz-head">
      <div>
        <a class="back-link" href="#home">← All subjects</a>
        <div class="quiz-title"><span class="pill" style="color:${subject.accent}">${escapeHTML(subject.shortName)}</span><h1>Full practice test</h1></div>
      </div>
      <div class="quiz-stats"><strong>${answeredCount}</strong> answered of ${state.questions.length}</div>
    </div>
    <div class="progress-track" aria-label="Test progress"><div class="progress-fill" style="width:${progress}%"></div></div>
    <div class="quiz-layout">
      <section class="question-card" aria-labelledby="question-text">
        <div class="question-kicker"><span>QUESTION ${state.current + 1} / ${state.questions.length}</span><span class="difficulty ${difficultyClass(question.difficulty)}">${escapeHTML(question.difficulty || 'Practice')}</span><span>·</span><span>${escapeHTML(question.topic)}</span></div>
        <h2 class="question-text" id="question-text">${escapeHTML(question.question)}</h2>
        <div class="options" role="radiogroup" aria-label="Answer options">
          ${question.options.map((option, index) => `
            <button class="option ${selected === index ? 'selected' : ''}" data-option="${index}" role="radio" aria-checked="${selected === index}">
              <span class="option-letter">${letters[index]}</span><span class="option-copy">${escapeHTML(option)}</span>
            </button>
          `).join('')}
        </div>
        <div class="question-footer">
          <button class="text-button ${marked ? 'marked' : ''}" id="mark-button">${marked ? '★' : '☆'} ${marked ? 'Marked for review' : 'Mark for review'}</button>
          <div class="button-row">
            <button class="button secondary" id="previous-button" ${state.current === 0 ? 'disabled' : ''}>Previous</button>
            ${state.current === state.questions.length - 1
              ? '<button class="button finish" id="finish-button">Finish test →</button>'
              : '<button class="button primary" id="next-button">Next question →</button>'}
          </div>
        </div>
      </section>
      ${renderNavigator(answeredCount)}
    </div>
  `;

  document.querySelectorAll('.option').forEach((button) => button.addEventListener('click', () => {
    state.answers[question.id] = Number(button.dataset.option);
    renderQuiz();
  }));
  document.querySelector('#previous-button')?.addEventListener('click', () => { state.current -= 1; renderQuiz(); });
  document.querySelector('#next-button')?.addEventListener('click', () => { state.current += 1; renderQuiz(); });
  document.querySelector('#finish-button')?.addEventListener('click', finishTest);
  document.querySelector('#mark-button')?.addEventListener('click', () => {
    if (state.marked.has(question.id)) state.marked.delete(question.id); else state.marked.add(question.id);
    renderQuiz();
  });
  document.querySelectorAll('.nav-number').forEach((button) => button.addEventListener('click', () => {
    state.current = Number(button.dataset.index);
    renderQuiz();
  }));
}

function renderNavigator(answeredCount) {
  return `
    <aside class="navigator" aria-label="Question navigator">
      <div class="navigator-head"><h2>Question navigator</h2><small>${answeredCount}/${state.questions.length}</small></div>
      <div class="nav-legend"><span class="answered">Answered</span><span class="marked">Review</span></div>
      <div class="question-grid">
        ${state.questions.map((question, index) => `
          <button class="nav-number ${index === state.current ? 'current' : ''} ${state.answers[question.id] !== undefined ? 'answered' : ''} ${state.marked.has(question.id) ? 'marked' : ''}" data-index="${index}" aria-label="Go to question ${index + 1}">${index + 1}</button>
        `).join('')}
      </div>
      <div class="nav-summary"><strong>${answeredCount}</strong> answered<br /><strong>${state.questions.length - answeredCount}</strong> remaining<br /><strong>${state.marked.size}</strong> marked for review</div>
    </aside>
  `;
}

function finishTest() {
  const unanswered = state.questions.length - Object.keys(state.answers).length;
  if (unanswered > 0 && !window.confirm(`${unanswered} question${unanswered === 1 ? '' : 's'} unanswered. Finish the test anyway?`)) return;
  state.finished = true;
  renderResults();
}

function renderResults() {
  const subject = state.subject;
  const correct = state.questions.filter((question) => state.answers[question.id] === question.answer).length;
  const answered = Object.keys(state.answers).length;
  const unanswered = state.questions.length - answered;
  const percentage = Math.round((correct / state.questions.length) * 100);
  const reviewQuestions = state.questions.filter((question) => state.answers[question.id] !== question.answer);

  app.className = 'page-content results-page';
  app.style.setProperty('--accent', subject.accent);
  app.innerHTML = `
    <section class="result-hero">
      <div class="eyebrow">${escapeHTML(subject.name)} · test complete</div>
      <h1>Good work. Keep going.</h1>
      <p>Here is your performance across all ${state.questions.length} questions.</p>
      <div class="score-circle"><strong>${percentage}%</strong><span>score</span></div>
    </section>
    <section class="result-stats" aria-label="Test results">
      <div class="result-stat"><strong>${correct}</strong><span>Correct answers</span></div>
      <div class="result-stat"><strong>${answered - correct}</strong><span>Needs review</span></div>
      <div class="result-stat"><strong>${unanswered}</strong><span>Unanswered</span></div>
    </section>
    <div class="result-actions"><button class="button primary" id="retry-button">Retry this subject</button><a class="button secondary" href="#home">Choose another subject</a></div>
    <section class="review-panel"><h2>Review queue <span style="color:var(--muted);font-weight:400">(${reviewQuestions.length})</span></h2><div class="review-list">
      ${reviewQuestions.length ? reviewQuestions.map((question) => {
        const answer = state.answers[question.id];
        const status = answer === undefined ? ['unanswered', 'Not answered'] : ['incorrect', 'Incorrect'];
        return `<div class="review-item"><span class="review-item-num">Q${question.id}</span><span class="review-item-copy">${escapeHTML(question.question)}</span><span class="review-item-status ${status[0]}">${status[1]}</span></div>`;
      }).join('') : '<p style="color:var(--green);font-size:.82rem">Perfect run — every answer was correct.</p>'}
    </div></section>
  `;
  document.querySelector('#retry-button').addEventListener('click', () => { startTest(subject.id); });
}

function handleRoute() {
  const cheatMatch = window.location.hash.match(/^#cheatsheets(?:\/(oops|os|dbms|sql))?$/);
  if (cheatMatch) return renderCheatsheets(cheatMatch[1] || 'oops');
  const match = window.location.hash.match(/^#test\/(oops|cn|os|sql)$/);
  if (match && state.banks[match[1]]) startTest(match[1]);
  else renderHome();
}

const menuButton = document.querySelector('#menu-button');
const siteNav = document.querySelector('.site-nav');
menuButton?.addEventListener('click', () => {
  const open = siteNav.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(open));
});
siteNav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
  siteNav.classList.remove('open');
  menuButton?.setAttribute('aria-expanded', 'false');
}));
window.addEventListener('hashchange', handleRoute);
loadBanks();
