# Website Plan: Morisco Thesis Portfolio
## *Moriscos and the Ottoman Empire: Entangled Histories in the Early Modern Mediterranean (1520–1620)*

**Deploy target:** `doganyunus.github.io/morisco-thesis`
**Stack:** Plain HTML · CSS · Vanilla JS · GSAP + ScrollTrigger (CDN)
**Last updated:** March 2026

---

## 1. Architecture Decision: Hybrid Multi-Page

### Decision: 1 primary scrollytelling page + 2 supporting pages

**Justified as follows:**

A pure single-page approach would work for the scrollytelling narrative, but would make the researcher CV and methodology appendix feel forced into the scroll. A pure multi-page approach would break the cinematic rhythm of the thesis story. The hybrid solves both:

| File | Role | Why separate? |
|------|------|---------------|
| `index.html` | Full scrollytelling narrative — the thesis journey | Core experience; long scroll; all animations live here |
| `researcher.html` | About Yunus Doğan — bio, CV, publications, links | CV content is dense and tabular; wrong rhythm for scroll narrative |
| `sources.html` | Archives, methodology, bibliography | Reference material; users scan, not scroll; needs its own layout |

All three pages share one CSS file and one JS file. Internal links between pages use relative paths only (`href="researcher.html"`, `href="sources.html"`). No domain is hardcoded anywhere.

---

## 2. Site Map

```
morisco-thesis/
│
├── index.html              ← Primary narrative scroll
├── researcher.html         ← About the researcher
├── sources.html            ← Sources & methodology
│
├── css/
│   └── main.css            ← Single stylesheet for all three pages
│
├── js/
│   └── main.js             ← Single JS file for all animations & interactions
│
├── images/
│   ├── hero/               ← Hero section backgrounds (large, atmospheric)
│   │   └── mediterranean-map-hero.jpg
│   ├── maps/               ← Historical maps and cartography
│   │   ├── piri-reis-andalusia.jpg
│   │   ├── braun-hogenberg-constantinople-1572.jpg
│   │   ├── lepanto-map.jpg
│   │   ├── portolan-1590.jpg
│   │   └── morisco-expulsion-routes.jpg
│   ├── portraits/          ← Historical portraits of key figures
│   │   ├── philip-ii-titian.jpg
│   │   ├── selim-ii.jpg
│   │   ├── sokollu-mehmed-pasha.jpg
│   │   ├── kilij-ali-pasha.jpg
│   │   └── yunus-dogan.jpg
│   ├── paintings/          ← Expulsion paintings and historical illustrations
│   │   ├── oromig-vinaros-1613.jpg
│   │   ├── mestre-denia-1613.jpg
│   │   ├── oromig-grao-valencia-1616.jpg
│   │   ├── moriscos-elect-king-vierge.jpg
│   │   └── spy-cesare-ripa-1618.jpg
│   ├── chapters/           ← Section-specific atmospheric images
│   │   ├── alpujarras-mountains.jpg
│   │   ├── algiers-harbor.jpg
│   │   ├── venice-lagoon.jpg
│   │   ├── galata-istanbul.jpg
│   │   └── mediterranean-sea.jpg
│   └── ui/                 ← Decorative elements, dividers, textures
│       ├── parchment-texture.jpg
│       ├── arabesque-divider.svg
│       └── scroll-indicator.svg
│
└── assets/
    └── favicon/
        ├── favicon.ico
        └── favicon.svg     ← A compass rose or crescent motif
```

---

## 3. Design System

### 3.1 Color Palette

```css
:root {
  /* Core palette */
  --color-deep-ocean:    #162039;   /* Deep Ottoman blue — hero backgrounds, nav */
  --color-cobalt:        #1E3A5F;   /* Mid-blue — section backgrounds */
  --color-terracotta:    #B85C38;   /* Terracotta — accent, headings on light bg */
  --color-burnt-sienna:  #8B3A22;   /* Darker accent — hover states, borders */
  --color-parchment:     #F2E8D5;   /* Aged parchment — main text bg */
  --color-sand:          #E0CEAA;   /* Warm sand — card backgrounds, dividers */
  --color-ink:           #2A1E14;   /* Near-black ink — body text on parchment */
  --color-gold:          #C9A84C;   /* Illuminated gold — pull quotes, icons */
  --color-gold-light:    #E8C97A;   /* Light gold — hover states */

  /* Text on dark backgrounds */
  --color-text-light:    #F0E4CC;   /* Warm off-white on deep blue/cobalt */
  --color-text-muted:    #A89880;   /* Muted warm grey — captions, metadata */

  /* Semantic roles */
  --color-bg-dark:       var(--color-deep-ocean);
  --color-bg-mid:        var(--color-cobalt);
  --color-bg-light:      var(--color-parchment);
  --color-accent:        var(--color-terracotta);
  --color-highlight:     var(--color-gold);
  --color-text-on-dark:  var(--color-text-light);
  --color-text-on-light: var(--color-ink);
}
```

**Alternating section rhythm:** The page alternates between dark (navy/cobalt) and light (parchment/sand) sections to create visual breathing and prevent monotony.

```
Hero            → dark (deep ocean, full bleed)
Contemporary    → dark (cobalt, text-heavy)
Historical ctx  → light (parchment, split layout)
Expulsion       → dark (full-bleed image, overlay text)
Ch I            → light
Ch II           → dark (map-forward)
Ch III          → light (spy/intelligence theme)
Ch IV           → dark (sea route map, cinematic)
Ch V            → light (Istanbul, warm tones)
Ch VI           → dark
Key Figures     → light (portrait gallery)
Maps            → dark (cartographic, atmospheric)
Sources         → light (reference-style)
About           → dark (closing, portrait)
Footer          → dark
```

