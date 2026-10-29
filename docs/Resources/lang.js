/**
 * Shared language toggle for all Resource pages.
 * Persists choice in localStorage so it carries across navigation.
 */

const LANG_KEY = 'rc-lang';

function applyLang(lang) {
  document.documentElement.setAttribute('lang', lang);

  // Translate elements with data-en / data-es attributes
  document.querySelectorAll('[data-en][data-es]').forEach(el => {
    const val = el.getAttribute(`data-${lang}`);
    // Use innerHTML for elements that contain links or HTML
    if (val.includes('<a') || val.includes('<br') || val.includes('<strong')) {
      el.innerHTML = val;
    } else {
      el.textContent = val;
    }
  });

  // Translate placeholders
  document.querySelectorAll('[data-en-placeholder]').forEach(el => {
    el.placeholder = el.getAttribute(`data-${lang}-placeholder`) || el.placeholder;
  });

  // Update toggle button text
  const btn = document.querySelector('.lang-toggle');
  if (btn) btn.textContent = lang === 'en' ? 'Español' : 'English';
}

function toggleLang() {
  const current = localStorage.getItem(LANG_KEY) || 'en';
  const next = current === 'en' ? 'es' : 'en';
  localStorage.setItem(LANG_KEY, next);
  applyLang(next);
}

// Apply saved language on page load
function initLang() {
  const saved = localStorage.getItem(LANG_KEY) || 'en';
  if (saved !== 'en') {
    applyLang(saved);
  }
}

// Run when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initLang);
} else {
  initLang();
}

// Expose for onclick handlers
window.toggleLang = toggleLang;
