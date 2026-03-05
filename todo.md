# TODO — Morisco Thesis Portfolio Website
## Build Checklist: Project Setup → Deployment

**Repository:** `doganyunus/morisco-thesis`
**Deploy target:** `doganyunus.github.io/morisco-thesis`
**Reference files:** `agents.md` (rules) · `plan.md` (architecture & design) · `research.md` (content)

> **How to use this file:**
> Each task is scoped to a single Cursor Agent session. Tasks within a phase are ordered — complete them top-to-bottom. Do not begin a phase until all tasks in the previous phase are checked. Mark complete with `[x]`.
>
> **Definition of done for each task:** The file(s) it touches can be opened in a browser or editor and the result is exactly as described — no placeholders, no broken references, no console errors for that task's scope.

---

## Phase 0 — Project Setup
*Goal: repository scaffolded, all empty files in place, git initialised, agents.md readable by any agent.*

- [ ] **0.1 — Create the full directory tree**
  Create every folder and placeholder file listed in `plan.md §2 Site Map`. Use `touch` to create empty files so paths exist before content is written. Exact structure:
  ```
  morisco-thesis/
  ├── index.html
  ├── researcher.html
  ├── sources.html
  ├── agents.md          ← copy from project root into repo
  ├── css/main.css
  ├── js/main.js
  ├── images/hero/.gitkeep
  ├── images/maps/.gitkeep
  ├── images/portraits/.gitkeep
  ├── images/paintings/.gitkeep
  ├── images/chapters/.gitkeep
  ├── images/ui/.gitkeep
  └── assets/favicon/.gitkeep
  ```
  Verify: `ls -R morisco-thesis/` shows every folder with no missing directories.

- [ ] **0.2 — Initialise git and create `.gitignore`**
  Run `git init` inside `morisco-thesis/`. Create `.gitignore` with exactly these entries and nothing else:
  ```
  .DS_Store
  Thumbs.db
  *.log
  ```
  Do not add `node_modules/` — there will never be one. Do not create any npm files.
  Verify: `git status` shows all files as untracked with no errors.

- [ ] **0.3 — Copy `agents.md` into the repository root**
  Copy `agents.md` from the project root (`20260305 website portfolio yunus/agents.md`) into `morisco-thesis/agents.md`. This ensures any agent working inside the repo finds it immediately.
  Verify: `morisco-thesis/agents.md` exists and is readable.

- [ ] **0.4 — Create a minimal `README.md`**
  Write `morisco-thesis/README.md` with: project title, one-sentence description, deploy URL, tech stack line, and a note pointing to `agents.md` for contributing rules. Do not elaborate beyond 15 lines.
  Verify: file exists and contains the deploy URL `doganyunus.github.io/morisco-thesis`.

- [ ] **0.5 — Write the `assets/favicon/favicon.svg`**
  Create a simple SVG favicon: a compass rose or an eight-pointed star motif in `--color-gold` (`#C9A84C`) on a `--color-deep-ocean` (`#162039`) background. Keep it under 1 KB. No external dependencies.
  Verify: the SVG file is valid, opens in a browser, and renders a recognisable icon at 16×16px.

---

## Phase 1 — Content Preparation
*Goal: all text content drafted in structured Markdown scratch-files before touching HTML. Writing and coding are separated so HTML authoring sessions are not blocked by content decisions.*

- [ ] **1.1 — Draft `content/nav-and-footer.md`**
  Create `morisco-thesis/content/` directory. Write a scratch file containing the exact text for: nav logo label, the three nav link labels and their `href` targets, footer copyright line, footer image credits list (all 11 images from `agents.md §7`), and footer links. This file is a writing reference — it will not be deployed.
  Verify: all 11 image credits from `agents.md` are present with correct attribution wording.

- [ ] **1.2 — Draft `content/index-sections.md`**
  Write the final text for every section of `index.html` in order. For each section include: heading text, body paragraphs, pull quote (if any), card/list content, and any labels or badges. Source all historical claims from `research.md`. Do not invent facts.
  Sections to cover: hero tagline · contemporary bridge (4 cards) · historical context (timeline + 3 text blocks) · expulsion stats (3 numbers + captions) · chapters 1–6 (heading + 2-paragraph summary + pull quote each) · four strategies (4 × heading + 2-sentence description) · key figures intro paragraph · maps section heading + captions for 3 map panels · methodology teaser paragraph · about-the-researcher short bio.
  Verify: every section has content; no section says "TBD" or "placeholder".

- [ ] **1.3 — Draft `content/researcher-page.md`**
  Write all content for `researcher.html` from `docs/cv_updated.pdf` (the CV in the `docs/` folder). Include: education timeline, manuscripts under review (2 items), grants and fellowships, invited lectures, conference presentations, teaching experience, technical competencies, working languages.
  Verify: content matches the CV exactly; no entries are missing or invented.

- [ ] **1.4 — Draft `content/sources-page.md`**
  Write all content for `sources.html`. Include: methodology overview (3 paragraphs from `plan.md §4.3`), full archives table (all 11 archives from `research.md §Methodology`), source types breakdown (5 categories), glossary (all terms from `research.md §Part VII` and dissertation Appendix 1). Do not include the full bibliography — that is out of scope for Phase 1; mark it `<!-- bibliography: to be added in Phase 2.4 -->`.
  Verify: glossary contains at least 25 terms; archives table has 11 rows.

---

## Phase 2 — HTML Structure
*Goal: all three HTML files fully marked up with semantic structure and real content. No styling yet — this phase produces well-formed, content-complete HTML that renders correctly as unstyled text.*

- [ ] **2.1 — Write the shared HTML `<head>` template**
  In a scratch file or directly in all three HTML files, establish the canonical `<head>` block from `agents.md §8` (DOCTYPE, charset, viewport, title, meta description, Open Graph tags, Google Fonts link, `css/main.css` link, favicon link). Apply the correct page-specific `<title>` and `<meta name="description">` to each of the three files:
  - `index.html`: "Moriscos & the Ottoman Empire — PhD Thesis Portfolio"
  - `researcher.html`: "About the Researcher — Moriscos & the Ottoman Empire"
  - `sources.html`: "Sources & Methodology — Moriscos & the Ottoman Empire"
  Verify: all three files have valid `<!DOCTYPE html>`, `<html lang="en">`, complete `<head>`, and GSAP CDN scripts before `</body>`.