### 3.2 Typography

**Google Fonts pair: Cormorant Garamond + Source Sans 3**

```html
<!-- In <head> of every HTML file -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Source+Sans+3:wght@300;400;600&display=swap" rel="stylesheet">
```

**Rationale:**
- **Cormorant Garamond** is a Garamond-revival with old-style ligatures and a distinctly manuscript, humanist feel. Its italic is exceptionally beautiful for pull quotes. It evokes the period without feeling costume-y.
- **Source Sans 3** is a clean, highly legible grotesque designed for long reading. It pairs with Cormorant without competing, and ensures body text remains effortlessly readable on both dark and light backgrounds.

```css
:root {
  /* Type scale — fluid via clamp() */
  --font-serif:        'Cormorant Garamond', Georgia, serif;
  --font-sans:         'Source Sans 3', system-ui, sans-serif;

  --text-hero:         clamp(3rem, 7vw, 6.5rem);    /* Hero title */
  --text-display:      clamp(2.2rem, 4.5vw, 4rem);  /* Section titles */
  --text-heading:      clamp(1.6rem, 3vw, 2.4rem);  /* Chapter headings */
  --text-subheading:   clamp(1.2rem, 2vw, 1.6rem);  /* Sub-headings */
  --text-pullquote:    clamp(1.4rem, 2.5vw, 2rem);  /* Pull quotes */
  --text-body:         clamp(1rem, 1.2vw, 1.15rem); /* Body copy */
  --text-caption:      0.85rem;                      /* Image captions */
  --text-label:        0.75rem;                      /* Tags, metadata labels */

  /* Line heights */
  --leading-tight:     1.2;
  --leading-base:      1.6;
  --leading-loose:     1.85;

  /* Letter spacing */
  --tracking-wide:     0.08em;  /* Uppercase labels, nav */
  --tracking-normal:   0.01em;
}
```

### 3.3 Spacing and Layout

```css
:root {
  /* Spacing scale */
  --space-xs:    0.5rem;
  --space-sm:    1rem;
  --space-md:    2rem;
  --space-lg:    4rem;
  --space-xl:    7rem;
  --space-xxl:   12rem;

  /* Container widths */
  --container-narrow:  680px;   /* Body text columns */
  --container-mid:     900px;   /* Chapter layouts */
  --container-wide:    1200px;  /* Full site wrapper */

  /* Section vertical padding */
  --section-pad-y:     clamp(5rem, 10vw, 10rem);

  /* Border radius */
  --radius-sm:         4px;
  --radius-md:         8px;
  --radius-card:       12px;

  /* Transitions */
  --transition-fast:   0.2s ease;
  --transition-base:   0.4s ease;
  --transition-slow:   0.7s cubic-bezier(0.16, 1, 0.3, 1);
}
```

### 3.4 Image Treatment

- **Hero images:** Full viewport, dark overlay (`rgba(22, 32, 57, 0.55)`) so text reads cleanly
- **Historical maps and paintings:** Displayed with a slight warm sepia filter (`filter: sepia(15%) contrast(105%)`) to unify the visual language of public domain images that vary in quality
- **Portraits:** Circular or oval crop in the figures gallery, with a thin gold border (`border: 2px solid var(--color-gold)`)
- **All images:** `loading="lazy"` except the hero; `object-fit: cover` for consistent sizing

---

## 4. Page-by-Page Content Plan

### 4.1 `index.html` — The Scrollytelling Narrative

#### Global nav (sticky, top)

```
[compass rose favicon]  MORISCOS & THE OTTOMAN EMPIRE
                         Home · Researcher · Sources
```

- Transparent on hero, transitions to semi-opaque dark on scroll
- Mobile: hamburger menu collapses to drawer
- Active section highlighted via ScrollTrigger

---

#### Section 1: HERO

**Content:**
- Full viewport height
- Background: the Braun & Hogenberg 1572 Constantinople bird's-eye view, heavily colour-treated to deep navy/teal, with a slow `scale(1.05)` Ken Burns zoom on page load
- Title (Cormorant Garamond, very large): *Moriscos and the Ottoman Empire*
- Subtitle: *Entangled Histories in the Early Modern Mediterranean, 1520–1620*
- Tagline (smaller, Source Sans, italic): *A PhD dissertation by Yunus Doğan*
- Scroll indicator: animated downward arrow or line pulse
- Thin decorative horizontal rule with arabesque SVG motif between title and subtitle

**Animation (GSAP):**
```javascript
// On load — staggered fade-in
gsap.from(".hero-title",    { opacity: 0, y: 40, duration: 1.2, ease: "power3.out" });
gsap.from(".hero-subtitle", { opacity: 0, y: 30, duration: 1, delay: 0.4, ease: "power3.out" });
gsap.from(".hero-tagline",  { opacity: 0, duration: 0.8, delay: 0.9 });
gsap.from(".scroll-cue",    { opacity: 0, y: -10, duration: 0.6, delay: 1.4, repeat: -1, yoyo: true });

// Background parallax on scroll
gsap.to(".hero-bg", {
  yPercent: 30,
  ease: "none",
  scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true }
});
```

---

#### Section 2: CONTEMPORARY BRIDGE — "History That Lives Today"

