# Systema Ratio — Design System & Architecture (`DESIGN.md`, v3 Kinetic Editorial)

**Systema Ratio** (*Hệ Thống Lý Trí*) synthesizes the editorial natural-history architecture of **Systema Intelligentiae** with the **OPERATE + READ** graph-and-inspector workspace of **Sci-Fi AI Atlas** to bring Đào Minh Châu’s *Học Tư Duy* (*Learning How to Think*, Hà Nội, 08/01/2026) alive in two standalone, culturally native editions:
- **Vietnamese Edition**: `vi.html` (`<html lang="vi">`) + `plates/vi/*.svg` (24 print-ready vector plates)
- **English Edition**: `en.html` (`<html lang="en">`) + `plates/en/*.svg` (24 print-ready vector plates)
- **Bilingual Gateway**: `index.html`

## 1. Semantic Visual Grammar ("Colour = Data Only" · *Systema Intelligentiae* Palette)

Surfaces stay calm and cool-neutral so colour always means data—never wallpaper:
- **Field-Guide Light Ground**: `--bg: #f5f6fb`, `--surface: #ffffff`, `--surface-2: #eef1f8`, `--surface-3: #e4e8f3`, `--ink: #15172e`, `--ink-2: #4a4f6a`, `--ink-3: #656b87`, `--line: #e1e5f0`, `--line-2: #cbd1e1`, `--ctrl-border: #7b829e` (`>= 3.5:1` non-text boundary contrast), `--accent: #3346e0` (cobalt-ultramarine), `--link-visited: #6b3fc4`, `--btn: #15172e` / `--btn-ink: #ffffff`.
- **Deep Cosmos Indigo Dark Ground**: `--bg: #0e1022`, `--surface: #171a33`, `--surface-2: #1f2342`, `--surface-3: #282d52`, `--ink: #f3f4fb`, `--ink-2: #b3b8d3`, `--ink-3: #8d93b3`, `--line: #2a2f52`, `--line-2: #3a4070`, `--ctrl-border: #646c99`, `--accent: #93a0ff`, `--link-visited: #c4b0ff`, `--btn: #f3f4fb` / `--btn-ink: #0e1022`.

| Domain / Chapter | Text Token (`>= 4.6:1`) | Light / Dark Text | Vivid Mark Token (`--m-*`) | Light / Dark Mark | Meaning |
|---|---|---|---|---|---|
| System 1 Traps & Biases | `--c-trap` | `#b81f2e` / `#ff7a86` | `--m-trap` | `#e5333f` / `#ff5c6a` | Crisis red: biases, fallacies, symptomatic traps |
| Ch. 1 · Overview / Metacognition | `--c-meta` | `#087087` / `#2fc7e6` | `--m-meta` | `#0aa6c9` / `#2fc7e6` | Wiring cyan: conscious supervision & 8-element frame |
| Ch. 2 · Creative Thinking | `--c-creative` | `#946200` / `#ffd23f` | `--m-creative` | `#e2a300` / `#ffd23f` | Program amber: divergence, redefinition, reframing |
| Ch. 3 · Critical Thinking | `--c-critical` | `#2458d3` / `#6e9bff` | `--m-critical` | `#2b6bef` / `#5b8cff` | Storage cobalt: two-tier immune filter & self-critique |
| Ch. 4 · Analytical Thinking | `--c-analytical` | `#0b7268` / `#38e0cf` | `--m-analytical` | `#0d9488` / `#38e0cf` | Make teal: structural decomposition ("flashlight in fog") |
| Ch. 5 · Logical Thinking | `--c-logical` | `#3346e0` / `#93a0ff` | `--m-logical` | `#3346e0` / `#93a0ff` | Ultramarine: formal grammar of valid inference |
| Ch. 6 · Systems Thinking | `--c-systems` | `#0b7547` / `#2dd490` | `--m-systems` | `#10a866` / `#2dd490` | Bio-emerald: wholes, emergence, R/B loops & delays (`//`) |
| Ch. 7 · Strategic Thinking | `--c-strategic` | `#b34a00` / `#ff9a3d` | `--m-strategic` | `#ff7a00` / `#ff9a3d` | Power tangerine: long-horizon agency, scenarios & game theory |
| Ch. 8 · Probabilistic Thinking | `--c-prob` | `#6835f0` / `#a88aff` | `--m-prob` | `#7a4dff` / `#a07fff` | CPU violet: distributions, Expected Value & Bayesian priors |
| Ch. 9 · Scientific Thinking | `--c-science` | `#bd1e68` / `#ff6ca8` | `--m-science` | `#ec3d8c` / `#ff5fa2` | Neuro magenta: falsifiability, controlled tests & convergence |