- [ ] **2.2 — Write the shared `<nav>` and `<footer>` markup**
  Write the `<nav class="site-nav" aria-label="Main navigation">` block once, then copy it identically into all three HTML files. Nav must contain: logo/title link to `index.html`, three navigation links (`index.html`, `researcher.html`, `sources.html`) with correct relative paths, skip link `<a class="skip-link" href="#main-content">` as first `<body>` child.
  Write the `<footer class="site-footer" aria-label="Site footer">` once and copy identically: copyright line, three footer links (relative), image credits as a `<ul>` using text from `content/nav-and-footer.md`.
  Verify: tab through the nav in a browser — all three links reach their correct pages without 404. Skip link is first focusable element.

- [ ] **2.3 — Write `index.html` §1–4: hero through expulsion**
  Using content from `content/index-sections.md`, mark up:
  - `<section id="hero">`: `<h1>`, subtitle `<p>`, tagline `<p>`, scroll cue element, `<img class="hero-bg">` with correct `alt` and HTML comment credit
  - `<section id="contemporary" aria-label="History That Lives Today">`: opening `<blockquote>`, four `<article class="bridge-card">` elements each with heading and two paragraphs, closing bridge sentence
  - `<section id="context" aria-label="Who Were the Moriscos?">`: left-column `<ol class="timeline">` with nine `<li>` entries using `<time>` elements, right-column three `<div class="text-block">` + `<figure>` with Oromig painting and `<figcaption>`
  - `<section id="expulsion" aria-label="The Expulsion">`: background `<img>`, three `<div class="stat">` elements each with `<span class="stat-number">` and `<span class="stat-label">`, closing sentence paragraph
  Verify: open `index.html` in browser — all four sections present as readable unstyled text; no broken image paths (use `onerror` console check); all `<time>` elements have `datetime` attributes.

- [ ] **2.4 — Write `index.html` §5–10: chapters 1–6**
  Mark up all six chapter sections. Each follows this pattern:
  ```html
  <section id="chapter-N" aria-label="[Chapter title]">
    <article class="chapter-block">
      <div class="chapter-image">
        <!-- figure + img + figcaption -->
      </div>
      <div class="chapter-text">
        <span class="strategy-badge">[STRATEGY]</span>  <!-- chapters 2–5 only -->
        <h2>[Chapter title]</h2>
        <p>[Summary paragraph 1]</p>
        <p>[Summary paragraph 2]</p>
        <blockquote>[Pull quote]<cite>[Source]</cite></blockquote>
      </div>
    </article>
  </section>
  ```
  Apply correct strategy badges: Chapter 2 → `[DIPLOMACY]`, Chapter 3 → `[INTELLIGENCE]`, Chapter 4 → `[MOBILITY]`, Chapter 5 → `[CONVERSION & IDENTITY]`. Chapters 1 and 6 have no badge.
  Image elements: use correct filenames from `agents.md §7 Image Rules` table, correct `alt` text, HTML comment credits. Use `images/` placeholder paths — images not yet present.
  Verify: six `<section>` elements with correct `id` values; all `alt` attributes present; no inline styles.

- [ ] **2.5 — Write `index.html` §11–15: strategies through about**
  Mark up:
  - `<section id="strategies">`: `<h2>`, four `<article class="strategy-quadrant">` each with SVG icon placeholder, `<h3>` label, `<p>` description
  - `<section id="figures">`: `<h2>`, two `<div class="portrait-row stagger-children">` each containing four `<article class="portrait-card">` with `<figure>` + oval `<img>` + `<figcaption>` + `<h3>` name + `<p>` dates + `<p>` role. Use content from `research.md §Part IV`.
  - `<section id="maps">`: `<h2>`, three `<div class="map-panel">` each with `<img>` + text overlay `<div>` with heading and caption
  - `<section id="methodology">`: `<h2>`, two paragraphs, three archive `<div class="archive-teaser">` blocks, `<a href="sources.html">` CTA
  - `<section id="about">`: `<h2>`, `<img>` portrait with `alt`, two-paragraph bio from `content/researcher-page.md`, `<a href="researcher.html">` CTA
  Verify: all five sections present; portrait cards have correct names from `research.md`; CTA links are relative paths.

- [ ] **2.6 — Write `researcher.html` complete markup**
  Using content from `content/researcher-page.md`, mark up the full CV page:
  - Page `<h1>`: Yunus Doğan, title, institution
  - Research interests: `<ul class="interest-tags">` with 5–6 `<li>` items
  - Education: `<ol class="edu-timeline">` with 5 entries, each `<li>` containing institution, degree, dates as `<time>`, advisor
  - Publications: two `<article class="publication-card">` entries, each with full citation
  - Grants and fellowships: `<dl>` with `<dt>` year + `<dd>` description for each entry
  - Conference presentations: `<details>`/`<summary>` accordion grouped by year
  - Teaching: simple `<ul>` list
  - Technical competencies: `<dl>` grouped by category
  - Languages: `<ul class="languages-list">` with name, level label, and a `<meter>` element for each
  Verify: page opens; all sections readable; accordion `<details>` elements open/close without JS; no ARIA errors.

- [ ] **2.7 — Write `sources.html` complete markup**
  Using content from `content/sources-page.md`, mark up:
  - Methodology overview: three `<article class="method-card">` (Trans-imperial / Microhistory / Digital Humanities)
  - Archives table: `<table>` with `<thead>` (Archive, Location, Key Collections) and 11 `<tbody>` rows — one per archive from `research.md §Methodology`
  - Source types: five `<div class="source-type">` blocks with icon placeholder, heading, description
  - Glossary: `<dl class="glossary">` with all terms from `research.md §Part VII`, two-column layout via CSS class
  - Bibliography placeholder: `<section id="bibliography">` with `<!-- bibliography: to be added -->` comment
  Verify: table has 11 rows; glossary has ≥ 25 `<dt>`/`<dd>` pairs; all IDs are unique across the page.

---