**Content:**
- Dark cobalt background, no image — pure text atmosphere
- Opening hook in large Cormorant italic pull-quote:
  *"In 2015, Spain offered citizenship to descendants of Sephardic Jews expelled in 1492. No comparable gesture was extended to the descendants of the Moriscos."*
- Four column cards (stacked on mobile) connecting 16th-century history to present:

| Card | 16th-century fact | Contemporary echo |
|------|------------------|-------------------|
| **The Refugee Question** | 300,000 Moriscos expelled 1609–1614; dispersed across the Mediterranean | Contemporary debates on refugee integration and religious minorities in Europe |
| **Fear of the "Other"** | Limpieza de sangre (purity of blood) statutes; suspicion of crypto-Islam; "fifth column" theory | Today's fears about Muslim communities in Western Europe; the proposed mosque in Granada |
| **Interconnected Worlds** | Europe, Ottoman Asia, and North Africa were entangled — their politics inseparable | Contemporary Mediterranean migration crises; the EU's relationship with Turkey and North Africa |
| **Empire and State-Building** | Habsburg Spain, the rise of Italian city-states, the Ottoman Empire — competing models of sovereignty | The national state model still shapes how we understand borders, citizenship, and belonging |

- Each card has a single-sentence header in gold, body in Source Sans, and a thin terracotta left border
- Bottom of section: a single line bridge into the thesis — *"This dissertation asks: how did the Moriscos navigate this world? What strategies did they use? And what does their story tell us about our own?"*

**Animation:** Cards stagger in left-to-right as section enters viewport.

---

#### Section 3: HISTORICAL CONTEXT — "Who Were the Moriscos?"

**Content:**
- Light parchment background
- Two-column split: left column = timeline; right column = explanatory text + one painting

**Left column — vertical timeline (dates as anchors):**
```
1492 → Fall of Granada; Capitulations guarantee Muslim rights
1499 → Cardinal Cisneros enforces mass conversions; Albaicín rebellion
1502 → Decree: all Castilian Muslims must convert or leave
1526 → Charles V decrees conversion in Aragon / Valencia
1556 → Philip II takes throne — tightening persecution begins
1567 → Pragmática: Arabic banned, manuscripts destroyed
1568 → Alpujarras Rebellion ignites
1609 → Edict of Expulsion signed, 22 September
1614 → Final expulsions complete — ~300,000 people displaced
```

**Right column — key text blocks:**
- "The Mudejars" — who they were before forced conversion
- "The New Christians" — the limpieza de sangre system, the Inquisition
- "Between Two Faiths" — crypto-Islam, taqiyya, cultural survival
- Image: *Embarco moriscos en el Grao de Valencia* (Pere Oromig, 1616) with caption

**Animation:** Timeline dots animate on in sequence; right column text blocks fade in on scroll.

---

#### Section 4: THE EXPULSION — Full-Width Cinematic Break

**Content:**
- Full viewport parallax image: *La Expulsión en el Puerto de Denia* (Vicente Mestre, 1613)
- Dark overlay
- Centered text overlay: large numerals and short phrases

```
~ 300,000  people expelled
  4 years  of successive decrees (1609–1614)
  7 ports  of embarkation along the Spanish coast
```

- Below the numbers, a single sentence: *"It was the largest forced displacement in early modern European history."*
- Scroll-trigger scrub: as user scrolls, the image translates upward (parallax) and the text fades from center

**Animation:**
```javascript
// Number counter — counts up as section enters
ScrollTrigger.create({
  trigger: ".expulsion-stats",
  onEnter: () => animateCounters()
});

// Parallax background
gsap.to(".expulsion-bg", {
  yPercent: -25,
  ease: "none",
  scrollTrigger: { scrub: true }
});
```

---

#### Section 5: CHAPTER SUMMARIES — "The Research"

This section introduces each chapter of the dissertation as a distinct visual block. Each chapter gets a dedicated sub-section with its own atmosphere.

---

##### Chapter I — Setting the Stage (1492–1568)

**Visual:** Piri Reis Andalusia map (full-bleed, sepia-treated)
**Theme:** From Mudejars to Moriscos; early appeals to North Africa, Mamluks, Ottomans
**Layout:** Image left (60%), text right (40%)
**Key claim (pull quote):** *"When Granada's hour of need came, no assistance was forthcoming from any quarter whatsoever."* — L.P. Harvey
**Text:** Short narrative paragraph + 3 bullet-point findings

---

##### Chapter II — Between Empire and Rebellion (1568–1580)

