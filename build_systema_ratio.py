#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds Systema Ratio (English + Vietnamese editions, 36 standalone print SVGs, and bilingual portal)."""
from pathlib import Path
from src.data_chapters_en import META_EN, CHAPTERS_EN
from src.data_chapters_vi import META_VI, CHAPTERS_VI
from src.data_atlas import TOOLS, PATHWAYS, BIASES, FALLACIES, EDITORIAL_NOTES
from src.svg_plates import build_plates
from src.template_app import render_edition
from src.template_css import APP_CSS

ROOT = Path(__file__).resolve().parent


def build_portal(cov_en: str, cov_vi: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" content="#15172e">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <script>
    try {{
      document.querySelector('meta[name="color-scheme"]').content = localStorage.getItem("sr-color-scheme") ?? "light dark";
    }} catch (e) {{}}
  </script>
  <title>Systema Ratio · Học Tư Duy / Learning How to Think — Kinetic Atlas &amp; 36 Case Studies</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600..900;1,9..144,600..800&family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..600&display=swap" rel="stylesheet">
  <style>{APP_CSS}
    .portal-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 26px;
      margin-block-start: 28px;
    }}
    @media (max-width: 860px) {{
      .portal-grid {{ grid-template-columns: 1fr; }}
    }}
    .portal-card {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: var(--surface);
      border: 2px solid var(--line);
      border-radius: var(--r-lg);
      padding: 28px;
      color: var(--ink);
      box-shadow: var(--shadow);
      transition: border-color 0.18s ease, transform 0.18s ease, box-shadow 0.18s ease;
    }}
    .portal-card:hover {{
      border-color: var(--accent);
      transform: translateY(-4px);
      box-shadow: var(--shadow-hover);
    }}
    .portal-cov-link {{
      display: block;
      text-decoration: none;
      margin-block-end: 18px;
    }}
  </style>