## Phase 3 — CSS Styling
*Goal: `css/main.css` fully written, design system applied, all layouts correct on desktop. Pages look polished and atmospheric at 1280px width.*

- [ ] **3.1 — Write CSS §1–3: custom properties, reset, typography base**
  Write the first three sections of `main.css` exactly as specified in `plan.md §3` and `agents.md §5`:
  - §1 All `:root` custom properties — every color, font, size, spacing, radius, and transition variable. Copy values verbatim from `agents.md §5.1–5.3`.
  - §2 CSS reset: `box-sizing: border-box` on `*`, `margin: 0`, `padding: 0`, `img { max-width: 100%; display: block }`, `html { scroll-behavior: smooth }`
  - §3 Typography base: `body { font-family: var(--font-sans); font-size: var(--text-body); line-height: var(--leading-base); color: var(--color-ink); background: var(--color-parchment) }`, `h1–h4 { font-family: var(--font-serif) }`, and all semantic heading size mappings
  Verify: open `index.html` — text renders in Cormorant Garamond for headings, Source Sans 3 for body. No 404 for font files (Google Fonts CDN loads).

- [ ] **3.2 — Write CSS §4: layout utilities**
  Write reusable layout classes:
  - `.container-narrow`, `.container-mid`, `.container-wide` — centered with `max-width` and `margin: 0 auto` and horizontal padding
  - `.section` — `padding: var(--section-pad-y) 0`
  - `.section--dark` — `background: var(--color-bg-dark); color: var(--color-text-on-dark)`
  - `.section--mid` — `background: var(--color-bg-mid); color: var(--color-text-on-dark)`
  - `.section--light` — `background: var(--color-bg-light); color: var(--color-text-on-light)`
  - `.split` — two-column grid `grid-template-columns: 1fr 1fr; gap: var(--space-lg)` (no `@media` yet — mobile breakpoints come in §24)
  - `.split--reversed` — same but with `direction: rtl` on container and `direction: ltr` on children
  Verify: add section classes to HTML sections, open browser — alternating dark/light rhythm is visible down the page.

- [ ] **3.3 — Write CSS §5: navigation component**
  Style `.site-nav`:
  - Fixed position, full width, top 0, z-index 100
  - Default: `background: transparent`
  - `.site-nav.scrolled` state: `background: rgba(22, 32, 57, 0.92); backdrop-filter: blur(8px)`
  - Flex layout: logo left, links right
  - Nav links: `font-family: var(--font-sans); font-size: var(--text-label); text-transform: uppercase; letter-spacing: var(--tracking-wide); color: var(--color-text-light)`
  - Gold underline draw animation on hover (CSS only — from `plan.md §5.3`)
  - `.skip-link`: visually hidden by default (`position: absolute; left: -9999px`), visible on `:focus` (`left: 1rem; top: 1rem; background: var(--color-gold); color: var(--color-ink); padding: 0.5rem 1rem; border-radius: var(--radius-sm)`)
  Verify: nav appears transparent over hero; underline animates on hover; skip link appears on keyboard Tab.

- [ ] **3.4 — Write CSS §6–7: buttons, CTAs, and card components**
  Style the following components:
  - `.btn` — base button: `font-family: var(--font-sans); font-size: var(--text-label); text-transform: uppercase; letter-spacing: var(--tracking-wide); padding: 0.75rem 1.75rem; border-radius: var(--radius-sm); transition: var(--transition-base); cursor: pointer; display: inline-block; text-decoration: none`
  - `.btn--primary` — `background: var(--color-terracotta); color: var(--color-text-light)`, hover: `background: var(--color-burnt-sienna)`
  - `.btn--outline` — `border: 1px solid var(--color-gold); color: var(--color-gold); background: transparent`, hover: `background: var(--color-gold); color: var(--color-ink)`
  - `.bridge-card` — parchment bg, `border-left: 3px solid var(--color-terracotta)`, padding, header in gold (`var(--color-gold)`, `var(--font-serif)`)
  - `.strategy-badge` — pill: `display: inline-block; font-size: var(--text-label); text-transform: uppercase; letter-spacing: var(--tracking-wide); border: 1px solid currentColor; padding: 0.25rem 0.75rem; border-radius: 9999px; color: var(--color-gold); margin-bottom: var(--space-sm)`
  Verify: visual check — cards have visible left border; badge renders as a pill; buttons have correct colours on dark and light backgrounds.

- [ ] **3.5 — Write CSS §8–9: timeline and pull quote components**
  Style `.timeline`:
  - `list-style: none`, each `<li>` with a left pseudo-element dot: `::before { content: ''; display: block; width: 10px; height: 10px; border-radius: 50%; background: var(--color-gold); margin-right: var(--space-sm) }`
  - `<time>` within timeline: bold, `color: var(--color-terracotta)` (on light bg)
  - Vertical line connecting dots: `border-left: 1px solid var(--color-sand)` on the `<ol>` with `padding-left: var(--space-md)`
  Style `blockquote.pull-quote`:
  - `font-family: var(--font-serif); font-style: italic; font-size: var(--text-pullquote); line-height: var(--leading-loose)`
  - On dark sections: `color: var(--color-gold)`
  - On light sections: `color: var(--color-terracotta)`
  - `border-left: 3px solid currentColor; padding-left: var(--space-md); margin: var(--space-lg) 0`
  - `<cite>`: `display: block; font-size: var(--text-caption); font-style: normal; color: var(--color-text-muted); margin-top: var(--space-xs)`
  Verify: timeline dots are visible; pull quote renders in italic gold on dark sections.

- [ ] **3.6 — Write CSS §10: image treatment classes**
  Write:
  - `.hero-bg` — `position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center`
  - `.hero-overlay` — `position: absolute; inset: 0; background: rgba(22, 32, 57, 0.55)`
  - `.img-historical` — `filter: sepia(15%) contrast(105%)`
  - `.portrait-img` — `border-radius: 50%; aspect-ratio: 1; object-fit: cover; border: 2px solid var(--color-gold); width: 120px; height: 120px`
  - `.full-bleed` — `width: 100%; height: 100%; object-fit: cover`
  - `.map-panel` — `position: relative; overflow: hidden; min-height: 60vh`
  - `.map-panel__overlay` — `position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: flex-end; padding: var(--space-lg); background: linear-gradient(to top, rgba(22,32,57,0.85) 0%, transparent 60%)`
  Verify: apply classes in HTML, visual check — hero image renders full-bleed with dark overlay; portrait images are circular with gold border.