**Visual:** Dark — full-bleed map image of the Alpujarras mountains + colour overlay in deep cobalt
**Theme:** Alpujarras Rebellion; appeals to Kılıç Ali Pasha; Sokollu Mehmed Pasha's strategy
**Layout:** Text left, atmospheric image/map panel right — reversed from Ch. I
**Key claim:** *"The Moriscos of Valencia and Aragon sent envoys to Istanbul in 1577, bearing gifts — and offering to fund an Ottoman fleet."*
**Narrative hook:** Tell the 1577 Istanbul mission story (envoys to Sokollu Mehmed Pasha and Kılıç Ali Pasha — offering to pay for an Ottoman fleet along Valencia's coast)
**Strategy label:** [DIPLOMACY] in gold uppercase label

---

##### Chapter III — Networks of Trust: Spies and Brokers (1568–1609)

**Visual:** Light parchment; the Cesare Ripa *spy* woodcut (1618) as decorative right-side element
**Theme:** Moriscos as intelligence agents for the Ottoman Empire; double agents; spy networks
**Layout:** Text-forward, two columns; spy typology list on right
**Key claim:** *"Their trans-imperial identities were not weaknesses to hide — they were tools to deploy."*
**Spy network breakdown** (icon + label for each type):
- Political intelligence: reporting conditions in Spain
- Military intelligence: mapping fortifications, tracking fleets
- Covert plotting: facilitating conspiracies
- Double agency: working for both Ottoman and Spanish sides
**Strategy label:** [INTELLIGENCE]

---

##### Chapter IV — Crossing the Mediterranean (1609–1614)

**Visual:** Dark — full-width Mediterranean sea image or portolan chart with animated route overlay
**Theme:** Exile routes through France, Italy, Venice; Ottoman diplomatic interventions
**Layout:** Horizontal "route map" — three route cards arranged left to right on a stylised sea background

```
[Western Route]          [Central Route]           [Eastern Route]
Spain → Oran/Algiers     Spain → France →           Venice →
                         Italy → Venice             Ragusa → Istanbul
```

**Narrative hook:** The 1609 envoy Hajı Ibrahim Müteferrika arrives in Venice — addresses the Doge in Spanish without a translator. The 1614 letter from Marseille hidden in fishing nets.
**Strategy label:** [MOBILITY]

---

##### Chapter V — A New Life in Istanbul (1609–1620s)

**Visual:** Light warm tones — Braun & Hogenberg Constantinople map, Galata highlighted
**Theme:** Morisco settlement in Galata; conversion, identity, community formation; political intermediation
**Layout:** Split — left half the Constantinople map with Galata circled/highlighted; right half text + small portrait of Ahmad b. Qasim al-Hajarī
**Key claim:** *"Dressed half Spanish, half Turkish — the Moriscos embodied the in-betweenness that defined Mediterranean life."*
**Strategy label:** [CONVERSION & IDENTITY]

---

##### Chapter VI — Settling the Stateless

**Visual:** Dark — Ottoman Balkans/Aegean atmospheric image
**Theme:** Broader settlement patterns in North Africa, Anatolia, Balkans; Ottoman policy
**Layout:** Map-forward — stylised Ottoman Empire outline showing settlement zones:
```
Morocco/Salé → Tunisia → Algiers → Istanbul/Galata → Salonica → Anatolia → Balkans
```
**Key claim:** *"The Ottomans did not merely receive the Moriscos — they directed them, settled them, and made them subjects."*

---

#### Section 6: THE FOUR STRATEGIES — Visual Summary

**Content:**
- Dark cobalt background
- Section heading: "How the Moriscos Survived"
- Sub-heading: "Four strategies across a century of displacement"
- Four large icon + label + description blocks in a 2×2 grid (stacks to 1 column on mobile)

```
[Compass icon]  DIPLOMACY        [Eye icon]       INTELLIGENCE
Envoys to Istanbul,              Morisco spies across the
Paris, Venice, and London.       Mediterranean — Ottoman and
A stateless people negotiating   Spanish sides alike.
across imperial frontiers.

[Wave icon]     MOBILITY         [Crescent icon]  CONVERSION
From Granada to Algiers,         Public Christianity,
Marseille to Venice to           private Islam — and the
Istanbul — movement as           complex remaking of
political strategy.              identity after expulsion.
```

**Animation:** Each quadrant slides in from a different direction (top-left, top-right, bottom-left, bottom-right) as the section enters.

---

#### Section 7: KEY FIGURES — Portrait Gallery

**Content:**
- Light parchment background
- Two rows of portrait cards, 4 per row (2 on mobile, 1 on very small screens)
- Each card: oval portrait image, name (Cormorant Garamond bold), dates, 2-line description, role badge

**Row 1: Morisco Figures**
1. Ahmad b. Qasim al-Hajarī — Scholar and diplomat (c.1570–1640)
2. Aben Humeya — Leader, Alpujarras Rebellion (d. 1569)
3. Jerónimo Enríquez — Procurator, Marseille diaspora (c.1610)
4. Hajı Ibrahim Müteferrika — Ottoman envoy of Morisco origin (c.1609)

**Row 2: Ottoman and European Figures**
5. Sokollu Mehmed Pasha — Grand Vizier (1506–1579)
6. Kılıç Ali Pasha — Grand Admiral (c.1500–1587)
7. Sultan Selim II — Ottoman Sultan (r.1566–1574)
8. Philip II — King of Spain (r.1556–1598)

**Animation:** Cards stagger fade-in with slight upward movement, 0.1s apart.
**On hover:** Card lifts slightly (`translateY(-4px)`), gold border intensifies, short bio expands (CSS transition, no JS needed).

---

#### Section 8: MAPS AND GEOGRAPHY — "Entangled Geographies"

**Content:**
- Dark background, cartographic atmosphere
- Section heading + short paragraph on the Mediterranean as "trans-imperial contact zone"
- Three full-width map panels in sequence, each with descriptive overlay:

**Map Panel 1:** Piri Reis Mediterranean map — *"The Ottoman View"* — caption about Ottoman cartographic tradition
**Map Panel 2:** Braun & Hogenberg Constantinople 1572 — *"The City of Refuge"* — callout to Galata district
**Map Panel 3:** 1590 Portolan chart — *"The Routes"* — overlaid with simplified Morisco migration paths

- Below maps: Geographic Quick Reference (3-column list)
  - Iberian Peninsula locations
  - North African locations
  - Ottoman Empire locations

**Animation:** Each map panel uses parallax (`yPercent: -15` on scroll) so the maps drift slowly behind the text overlays.

---

#### Section 9: ABOUT THE RESEARCH — Methodology Teaser

**Content:**
- Light parchment
- Short paragraph on the trans-imperial, multi-archival methodology
- Three highlighted archival images/icons:
  - AGS Simancas (Spain)
  - ASV Venice (Italy)
  - BOA Istanbul (Turkey)
- Pull quote about the challenge of reconstructing stateless diaspora histories
- CTA: → Read full sources & methodology (`sources.html`)

---

#### Section 10: ABOUT THE RESEARCHER

**Content:**
- Dark background
- Two-column: left = portrait of Yunus Doğan; right = bio + links
- Short bio (3 sentences: who, what, where)
- Key credentials: EUI Florence, Paul Oskar Kristeller Fellowship, archival research in 7 countries
- Links: Full CV, Academia.edu or ORCID, email
- CTA: → Full researcher profile (`researcher.html`)

---

#### Footer

- Dark, minimal
- Thesis title and author
- Links: Home · Researcher · Sources
- Copyright line: `© Yunus Doğan, 2026 · PhD dissertation, European University Institute`
- Small print: image credits (public domain attributions)
- No hardcoded domain; all links relative

---

### 4.2 `researcher.html` — About the Researcher

**Layout:** Standard academic CV layout with visual polish — not a raw PDF résumé but a designed page.

**Sections:**
1. **Header:** Name, title, institution, photo, contact
2. **Research interests:** 4–6 keyword chips (terracotta pill badges)
3. **Education:** Timeline layout
4. **Publications:** Cards for each manuscript under review; styled as academic citations with full metadata
5. **Grants and fellowships:** Icon + year + description list
6. **Conference presentations:** Accordion (expandable list by year)
7. **Languages:** Horizontal bar charts showing proficiency levels (CSS-only, no library needed)
8. **Technical competencies:** Tag cloud / badge grid
9. **Teaching experience**
10. **Footer:** same as index.html

---

### 4.3 `sources.html` — Sources and Methodology

**Layout:** Reference-style, slightly denser typography, comfortable for reading.

**Sections:**
1. **Methodology overview:** 3-column intro cards (Trans-imperial approach / Microhistory / Digital Humanities)
2. **Archives table:** Full table of archives visited with country flags and key collection names
3. **Source types:** Visual breakdown (pie or icon grid) — diplomatic correspondence, inquisitorial records, civil chancery, Ottoman registers, chronicles
4. **Primary sources bibliography:** Alphabetical list, academic citation style
5. **Secondary sources:** Grouped by theme (Morisco studies, Ottoman history, Mediterranean history, diplomatic history)
6. **Glossary:** Full glossary from research.md, in two columns
7. **Footer:** same

---

## 5. Animation Plan by Section

All animations use GSAP 3 + ScrollTrigger. The CDN links are:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
```

### 5.1 Global Utilities (set up once in `main.js`)

```javascript
gsap.registerPlugin(ScrollTrigger);

// Reusable fade-up reveal for any element with class .reveal
document.querySelectorAll('.reveal').forEach(el => {
  gsap.from(el, {
    opacity: 0,
    y: 50,
    duration: 0.9,
    ease: 'power3.out',
    scrollTrigger: {
      trigger: el,
      start: 'top 85%',
      toggleActions: 'play none none none'
    }
  });
});

// Reusable stagger for any .stagger-children container
document.querySelectorAll('.stagger-children').forEach(container => {
  gsap.from(container.children, {
    opacity: 0,
    y: 40,
    duration: 0.7,
    ease: 'power2.out',
    stagger: 0.12,
    scrollTrigger: { trigger: container, start: 'top 80%' }
  });
});
```

### 5.2 Section-by-Section Animation Detail

| Section | Animation | Technique | Notes |
|---------|-----------|-----------|-------|
| **Hero** | Title/subtitle staggered fade-in on load; background Ken Burns zoom; parallax scroll out | GSAP timeline on load; `scrub: true` ScrollTrigger on bg | Parallax: `yPercent: 30` as hero exits viewport |
| **Contemporary Bridge** | Four cards slide in from left with stagger | `.stagger-children` utility | 0.15s stagger between cards |
| **Historical Context** | Timeline dots draw in top-to-bottom; right text blocks fade-up | SVG stroke animation + `.reveal` | Each timeline dot triggers its label |
| **Expulsion Stats** | Number counters (0 → 300,000 etc.) when section enters | Custom counter function, ScrollTrigger `onEnter` | Use `requestAnimationFrame` for smooth count |
| **Chapter II (1577 story)** | Horizontal map scroll — as user scrolls, a stylised route line draws from Spain to Istanbul | `drawSVG` (GSAP) or `stroke-dashoffset` CSS trick | SVG path of Mediterranean, drawn on scroll |
| **Chapter IV (Routes)** | Three route cards animate in left-to-right; sea background has slow parallax | `.stagger-children` + bg parallax | Cards appear with `xPercent: -30` start |
| **Four Strategies** | Each quadrant enters from its respective corner | Four individual `.from()` with `x` and `y` offsets | `scrub: false`, play once on enter |
| **Portrait Gallery** | Cards stagger fade-up in two rows | `.stagger-children` on each row | Row 2 has slight extra delay |
| **Map Panels** | Each map panel parallaxes at different rate; text overlay fades in when panel is centered | Per-element `scrub: true` with different `yPercent` | Creates depth between map and text layers |
| **Nav** | Transitions from transparent to dark-bg on first scroll; active section updates | ScrollTrigger `onEnter`/`onLeave` per section | `gsap.to(nav, { backgroundColor: ... })` |

### 5.3 CSS-Only Animations (no GSAP needed)

```css
/* Hover lift on portrait cards */
.portrait-card {
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}
.portrait-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.25);
}