## 2. Kinetic Editorial Typography, Motion & Anti-Slop Hard Rules
- **Strict 3-Font System (`<= 3` Typefaces)**:
  - **Display (`--display`)**: `Fraunces` (variable optical-size soft serif `9..144`, weights `600..900`, roman + expressive italic accents) with `text-wrap: balance` and 100% Vietnamese diacritic coverage.
  - **Body, Subheads & Interactive Pills (`--body` / `--kicker`)**: `Plus Jakarta Sans` (`400..800`, 16px base, `tabular-nums lining-nums`, `text-wrap: pretty`, curly typographic quotes) across both web UI and standalone SVG plates.
  - **Monospace (`--mono`)**: `JetBrains Mono` (`>= 12px` floor) reserved for Bayesian formulas, probabilities, Decision Memos, Socratic AI prompts, and timeline markers.
- ***Systema Intelligentiae* Light & Deep Cosmos Dark Themes**: Clean `#f5f6fb` field-guide light paper and `#0e1022` deep cosmos indigo dark ground powered by `<meta name="color-scheme" content="light dark">`, `:root:has(> head > meta...)`, CSS `light-dark()`, `color-mix(in oklab, ...)` tint generation, and `@media (forced-colors: active)` high-contrast fallbacks.
- **Scroll-Driven Animations & Directional Transitions**:
  - Top 9-ray spectrum progress bar (`#scrollProgress`) driven by `animation-timeline: scroll(root block)` with lightweight JS scroll fallback.
  - Scrollytelling beam fills (`timeline-scope: --sc-1 .. --sc-9` + `view-timeline`) and `.scrolly-step` entry reveals (`@supports ((animation-timeline: view()) and (animation-range: entry))`), strictly gated behind `@media (prefers-reduced-motion: no-preference)`.
  - `document.startViewTransition({ update, types: [direction] })` slide transitions across all 7 views and 9 chapters.
- **Anti-Slop Guardrails**: Zero `border-left: 3px solid` stripes, zero decorative UI emoji (inline `<svg><symbol>` sprite + `<use>`), distinct `:visited` link styling, tactile button press states, and `44x44px` minimum touch targets.

## 3. Propulsive Narrative, 36 Real Case Studies & 7 Live Labs
1. **Cold-Open System 1 Mirror Test (`#sec-mirror`)**: Three 5-second intuition traps let readers catch their own System 1 misfiring before touching theory.
2. **Split-Screen Scrollytelling Flagship (`#sec-scrolly`)**: Scrolling 9 chapter acts on the left dynamically morphs a sticky right-hand **Live Prism Stage** (vector illustration + historical case flashpoint + Minh's life arc).
3. **36 Linked Real-World Case Studies Vault (`#view-cases` + 4 per chapter in `#view-reader`)**: Filterable by 5 industry domains, by Chapter 1–9, or live `/` search, each pairing a gripping real-world crisis/breakthrough (*Mata v. Avianca* ChatGPT fake lawsuits, J.C. Penney's \$4.3B anchoring crash, 1902 Hanoi's Cobra-Effect rat bounty, Abraham Wald, Toyota Andon, Boeing 737 MAX MCAS, Shell 1973 scenarios, USS Scorpion Bayesian search, Eddington's 1919 eclipse) with canonical external dossiers (`Wikipedia`, `NobelPrize.org`, `HBR`, `US NPS`, `James Lind Library`) and 1-click simulator links.
4. **7 Live Cognitive Simulators (`#view-labs`)**: Paul–Elder 8-Element Octagon, Wald Bomber Inversion, Systems Loops & Delay `τ`, 5 Game Theory Matrices, Bayesian 100-Grid & Black-Swan EV, 7-Step Scientific Convergence Reactor, plus **Lab #7: Personal Decision Stress-Tester & 1-Click Memo Builder** (5-axis pentagon radar gauge + clipboard Decision Memo export).
5. **24 Vector Book Plates & 23 Linked Classics**: 18 methodological plates + 6 narrative story vignettes alongside chapter-coded Book Spine Cards linking to Open Library and Google Books.

## 4. Responsive & Mobile Adaptation
- **<= 1140px**: Top 7-pill navigation collapses cleanly into a thumb-reachable 6-item **Fixed Mobile Bottom Bar** (`Story`, `36 Cases`, `Map`, `7 Labs`, `Biases`, `Chapters`) with `env(safe-area-inset-bottom)`.
- **<= 820px Method Atlas**: Defaults to scannable **Stage-Grouped Tool Cards** with instant scroll-to-inspector feedback, plus a 1-tap toggle for the full 960px cladogram.
- **Container-Query Master Table**: `@container (width < 680px)` transforms all 29 tool rows into labeled cards with full-width `<caption>`.