- [ ] **3.7 — Write CSS §11: hero section layout**
  Style `#hero`:
  - `position: relative; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden`
  - `.hero__content` — `position: relative; z-index: 2; text-align: center; max-width: 900px; padding: 0 var(--space-md)`
  - `.hero__title` — `font-size: var(--text-hero); font-weight: 300; color: var(--color-text-light); line-height: var(--leading-tight); margin-bottom: var(--space-sm)`
  - `.hero__subtitle` — `font-size: var(--text-subheading); color: var(--color-text-muted); font-weight: 300; margin-bottom: var(--space-md)`
  - `.hero__tagline` — `font-family: var(--font-sans); font-size: var(--text-body); color: var(--color-text-muted); font-style: italic`
  - `.scroll-cue` — `position: absolute; bottom: var(--space-lg); left: 50%; transform: translateX(-50%); color: var(--color-text-muted)` + `scrollPulse` animation from `plan.md §5.3`
  Verify: hero fills full viewport; title, subtitle, tagline centred; scroll cue pulses at bottom.

- [ ] **3.8 — Write CSS §12–14: contemporary bridge, historical context, expulsion**
  Style:
  - `#contemporary`: four-column grid `grid-template-columns: repeat(4, 1fr)`, gap, section padding; bridge-card component already done in §3.4
  - `#context` `.split` layout: timeline column and text column side-by-side; text blocks with `margin-bottom: var(--space-lg)` between them; sub-headings in terracotta
  - `#expulsion`: `position: relative; min-height: 80vh; display: flex; align-items: center; justify-content: center`; stats container: `display: flex; gap: var(--space-xl); text-align: center`; `.stat-number`: `font-family: var(--font-serif); font-size: var(--text-display); color: var(--color-text-light)`; `.stat-label`: `font-family: var(--font-sans); font-size: var(--text-caption); text-transform: uppercase; letter-spacing: var(--tracking-wide); color: var(--color-text-muted)`
  Verify: contemporary bridge shows as 4 equal-width cards; expulsion stats are large centered numbers over background image.

- [ ] **3.9 — Write CSS §15: chapter block shared styles and per-chapter specifics**
  Shared `.chapter-block` styles: `.split` layout (50/50); `.chapter-image` with `position: relative; overflow: hidden; min-height: 400px`; `.chapter-text` with padding and max-width.
  Per-chapter: even chapters (`#chapter-2`, `#chapter-4`, `#chapter-6`) get `.split--reversed` to alternate image side. Chapter text headings: `font-size: var(--text-heading); margin-bottom: var(--space-md)`. Chapter body paragraphs: `max-width: var(--container-narrow)`.
  Verify: chapters alternate image-left / image-right on desktop; chapter headings sized correctly.

- [ ] **3.10 — Write CSS §16–17: four strategies and portrait gallery**
  Style `#strategies`:
  - `display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-md)`
  - `.strategy-quadrant`: `padding: var(--space-lg); border: 1px solid rgba(201,168,76,0.2); border-radius: var(--radius-card)`
  - Icon placeholder: `width: 48px; height: 48px; background: var(--color-gold); border-radius: 50%; margin-bottom: var(--space-md); opacity: 0.8`
  - Quadrant heading: `font-size: var(--text-subheading); color: var(--color-gold); font-family: var(--font-serif); text-transform: uppercase; letter-spacing: var(--tracking-wide)`
  Style `#figures`:
  - `.portrait-row`: `display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-md); margin-bottom: var(--space-xl)`
  - `.portrait-card`: `text-align: center; padding: var(--space-md)`; hover lift from `plan.md §5.3`
  - Portrait heading: `font-family: var(--font-serif); font-size: var(--text-subheading); margin: var(--space-sm) 0 var(--space-xs)`
  Verify: strategies show as a 2×2 grid; portrait gallery shows 4-per-row; hover lifts cards.

- [ ] **3.11 — Write CSS §18–20: maps, methodology teaser, footer**
  Style `#maps`:
  - Three `.map-panel` stacked vertically, each `min-height: 70vh`
  - Panel image: `position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover`
  - Overlay text left-aligned, bottom-positioned via `.map-panel__overlay`
  Style `#methodology`: three `.archive-teaser` items in a row — icon + country + archive name; CTA button centred below.
  Style `.site-footer`: `background: var(--color-deep-ocean); color: var(--color-text-muted); padding: var(--space-xl) 0`; flex layout — nav links left, copyright centre, empty right; credits list below in small text.
  Verify: map panels stack with full-bleed images and readable text overlay; footer is compact and legible.

- [ ] **3.12 — Write CSS §21–22: `researcher.html` and `sources.html` page overrides**
  For `researcher.html`:
  - `.edu-timeline li`: left-border style matching main timeline but in a lighter colour
  - `.publication-card`: white/parchment card with citation metadata in muted colour
  - `.languages-list meter`: style the HTML `<meter>` element or replace with a CSS-only progress bar using `--level` CSS custom property on each `<li>`
  - `.interest-tags li`: pill badge style matching `.strategy-badge` but smaller
  For `sources.html`:
  - `table`: full-width, `border-collapse: collapse`, alternating row backgrounds (`var(--color-parchment)` / `var(--color-sand)`), `<th>` in terracotta
  - `.glossary`: `column-count: 2; column-gap: var(--space-xl)` — auto two-column on desktop
  - `.method-card`: three equal cards in a row with top border in terracotta
  Verify: both secondary pages look polished and consistent with the main design system.

- [ ] **3.13 — Write CSS §23: utility classes**
  Write:
  - `.reveal` — sets initial state `opacity: 0; transform: translateY(50px); transition: opacity 0.9s, transform 0.9s` for CSS fallback when GSAP unavailable
  - `.reveal.is-visible` — `opacity: 1; transform: translateY(0)` (toggled by JS as a fallback)
  - `.stagger-children > *` — same initial hidden state
  - `.visually-hidden` — `position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap`
  - `.text-gold` — `color: var(--color-gold)`
  - `.text-terracotta` — `color: var(--color-terracotta)`
  - `.text-muted` — `color: var(--color-text-muted)`
  Verify: `.visually-hidden` elements are invisible but accessible; `.reveal` initial state is hidden.