/* Scroll indicator pulse */
@keyframes scrollPulse {
  0%, 100% { opacity: 1; transform: translateY(0); }
  50%       { opacity: 0.4; transform: translateY(6px); }
}
.scroll-cue { animation: scrollPulse 2s ease infinite; }

/* Nav link underline draw */
.nav-link::after {
  content: '';
  display: block;
  height: 1px;
  background: var(--color-gold);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform var(--transition-fast);
}
.nav-link:hover::after { transform: scaleX(1); }
```

---

## 6. Responsive Design

### Breakpoints

```css
/* Mobile first */
/* xs: 0–479px  — single column, large touch targets */
/* sm: 480–767px — still single column, slightly more density */
/* md: 768–1023px — 2-column layouts unlock */
/* lg: 1024px+  — full desktop layout */

@media (min-width: 768px)  { /* md — 2-col unlocks */ }
@media (min-width: 1024px) { /* lg — full layout   */ }
@media (min-width: 1400px) { /* xl — max-width cap */ }
```

### Key Responsive Behaviours by Section

| Section | Mobile (< 768px) | Desktop (≥ 1024px) |
|---------|-----------------|-------------------|
| Hero | Title scales to `clamp(2.5rem, 8vw, 4rem)`; portrait-format map crop | Full landscape map, large title |
| Contemporary Bridge | 4 cards stacked vertically | 2×2 grid or 4-column row |
| Historical Context | Timeline above, text below (stacked) | Left timeline, right text (split) |
| Chapter layouts | Image above, text below | Image 50%, text 50% side-by-side |
| Chapter IV routes | Cards stacked vertically | Horizontal 3-card row |
| Portrait Gallery | 2-per-row grid | 4-per-row grid |
| Map panels | Single column, image above text | Full-bleed parallax with text overlay |
| Researcher page | Single column, stacked | Two-column intro, table layout |

### Image Strategy for Small Screens

All large section background images use `srcset` with two sizes:
```html
<img
  srcset="images/maps/constantinople-sm.jpg 768w,
          images/maps/constantinople-lg.jpg 1600w"
  sizes="(max-width: 768px) 100vw, 100vw"
  src="images/maps/constantinople-lg.jpg"
  alt="1572 bird's-eye view of Constantinople by Braun and Hogenberg"
  loading="lazy"