</head>
<body>
  <div id="scrollProgress"></div>
  <a href="#portal-heading" class="skip-link visually-hidden">Skip to edition selector</a>
  <header class="site-head">
    <div class="head-wrap" style="max-width:1200px;">
      <span class="brand">
        <span class="brand-mark" aria-hidden="true">
          <i style="background:var(--m-meta)"></i><i style="background:var(--m-creative)"></i><i style="background:var(--m-critical)"></i>
          <i style="background:var(--m-analytical)"></i><i style="background:var(--m-logical)"></i><i style="background:var(--m-systems)"></i>
          <i style="background:var(--m-strategic)"></i><i style="background:var(--m-prob)"></i><i style="background:var(--m-science)"></i>
        </span>
        <span lang="la">Systema Ratio</span>
      </span>
      <div class="head-tools">
        <a class="tool-pill" href="vi.html" lang="vi">Tiếng Việt</a>
        <a class="tool-pill" href="en.html" lang="en">English</a>
        <button type="button" class="tool-pill" aria-label="Toggle color theme" onclick="const m=document.querySelector('meta[name=color-scheme]');const d=m.content==='dark'||(m.content!=='light'&&matchMedia('(prefers-color-scheme: dark)').matches);const n=d?'light':'dark';m.content=n;try{{localStorage.setItem('sr-color-scheme',n)}}catch(e){{}}">
          <span>Light / Dark</span>
        </button>
      </div>
    </div>
  </header>
  <main class="wrap" style="max-width:1200px;">
    <div style="text-align:center;max-width:76ch;margin:4px auto 0;">
      <span class="eyebrow">Kinetic Editorial Edition · Systema Intelligentiae × Sci-Fi AI Atlas</span>
      <h1 id="portal-heading" tabindex="-1" style="font-size:clamp(2.4rem,4.8vw,3.85rem);font-weight:800;margin-block-end:12px;">
        <span lang="la">Systema Ratio</span> · <em class="hero-accent">Living Casebook</em>
      </h1>
      <p style="font-size:17.5px;color:var(--ink-2);">
        Split-screen scrollytelling, <strong>36 linked real-world case studies</strong>, 7 live cognitive simulators, Socratic AI sparring, 24 vector plates &amp; 23 classic books for
        <strong>Đào Minh Châu’s <em>Học Tư Duy</em> (2026)</strong>.
      </p>
    </div>

    <div class="portal-grid">
      <div class="portal-card" lang="vi">
        <div>
          <span class="pill-tag" style="color:var(--accent);">Ấn bản Tiếng Việt Hiện Đại · VI</span>
          <h2 style="font-size:27px;margin-block-end:8px;">Hệ Thống Lý Trí · Học Tư Duy</h2>
          <p style="color:var(--ink-2);font-size:15px;margin-block-end:16px;">
            Trải nghiệm scrollytelling 9 lăng kính gắn liền tuổi 22–30 của Minh, kho 36 hồ sơ tình huống thực chiến có liên kết gốc, 7 phòng thí nghiệm sống, lệnh AI phản biện Socratic và 24 bản vẽ vector chuẩn in ấn.
          </p>
          <a class="portal-cov-link plate-svg-wrap" href="vi.html" aria-label="Mở Ấn bản Tiếng Việt">{cov_vi}</a>
        </div>
        <div style="display:grid;gap:8px;">
          <a class="btn-primary" href="vi.html" style="justify-content:center;">Mở Ấn bản Tiếng Việt (vi.html) →</a>
          <a class="btn-ghost" href="vi.html#cases" style="justify-content:center;">Vào thẳng Kho 36 Hồ sơ Thực chiến →</a>
        </div>
      </div>

      <div class="portal-card" lang="en">
        <div>
          <span class="pill-tag" style="color:var(--c-critical);">International English Edition · EN</span>
          <h2 style="font-size:27px;margin-block-end:8px;">Systema Ratio · Learning How to Think</h2>
          <p style="color:var(--ink-2);font-size:15px;margin-block-end:16px;">
            Full 9-chapter split-screen scrollytelling, 36 linked historical &amp; business case dossiers, 7 hands-on simulators (with 1-page PDF Decision Sheet &amp; Socratic AI Sparring), 24 vector plates, and 23 classic books.
          </p>
          <a class="portal-cov-link plate-svg-wrap" href="en.html" aria-label="Open English Edition">{cov_en}</a>
        </div>
        <div style="display:grid;gap:8px;">
          <a class="btn-primary" href="en.html" style="justify-content:center;">Open English Edition (en.html) →</a>
          <a class="btn-ghost" href="en.html#cases" style="justify-content:center;">Jump to 36 Real Case Studies →</a>
        </div>
      </div>
    </div>
  </main>
</body>
</html>"""


def main():
    # 1. Build inline + standalone vector plates for EN and VI
    plates_en_inline = build_plates("en", standalone=False)
    plates_vi_inline = build_plates("vi", standalone=False)
    plates_en_print = build_plates("en", standalone=True)
    plates_vi_print = build_plates("vi", standalone=True)

    for lang_code, p_list in [("en", plates_en_print), ("vi", plates_vi_print)]:
        out_dir = ROOT / "plates" / lang_code
        out_dir.mkdir(parents=True, exist_ok=True)
        for p in p_list:
            (out_dir / f'{p["slug"]}.svg').write_text(p["svg"], encoding="utf-8")

    # 2. Render en.html and vi.html
    html_en = render_edition("en", META_EN, CHAPTERS_EN, TOOLS, PATHWAYS, BIASES, FALLACIES, EDITORIAL_NOTES, plates_en_inline)
    html_vi = render_edition("vi", META_VI, CHAPTERS_VI, TOOLS, PATHWAYS, BIASES, FALLACIES, EDITORIAL_NOTES, plates_vi_inline)

    (ROOT / "en.html").write_text(html_en, encoding="utf-8")
    (ROOT / "vi.html").write_text(html_vi, encoding="utf-8")

    # 3. Render bilingual portal index.html
    portal_html = build_portal(plates_en_inline[0]["svg"], plates_vi_inline[0]["svg"])
    (ROOT / "index.html").write_text(portal_html, encoding="utf-8")

    print(f"Built en.html ({len(html_en):,} bytes), vi.html ({len(html_vi):,} bytes), index.html, and 48 SVG plates.")


if __name__ == "__main__":
    main()