- [ ] **3.14 — Write CSS §24: all responsive media queries**
  Write all `@media` blocks in a single pass. For each breakpoint, apply the rules from `plan.md §6 Responsive Design`:
  - `@media (max-width: 767px)`: stack all `.split` to single column; `.portrait-row` → `grid-template-columns: repeat(2, 1fr)`; `#contemporary .grid-4` → single column; `#strategies` → single column; hide `.chapter-image` text overlays if needed
  - `@media (min-width: 768px)`: `.split` → two columns; contemporary bridge → `repeat(2, 1fr)`
  - `@media (min-width: 1024px)`: contemporary bridge → `repeat(4, 1fr)`; portrait gallery → `repeat(4, 1fr)`
  - Add hamburger nav toggle styles at `max-width: 767px`: `.site-nav__links` hidden by default, `.site-nav__links.is-open` shown as dropdown
  Verify: resize browser from 375px to 1400px — no horizontal scroll at any width; all multi-column layouts stack correctly on mobile.

- [ ] **3.15 — Write CSS §25: `prefers-reduced-motion` block**
  Add as the final CSS block, verbatim from `agents.md §9`:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
    }
  }
  ```
  Also set `.scroll-cue { animation: none }` within this block.
  Verify: in browser DevTools, enable "Emulate prefers-reduced-motion: reduce" — all animations stop immediately.

---

## Phase 4 — GSAP Animations
*Goal: `js/main.js` fully written with all animations from `plan.md §5`. All animations respect `prefers-reduced-motion`. Performance is smooth (no jank on scroll).*

- [ ] **4.1 — Write `main.js` §1–3: setup, guard, and navigation behaviour**
  Write the first three sections of `main.js` in order:
  - §1: `gsap.registerPlugin(ScrollTrigger)` inside `DOMContentLoaded`
  - §2: `const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches`
  - §3: Navigation scroll behaviour — use `ScrollTrigger.create` to add/remove `.scrolled` class on `.site-nav` when page scrolls past 80px. Mobile hamburger toggle: add click handler on hamburger button to toggle `.is-open` on `.site-nav__links`. Active section highlighting: use `ScrollTrigger` `onEnter`/`onLeave` per section to add/remove `.active` class on corresponding nav links.
  Comment every GSAP block per `agents.md §10`.
  Verify: nav gains dark background on scroll; hamburger opens/closes on mobile; no console errors.

- [ ] **4.2 — Write `main.js` §4: hero load animations and Ken Burns effect**
  Inside `if (!prefersReducedMotion)` block, write the hero animation sequence from `plan.md §4.1`:
  ```javascript
  // Hero title — fades up 40px on page load
  gsap.from(".hero__title", { opacity: 0, y: 40, duration: 1.2, ease: "power3.out" });
  // Hero subtitle — fades up 30px, 0.4s delay
  gsap.from(".hero__subtitle", { opacity: 0, y: 30, duration: 1, delay: 0.4, ease: "power3.out" });
  // Hero tagline — fades in, 0.9s delay
  gsap.from(".hero__tagline", { opacity: 0, duration: 0.8, delay: 0.9 });
  // Scroll cue — fades in at 1.4s
  gsap.from(".scroll-cue", { opacity: 0, duration: 0.6, delay: 1.4 });
  // Hero background — Ken Burns: slow scale from 1 to 1.05 over 8s
  gsap.to(".hero-bg", { scale: 1.05, duration: 8, ease: "none" });
  ```
  Also in `gsap.matchMedia` desktop block, write the hero parallax scroll-out (`yPercent: 30, scrub: true`).
  Verify: on page load, title, subtitle, and tagline appear in sequence; hero image has subtle zoom; scroll causes background parallax.

- [ ] **4.3 — Write `main.js` §5: global `.reveal` and `.stagger-children` utilities**
  Write the two reusable ScrollTrigger utilities from `plan.md §5.1` inside `if (!prefersReducedMotion)`:
  ```javascript
  // Global .reveal — fade up any element with this class when it enters viewport
  document.querySelectorAll('.reveal').forEach(el => { ... });
  // Global .stagger-children — stagger-animate children of any .stagger-children container
  document.querySelectorAll('.stagger-children').forEach(container => { ... });
  ```
  Comment each block per the rule.
  Verify: add `.reveal` to a heading in `index.html`, open browser — heading appears with fade-up when scrolled into view.

- [ ] **4.4 — Write `main.js` §6: expulsion stat counters**
  Write a counter animation function triggered by `ScrollTrigger` `onEnter` for `#expulsion`. Each `.stat-number` element has a `data-target` attribute with its final value. The function uses `requestAnimationFrame` to count from 0 to the target over 2 seconds.
  Add `data-target="300000"`, `data-target="4"`, `data-target="7"` to the three stat number elements in `index.html`.
  Verify: scroll to expulsion section — numbers count up from zero; animation does not re-trigger if user scrolls back.

- [ ] **4.5 — Write `main.js` §7: Chapter II Mediterranean route SVG draw**
  Create a simple inline SVG in the Chapter II section in `index.html` — a stylised path from Spain to Istanbul across the Mediterranean. The `<path>` has `fill: none; stroke: var(--color-gold); stroke-width: 2` and uses `stroke-dasharray` / `stroke-dashoffset` technique.
  In `main.js`, animate `strokeDashoffset` from full path length to 0 using `scrollTrigger: { scrub: true }` so the line draws as the user scrolls through the section.
  Verify: scroll through Chapter II — a gold line gradually draws from left (Spain) to right (Istanbul).

- [ ] **4.6 — Write `main.js` §8: parallax backgrounds (desktop only)**
  Inside `gsap.matchMedia("(min-width: 768px)")`, write parallax animations for:
  - `#expulsion` background: `yPercent: -25, ease: "none", scrub: true`
  - `#chapter-4` background: `yPercent: -20, ease: "none", scrub: true`
  - `#maps` three panels: each at a slightly different rate (`yPercent: -15`, `-18`, `-12`) to create depth
  Each must have a comment describing what it does and when it fires.
  Verify: on desktop, scroll through expulsion and chapter 4 — backgrounds drift at different speed than foreground text.