>
```
On mobile, parallax is disabled via media query (parallax on mobile causes jank):
```javascript
const mm = gsap.matchMedia();
mm.add("(min-width: 768px)", () => {
  // parallax animations — desktop only
  gsap.to(".hero-bg", { yPercent: 30, ease: "none",
    scrollTrigger: { scrub: true } });
});
```

---

## 7. Accessibility

### Requirements and Implementation

| Requirement | Implementation |
|------------|----------------|
| All images have `alt` text | Mandatory attribute on every `<img>`; decorative images get `alt=""` + `role="presentation"` |
| Colour contrast ≥ 4.5:1 (WCAG AA) | Deep ocean + off-white text: ~13:1. Parchment + ink: ~14:1. Terracotta on parchment: checked against WCAG — use `#8B3A22` (darker) if needed |
| Keyboard navigation | All interactive elements reachable by `Tab`; focus visible via `outline: 2px solid var(--color-gold)` |
| Skip to main content | `<a class="skip-link" href="#main-content">Skip to main content</a>` as first element in `<body>` |
| Animated content | `prefers-reduced-motion` media query disables GSAP animations; elements appear at final state instead |
| Semantic HTML | `<main>`, `<nav>`, `<section>` with `aria-label`, `<article>` for chapter blocks, `<figure>` + `<figcaption>` for images |
| Form/link labels | All nav links and CTA buttons have descriptive text (no "click here") |
| Language attribute | `<html lang="en">` on all pages |

```css
/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

```javascript
// In main.js — check before registering ScrollTrigger animations
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReducedMotion) {
  // Register all GSAP animations
}
```

---

## 8. Technical Conventions

### CDN Stack (all via CDN, no npm)

```html
<!-- GSAP core + ScrollTrigger — always the last scripts before </body> -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"
        integrity="sha512-..." crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"
        integrity="sha512-..." crossorigin="anonymous"></script>
<script src="js/main.js" defer></script>
```

No jQuery, no Bootstrap, no React — everything in vanilla HTML/CSS/JS.

### HTML Template (shared structure for all 3 pages)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Moriscos & the Ottoman Empire — [PAGE TITLE]</title>
  <meta name="description" content="PhD dissertation by Yunus Doğan, European University Institute, 2026.">

  <!-- Open Graph (for link previews) -->
  <meta property="og:title" content="Moriscos & the Ottoman Empire">
  <meta property="og:description" content="Entangled Histories in the Early Modern Mediterranean, 1520–1620">
  <meta property="og:image" content="images/hero/mediterranean-map-hero.jpg">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Source+Sans+3:wght@300;400;600&display=swap" rel="stylesheet">

  <!-- Stylesheet -->
  <link rel="stylesheet" href="css/main.css">

  <!-- Favicon -->
  <link rel="icon" href="assets/favicon/favicon.svg" type="image/svg+xml">
</head>
<body>

  <a class="skip-link" href="#main-content">Skip to main content</a>

  <nav class="site-nav" aria-label="Main navigation">
    <!-- nav content -->
  </nav>

  <main id="main-content">
    <!-- page content -->
  </main>

  <footer class="site-footer">
    <!-- footer content -->
  </footer>

  <!-- GSAP (bottom of body) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <script src="js/main.js" defer></script>
</body>
</html>
```