- [ ] **4.7 — Write `main.js` §9: four strategies quadrant entrance**
  Animate each `.strategy-quadrant` entering from its respective corner:
  - Top-left quadrant: `from({ x: -60, y: -60, opacity: 0 })`
  - Top-right quadrant: `from({ x: 60, y: -60, opacity: 0 })`
  - Bottom-left quadrant: `from({ x: -60, y: 60, opacity: 0 })`
  - Bottom-right quadrant: `from({ x: 60, y: 60, opacity: 0 })`
  All: `duration: 0.8, ease: "power2.out"`, `scrollTrigger: { trigger: "#strategies", start: "top 75%" }`
  Verify: scroll to strategies section — four cards fly in from corners simultaneously.

- [ ] **4.8 — Write `main.js` §10–11: page-specific interactions**
  §10 — `researcher.html` conference accordion: the `<details>`/`<summary>` elements work natively in HTML, but add a smooth height transition using `max-height` CSS + JS toggle for browsers that support it. Check `document.location.pathname` to run this code only on `researcher.html`.
  §11 — `sources.html`: no GSAP needed. Add a plain JS search/filter for the glossary — an `<input type="search">` above the `<dl>` that filters visible `<dt>`/`<dd>` pairs by text match. Show "No results" if nothing matches.
  Verify: accordion on researcher page opens with smooth animation; glossary filter narrows terms in real time.

- [ ] **4.9 — Final animation audit: add `.reveal` and `.stagger-children` classes to HTML**
  Now that animations are working, go back through `index.html` and add `.reveal` to every standalone heading and paragraph that should fade in, and `.stagger-children` to every container whose children should stagger. Apply to: contemporary bridge card container, timeline items, chapter text blocks, portrait rows, map overlay text, methodology archive teasers.
  Verify: scroll through the entire `index.html` from top to bottom — all sections animate in cleanly with no elements permanently hidden.

---

## Phase 5 — Image Sourcing and Optimisation
*Goal: all confirmed public domain images downloaded, named correctly, sized for web, and placed in the right directory. No broken `<img>` paths remain.*

- [ ] **5.1 — Download hero image: Braun & Hogenberg Constantinople 1572**
  Source: `https://commons.wikimedia.org/wiki/File:1572_bird%27s_eye_view_map_of_Constantinople_-_Byzantium_Nunc_Constantinopolis.jpg`
  Download the largest available resolution. Save as `images/hero/mediterranean-map-hero.jpg`.
  Verify: file exists at the path; dimensions are at least 2000px wide.

- [ ] **5.2 — Download and place all map images**
  Download and save in `images/maps/`:
  - `piri-reis-mediterranean.jpg` from `commons.wikimedia.org/wiki/File:Piri_Reis_map_of_Europe_and_the_Mediterranean_Sea.jpg`
  - `portolan-1590.jpg` from `commons.wikimedia.org/wiki/File:1590_Portolan_chart_of_the_Mediterranean_Sea_and_Europe.png` (convert to JPEG)
  - `braun-hogenberg-constantinople-1572.jpg` — same file as hero but a separate copy for use in Chapter V map section
  - `lepanto-map.jpg` from `commons.wikimedia.org/wiki/File:Battle_of_Lepanto_1571.jpg`
  Verify: all four files exist in `images/maps/`; each is at least 800px wide.

- [ ] **5.3 — Download and place all paintings**
  Download and save in `images/paintings/`:
  - `mestre-denia-1613.jpg` from `commons.wikimedia.org/wiki/File:La_Expulsi%C3%B3n_en_el_Puerto_de_Denia._Vicente_Mostre.jpg`
  - `oromig-grao-valencia-1616.jpg` from `commons.wikimedia.org/wiki/File:Embarco_moriscos_en_el_Grao_de_valencia.jpg`
  - `moriscos-elect-king-vierge.jpg` from `commons.wikimedia.org/wiki/File:Los_Monfies_de_las_Alpujarras_Illustration_pag_204.jpg`
  - `spy-cesare-ripa-1618.jpg` — search Wikimedia Commons for Cesare Ripa *Nova Iconologia* 1618 spy image
  Verify: all four files exist; no file is below 400px on its shorter dimension.

- [ ] **5.4 — Download and place all portrait images**
  Download and save in `images/portraits/`:
  - `philip-ii-titian.jpg` from `commons.wikimedia.org/wiki/File:Philip_II,_King_of_Spain_(by_Titian%27s_school).jpg`
  - `selim-ii.jpg` from `commons.wikimedia.org/wiki/File:Sultan_Selim_II_with_2_servants.jpg`
  - `sokollu-mehmed-pasha.jpg` from `en.wikipedia.org/wiki/File:Mehmed_Sokolović_(ca_1505-1579).png`
  - `kilij-ali-pasha.jpg` from `commons.wikimedia.org/wiki/File:Lala_Mustafa_Paşa_ve_Kılıç_Ali_Paşa.JPG`
  - `yunus-dogan.jpg` — placeholder: create a solid `#1E3A5F` rectangle at 400×400px as a placeholder until the researcher provides a photo
  Verify: all five files exist in `images/portraits/`.

- [ ] **5.5 — Download atmospheric chapter images**
  Find and download atmospheric public domain images for chapter section backgrounds. Save in `images/chapters/`. Each must be ≥ 1200px wide and clearly public domain:
  - `alpujarras-mountains.jpg` — mountainous Spanish landscape (search Wikimedia Commons for Alpujarras)
  - `algiers-harbor.jpg` — historical view of Algiers harbour (16th–19th century engraving or painting)
  - `venice-lagoon.jpg` — Venice lagoon or canal, historical view
  - `galata-istanbul.jpg` — Galata tower or Golden Horn historical image
  - `mediterranean-sea.jpg` — open Mediterranean sea, historical map or painting background
  Record each source URL in a new file `images/chapters/SOURCES.md` for audit trail.
  Verify: five files exist; `SOURCES.md` lists their origins.