### CSS Architecture (single `main.css`)

Structured in the following order using comments as dividers:
```
1.  Custom properties (design tokens)
2.  CSS reset / base styles
3.  Typography
4.  Layout utilities (.container, .grid, .flex)
5.  Component: Navigation
6.  Component: Buttons and CTAs
7.  Component: Cards (portrait, chapter, contemporary-bridge)
8.  Component: Timeline
9.  Component: Pull quotes
10. Component: Image treatments
11. Section: Hero
12. Section: Contemporary Bridge
13. Section: Historical Context
14. Section: Expulsion stats
15. Section: Chapter blocks (shared + per-chapter specifics)
16. Section: Four Strategies
17. Section: Portrait Gallery
18. Section: Maps
19. Section: About / Researcher teaser
20. Section: Footer
21. Page: researcher.html specific overrides
22. Page: sources.html specific overrides
23. Utilities (.reveal, .stagger-children, .skip-link, .visually-hidden)
24. @media queries (md, lg, xl)
25. @media (prefers-reduced-motion)
```

### JS Architecture (single `main.js`)

```javascript
// main.js structure
// ─────────────────
// 1. Imports / plugin registration
// 2. Utility: prefersReducedMotion check
// 3. Navigation: scroll behaviour + active section highlight
// 4. Hero: load animations + Ken Burns effect
// 5. Global: .reveal and .stagger-children ScrollTrigger setup
// 6. Section: Expulsion stat counters
// 7. Section: Chapter II route SVG draw
// 8. Section: Parallax backgrounds (desktop only via matchMedia)
// 9. Section: Four Strategies quadrant entrance
// 10. Section: Portrait card hover enhancement (JS-optional, CSS fallback exists)
// 11. Page-specific: researcher.html accordion for conference presentations
// 12. Page-specific: sources.html (none needed — CSS-only)
```

---

## 9. Image Sourcing and Credits

All images used must be either:
- Public domain (pre-1928 creation, or explicitly released)
- CC0 / CC-BY licensed from Wikimedia Commons or similar

### Confirmed Public Domain Sources (from research.md)