- [ ] **5.6 — Optimise all images for web delivery**
  Process every image in `images/` (excluding `.gitkeep` and `.md` files):
  - Hero image: resize to 1920px wide, compress to ≤ 300KB JPEG at quality 85
  - Chapter backgrounds and map panels: resize to 1600px wide, compress to ≤ 200KB
  - Portraits: resize to 400px wide (square crop centred), compress to ≤ 60KB
  - Paintings: resize to 1200px wide, compress to ≤ 150KB
  - Create `*-sm.jpg` versions (768px wide) of hero and all full-bleed background images for `srcset`
  Use any available image editor or command-line tool available on the system (ImageMagick if installed; otherwise document that manual optimisation is needed).
  Verify: no JPEG in `images/` exceeds the limits above; `*-sm.jpg` files exist for hero and map panels.

- [ ] **5.7 — Update HTML `srcset` attributes for all large images**
  For every `<img>` that uses a full-bleed background (hero, expulsion, chapter backgrounds, map panels), update the markup to use `srcset`:
  ```html
  srcset="images/hero/mediterranean-map-hero-sm.jpg 768w,
          images/hero/mediterranean-map-hero.jpg 1920w"
  sizes="100vw"
  ```
  For portrait and painting images, a single `src` is sufficient — no `srcset` needed.
  Verify: in browser DevTools → Network tab, set throttle to "Fast 3G" and reload — the browser requests the `-sm` version at 375px viewport width.

---

## Phase 6 — Testing
*Goal: all three pages work correctly in Chrome, Firefox, and Safari on both desktop and mobile. No accessibility violations. No broken paths. Lighthouse score ≥ 85 on mobile.*

- [ ] **6.1 — Cross-browser smoke test: Chrome**
  Open `index.html`, `researcher.html`, and `sources.html` in Chrome (latest). Check:
  - All fonts load (Cormorant Garamond and Source Sans 3 visible)
  - All images load (no broken image icons)
  - Nav links navigate to correct pages
  - GSAP animations play on `index.html`
  - No console errors
  Document any failures in a `BUGS.md` file.

- [ ] **6.2 — Cross-browser smoke test: Firefox**
  Repeat 6.1 in Firefox (latest). Pay particular attention to: CSS `backdrop-filter` (nav); `column-count` on the glossary; `<meter>` element appearance; SVG route draw animation.
  Document any failures in `BUGS.md`.

- [ ] **6.3 — Cross-browser smoke test: Safari**
  Repeat 6.1 in Safari (latest on macOS). Pay particular attention to: `scroll-behavior: smooth`; GSAP ScrollTrigger timing; `srcset` image loading; `<details>`/`<summary>` accordion styling.
  Document any failures in `BUGS.md`.

- [ ] **6.4 — Mobile viewport test at 375px**
  Using Chrome DevTools device emulator, set viewport to iPhone SE (375×667). Check every section of `index.html`:
  - No horizontal scroll at any point
  - All multi-column layouts are single-column
  - Typography is readable (no text smaller than 14px)
  - Images load and don't overflow
  - Nav hamburger works
  - GSAP parallax is disabled (verify no jank)
  Document any failures in `BUGS.md`.

- [ ] **6.5 — Keyboard navigation audit**
  Open `index.html` in Chrome. Press Tab from the top of the page. Verify:
  - Skip link is the first focusable element and jumps to `#main-content` when activated
  - All nav links are reachable and have visible focus outline (gold, 2px)
  - All `<a>` and `<button>` elements in the page are Tab-reachable in logical reading order
  - No focus traps (Tab cycles through the whole page and returns to the browser address bar)
  Repeat for `researcher.html` and `sources.html`.
  Document any failures in `BUGS.md`.

- [ ] **6.6 — Screen reader spot-check**
  Using macOS VoiceOver (`Cmd+F5`), navigate `index.html` with keyboard:
  - VoiceOver announces each `<section>` label via `aria-label`
  - Images are announced with their `alt` text (not as "image")
  - Pull quotes are announced as `blockquote`
  - The timeline is announced as a list
  - Portrait cards are announced with name and role
  Note any confusing announcements in `BUGS.md`.

- [ ] **6.7 — Colour contrast audit**
  Open Chrome DevTools → Accessibility → Colour Contrast. Verify these exact pairs meet WCAG AA (4.5:1):
  - `#F0E4CC` on `#162039`: expected ~13:1 ✓
  - `#F0E4CC` on `#1E3A5F`: expected ~9:1 ✓
  - `#2A1E14` on `#F2E8D5`: expected ~14:1 ✓
  - `#C9A84C` on `#162039` (gold on deep ocean): check — if below 4.5:1 for body text, use only for decorative elements and headings; use `#F0E4CC` for body text
  - `#B85C38` on `#F2E8D5` (terracotta on parchment): check — if below 4.5:1, switch to `#8B3A22` (burnt sienna) for text uses
  Document any failures in `BUGS.md` and apply fixes.

- [ ] **6.8 — All relative link audit**
  Search every `.html`, `.css`, and `.js` file for any occurrence of `http://`, `https://`, or an absolute path starting with `/` (except for CDN links in `<script>` and `<link>` tags, and Google Fonts `<link>` tags, which are permitted to be absolute).
  Fix any relative path violations found.
  Verify: `grep -r "https://doganyunus" morisco-thesis/` returns zero results.

- [ ] **6.9 — Validate all HTML files**
  Submit `index.html`, `researcher.html`, and `sources.html` to the W3C validator at `validator.w3.org`. Fix any errors (not warnings). Common issues to check: duplicate `id` attributes, unclosed tags, `<time>` elements missing `datetime`, `<img>` missing `alt`.
  Verify: all three files return zero errors from the W3C validator.

- [ ] **6.10 — Run Lighthouse audit on `index.html`**
  In Chrome DevTools → Lighthouse, run a mobile audit on `index.html`. Target scores:
  - Performance: ≥ 85
  - Accessibility: ≥ 95
  - Best Practices: ≥ 90
  - SEO: ≥ 90
  Common performance fixes: ensure images are compressed; ensure GSAP loads after page is interactive; ensure no render-blocking resources other than fonts.
  Document scores and any Critical or High severity issues in `BUGS.md`.

- [ ] **6.11 — Fix all items in `BUGS.md`**
  Address every documented failure from tasks 6.1–6.10 in priority order:
  1. Broken links or missing images (functional blockers)
  2. Accessibility failures (WCAG violations)
  3. Cross-browser rendering issues
  4. Lighthouse performance issues
  5. Visual polish issues
  After fixes, re-run the relevant tests to confirm resolution.
  Verify: `BUGS.md` has no open items; all fixes tested.

---

## Phase 7 — GitHub Pages Deployment
*Goal: live site at `doganyunus.github.io/morisco-thesis` with all pages accessible and all relative paths resolving correctly in the GitHub Pages subdirectory context.*

- [ ] **7.1 — Create GitHub repository**
  Create a public repository named `morisco-thesis` on the `doganyunus` GitHub account. Do not initialise with a README — the local git already has one.
  Verify: `https://github.com/doganyunus/morisco-thesis` is accessible.

- [ ] **7.2 — Set remote and push initial commit**
  Inside `morisco-thesis/`:
  ```bash
  git add .
  git commit -m "Initial build: complete HTML, CSS, JS, and images"
  git branch -M main
  git remote add origin https://github.com/doganyunus/morisco-thesis.git
  git push -u origin main
  ```
  Verify: all files appear on GitHub in the correct folder structure; no files missing.

- [ ] **7.3 — Enable GitHub Pages**
  On GitHub: go to repository Settings → Pages → Source. Select `Deploy from a branch`, branch `main`, folder `/ (root)`. Save.
  Wait for the deployment action to complete (usually 1–2 minutes).
  Verify: GitHub shows the site URL `https://doganyunus.github.io/morisco-thesis/`; clicking it loads `index.html`.

- [ ] **7.4 — Test all pages on the live URL**
  Open `https://doganyunus.github.io/morisco-thesis/` in a browser. Check:
  - `index.html` loads correctly
  - Navigate to `researcher.html` via nav link — loads correctly
  - Navigate to `sources.html` via nav link — loads correctly
  - Back button works correctly on all three pages
  - All images load (no broken icons)
  - Fonts load (not falling back to system serif/sans)
  - GSAP animations play
  Verify: no 404 errors in the Network tab for any resource.

- [ ] **7.5 — Test all image paths in the GitHub Pages subdirectory context**
  GitHub Pages serves the site at `/morisco-thesis/` (a subdirectory), not `/`. All relative paths must resolve correctly in this context. Specifically verify:
  - CSS `url('../images/...')` paths resolve correctly
  - All `<img src="images/...">` paths in HTML resolve correctly
  - The favicon loads
  If any images show as 404, the path structure needs adjustment.
  Verify: open browser DevTools → Network tab on the live URL — zero 404 responses for images or stylesheets.

- [ ] **7.6 — Test the live site on a real mobile device**
  Open `https://doganyunus.github.io/morisco-thesis/` on an actual smartphone (not an emulator). Check:
  - Page scrolls smoothly
  - No horizontal overflow
  - Images load at appropriate sizes (the `-sm.jpg` versions should load)
  - Nav hamburger works
  - Touch interactions work on all interactive elements
  Verify: site is usable on mobile without zooming or horizontal scrolling.

- [ ] **7.7 — Add a canonical URL `<meta>` and verify Open Graph preview**
  Add `<link rel="canonical" href="https://doganyunus.github.io/morisco-thesis/">` to `index.html`.
  Test the Open Graph preview by pasting the URL into a social card checker (e.g. `opengraph.xyz`). Verify: title, description, and hero image appear correctly in the preview card.

- [ ] **7.8 — Tag the release**
  Create a git tag for the initial deployment:
  ```bash
  git tag -a v1.0.0 -m "Initial public release"
  git push origin v1.0.0
  ```
  Verify: tag appears in the GitHub repository's Releases section.

---

## Phase 8 — Post-Launch Polish
*These tasks are not blockers for launch but should be completed within the first week after deployment.*

- [ ] **8.1 — Replace the portrait placeholder with a real photo**
  When Yunus Doğan provides a headshot, replace `images/portraits/yunus-dogan.jpg`. Crop to square (400×400px), compress to ≤ 60KB, update `alt` attribute with a natural-language description. Delete `images/chapters/SOURCES.md` noting this task as done after replacing.

- [ ] **8.2 — Refine animation timing on real devices**
  After watching the site on 3+ real devices, adjust any animation durations or easing values that feel slow or jarring. Common adjustments: reduce hero title duration from 1.2s to 0.9s on mobile; increase stagger delay if cards overlap awkwardly.

- [ ] **8.3 — Add the bibliography to `sources.html`**
  Replace the `<!-- bibliography: to be added -->` comment with the full primary and secondary bibliography from `research.md §Part VIII`. Format as a `<ul>` with `<li>` elements, hanging indent via CSS.

- [ ] **8.4 — Run a final Lighthouse audit post-deployment**
  Run Lighthouse on the live GitHub Pages URL (not localhost). Post-deployment scores may differ from local due to CDN latency. Record the final scores in `README.md`. If Performance drops below 80, investigate and fix.

- [ ] **8.5 — Proofread all visible text**
  Read every visible word on all three pages. Check: spelling, punctuation, consistency of capitalisation for proper nouns (Morisco, Mudéjar, limpieza de sangre, Sublime Porte), historical dates, and name spellings as per `agents.md §12`.

---

## Summary

| Phase | Tasks | Estimated sessions |
|-------|-------|-------------------|
| 0 — Project Setup | 5 | 1 |
| 1 — Content Preparation | 4 | 2 |
| 2 — HTML Structure | 7 | 4 |
| 3 — CSS Styling | 15 | 5 |
| 4 — GSAP Animations | 9 | 3 |
| 5 — Images | 7 | 2 |
| 6 — Testing | 11 | 3 |
| 7 — Deployment | 8 | 1 |
| 8 — Post-launch | 5 | ongoing |
| **Total** | **71** | **~21** |

---

*Last updated: March 2026*
*Source of truth: `agents.md` (rules) · `plan.md` (design) · `research.md` (content)*