| Image | Source URL | Credit line for footer |
|-------|-----------|------------------------|
| Braun & Hogenberg Constantinople (1572) | commons.wikimedia.org/wiki/File:1572_bird%27s_eye_view... | Georg Braun & Frans Hogenberg, 1572. Public domain. |
| Piri Reis — Europe & Mediterranean | commons.wikimedia.org/wiki/File:Piri_Reis_map_of_Europe... | Piri Reis, 16th c. Public domain. |
| 1590 Portolan chart | commons.wikimedia.org/wiki/File:1590_Portolan_chart... | Joan Riezo, Messina, 1590. Public domain. |
| La Expulsión en el Puerto de Denia | commons.wikimedia.org/wiki/File:La_Expulsi%C3%B3n... | Vicente Mestre, 1613. Public domain. |
| Embarco moriscos — Grao de Valencia | commons.wikimedia.org/wiki/File:Embarco_moriscos... | Pere Oromig, 1616. Public domain. |
| Philip II (Titian's school) | commons.wikimedia.org/wiki/File:Philip_II,_King... | School of Titian, c.1550s. Public domain. |
| Sultan Selim II with servants | commons.wikimedia.org/wiki/File:Sultan_Selim_II... | Nakkaş Osman, c.1570. Public domain. |
| Sokollu Mehmed Pasha | en.wikipedia.org/wiki/File:Mehmed_Sokolović... | Dominicus Custos after G.B. Fontana, 1603. Public domain. |
| Kılıç Ali Pasha — Nusretname | commons.wikimedia.org/wiki/File:Lala_Mustafa_Paşa... | Ottoman manuscript *Nusretname*, 1570s. Public domain. |
| Battle of Lepanto (1571) | commons.wikimedia.org/wiki/File:Battle_of_Lepanto... | Anonymous, c.1571. Public domain. |
| Urrabieta y Vierge — Deportación | commons.wikimedia.org/wiki/File:Los_Monfies_de_las_Alpujarras... | Daniel Urrabieta y Vierge, 1859. Public domain. |

All image credits aggregated in the footer under: *"Historical images are in the public domain. Full attributions listed below."*

---

## 10. Prioritized Build Order

Build in this exact sequence to avoid rework. Each phase is independently testable.

### Phase 1 — Structure (estimated: 1 day)
**Goal:** All three HTML files exist with correct semantic structure; all sections present but unstyled.
1. Create file/folder structure
2. Write `index.html` — all sections with placeholder text, correct `<section>` tags with `id` attributes, all images referenced (even if missing)
3. Write `researcher.html` — full CV content in semantic markup
4. Write `sources.html` — archives table, glossary, bibliography
5. Add shared `<nav>` and `<footer>` to all three pages
6. Verify all relative links work (`href="researcher.html"`, `href="sources.html"`, `href="index.html"`)

### Phase 2 — Design System (estimated: 0.5 days)
**Goal:** CSS custom properties and typography applied; pages look intentional even without layout.
1. Create `css/main.css`
2. Write CSS reset and base styles
3. Define all custom properties (colors, fonts, spacing, transitions)
4. Apply typography scale: headings get Cormorant, body gets Source Sans
5. Verify fonts load from Google Fonts CDN

### Phase 3 — Layout (estimated: 1.5 days)
**Goal:** Every section has correct layout — grid, columns, full-bleed images — on desktop.
1. Navigation — sticky, transparent-to-dark behaviour (CSS only first)
2. Hero — full-viewport, background image, centered text
3. Contemporary Bridge — 4-card grid
4. Historical Context — split timeline/text layout
5. Expulsion — full-bleed stats overlay
6. Each chapter block — alternating image/text splits
7. Four Strategies — 2×2 grid
8. Portrait Gallery — 4-column card grid
9. Map panels — full-bleed with overlay text
10. Footer layout

### Phase 4 — Responsive (estimated: 1 day)
**Goal:** All sections work cleanly on a 375px mobile screen.
1. Audit every section at 375px
2. Apply mobile breakpoints: stack all multi-column layouts
3. Adjust font sizes via `clamp()` values
4. Reduce section padding on mobile
5. Test navigation hamburger menu
6. Test portrait gallery at 2-per-row on mobile

### Phase 5 — Images (estimated: 0.5 days)
**Goal:** All actual historical images downloaded, optimised, and placed.
1. Download all images from Wikimedia Commons sources listed above
2. Optimise: compress JPEGs to ≤ 300kb for hero, ≤ 150kb for cards and portraits
3. Create two-size versions for `srcset` (sm: 768px wide, lg: 1600px wide for hero; single size for cards)
4. Place in correct `images/` subdirectory
5. Verify all `src` and `srcset` paths are correct relative paths

### Phase 6 — GSAP Animations (estimated: 1 day)
**Goal:** All scroll animations working; performance is smooth.
1. Include GSAP + ScrollTrigger CDN links in all HTML files
2. Create `js/main.js`
3. Implement `prefersReducedMotion` guard
4. Hero load animations
5. Global `.reveal` and `.stagger-children` utilities
6. Navigation scroll behaviour
7. Expulsion stat counters
8. Chapter II route SVG draw (or simplified CSS version)
9. Parallax backgrounds (desktop only via `gsap.matchMedia`)
10. Four Strategies quadrant entrance

### Phase 7 — Accessibility Pass (estimated: 0.5 days)
1. Audit every `<img>` — add missing `alt` attributes
2. Check colour contrast with browser DevTools or WebAIM
3. Tab through entire site — fix any non-focusable interactive elements
4. Verify `skip-link` works
5. Add `aria-label` to all `<nav>` and `<section>` elements
6. Add `<html lang="en">` to all pages

### Phase 8 — GitHub Pages Deploy (estimated: 0.5 days)
1. Create GitHub repository: `doganyunus/morisco-thesis`
2. Push all files
3. Enable GitHub Pages from `main` branch / root
4. Verify live URL: `https://doganyunus.github.io/morisco-thesis/`
5. Check all relative links work in production (no 404s)
6. Test on actual mobile device

### Phase 9 — Polish (ongoing)
- Refine spacing and typography rhythm
- Fine-tune animation timing and easing curves
- Add loading states / skeleton screens if needed
- Browser test: Chrome, Firefox, Safari
- Performance audit: aim for Lighthouse score > 85 on mobile

---

## 11. Sections Reference Table

Quick reference for the `index.html` section structure.

| Section `id` | Label | Background | Key Visual | Strategy badge |
|-------------|-------|-----------|------------|----------------|
| `#hero` | — | Dark (map image) | Constantinople map parallax | — |
| `#contemporary` | History That Lives Today | Dark cobalt | 4 text cards | — |
| `#context` | Who Were the Moriscos? | Light parchment | Timeline + painting | — |
| `#expulsion` | The Expulsion | Dark (painting) | Mestre Denia 1613, stat overlay | — |
| `#chapter-1` | Setting the Stage | Light parchment | Piri Reis Andalusia map | — |
| `#chapter-2` | Between Empire and Rebellion | Dark cobalt | Alpujarras + Istanbul route | [DIPLOMACY] |
| `#chapter-3` | Networks of Trust | Light parchment | Cesare Ripa spy woodcut | [INTELLIGENCE] |
| `#chapter-4` | Crossing the Mediterranean | Dark (sea) | Portolan + route cards | [MOBILITY] |
| `#chapter-5` | A New Life in Istanbul | Light warm | Braun & Hogenberg, Galata callout | [CONVERSION] |
| `#chapter-6` | Settling the Stateless | Dark | Ottoman settlement map | — |
| `#strategies` | How the Moriscos Survived | Dark cobalt | 4-quadrant icon grid | — |
| `#figures` | Key Figures | Light parchment | Portrait gallery | — |
| `#maps` | Entangled Geographies | Dark | Map parallax panels | — |
| `#methodology` | About the Research | Light parchment | Archives teaser | — |
| `#about` | About the Researcher | Dark | Portrait + bio | — |
| `#footer` | — | Dark | — | — |

---

*Plan prepared: March 2026*
*For: Yunus Doğan portfolio website — doganyunus.github.io/morisco-thesis*
