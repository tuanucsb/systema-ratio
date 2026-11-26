# -*- coding: utf-8 -*-
"""Renders complete standalone English and Vietnamese HTML editions of Systema Ratio (v3 — Kinetic Editorial, Scrollytelling, 36 Case Studies & Decision Builder)."""
import html
import json
import re
from src.template_css import APP_CSS
from src.data_story import MIRROR_TRAPS, BOOK_TOURS, SAGA_BEATS, MINH_ARC, SHORT_NODE_NAMES
from src.data_library import STORIES_ANTHOLOGY, DILEMMA_ROULETTE, BOOKS_LIBRARY
from src.data_cases import CASE_CATEGORIES, CASES_VAULT


def pq(s: str) -> str:
    txt = str(s)
    txt = re.sub(r"(\w)'(\w)", r"\1’\2", txt)
    txt = re.sub(r'(^|[\s(\[—–:-])"', r"\1“", txt)
    txt = txt.replace('"', "”")
    txt = re.sub(r"(^|[\s(\[—–:-])'", r"\1‘", txt)
    txt = txt.replace("'", "’")
    return txt


RAW_JSON_KEYS = {
    "id", "ch", "cid", "cat", "part", "stage", "lane", "url", "ol", "gb",
    "lab", "target", "view", "sub", "color", "hex", "plate_id", "svg",
    "slug", "wise", "rests_on", "powers", "nodes", "lang",
}


def pq_data(obj, key=None):
    if key in RAW_JSON_KEYS:
        return obj
    if key == "links" and isinstance(obj, list):
        return [[pq(lbl), tgt] for lbl, tgt in obj]
    if isinstance(obj, str):
        return pq(obj)
    if isinstance(obj, list):
        return [pq_data(x) for x in obj]
    if isinstance(obj, tuple):
        return [pq_data(x) for x in obj]
    if isinstance(obj, dict):
        return {k: pq_data(v, k) for k, v in obj.items()}
    return obj


def esc_raw(s: str) -> str:
    return html.escape(str(s), quote=True)


def esc(s: str) -> str:
    return html.escape(pq(str(s)), quote=True)


SVG_SPRITE = """<svg xmlns="http://www.w3.org/2000/svg" hidden aria-hidden="true">
  <symbol id="ic-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14.5 14.5 0 0 0 0 18 14.5 14.5 0 0 0 0-18Z"/></symbol>
  <symbol id="ic-download" viewBox="0 0 24 24"><path d="M12 4v11m0 0-4-4m4 4 4-4M4 19h16"/></symbol>
  <symbol id="ic-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.93 4.93l1.41 1.41m11.32 11.32 1.41 1.41M2 12h2m16 0h2M4.93 19.07l1.41-1.41m11.32-11.32 1.41-1.41"/></symbol>
  <symbol id="ic-moon" viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></symbol>
  <symbol id="ic-play" viewBox="0 0 24 24"><polygon points="6,4 20,12 6,20" fill="currentColor" stroke="none"/></symbol>
  <symbol id="ic-compass" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><polygon points="10,10 16,8 14,14 8,16"/></symbol>
  <symbol id="ic-map" viewBox="0 0 24 24"><circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="8" r="2.5"/><circle cx="16" cy="18" r="2.5"/><path d="M8.3 6.6 15.6 7.7M7.5 8l7 8.5"/></symbol>
  <symbol id="ic-flask" viewBox="0 0 24 24"><path d="M9 3h6m-5 0v5.5L4.8 18A2 2 0 0 0 6.5 21h11a2 2 0 0 0 1.7-3L14 8.5V3"/></symbol>
  <symbol id="ic-shield" viewBox="0 0 24 24"><path d="M12 3 4 6.5v5.5c0 5 3.4 8.2 8 9.5 4.6-1.3 8-4.5 8-9.5V6.5L12 3Z"/><path d="M12 8v4m0 4h.01"/></symbol>
  <symbol id="ic-layers" viewBox="0 0 24 24"><polygon points="12,3 3,8 12,13 21,8"/><path d="m3 13 9 5 9-5M3 17.5l9 5 9-5"/></symbol>
  <symbol id="ic-book" viewBox="0 0 24 24"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v17H6.5A2.5 2.5 0 0 0 4 22V5.5Z"/><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/></symbol>
  <symbol id="ic-spark" viewBox="0 0 24 24"><path d="m12 3 2.2 5.8L20 11l-5.8 2.2L12 19l-2.2-5.8L4 11l5.8-2.2L12 3Z"/></symbol>
  <symbol id="ic-shuffle" viewBox="0 0 24 24"><path d="M16 3h5v5M4 20 21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/></symbol>
  <symbol id="ic-ext" viewBox="0 0 24 24"><path d="M14 4h6v6M10 14 20 4M18 13v6a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h6"/></symbol>
  <symbol id="ic-briefcase" viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 12h18"/></symbol>
  <symbol id="ic-sliders" viewBox="0 0 24 24"><path d="M4 21v-7m0-4V3m8 18v-9m0-4V3m8 18v-5m0-4V3M1 14h6m2-6h6m2 8h6"/></symbol>
  <symbol id="ic-copy" viewBox="0 0 24 24"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></symbol>
  <symbol id="ic-check" viewBox="0 0 24 24"><path d="m5 12 5 5L20 7"/></symbol>
  <symbol id="ic-printer" viewBox="0 0 24 24"><path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></symbol>
</svg>"""


def icon_html(name: str) -> str:
    return f'<svg class="ic" width="16" height="16" aria-hidden="true"><use href="#ic-{name}"/></svg>'


def render_edition(lang: str, meta: dict, chapters: list, tools: list, pathways: list,
                   biases: list, fallacies: list, ed_notes: list, plates: list) -> str:
    en = lang == "en"
    T = lambda e, v: e if en else v

    # Prepare localized JS payload for 29 tools (with crisp non-truncated short_name!)
    js_tools = []
    for idx, tl in enumerate(tools):
        loc = tl[lang]
        sn_pair = SHORT_NODE_NAMES.get(tl["id"], (loc["name"], loc["name"]))
        short_nm = sn_pair[0] if en else sn_pair[1]
        js_tools.append({
            "id": tl["id"],
            "idx": idx + 1,
            "ch": tl["ch"],
            "part": tl["part"],
            "stage": tl["stage"],
            "lane": tl["lane"],
            "pages": tl["pages"],
            "name": loc["name"],
            "short_name": short_nm,
            "when": loc["when"],
            "what": loc["what"],
            "steps": loc["steps"],
            "pitfall": loc["pitfall"],
            "example": loc["example"],
            "rests_on": tl["rests_on"],
            "powers": tl["powers"],
        })

    js_pathways = []
    for p in pathways:
        beats_map = SAGA_BEATS.get(p["id"], {})
        steps_list = []
        for nid in p["nodes"]:
            bt = beats_map.get(nid, ("", "", "atlas:" + nid))
            steps_list.append({
                "id": nid,
                "beat": bt[0] if en else bt[1],
                "lab": bt[2],
            })
        js_pathways.append({
            "id": p["id"],
            "color": p["color"],
            "name": p[lang]["name"],
            "desc": p[lang]["desc"],
            "nodes": p["nodes"],
            "steps": steps_list,
        })

    js_tours = [
        {
            "id": tr["id"],
            "color": tr["color"],
            "name": tr["name_en"] if en else tr["name_vi"],
            "stops": [
                {
                    "view": st["view"],
                    "sub": st["sub"],
                    "label": st["label_en"] if en else st["label_vi"],
                    "beat": st["beat_en"] if en else st["beat_vi"],
                }
                for st in tr["stops"]
            ],
        }
        for tr in BOOK_TOURS
    ]

    js_minh = [
        {
            "ch": m["ch"],
            "age": m["age_en"] if en else m["age_vi"],
            "headline": m["headline_en"] if en else m["headline_vi"],
            "story": m["story_en"] if en else m["story_vi"],
            "lab": m["lab"],
        }
        for m in MINH_ARC
    ]
    minh_by_ch = {m["ch"]: m for m in js_minh}

    js_traps = [
        {
            "id": tr["id"],
            "num": tr["num"],
            "tag": tr["tag_en"] if en else tr["tag_vi"],
            "title": tr["title_en"] if en else tr["title_vi"],
            "q": tr["q_en"] if en else tr["q_vi"],
            "opt_trap": tr["opt_trap_en"] if en else tr["opt_trap_vi"],
            "opt_wise": tr["opt_wise_en"] if en else tr["opt_wise_vi"],
            "caught": tr["caught_en"] if en else tr["caught_vi"],
            "passed": tr["passed_en"] if en else tr["passed_vi"],
            "explain": tr["explain_en"] if en else tr["explain_vi"],
            "cta": tr["cta_en"] if en else tr["cta_vi"],
            "target": tr["target"],
        }
        for tr in MIRROR_TRAPS
    ]

    js_chapters = {
        c["id"]: {"num": c["num"], "title": c["title"], "color": c["color"], "hex": c["hex"]}
        for c in chapters
    }

    ch_plate_map = {
        "ch1": "p03", "ch2": "p06", "ch3": "p08", "ch4": "p10", "ch5": "p11",
        "ch6": "p12", "ch7": "p15", "ch8": "p17", "ch9": "p18",
    }
    ch_extra_plate_map = {
        "ch1": "p19", "ch2": "p20", "ch3": "p09", "ch4": "p21", "ch5": "p02",
        "ch6": "p22", "ch7": "p14", "ch8": "p23", "ch9": "p24",
    }
    plates_by_id = {p["id"]: p for p in plates}
    ic_ext = icon_html("ext")

    js_stories = [
        {
            "id": st["id"],
            "ch": st["ch"],
            "plate_id": st["plate_id"],
            "pages": st["pages"],
            "title": st["title_en"] if en else st["title_vi"],
            "hook": st["hook_en"] if en else st["hook_vi"],
            "twist": st["twist_en"] if en else st["twist_vi"],
            "cta": st["cta_en"] if en else st["cta_vi"],
            "target": st["target"],
            "svg": plates_by_id[st["plate_id"]]["svg"],
        }
        for st in STORIES_ANTHOLOGY
    ]

    js_dilemmas = [
        {
            "id": dl["id"],
            "context": dl["context_en"] if en else dl["context_vi"],
            "q": dl["q_en"] if en else dl["q_vi"],
            "a": dl["a_en"] if en else dl["a_vi"],
            "b": dl["b_en"] if en else dl["b_vi"],
            "wise": dl["wise"],
            "reveal": dl["reveal_en"] if en else dl["reveal_vi"],
            "target": dl["target"],
            "cta": dl["cta_en"] if en else dl["cta_vi"],
        }
        for dl in DILEMMA_ROULETTE
    ]

    js_cases = [
        {
            "id": cs["id"],
            "ch": cs["ch"],
            "cat": cs["cat"],
            "year": cs["year"],
            "domain": cs["domain_en"] if en else cs["domain_vi"],
            "title": cs["title_en"] if en else cs["title_vi"],
            "story": cs["story_en"] if en else cs["story_vi"],
            "lesson": cs["lesson_en"] if en else cs["lesson_vi"],
            "url": cs["url"],
            "src_label": cs["src_label"],
            "lab": cs["lab"],
        }
        for cs in CASES_VAULT
    ]
    cases_by_ch = {}
    for cs in js_cases:
        cases_by_ch.setdefault(cs["ch"], []).append(cs)

    def render_case_card(cs: dict, with_filters: bool = False, h_tag: str = "h3") -> str:
        c_info = js_chapters[cs["ch"]]
        data_attrs = ""
        if with_filters:
            q_blob = f'{cs["title"]} {cs["story"]} {cs["lesson"]} {cs["domain"]} {cs["year"]}'.lower()
            data_attrs = (
                f' data-caseid="{esc_raw(cs["id"])}"'
                f' data-ch="{esc_raw(cs["ch"])}"'
                f' data-cat="{esc_raw(cs["cat"])}"'
                f' data-search="{esc_raw(q_blob)}"'
            )
        lab_target = cs["lab"]
        lbl_takeaway = T("Conscious Takeaway:", "Bài học Tư duy:")
        lbl_try = T("Try Lab / Tool →", "Thử Công cụ →")
        return (
            f'<article class="case-card"{data_attrs} style="--cc:{c_info["color"]}">'
            f'<div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-block-end:8px;">'
            f'<span class="pill-tag" style="margin:0;color:{c_info["color"]};border-color:color-mix(in oklab, {c_info["color"]} 40%, var(--line));">'
            f'Ch. {c_info["num"]} · {esc(cs["domain"])}</span>'
            f'<span class="badge-mini">{esc(cs["year"])}</span>'
            f'</div>'
            f'<{h_tag} class="hd" style="font-size:19px;font-weight:750;line-height:1.2;margin-block-end:8px;">{esc(cs["title"])}</{h_tag}>'
            f'<p style="font-size:14.5px;color:var(--ink-2);margin-block-end:12px;">{esc(cs["story"])}</p>'
            f'<div class="case-lesson-box">'
            f'<strong style="color:{c_info["color"]};">{esc(lbl_takeaway)}</strong> {esc(cs["lesson"])}'
            f'</div>'
            f'</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;padding-block-start:6px;border-block-start:1px solid var(--line);">'
            f'<a class="ext-book-link" href="{esc_raw(cs["url"])}" target="_blank" rel="noopener noreferrer">'
            f'<span>{esc(cs["src_label"])}</span>{ic_ext}</a>'
            f'<button type="button" class="tool-pill" onclick="jumpTarget(\'{esc_raw(lab_target)}\')">{esc(lbl_try)}</button>'
            f'</div>'
            f'</article>'
        )

    all_cases_cards_html = "".join(render_case_card(cs, with_filters=True, h_tag="h3") for cs in js_cases)
    spotlight_ids = ["cs-avianca-ai", "cs-jcpenney", "cs-hanoi-rats"]
    spotlight_cases_html = "".join(
        render_case_card(next(x for x in js_cases if x["id"] == sid), h_tag="h3")
        for sid in spotlight_ids
    )
    case_cat_pills_html = ""
    for cat_id, cat_en, cat_vi in CASE_CATEGORIES:
        cat_lbl = cat_en if en else cat_vi
        pr_cat = "true" if cat_id == "all" else "false"
        case_cat_pills_html += (
            f'<button type="button" class="saga-pill case-cat-pill" data-cat="{esc_raw(cat_id)}" aria-pressed="{pr_cat}" onclick="setCaseCategory(\'{esc_raw(cat_id)}\')">'
            f'{esc(cat_lbl)}</button>'
        )

    hero_ray_pills_html = ""
    scrolly_steps_html = ""
    scrolly_beams_html = ""
    js_scrolly = []
    lbl_flash = T("Real-World Flashpoint:", "Điểm nóng Thực chiến:")
    lbl_4cases = T("4 Chapter Cases →", "4 Hồ sơ Thực tế →")
    lbl_openlab = T("Open Lab →", "Mở Mô phỏng →")
    lbl_readch = T("Read Ch.", "Đọc Ch.")

    for i, c in enumerate(chapters):
        cid = c["id"]
        c_col = c["color"]
        hero_ray_pills_html += (
            f'<button type="button" class="ray-chip" style="--rc:{c_col}" onclick="jumpToScrollyChapter({i})">'
            f'<span style="width:8px;height:8px;border-radius:50%;background:{c_col};" aria-hidden="true"></span>'
            f'<span>{c["num"]} · {esc(c["title"])}</span></button>'
        )
        lead_cs = cases_by_ch[cid][0]
        au_q, txt_q = c["quotes"][0]
        m_arc = minh_by_ch[cid]
        act_cls = " is-active" if i == 0 else ""
        beam_cur = "true" if i == 0 else "false"
        lead_lab = lead_cs["lab"]
        scrolly_steps_html += (
            f'<article class="scrolly-step{act_cls}" id="sc-step-{cid}" data-scidx="{i}" style="--sc-col:{c_col}" onclick="selectScrollyStep({i})">'
            f'<span class="eyebrow" style="color:{c_col};margin-block-end:4px;">Ch. {c["num"]} · {esc(c["role_tag"])} · {esc(c["pages"])}</span>'
            f'<h3 class="hd" style="font-size:22px;font-weight:800;margin-block-end:6px;">{c["num"]}. {esc(c["title"])}</h3>'
            f'<blockquote class="scrolly-quote">“{esc(txt_q)}” '
            f'<span style="font-style:normal;font-family:var(--kicker);font-size:13px;font-weight:700;color:var(--ink-2);">· {esc(au_q)}</span></blockquote>'
            f'<p style="font-size:14.5px;color:var(--ink-2);margin-block-end:12px;">'
            f'<strong style="color:{c_col};">{esc(lbl_flash)}</strong> {esc(lead_cs["title"])} ({esc(lead_cs["year"])})</p>'
            f'<div style="display:flex;gap:8px;flex-wrap:wrap;">'
            f'<button type="button" class="tool-pill" onclick="event.stopPropagation();switchView(\'cases\', \'{cid}\', true)">{esc(lbl_4cases)}</button>'
            f'<button type="button" class="tool-pill" onclick="event.stopPropagation();jumpTarget(\'{esc_raw(lead_lab)}\')">{esc(lbl_openlab)}</button>'
            f'<button type="button" class="tool-pill" onclick="event.stopPropagation();switchView(\'reader\', \'{cid}\', true)">{esc(lbl_readch)} {c["num"]} →</button>'
            f'</div></article>'
        )
        scrolly_beams_html += (
            f'<button type="button" class="stage-beam-btn" data-scbeam="{i}" aria-current="{beam_cur}" '
            f'aria-label="Ch. {c["num"]}: {esc(c["title"])}" style="--bc:{c_col}" onclick="scrollToScrollyStep({i})">'
            f'<span>{c["num"]}</span>'
            f'<span class="beam-track" aria-hidden="true"><span class="beam-fill"></span></span></button>'
        )
        js_scrolly.append({
            "cid": cid,
            "num": c["num"],
            "title": c["title"],
            "metaphor": c["metaphor"],
            "color": c_col,
            "svg": plates_by_id[ch_plate_map[cid]]["svg"],
            "minh_age": m_arc["age"],
            "minh_head": m_arc["headline"],
            "minh_story": m_arc["story"],
            "case_title": lead_cs["title"],
            "case_story": lead_cs["story"],
            "case_url": lead_cs["url"],
            "case_src": lead_cs["src_label"],
            "lab": lead_lab,
        })

    def render_book_card(bk: dict) -> str:
        c_info = js_chapters[bk["ch"]]
        ttl = bk["title_en"] if en else bk["title_vi"]
        why = bk["why_en"] if en else bk["why_vi"]
        return (
            f'<article class="book-card" style="--bc:{c_info["color"]}">'
            f'<div class="book-spine" aria-hidden="true"></div>'
            f'<div class="book-body">'
            f'<div>'
            f'<span style="font-family:var(--mono);font-size:12px;font-weight:700;color:{c_info["color"]};">'
            f'{esc(T("Ch.", "Ch."))} {c_info["num"]} · {esc(bk["author"])} ({esc(bk["year"])})</span>'
            f'<h4 style="font-size:16.5px;margin-block:4px 6px;">{esc(ttl)}</h4>'
            f'<p style="font-size:13.5px;color:var(--ink-2);">{esc(why)}</p>'
            f'</div>'
            f'<div class="book-links">'
            f'<a class="ext-book-link" href="{esc_raw(bk["ol"])}" target="_blank" rel="noopener noreferrer">'
            f'<span>Open Library</span>{ic_ext}</a>'
            f'<a class="ext-book-link" href="{esc_raw(bk["gb"])}" target="_blank" rel="noopener noreferrer">'
            f'<span>Google Books</span>{ic_ext}</a>'
            f'</div>'
            f'</div></article>'
        )

    all_books_cards_html = "".join(render_book_card(bk) for bk in BOOKS_LIBRARY)

    story_pick_btns_html = ""
    for i, st in enumerate(js_stories):
        c_col = js_chapters[st["ch"]]["color"]
        c_num = js_chapters[st["ch"]]["num"]
        pr = "true" if i == 0 else "false"
        story_pick_btns_html += (
            f'<button type="button" class="story-pick-btn" data-stidx="{i}" aria-pressed="{pr}" onclick="selectBookStory({i})">'
            f'<span style="width:9px;height:9px;border-radius:50%;background:{c_col};flex:none;" aria-hidden="true"></span>'
            f'<span style="flex:1;">{esc(st["title"])}</span>'
            f'<span class="badge-mini">Ch.{c_num}</span></button>'
        )

    # 1. Cold-Open 15-Second Mirror Traps HTML
    mirror_cards_html = ""
    for idx, tr in enumerate(js_traps):
        mirror_cards_html += (
            f'<article class="trap-quiz-card" id="qcard-{tr["id"]}">'
            f'<div>'
            f'<span class="pill-tag"><strong style="font-family:var(--mono);color:var(--c-trap);">{tr["num"]}</strong> {esc(tr["tag"])}</span>'
            f'<h3 style="font-size:18px;margin-block-end:6px;">{esc(tr["title"])}</h3>'
            f'<p style="font-size:14.5px;color:var(--ink-2);">{esc(tr["q"])}</p>'
            f'</div>'
            f'<div>'
            f'<div class="quiz-choices">'
            f'<button type="button" class="quiz-opt" data-qidx="{idx}" data-kind="trap" onclick="answerMirrorTrap({idx}, \'trap\')">{esc(tr["opt_trap"])}</button>'
            f'<button type="button" class="quiz-opt" data-qidx="{idx}" data-kind="wise" onclick="answerMirrorTrap({idx}, \'wise\')">{esc(tr["opt_wise"])}</button>'
            f'</div>'
            f'<div id="qrev-{idx}" class="quiz-reveal" hidden style="margin-block-start:10px;"></div>'
            f'</div>'
            f'</article>'
        )

    # 2. Four Floors buttons (with mobile-safe .floor-meta!)
    floors_btns = ""
    for i, fl in enumerate(meta["floors"]):
        pressed = "true" if i == 3 else "false"
        floors_btns += (
            f'<button type="button" class="floor-btn" data-floor="{i}" aria-pressed="{pressed}" style="--fc:{fl["color"]}" onclick="selectFloor({i})">'
            f'<span class="floor-bar" aria-hidden="true"></span>'
            f'<span><strong style="display:block;font-size:15.5px;margin-block-end:2px;">{esc(fl["name"])}</strong>'
            f'<span style="font-size:14px;color:var(--ink-2);">{esc(fl["one"])}</span></span>'
            f'<span class="floor-meta">'
            f'<strong style="display:block;color:var(--ink);">{esc(fl["num"])}</strong>'
            f'<span style="color:var(--ink-3);">{esc(fl["badge"])}</span></span></button>'
        )

    # 3. Protagonist 9-Chapter Quick-Jump Scrubber (wired directly into Scrollytelling!)
    minh_btns_html = ""
    for i, m in enumerate(js_minh):
        c_col = js_chapters[m["ch"]]["color"]
        c_num = js_chapters[m["ch"]]["num"]
        c_ttl = js_chapters[m["ch"]]["title"]
        pressed = "true" if i == 0 else "false"
        age_short = m["age"].split("·")[0].strip()
        minh_btns_html += (
            f'<button type="button" class="minh-stop" data-minh="{i}" aria-pressed="{pressed}" style="--mc:{c_col}" onclick="scrollToScrollyStep({i})">'
            f'<span style="display:block;font-family:var(--mono);font-size:12px;font-weight:700;color:{c_col};">{esc(age_short)}</span>'
            f'<strong style="display:block;font-size:13px;margin-block-start:2px;">{c_num}. {esc(c_ttl)}</strong>'
            f'</button>'
        )

    # 4. AI Era 4 cards (clean sentence-case pill tags, zero colored-left-border!)
    ai_cards = "".join(
        f'<div class="info-card">'
        f'<span class="pill-tag" style="color:var(--accent);">{esc(c["tag"])}</span>'
        f'<h3 style="font-size:17.5px;margin-block-end:6px;">{esc(c["head"])}</h3>'
        f'<p style="font-size:14.5px;color:var(--ink-2);">{esc(c["body"])}</p></div>'
        for c in meta["ai_era"]["cards"]
    )

    # 5. Six Question Threads
    threads_btns = "".join(
        f'<button type="button" class="thread-btn" data-thread="{i}" aria-pressed="{"true" if i == 0 else "false"}" onclick="selectThread({i})">'
        f'<span style="display:block;font-family:var(--mono);font-size:12px;color:var(--ink-3);margin-block-end:3px;">{esc(th["tag"])}</span>'
        f'{esc(th["q"])}</button>'
        for i, th in enumerate(meta["threads"])
    )

    # 6. Biases & Fallacies HTML (clean editorial borders, zero border-left slop!)
    biases_html = ""
    for b in biases:
        bl = b[lang]
        prov_sub = f' · <span style="color:var(--ink-3);">{esc(b["proverb_en"])}</span>' if en else ""
        biases_html += (
            f'<article class="sec-card" style="margin-block-end:0;padding:20px;border-color:color-mix(in oklab, var(--c-trap) 28%, var(--line));">'
            f'<div style="display:flex;justify-content:space-between;gap:8px;align-items:center;margin-block-end:8px;">'
            f'<span class="pill-tag" style="margin:0;color:var(--c-trap);font-family:var(--mono);">#{b["num"]:02d} · {esc(b["page"])}</span>'
            f'</div>'
            f'<h3 style="font-size:18.5px;margin-block-end:6px;">{esc(bl["name"])}</h3>'
            f'<p style="font-size:14px;font-weight:700;color:var(--c-strategic);margin-block-end:8px;"><span lang="vi">{esc(b["proverb_vi"])}</span>{prov_sub}</p>'
            f'<p style="font-size:14.5px;color:var(--ink);margin-block-end:8px;">{esc(bl["mech"])}</p>'
            f'<p style="font-size:14px;color:var(--ink-2);margin-block-end:12px;"><strong>{esc(T("Book example:", "Ví dụ trong sách:"))}</strong> {esc(bl["case"])}</p>'
            f'<div style="padding:10px 12px;border-radius:8px;background:color-mix(in oklab, var(--c-analytical) 8%, var(--surface-2));border:1px solid color-mix(in oklab, var(--c-analytical) 30%, var(--line));font-size:13.5px;">'
            f'<strong style="color:var(--c-analytical);">{esc(T("System 2 Antidote:", "Thuốc giải Hệ thống 2:"))}</strong> {esc(bl["antidote"])}</div>'
            f'</article>'
        )

    fallacies_html = "".join(
        f'<div class="info-card">'
        f'<span class="pill-tag" style="color:var(--c-critical);">{esc(f["cat_en"] if en else f["cat_vi"])}</span>'
        f'<h3 style="font-size:16.5px;margin-block-end:6px;">{esc(f[lang]["name"])}</h3>'
        f'<p style="font-size:14px;color:var(--ink-2);">{esc(f[lang]["ex"])}</p></div>'
        for f in fallacies
    )

    # 7. 18 Book Plates Gallery HTML (with SVG download icon instead of emoji!)
    dl_icon = icon_html("download")
    plates_html = ""
    for p in plates:
        svg_path = f'plates/{lang}/{p["slug"]}.svg'
        plates_html += (
            f'<figure class="plate-card" id="plate-{p["id"]}">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;margin-block-end:10px;">'
            f'<div><span class="eyebrow" style="color:var(--accent);margin-block-end:4px;">{esc(p["ch"])} · {esc(p["manuscript_ref"])}</span>'
            f'<h3 style="font-size:20px;">{esc(p["title"])}</h3></div>'
            f'<a class="tool-pill" href="{esc_raw(svg_path)}" download="{esc_raw(p["slug"])}-{lang}.svg">'
            f'{dl_icon}<span>{esc(T("Download Print SVG", "Tải SVG In Ấn"))}</span></a></div>'
            f'<p style="font-size:15px;font-weight:600;color:var(--ink);margin-block-end:12px;">{esc(p["say"])}</p>'
            f'<div class="plate-svg-wrap">{p["svg"]}</div>'
            f'<figcaption style="margin-block-start:10px;font-size:14px;color:var(--ink-2);">'
            f'<strong>{esc(T("Illustration rationale:", "Lý do thiết kế minh họa:"))}</strong> {esc(p["rationale"])}</figcaption>'
            f'</figure>'
        )

    ed_notes_html = "".join(
        f'<li style="margin-block-end:8px;"><strong>{esc(n["page"])}:</strong> {esc(n[lang])}</li>'
        for n in ed_notes
    )

    # 8. 9-Chapter Reader TOC & Spec-Boards + Minh Story Thread + Prev/Next Chapter Footer!
    toc_btns = ""
    for i, c in enumerate(chapters):
        cid = c["id"]
        cur = "true" if i == 0 else "false"
        toc_btns += (
            f'<button type="button" class="toc-btn" data-ch="{cid}" aria-current="{cur}" onclick="selectChapter(\'{cid}\', true)">'
            f'<span style="width:9px;height:9px;border-radius:50%;background:{c["color"]};display:inline-block;flex:none;" aria-hidden="true"></span>'
            f'<span>{c["num"]}. {esc(c["title"])}</span></button>'
        )

    chapters_panes = ""
    for i, c in enumerate(chapters):
        cid = c["id"]
        hid = "" if i == 0 else " hidden"
        q_html = "".join(
            f'<blockquote style="margin:0 0 8px;padding:10px 14px;background:var(--surface-2);border:1px solid var(--line);border-radius:8px;font-size:14.5px;">'
            f'“{esc(qt)}” · <strong>{esc(au)}</strong></blockquote>'
            for au, qt in c["quotes"]
        )
        pr_html = "".join(f"<li style='margin-block-end:5px;'>{esc(pr)}</li>" for pr in c["principles"])
        tr_html = "".join(f"<li style='margin-block-end:5px;'>{esc(tr)}</li>" for tr in c["traps"])
        ex_html = "".join(f"<li style='margin-block-end:5px;'>{esc(ex)}</li>" for ex in c["exercises"])
        rd_html = "".join(f"<li style='margin-block-end:4px;'>{esc(rd)}</li>" for rd in c["reading"])

        ch_tools_chips = ""
        for tid in c["tools"]:
            tnm = next(x["name"] for x in js_tools if x["id"] == tid)
            ch_tools_chips += f'<button type="button" class="tool-pill" onclick="openToolModal(\'{tid}\')">{esc(tnm)} →</button>'

        m_arc = minh_by_ch[cid]
        minh_box = (
            f'<div style="margin-block-end:18px;padding:14px 16px;border-radius:10px;background:color-mix(in oklab, {c["color"]} 8%, var(--surface-2));border:1px solid color-mix(in oklab, {c["color"]} 32%, var(--line));">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-block-end:4px;">'
            f'<span style="font-family:var(--mono);font-size:12px;font-weight:700;color:{c["color"]};">{esc(T("LIVE CASE THREAD · MINH’S JOURNEY", "MẠCH TRUYỆN XUYÊN SUỐT · HÀNH TRÌNH CỦA MINH"))} · {esc(m_arc["age"])}</span>'
            f'<button type="button" class="tool-pill" onclick="jumpTarget(\'{m_arc["lab"]}\')">{esc(T("Try Matching Lab →", "Thử Mô phỏng →"))}</button>'
            f'</div>'
            f'<strong style="display:block;font-size:15.5px;margin-block-end:3px;">{esc(m_arc["headline"])}</strong>'
            f'<p style="font-size:14.5px;color:var(--ink-2);">{esc(m_arc["story"])}</p>'
            f'</div>'
        )

        # Prev / Next chapter directional buttons
        prev_btn = ""
        if i > 0:
            pc = chapters[i - 1]
            pid = pc["id"]
            prev_btn = (
                f'<button type="button" class="btn-ghost" style="justify-content:flex-start;text-align:start;" onclick="selectChapter(\'{pid}\', true)">'
                f'<span>← {esc(T("Previous:", "Chương trước:"))} <strong>{pc["num"]}. {esc(pc["title"])}</strong></span></button>'
            )
        else:
            prev_btn = (
                f'<button type="button" class="btn-ghost" style="justify-content:flex-start;" onclick="switchView(\'overview\')">'
                f'<span>← {esc(T("Back to 4-Floor Overview", "Về Tổng quan 4 Tầng"))}</span></button>'
            )

        if i < len(chapters) - 1:
            nc = chapters[i + 1]
            nid = nc["id"]
            next_btn = (
                f'<button type="button" class="btn-primary" style="justify-content:space-between;" onclick="selectChapter(\'{nid}\', true)">'
                f'<span>{esc(T("Next Chapter:", "Chương tiếp:"))} <strong>{nc["num"]}. {esc(nc["title"])}</strong></span><span>→</span></button>'
            )
        else:
            next_btn = (
                f'<button type="button" class="btn-primary" style="justify-content:space-between;" onclick="jumpTarget(\'labs:science\')">'
                f'<span>{esc(T("Run the 7-Step Scientific Reactor", "Vận hành Lò Hội tụ Khoa học 7 Bước"))}</span><span>→</span></button>'
            )

        ch_svg = plates_by_id[ch_plate_map[cid]]["svg"]
        extra_plate = plates_by_id[ch_extra_plate_map[cid]]
        extra_svg_box = (
            f'<figure style="margin:18px 0;padding:16px;border-radius:10px;background:var(--surface-2);border:1px solid var(--line);">'
            f'<span class="eyebrow" style="color:{c["color"]};margin-block-end:4px;">{esc(extra_plate["manuscript_ref"])}</span>'
            f'<strong style="display:block;font-size:16px;margin-block-end:8px;">{esc(extra_plate["title"])}</strong>'
            f'<div class="plate-svg-wrap">{extra_plate["svg"]}</div>'
            f'<figcaption style="font-size:13.5px;color:var(--ink-2);margin-block-start:8px;">{esc(extra_plate["say"])}</figcaption>'
            f'</figure>'
        )
        ch_books = [bk for bk in BOOKS_LIBRARY if bk["ch"] == cid]
        ch_books_html = "".join(render_book_card(bk) for bk in ch_books)
        ch_cases_html = "".join(render_case_card(cs, h_tag="h4") for cs in cases_by_ch.get(cid, []))

        chapters_panes += (
            f'<article class="sec-card ch-pane" id="pane-{cid}"{hid} style="border-block-start:4px solid {c["color"]};">'
            f'<span class="eyebrow">{esc(c["part_name"])} · {esc(c["pages"])} · {esc(c["role_tag"])}</span>'
            f'<h2 id="heading-{cid}" tabindex="-1" style="font-size:28px;margin-block-end:6px;">{c["num"]}. {esc(c["title"])}</h2>'
            f'<p style="font-size:14.5px;color:var(--ink-3);margin-block-end:16px;">{esc(T("Visual Metaphor:", "Ẩn dụ trực quan:"))} <strong>{esc(c["metaphor"])}</strong></p>'
            f'{minh_box}'
            f'<div style="margin-block-end:18px;">{q_html}</div>'
            f'<div class="plate-svg-wrap" style="margin-block-end:20px;">{ch_svg}</div>'
            f'<h3 style="font-size:18px;margin-block:18px 6px;">1 · {esc(T("Core Concept", "Khái niệm Cốt lõi"))}</h3>'
            f'<p style="font-size:15.5px;margin-block-end:14px;">{esc(c["concept"])}</p>'
            f'<h3 style="font-size:18px;margin-block:18px 6px;">2 · {esc(T("Guiding Principles", "Nguyên lý Dẫn dắt"))}</h3>'
            f'<ul style="padding-inline-start:20px;margin-block:0 14px;">{pr_html}</ul>'
            f'{extra_svg_box}'
            f'<h3 style="font-size:18px;margin-block:18px 8px;">3 · {esc(T("Practical Tools (Click to Inspect)", "Công cụ Thực hành (Nhấn để xem chi tiết)"))}</h3>'
            f'<div style="display:flex;gap:8px;flex-wrap:wrap;margin-block-end:16px;">{ch_tools_chips}</div>'
            f'<h3 style="font-size:18px;margin-block:18px 6px;color:var(--c-trap);">4 · {esc(T("Common Traps & Barriers", "Các Lỗi Phổ biến & Rào cản"))}</h3>'
            f'<ul style="padding-inline-start:20px;margin-block:0 14px;">{tr_html}</ul>'
            f'<h3 style="font-size:18px;margin-block:18px 6px;">5 · {esc(T("Practice Exercises", "Bài tập Rèn luyện"))}</h3>'
            f'<ol style="padding-inline-start:20px;margin-block:0 14px;">{ex_html}</ol>'
            f'<h3 style="font-size:18px;margin-block:18px 6px;">6 · {esc(T("Chapter Synthesis", "Kết luận Chương"))}</h3>'
            f'<p style="font-size:15px;font-weight:600;padding:14px 16px;background:var(--surface-2);border:1px solid var(--line);border-radius:8px;margin-block-end:14px;">{esc(c["synthesis"])}</p>'
            f'<h3 style="font-size:18px;margin-block:22px 10px;color:{c["color"]};">7 · {esc(T("Real-World Case Studies & Linked Dossiers (4 Cases)", "Hồ Sơ Tình Huống Thực Chiến & Tài Liệu Gốc (4 Vụ Việc)"))}</h3>'
            f'<div class="cases-grid" style="margin-block-end:18px;">{ch_cases_html}</div>'
            f'<h3 style="font-size:18px;margin-block:18px 8px;">8 · {esc(T("Suggested Books & Classic Companions (Click to Explore)", "Tủ Sách Đọc Thêm Gợi Ý (Nhấn để Tra cứu Sách)"))}</h3>'
            f'<div class="books-grid" style="margin-block-end:12px;">{ch_books_html}</div>'
            f'<div class="teach-only teach-callout"><strong>{esc(T("Educator Subject-Teaching Prompt:", "Gợi ý Giảng dạy Lồng ghép Môn học:"))}</strong> {esc(c["educator_note"])}</div>'
            f'<div class="ch-nav-footer">{prev_btn}{next_btn}</div>'
            f'</article>'
        )

    table_rows = ""
    for tl in js_tools:
        ch_num = js_chapters[tl["ch"]]["num"]
        ch_nm = js_chapters[tl["ch"]]["title"]
        tid = tl["id"]
        table_rows += (
            f'<tr onclick="openToolModal(\'{tid}\')">'
            f'<th scope="row">{tl["idx"]}. {esc(tl["name"])}</th>'
            f'<td>{esc(T("Ch.", "Ch."))} {ch_num} · {esc(ch_nm)} <span class="badge-mini">p. {esc(tl["pages"])}</span></td>'
            f'<td>{esc(tl["when"])}</td>'
            f'<td>{esc(tl["what"])}</td></tr>'
        )

    payload_json = json.dumps(pq_data({
        "lang": lang,
        "meta": {
            "floors": meta["floors"],
            "threads": meta["threads"],
            "theme_light": meta["theme_light"],
            "theme_dark": meta["theme_dark"],
        },
        "chapters": js_chapters,
        "tools": js_tools,
        "pathways": js_pathways,
        "tours": js_tours,
        "minh": js_minh,
        "traps": js_traps,
        "stories": js_stories,
        "dilemmas": js_dilemmas,
        "cases": js_cases,
        "scrolly": js_scrolly,
    }), ensure_ascii=False)

    cover_svg_inline = plates_by_id["p01"]["svg"]
    epilogue_svg_inline = plates_by_id["p24"]["svg"]
    ic_shuffle = icon_html("shuffle")
    ic_briefcase = icon_html("briefcase")
    ic_sliders = icon_html("sliders")
    ic_printer = icon_html("printer")
    saga_pills_html = ""
    for p in js_pathways:
        pid = p["id"]
        saga_pills_html += f'<button type="button" class="saga-pill" data-saga="{esc_raw(pid)}" aria-pressed="false" onclick="setSaga(\'{esc_raw(pid)}\')">{esc(p["name"])}</button>'

    ch_options_html = "".join(
        f'<option value="{c["id"]}">{c["num"]}. {esc(c["title"])}</option>'
        for c in chapters
    )

    ic_globe = icon_html("globe")
    ic_play = icon_html("play")
    ic_spark = icon_html("spark")
    ic_compass = icon_html("compass")
    ic_map = icon_html("map")
    ic_flask = icon_html("flask")
    ic_shield = icon_html("shield")
    ic_layers = icon_html("layers")
    ic_book = icon_html("book")

    mob_lbl_overview = esc(T("Story", "Truyện"))
    mob_lbl_cases = esc(T("36 Cases", "36 Hồ sơ"))
    mob_lbl_atlas = esc(T("Map", "Bản đồ"))
    mob_lbl_labs = esc(T("7 Labs", "7 Lab"))
    mob_lbl_traps = esc(T("Biases", "Bẫy"))
    mob_lbl_reader = esc(T("Chapters", "Chương"))

    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" content="#15172e">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <script>
    try {{
      document.querySelector('meta[name="color-scheme"]').content = localStorage.getItem("sr-color-scheme") ?? "light dark";
    }} catch (e) {{}}
  </script>
  <title>{esc(meta["site_title"])}</title>
  <meta name="description" content="{esc(meta["hero"]["lede"])}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600..900;1,9..144,600..800&family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..600&display=swap" rel="stylesheet">
  <style>{APP_CSS}</style>
</head>
<body>
  {SVG_SPRITE}
  <div id="scrollProgress"></div>
  <a href="#main-heading" class="skip-link visually-hidden">{esc(meta["skip_text"])}</a>
  <div id="srAnnouncer" class="visually-hidden" aria-live="polite"></div>

  <header class="site-head">
    <div class="head-wrap">
      <a class="brand" href="#overview" onclick="switchView('overview', null, true);return false;">
        <span class="brand-mark" aria-hidden="true">
          <i style="background:var(--m-meta)"></i><i style="background:var(--m-creative)"></i><i style="background:var(--m-critical)"></i>
          <i style="background:var(--m-analytical)"></i><i style="background:var(--m-logical)"></i><i style="background:var(--m-systems)"></i>
          <i style="background:var(--m-strategic)"></i><i style="background:var(--m-prob)"></i><i style="background:var(--m-science)"></i>
        </span>
        <span lang="la">{esc(meta["brand_name"])}</span>
        <span class="brand-sub">{esc(meta["brand_sub"])}</span>
      </a>

      <nav class="site-nav" aria-label="{esc(T("Primary", "Điều hướng chính"))}">
        <button type="button" class="nav-link" data-view="overview" aria-current="page" onclick="switchView('overview', null, true)">{esc(meta["nav"]["overview"])}</button>
        <button type="button" class="nav-link" data-view="cases" onclick="switchView('cases', null, true)">{esc(meta["nav"]["cases"])}<span class="nav-count">36</span></button>
        <button type="button" class="nav-link" data-view="atlas" onclick="switchView('atlas', null, true)">{esc(meta["nav"]["atlas"])}</button>
        <button type="button" class="nav-link" data-view="labs" onclick="switchView('labs', null, true)">{esc(meta["nav"]["labs"])}</button>
        <button type="button" class="nav-link" data-view="traps" onclick="switchView('traps', null, true)">{esc(meta["nav"]["traps"])}</button>
        <button type="button" class="nav-link" data-view="plates" onclick="switchView('plates', null, true)">{esc(meta["nav"]["plates"])}</button>
        <button type="button" class="nav-link" data-view="reader" onclick="switchView('reader', null, true)">{esc(meta["nav"]["reader"])}</button>
      </nav>

      <div class="head-tools">
        <button type="button" class="tool-pill" onclick="openDilemmaRoulette()" aria-label="{esc(T("Spin Dilemma", "Thử Tình huống"))}">
          {ic_shuffle}
          <span class="teach-lbl-long">{esc(T("Spin Dilemma", "Thử Tình huống"))}</span>
        </button>
        <button type="button" id="teachBtn" class="tool-pill" aria-pressed="false" aria-label="{esc(meta["depth_label"])}" onclick="toggleTeachMode()">
          {ic_spark}
          <span class="teach-lbl-long">{esc(meta["depth_label"])}</span>
          <span class="badge-mini">{esc(meta["depth_badge"])}</span>
        </button>
        <a id="langSwitchLink" class="tool-pill" href="{esc_raw(meta["other_href"])}" lang="{esc_raw(meta["other_lang"])}" aria-label="{esc(meta["other_label"])}">
          {ic_globe}
          <span class="lang-lbl-long">{esc(meta["other_label"])}</span>
          <span class="lang-lbl-short">{esc(T("VI", "EN"))}</span>
        </a>
        <button type="button" id="themeBtn" class="tool-pill" onclick="toggleColorScheme()" aria-label="{esc(meta["theme_dark"])}">
          <svg class="ic" width="16" height="16" aria-hidden="true"><use id="themeUse" href="#ic-moon"/></svg>
          <span id="themeText" class="visually-hidden">{esc(meta["theme_dark"])}</span>
        </button>
      </div>
    </div>
  </header>

  <!-- PERSISTENT CROSS-VIEW GUIDED STORY WALKER RIBBON -->
  <aside id="journeyBar" class="journey-bar" hidden aria-label="{esc(T("Guided Story Journey", "Thanh Dẫn chuyện Hành trình"))}">
    <div class="journey-inner" id="journeyInner"></div>
  </aside>

  <main class="wrap">
    <!-- ==================================================================
         VIEW 1: OVERVIEW, COLD-OPEN SYSTEM 1 TEST, 4 FLOORS & MINH'S ARC
         ================================================================== -->
    <section id="view-overview" class="view-section">
      <div class="hero-grid">
        <div>
          <span class="eyebrow">{esc(meta["hero"]["eyebrow"])}</span>
          <h1 id="main-heading" tabindex="-1" class="hero-title">
            {esc(meta["hero"]["title_main"])}<em class="hero-accent">{esc(meta["hero"]["title_accent"])}</em>
          </h1>
          <div class="spectrum-bar" aria-hidden="true">
            <span style="background:var(--m-meta)"></span><span style="background:var(--m-creative)"></span><span style="background:var(--m-critical)"></span>
            <span style="background:var(--m-analytical)"></span><span style="background:var(--m-logical)"></span><span style="background:var(--m-systems)"></span>
            <span style="background:var(--m-strategic)"></span><span style="background:var(--m-prob)"></span><span style="background:var(--m-science)"></span>
          </div>
          <p class="lede">{esc(meta["hero"]["lede"])}</p>

          <div class="edition-ledger" aria-label="{esc(T("Edition scope", "Quy mô ấn bản"))}">
            <span><strong>36</strong> {esc(T("Real Case Studies", "Hồ sơ Thực chiến"))}</span>
            <span>·</span>
            <span><strong>9</strong> {esc(T("Scrollytelling Acts", "Chương Scrollytelling"))}</span>
            <span>·</span>
            <span><strong>7</strong> {esc(T("Live Simulators", "Phòng Thí nghiệm Sống"))}</span>
            <span>·</span>
            <span><strong>29</strong> {esc(T("Cognitive Tools", "Công cụ Tư duy"))}</span>
            <span>·</span>
            <span><strong>24</strong> {esc(T("Vector Plates", "Bản vẽ Vector"))}</span>
          </div>

          <div class="cta-row">
            <button type="button" class="btn-primary" onclick="switchView('cases', null, true)">
              {ic_briefcase}
              <span>{esc(T("Explore 36 Real Case Studies →", "Khám phá 36 Hồ sơ Thực tế →"))}</span>
            </button>
            <button type="button" class="btn-ghost" onclick="startGuidedTour('awakening-tour')">
              {ic_play}
              <span>{esc(T("5-Stop Guided Story", "Hành trình Dẫn chuyện"))}</span>
            </button>
            <button type="button" class="btn-ghost" onclick="switchView('labs', 'builder', true)">
              {ic_sliders}
              <span>{esc(T("Decision Stress-Tester", "Thử Lửa Quyết Định"))}</span>
            </button>
            <button type="button" id="resumeBtn" class="tool-pill" hidden onclick="resumeLastChapter()"></button>
          </div>
        </div>

        <div style="max-width:490px;width:100%;justify-self:center;">
          <div class="plate-svg-wrap">{cover_svg_inline}</div>
          <div class="hero-ray-pills" aria-label="{esc(T("Jump to chapter lens", "Nhảy tới lăng kính chương"))}">
            {hero_ray_pills_html}
          </div>
        </div>
      </div>

      <!-- SCENE I: 15-SECOND COLD OPEN — CATCH YOUR SYSTEM 1 IN THE ACT -->
      <div class="sec-card" id="sec-mirror">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;">
          <div>
            <span class="eyebrow" style="color:var(--c-trap);">{esc(T("Prologue · Don’t Take Our Word For It: Test Your Own Intuition First", "Mở màn Tương tác · Đừng Vội Tin Sách: Hãy Thử Phản Xạ Của Chính Bạn Trong 15 Giây"))}</span>
            <h2 style="font-size:26px;margin-block-end:4px;">{esc(T("Three 5-second traps where smart minds misfire", "Ba cái bẫy 5 giây khiến trí óc thông minh vẫn sập hầm"))}</h2>
            <p style="color:var(--ink-2);max-width:72ch;">{esc(T("Pick your honest gut answer on each card below to see Kahneman’s System 1 and Đào Minh Châu’s System 2 antidotes in action.", "Chọn nhanh đáp án trực giác đầu tiên của bạn ở từng thẻ để tận mắt thấy Hệ thống 1 đánh lừa ta ra sao."))}</p>
          </div>
          <span id="mirrorScoreBadge" class="pill-tag" style="font-family:var(--mono);font-size:13px;padding:6px 12px;">
            {esc(T("System 2 Reflex: 0 / 3 Tested", "Phản xạ Hệ thống 2: 0 / 3 Đã thử"))}
          </span>
        </div>
        <div class="mirror-grid">{mirror_cards_html}</div>
      </div>

      <!-- SCENE I-B: SPLIT-SCREEN SCROLLYTELLING FLAGSHIP + MINH'S AGE 22->30 TIMELINE -->
      <div class="sec-card" id="sec-scrolly">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;">
          <div>
            <span class="eyebrow" style="color:var(--accent);">{esc(T("Kinetic Scrollytelling · 9 Lenses, 9 Flashpoints & Minh’s Age 22–30 Journey", "Trải Nghiệm Scrollytelling · 9 Lăng Kính, 9 Bước Ngoặt & Hành Trình Tuổi 22–30 Của Minh"))}</span>
            <h2 style="font-size:27px;margin-block-end:6px;">{esc(T("Watch the prism refract: 9 chapters, 9 real-world flashpoints, 1 living system", "Chiếc lăng kính 9 tia sáng: 9 chương sách gắn liền 9 bước ngoặt thực chiến"))}</h2>
            <p style="color:var(--ink-2);max-width:76ch;">{esc(T("Scroll the nine chapter cards on the left—or tap any stop along Minh’s timeline—to morph the live vector illustration, historical case dossier, and protagonist arc.", "Cuộn dọc 9 thẻ chương bên trái—hoặc chọn mốc tuổi của Minh trên thanh thời gian—để biến đổi trực tiếp bản vẽ vector, hồ sơ lịch sử và câu chuyện xuyên suốt."))}</p>
          </div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <button type="button" class="tool-pill" onclick="switchView('plates', null, true)">
              {ic_layers}
              <span>{esc(T("24 Vector Plates →", "24 Bản vẽ Vector →"))}</span>
            </button>
            <button type="button" class="tool-pill" onclick="switchView('cases', null, true)">
              {ic_briefcase}
              <span>{esc(T("All 36 Case Studies →", "Trọn bộ 36 Hồ sơ →"))}</span>
            </button>
          </div>
        </div>

        <div class="minh-rail" role="group" aria-label="{esc(T("Minh Age 22 to 30 chapter timeline", "Dòng thời gian 9 chương của Minh"))}">
          {minh_btns_html}
        </div>

        <div class="scrolly-layout">
          <div class="scrolly-steps">
            {scrolly_steps_html}
          </div>
          <aside class="scrolly-sticky-stage" id="scrollyStickyStage" aria-live="polite">
            <div class="stage-beam-strip" role="group" aria-label="{esc(T("9 prism beams", "9 tia lăng kính"))}">
              {scrolly_beams_html}
            </div>
            <div id="scrollyStageContent"></div>
          </aside>
        </div>
      </div>

      <!-- SCENE I-C: FEATURED REAL-WORLD CASE DOSSIERS SPOTLIGHT -->
      <div class="sec-card" id="sec-case-spotlight">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;margin-block-end:16px;">
          <div>
            <span class="eyebrow" style="color:var(--c-strategic);">{esc(T("Case Study Vault Preview · Theory Tested Against High-Stakes Reality", "Kho Hồ Sơ Thực Chiến · Khi Lý Thuyết Va Chạm Thực Tế Khốc Liệt"))}</span>
            <h2 style="font-size:26px;margin-block-end:4px;">{esc(T("From ChatGPT courtroom hallucinations to 1902 Hanoi’s tailless rats", "Từ vụ luật sư nộp án lệ giả của ChatGPT đến đàn chuột cụt đuôi Hà Nội 1902"))}</h2>
            <p style="color:var(--ink-2);max-width:74ch;">{esc(T("Every single chapter is backed by four documented historical, scientific, or business case studies with primary external links.", "Mỗi chương sách đều gắn với 4 vụ việc có thật trong lịch sử, khoa học, y học và kinh doanh kèm liên kết tra cứu hồ sơ gốc."))}</p>
          </div>
          <button type="button" class="btn-primary" onclick="switchView('cases', null, true)">
            {ic_briefcase}
            <span>{esc(T("Open All 36 Linked Cases →", "Mở Kho 36 Hồ sơ Thực chiến →"))}</span>
          </button>
        </div>
        <div class="cases-grid">{spotlight_cases_html}</div>
      </div>

      <!-- SCENE II: FOUR FLOORS OF CONSCIOUS REASON -->
      <div class="sec-card" id="sec-floors">
        <span class="eyebrow">{esc(T("Act I · The Architectural Stack", "Hồi I · Kiến trúc Ngôi nhà 4 Tầng của Lý trí"))}</span>
        <h2 style="font-size:26px;margin-block-end:6px;">{esc(meta["floors_heading"])}</h2>
        <p style="color:var(--ink-2);max-width:74ch;">{esc(meta["floors_sub"])}</p>

        <div class="floors-list" role="group" aria-label="{esc(meta["floors_heading"])}">
          {floors_btns}
        </div>
        <div id="floorDetail" class="floor-detail" aria-live="polite"></div>
        <p style="margin-block-start:12px;font-size:14px;color:var(--c-analytical);font-weight:600;">
          ↺ {esc(meta["simon_loop"])}
        </p>
      </div>

      <!-- SCENE III: ILLUSTRATED PARABLES & STORIES FROM THE BOOK -->
      <div class="sec-card" id="sec-stories">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;">
          <div>
            <span class="eyebrow" style="color:var(--c-science);">{esc(T("Illustrated Story Theater · 8 Iconic Parables & Breakthroughs", "Rạp Chuyện Kể Minh Họa · 8 Giai Thoại & Ngụ Ngôn Kinh Điển Trong Sách"))}</span>
            <h2 style="font-size:25px;margin-block-end:6px;">{esc(T("Stories where a single shift in thinking changed history", "Những câu chuyện nơi một cú xoay góc nhìn làm thay đổi lịch sử"))}</h2>
            <p style="color:var(--ink-2);max-width:76ch;">{esc(T("Select any story on the left to inspect its bespoke vector illustration, the instinctive trap, and the breakthrough move.", "Chọn từng câu chuyện bên trái để xem tranh minh họa vector, cái bẫy trực giác và bước ngoặt tư duy."))}</p>
          </div>
          <button type="button" class="tool-pill" onclick="switchView('reader', 'books', true)">
            {ic_book}
            <span>{esc(T("Browse 23 Suggested Books →", "Mở Tủ sách 23 Tác phẩm Gợi ý →"))}</span>
          </button>
        </div>
        <div class="story-theater">
          <div class="story-nav-list" role="group" aria-label="{esc(T("Book stories", "Danh sách chuyện kể"))}">
            {story_pick_btns_html}
          </div>
          <div id="storyTheaterStage" class="floor-detail" aria-live="polite"></div>
        </div>
      </div>

      <!-- SCENE IV: AI ERA PREFACE SYNTHESIS -->
      <div class="sec-card">
        <span class="eyebrow">{esc(meta["ai_era"]["eyebrow"])}</span>
        <h2 style="font-size:24px;margin-block-end:14px;">{esc(meta["ai_era"]["title"])}</h2>
        <div class="cards-grid-4">{ai_cards}</div>
      </div>

      <!-- SCENE V: SIX STRUCTURAL QUESTIONS -->
      <div class="sec-card">
        <span class="eyebrow">{esc(T("Act III · Six Paradoxes Through the Book", "Hồi III · Sáu Nghịch lý Xuyên suốt Cuốn sách"))}</span>
        <h2 style="font-size:24px;margin-block-end:6px;">{esc(meta["threads_heading"])}</h2>
        <p style="color:var(--ink-2);margin-block-end:14px;">{esc(meta["threads_sub"])}</p>
        <div class="threads-grid">{threads_btns}</div>
        <div id="threadOut" class="thread-out"></div>
      </div>

      <!-- EPILOGUE BIRD PARABLE + FULL PLATE 24 ILLUSTRATION -->
      <div class="sec-card" style="background:color-mix(in oklab, var(--accent) 6%, var(--surface));border-color:color-mix(in oklab, var(--accent) 32%, var(--line));">
        <span class="eyebrow" style="color:var(--accent);">{esc(meta["epilogue"]["eyebrow"])}</span>
        <h2 style="font-size:24px;margin-block-end:8px;">{esc(meta["epilogue"]["title"])}</h2>
        <p style="font-size:15.5px;color:var(--ink-2);max-width:78ch;margin-block-end:12px;">{esc(meta["epilogue"]["story"])}</p>
        <p style="font-size:16px;font-weight:700;color:var(--ink);margin-block-end:16px;">{esc(meta["epilogue"]["moral"])}</p>
        <div class="plate-svg-wrap">{epilogue_svg_inline}</div>
      </div>
    </section>

    <!-- ==================================================================
         VIEW 1-B: 36 REAL-WORLD CASE STUDIES VAULT (FILTERABLE & LINKED)
         ================================================================== -->
    <section id="view-cases" class="view-section" hidden>
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;margin-block-end:14px;">
        <div>
          <span class="eyebrow" style="color:var(--c-strategic);">{esc(T("Real-World Evidence Vault · 36 Linked Historical, Scientific & Business Dossiers", "Kho Hồ Sơ Thực Chiến · 36 Vụ Việc Lịch Sử, Khoa Học, Công Nghệ & Kinh Doanh"))}</span>
          <h2 id="heading-cases" tabindex="-1" style="font-size:30px;margin-block-end:6px;">{esc(T("36 moments where thinking methods saved billions, lives, or empires", "36 bước ngoặt nơi phương pháp tư duy định đoạt hàng tỷ đô la và sinh mạng"))}</h2>
          <p style="color:var(--ink-2);max-width:80ch;">{esc(T("Filter by domain or chapter, search any topic, read the primary external dossier, and jump straight into the matching interactive simulator.", "Lọc theo lĩnh vực hoặc chương sách, tìm kiếm nhanh bằng phím (/), mở tài liệu hồ sơ gốc và nhảy thẳng vào mô phỏng tương ứng."))}</p>
        </div>
        <span id="caseCountBadge" class="pill-tag" style="font-family:var(--mono);font-size:13px;padding:7px 14px;">
          36 / 36
        </span>
      </div>

      <div class="atlas-toolbar" role="group" aria-label="{esc(T("Case study domain filters", "Bộ lọc lĩnh vực hồ sơ"))}">
        {case_cat_pills_html}
      </div>

      <div class="atlas-toolbar" style="margin-block-end:20px;">
        <label for="caseSearch" class="visually-hidden">{esc(T("Search 36 case studies", "Tìm trong 36 hồ sơ"))}</label>
        <input id="caseSearch" type="search" placeholder="{esc(T("Search 36 cases (/): ChatGPT, Hanoi, Toyota, Boeing, Nobel, Bayes, SVB…", "Tìm hồ sơ (/): ChatGPT, Hà Nội 1902, Toyota, Boeing, Nobel, Bayes, SVB…"))}"
               oninput="filterCasesVault()" style="padding:9px 14px;border-radius:10px;border:1.5px solid var(--line-2);background:var(--surface);min-width:240px;flex:1;max-width:460px;">
        <label for="caseChFilter" style="font-family:var(--kicker);font-size:14px;font-weight:700;">{esc(T("Chapter:", "Chương:"))}</label>
        <select id="caseChFilter" onchange="filterCasesVault(true)" style="padding:9px 12px;border-radius:10px;border:1.5px solid var(--line-2);background:var(--surface);">
          <option value="all">{esc(T("All 9 Chapters (36 Cases)", "Tất cả 9 Chương (36 Hồ sơ)"))}</option>
          {ch_options_html}
        </select>
      </div>

      <div id="caseEmptyState" class="floor-detail" hidden style="margin-block-end:16px;"></div>

      <div id="casesVaultGrid" class="cases-grid">
        {all_cases_cards_html}
      </div>
    </section>

    <!-- ==================================================================
         VIEW 2: METHOD ATLAS & DEPENDENCY NETWORK (SCI-FI AI ATLAS STYLE)
         ================================================================== -->
    <section id="view-atlas" class="view-section" hidden>
      <div style="margin-block-end:14px;">
        <span class="eyebrow">{esc(T("Operate + Read Workspace · 3 Parts · 9 Chapters · 29 Tools", "Không gian Tương tác · 3 Phần · 9 Chương · 29 Công cụ"))}</span>
        <h2 id="heading-atlas" tabindex="-1" style="font-size:28px;margin-block-end:4px;">{esc(T("Everything rests on something older: The Methodological Cladogram", "Mọi phương pháp nâng cao đều tựa trên nền tảng đi trước"))}</h2>
        <p style="color:var(--ink-2);max-width:80ch;">{esc(T("Launch any Guided Saga to activate the step-by-step Story Walker, or click any tool node (or use Arrow keys) to inspect upstream prerequisites and downstream unlocks.", "Chọn một Lộ trình thực tế để bật Thanh dẫn chuyện từng bước, hoặc nhấn vào bất kỳ công cụ nào (hỗ trợ phím Mũi tên) để tra cứu tiền đề và năng lực mở khóa."))}</p>
      </div>

      <div class="atlas-toolbar">
        <button type="button" class="saga-pill" data-saga="all" aria-pressed="true" onclick="setSaga('all')">{esc(T("All 29 Tools", "Tất cả 29 Công cụ"))}</button>
        {saga_pills_html}
      </div>

      <div class="atlas-toolbar">
        <label for="atlasSearch" class="visually-hidden">{esc(T("Search tools", "Tìm kiếm công cụ"))}</label>
        <input id="atlasSearch" type="search" placeholder="{esc(T("Search tool (/): Bayes, SWOT, Wald, SCAMPER, CLD…", "Tìm công cụ (/): Bayes, SWOT, Đảo ngược, SCAMPER, Xương cá…"))}"
               oninput="renderAtlasGraph()" style="padding:8px 14px;border-radius:8px;border:1px solid var(--line-2);background:var(--surface);min-width:240px;flex:1;max-width:420px;">
        <label for="atlasChFilter" style="font-size:14px;font-weight:600;">{esc(T("Chapter:", "Chương:"))}</label>
        <select id="atlasChFilter" onchange="renderAtlasGraph()" style="padding:8px 12px;border-radius:8px;border:1px solid var(--line-2);background:var(--surface);">
          <option value="all">{esc(T("All 9 Chapters", "Tất cả 9 Chương"))}</option>
          {ch_options_html}
        </select>
        <button type="button" id="atlasMobModeBtn" class="tool-pill atlas-mode-toggle" onclick="toggleMobileAtlasMode()">
          <span>{esc(T("Show Vector Graph", "Xem Đồ thị Mạng lưới"))}</span>
        </button>
      </div>

      <div id="atlasEmptyState" class="floor-detail" hidden style="margin-block-end:14px;"></div>

      <div id="atlasWorkspace" class="atlas-workspace">
        <div>
          <div class="graph-panel" tabindex="0" role="region" aria-label="{esc(T("Methodological dependency network", "Đồ thị phụ thuộc phương pháp"))}">
            <svg id="atlasSvg" viewBox="0 0 960 880" role="img"
                 aria-label="{esc(T("Three-stage network graph connecting all 29 thinking tools from Part I through Part III.", "Đồ thị mạng lưới 3 giai đoạn kết nối 29 công cụ tư duy từ Phần I đến Phần III."))}"
                 style="width:100%;min-width:720px;height:auto;display:block;"></svg>
          </div>
          <div id="atlasMobileCards" class="atlas-mobile-cards"></div>
        </div>
        <aside id="atlasInspector" class="inspector-panel" aria-labelledby="inspTitle">
          <!-- Populated dynamically by selectTool() -->
        </aside>
      </div>
    </section>

    <!-- ==================================================================
         VIEW 3: SEVEN INTERACTIVE THINKING LABS (ACCESSIBLE TABLIST)
         ================================================================== -->
    <section id="view-labs" class="view-section" hidden>
      <span class="eyebrow">{esc(T("Practice Thinking! · 7 Live Interactive Laboratories", "Thực hành Tư duy! · 7 Phòng Thí nghiệm Mô phỏng Trực tiếp"))}</span>
      <h2 id="heading-labs" tabindex="-1" style="font-size:28px;margin-block-end:6px;">{esc(T("Test the book’s models and your own real decisions live", "Tự tay kiểm nghiệm các mô hình trong sách và chính quyết định của bạn"))}</h2>
      <p style="color:var(--ink-2);margin-block-end:14px;">{esc(T("Switch between the seven simulators below, including the new Personal Decision Stress-Tester & Memo Builder.", "Chuyển đổi giữa 7 phòng thí nghiệm dưới đây, bao gồm Bàn Thử Lửa Quyết Định Cá Nhân & Xuất Bản Ghi Nhớ mới."))}</p>

      <div class="lab-tablist" role="tablist" aria-label="{esc(T("Interactive Thinking Simulators", "Các phòng thí nghiệm tư duy tương tác"))}">
        <button type="button" role="tab" id="tab-octagon" data-lab="octagon" aria-selected="true" onclick="selectLab('octagon')">1 · {esc(T("8-Element Octagon", "Bát giác 8 Thành tố"))}</button>
        <button type="button" role="tab" id="tab-wald" data-lab="wald" aria-selected="false" onclick="selectLab('wald')">2 · {esc(T("Wald Inversion", "Máy bay Wald"))}</button>
        <button type="button" role="tab" id="tab-systems" data-lab="systems" aria-selected="false" onclick="selectLab('systems')">3 · {esc(T("Systems Loops", "Vòng Hệ thống"))}</button>
        <button type="button" role="tab" id="tab-games" data-lab="games" aria-selected="false" onclick="selectLab('games')">4 · {esc(T("5 Game Matrices", "5 Trò chơi"))}</button>
        <button type="button" role="tab" id="tab-bayes" data-lab="bayes" aria-selected="false" onclick="selectLab('bayes')">5 · {esc(T("Bayes & EV", "Lưới Bayes & EV"))}</button>
        <button type="button" role="tab" id="tab-science" data-lab="science" aria-selected="false" onclick="selectLab('science')">6 · {esc(T("Science Reactor", "Lò Khoa học"))}</button>
        <button type="button" role="tab" id="tab-builder" data-lab="builder" aria-selected="false" onclick="selectLab('builder')">7 · {esc(T("Decision Stress-Tester ★", "Thử Lửa Quyết Định ★"))}</button>
      </div>

      <!-- LAB 1: PAUL-ELDER 8-ELEMENT OCTAGON -->
      <div role="tabpanel" id="panel-octagon" aria-labelledby="tab-octagon">
        <div class="lab-panel-inner">
          <div class="lab-head-bar">
            <div>
              <h3 style="font-size:21px;margin-block-end:4px;">{esc(T("Paul & Elder’s 8-Element Conscious Thinking Octagon (Ch. 1 & Ch. 3)", "Bát giác Động 8 Thành tố Tư duy Có Ý thức (Chương 1 & 3)"))}</h3>
              <p style="font-size:14.5px;color:var(--ink-2);">{esc(T("Click any of the 8 vertices on the octagon and switch real-world scenarios.", "Nhấn vào từng đỉnh từ 1 đến 8 trên hình bát giác và đổi kịch bản thực tế."))}</p>
            </div>
            <div class="lab-head-ctrl">
              <label for="octPreset" style="font-size:13.5px;font-weight:700;display:block;margin-block-end:4px;">{esc(T("Scenario:", "Tình huống:"))}</label>
              <select id="octPreset" onchange="renderOctagonLab()" style="padding:8px 12px;border-radius:8px;border:1px solid var(--line-2);background:var(--bg);width:100%;">
                <option value="0">{esc(T("1. Grad School Now vs. Work First (p. 21)", "1. Học Cao học ngay hay Đi làm trước (tr. 21)"))}</option>
                <option value="1">{esc(T("2. Making AI a Partner vs. Crutch (p. 5)", "2. Biến AI thành Đối tác thay vì Nghĩ hộ (tr. 5)"))}</option>
                <option value="2">{esc(T("3. Ban Petrol Motorbikes Immediately? (p. 59)", "3. Chuyển đổi Xe xăng sang Xe điện (tr. 59)"))}</option>
              </select>
            </div>
          </div>
          <div class="sim-grid">
            <svg id="octSvg" viewBox="0 0 520 420" role="img" aria-label="Interactive 8-element octagon" style="width:100%;height:auto;background:var(--bg);border-radius:10px;border:1px solid var(--line);"></svg>
            <div id="octDetail" class="floor-detail"></div>
          </div>
        </div>
      </div>

      <!-- LAB 2: ABRAHAM WALD WWII BOMBER -->
      <div role="tabpanel" id="panel-wald" aria-labelledby="tab-wald" hidden="until-found">
        <div class="lab-panel-inner">
          <div class="lab-head-bar">
            <div>
              <h3 style="font-size:21px;margin-block-end:4px;">{esc(T("Inversion Lab: Click Any Zone on Abraham Wald’s WWII Bomber (Ch. 2, p. 31)", "Phòng Thí nghiệm Đảo ngược: Nhấn vào Từng Vùng Thân Máy bay Wald (Chương 2, tr. 31)"))}</h3>
              <p style="font-size:14.5px;color:var(--ink-2);">{esc(T("Compare what System 1 sees on survivors against what killed the missing planes.", "So sánh phán đoán cảm tính nhìn vào vết đạn hiện hữu với lập luận đảo ngược của Abraham Wald."))}</p>
            </div>
            <div style="display:flex;gap:6px;flex-wrap:wrap;">
              <button type="button" id="waldMode1" class="saga-pill" aria-pressed="false" onclick="setWaldMode('naive')">{esc(T("System 1: Armor Red Hits", "Hệ thống 1: Bọc chỗ trúng đạn"))}</button>
              <button type="button" id="waldMode2" class="saga-pill" aria-pressed="true" onclick="setWaldMode('wald')">{esc(T("Wald Inversion: Armor Clean Zones", "Đảo ngược Wald: Bọc vùng trắng"))}</button>
            </div>
          </div>
          <div class="sim-grid">
            <svg id="waldSvg" viewBox="0 0 540 400" role="img" aria-label="Interactive WWII bomber survivorship map" style="width:100%;height:auto;background:var(--bg);border-radius:10px;border:1px solid var(--line);"></svg>
            <div id="waldDetail" class="floor-detail"></div>
          </div>
        </div>
      </div>

      <!-- LAB 3: SYSTEMS THINKING CLD & BOT SIMULATOR -->
      <div role="tabpanel" id="panel-systems" aria-labelledby="tab-systems" hidden="until-found">
        <div class="lab-panel-inner">
          <h3 style="font-size:21px;margin-block-end:4px;">{esc(T("Systems Dynamics Simulator: Feedback Polarity & Time Delay τ (Ch. 6, pp. 111–123)", "Mô phỏng Động học Hệ thống: Vòng Phản hồi R/B & Độ trễ Thời gian τ (Chương 6)"))}</h3>
          <p style="font-size:14.5px;color:var(--ink-2);margin-block-end:16px;">{esc(T("Pick one of the book’s 4 systems or adjust growth rate & feedback delay to see why systems S-curve, oscillate, or collapse.", "Chọn 1 trong 4 hệ thống của sách hoặc kéo thanh trượt Độ mạnh vòng lặp & Độ trễ τ để xem vì sao hệ thống đi theo chữ S, dao động con lắc hay bùng nổ sụp đổ."))}</p>
          <div style="display:flex;gap:6px;flex-wrap:wrap;margin-block-end:16px;">
            <button type="button" class="saga-pill sys-preset" data-sp="scurve" aria-pressed="true" onclick="setSysPreset('scurve')">{esc(T("S-Curve (Startup R1 -> Market Cap B1)", "Chữ S (Khởi nghiệp R1 -> Bão hòa B1)"))}</button>
            <button type="button" class="saga-pill sys-preset" data-sp="osc" aria-pressed="false" onclick="setSysPreset('osc')">{esc(T("Delayed Oscillation (Savanna / Economy)", "Dao động Con lắc (Do độ trễ //)"))}</button>
            <button type="button" class="saga-pill sys-preset" data-sp="runaway" aria-pressed="false" onclick="setSysPreset('runaway')">{esc(T("Unchecked Runaway (Blame R1 / Bank Run)", "Tăng Mất Kiểm Soát (Giấu lỗi / Rút tiền NH)"))}</button>
            <button type="button" class="saga-pill sys-preset" data-sp="symptom" aria-pressed="false" onclick="setSysPreset('symptom')">{esc(T("Painkiller Trap (Quick B + Delayed Disease R//)", "Bẫy Thuốc Giảm Đau (Chữa triệu chứng tr. 118)"))}</button>
          </div>
          <div class="sim-grid">
            <svg id="sysBotSvg" viewBox="0 0 580 340" role="img" aria-label="Behavior over time simulation curve" style="width:100%;height:auto;background:var(--bg);border-radius:10px;border:1px solid var(--line);"></svg>
            <div class="floor-detail">
              <div class="ctrl-row">
                <label for="sysGain"><span>{esc(T("Reinforcing / Corrective Gain (r)", "Cường độ Tác động Phản hồi (r)"))}</span><strong id="sysGainVal">0.35</strong></label>
                <input id="sysGain" type="range" min="0.10" max="0.85" step="0.05" value="0.35" oninput="updateSysSim()">
              </div>
              <div class="ctrl-row">
                <label for="sysDelay"><span>{esc(T("Feedback Time Delay τ (steps //)", "Độ trễ Thời gian τ (ký hiệu //)"))}</span><strong id="sysDelayVal">1</strong></label>
                <input id="sysDelay" type="range" min="0" max="9" step="1" value="1" oninput="updateSysSim()">
              </div>
              <div id="sysExplain" style="margin-block-start:12px;font-size:14.5px;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- LAB 4: STRATEGIC GAME THEORY ARENA -->
      <div role="tabpanel" id="panel-games" aria-labelledby="tab-games" hidden="until-found">
        <div class="lab-panel-inner">
          <h3 style="font-size:21px;margin-block-end:4px;">{esc(T("Strategic Game Theory Arena: Play All 5 Book Archetypes (Ch. 7, pp. 136–139)", "Đấu trường Lý thuyết Trò chơi: Tương tác 5 Trò chơi Kinh điển (Chương 7)"))}</h3>
          <p style="font-size:14.5px;color:var(--ink-2);margin-block-end:14px;">{esc(T("Select a game and click any cell in the payoff table to inspect strategic incentives, Nash traps, and cooperative solutions.", "Chọn trò chơi rồi nhấn vào từng ô kết quả để xem điểm lợi ích, cái bẫy cá nhân và nguyên tắc hợp tác khôn ngoan."))}</p>
          <div style="display:flex;gap:6px;flex-wrap:wrap;margin-block-end:16px;">
            <button type="button" class="saga-pill gm-btn" data-gm="pd" aria-pressed="true" onclick="selectGame('pd')">{esc(T("1. Prisoner’s Dilemma", "1. Tiến thoái Lưỡng nan Tù nhân"))}</button>
            <button type="button" class="saga-pill gm-btn" data-gm="chicken" aria-pressed="false" onclick="selectGame('chicken')">{esc(T("2. Chicken Game", "2. Trò chơi Gà"))}</button>
            <button type="button" class="saga-pill gm-btn" data-gm="sexes" aria-pressed="false" onclick="selectGame('sexes')">{esc(T("3. Battle of the Sexes", "3. Cuộc chiến Giới tính"))}</button>
            <button type="button" class="saga-pill gm-btn" data-gm="cake" aria-pressed="false" onclick="selectGame('cake')">{esc(T("4. Fair Cake-Cutting", "4. Chia Bánh Công bằng"))}</button>
            <button type="button" class="saga-pill gm-btn" data-gm="rps" aria-pressed="false" onclick="selectGame('rps')">{esc(T("5. Rock–Paper–Scissors", "5. Oẳn tù tỳ (Tổng = 0)"))}</button>
          </div>
          <div class="sim-grid">
            <div id="gameBoard" style="overflow-x:auto;"></div>
            <div id="gameDetail" class="floor-detail"></div>
          </div>
        </div>
      </div>

      <!-- LAB 5: BAYESIAN 100-GRID & EXPECTED VALUE -->
      <div role="tabpanel" id="panel-bayes" aria-labelledby="tab-bayes" hidden="until-found">
        <div class="lab-panel-inner">
          <div class="lab-head-bar">
            <div>
              <h3 style="font-size:21px;margin-block-end:4px;">{esc(T("Bayesian Belief Updater & Expected Value Stress-Tester (Ch. 8, pp. 146–157)", "Máy tính Cập nhật Bayes Trực quan & Kỳ vọng EV (Chương 8, tr. 146–157)"))}</h3>
              <p style="font-size:14.5px;color:var(--ink-2);">{esc(T("Load the Medical Paradox or the p. 157 Hit-and-Run Cab problem, or drag the sliders.", "Chọn bài toán Chẩn đoán Y khoa hoặc Taxi Xanh – Đỏ (tr. 157), hoặc kéo thanh trượt thử nghiệm."))}</p>
            </div>
            <div style="display:flex;gap:6px;flex-wrap:wrap;">
              <button type="button" class="saga-pill" onclick="loadBayesPreset(1, 99, 2)">{esc(T("Medical 1% Prior (-> 33.3%)", "Xét nghiệm Bệnh 1% (-> 33,3%)"))}</button>
              <button type="button" class="saga-pill" onclick="loadBayesPreset(0.1, 99, 2)">{esc(T("Rare 0.1% Prior (-> 4.7%)", "Bệnh hiếm 0,1% (-> 4,7%)"))}</button>
              <button type="button" class="saga-pill" onclick="loadBayesPreset(60, 15, 85)">{esc(T("p.157 Green Cab | 'Red' Witness (-> 20.9%)", "Bài tập Taxi Xanh khi khai 'Đỏ' (-> 20,9%)"))}</button>
            </div>
          </div>
          <div class="sim-grid">
            <div>
              <svg id="bayesGridSvg" viewBox="0 0 460 320" role="img" aria-label="100-unit Bayesian frequency grid" style="width:100%;height:auto;background:var(--bg);border-radius:10px;border:1px solid var(--line);"></svg>
            </div>
            <div class="floor-detail">
              <div class="ctrl-row">
                <label for="byPrior"><span>{esc(T("Prior Base Rate P(A)", "Xác suất Cơ sở P(A)"))}</span><strong id="byPriorVal">1.0%</strong></label>
                <input id="byPrior" type="range" min="0.1" max="90" step="0.1" value="1" oninput="updateBayes()">
              </div>
              <div class="ctrl-row">
                <label for="bySens"><span>{esc(T("Likelihood if True P(B | A)", "Xác suất xuất hiện B khi có A: P(B|A)"))}</span><strong id="bySensVal">99%</strong></label>
                <input id="bySens" type="range" min="5" max="100" step="1" value="99" oninput="updateBayes()">
              </div>
              <div class="ctrl-row">
                <label for="byFp"><span>{esc(T("False-Alarm Rate P(B | ¬A)", "Xác suất B xuất hiện giả khi ¬A: P(B|¬A)"))}</span><strong id="byFpVal">2%</strong></label>
                <input id="byFp" type="range" min="0.5" max="90" step="0.5" value="2" oninput="updateBayes()">
              </div>
              <div id="bayesReadout" style="margin-block-start:10px;padding-block-start:10px;border-block-start:1px solid var(--line);"></div>
              <div style="margin-block-start:12px;padding-block-start:12px;border-block-start:1px solid var(--line);">
                <label style="display:flex;align-items:center;gap:10px;min-block-size:44px;font-size:14px;font-weight:700;cursor:pointer;">
                  <input type="checkbox" id="swanToggle" onchange="updateBayes()" style="width:18px;height:18px;flex:none;">
                  <span>{esc(T("Add 1% Black Swan Tail Risk (−95% wipeout) to Table 8.1 (+8% EV)", "Thêm 1% Rủi ro Thiên nga đen (mất −95%) vào Bảng 8.1 (EV +8%)"))}</span>
                </label>
                <p id="swanReadout" style="font-size:13.5px;color:var(--ink-2);margin-block-start:6px;"></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- LAB 6: SCIENTIFIC CONVERGENCE ENGINE -->
      <div role="tabpanel" id="panel-science" aria-labelledby="tab-science" hidden="until-found">
        <div class="lab-panel-inner">
          <h3 style="font-size:21px;margin-block-end:4px;">{esc(T("The 7-Step Scientific Convergence Reactor (Ch. 9, pp. 164–169)", "Lò Phản ứng Hội tụ 7 Bước Phương pháp Khoa học (Chương 9, tr. 164–169)"))}</h3>
          <p style="font-size:14.5px;color:var(--ink-2);margin-block-end:14px;">{esc(T("Click each step (1–7) to see which of the 8 Thinking Methods activate, using p. 166’s Office Fatigue experiment.", "Nhấn vào từng bước (1–7) để xem những phương pháp tư duy nào trong 8 chương trước cùng kích hoạt."))}</p>
          <div class="sim-grid">
            <svg id="sciSvg" viewBox="0 0 520 390" role="img" aria-label="7-step scientific convergence wheel" style="width:100%;height:auto;background:var(--bg);border-radius:10px;border:1px solid var(--line);"></svg>
            <div id="sciDetail" class="floor-detail"></div>
          </div>
        </div>
      </div>

      <!-- LAB 7: PERSONAL DECISION STRESS-TESTER & MEMO BUILDER -->
      <div role="tabpanel" id="panel-builder" aria-labelledby="tab-builder" hidden="until-found">
        <div class="lab-panel-inner">
          <div class="lab-head-bar">
            <div>
              <span class="eyebrow" style="color:var(--accent);">{esc(T("Capstone Synthesis · Apply Chapters 1, 2, 4, 6, 8 & 9 to Your Own Life", "Tổng Hợp Thực Hành · Đưa Quyết Định Thật Của Bạn Qua 5 Trạm Kiểm Định"))}</span>
              <h3 style="font-size:22px;margin-block-end:4px;">{esc(T("Personal Decision Stress-Tester & 1-Click Memo Builder", "Bàn Thử Lửa Quyết Định Cá Nhân & Xuất Bản Ghi Nhớ Tư Duy"))}</h3>
              <p style="font-size:14.5px;color:var(--ink-2);">{esc(T("Type any career, product, or financial dilemma (or load a preset), score how rigorously you have tested each dimension, and export a structured memo.", "Nhập câu hỏi quyết định của riêng bạn (hoặc chọn mẫu gợi ý), chấm mức độ kiểm định trên 5 trục phương pháp để phát hiện điểm mù và sao chép Bản ghi nhớ."))}</p>
            </div>
            <div style="display:flex;gap:6px;flex-wrap:wrap;">
              <button type="button" class="saga-pill" onclick="loadBuilderPreset(0)">{esc(T("Preset 1: Quit Job for AI Startup?", "Mẫu 1: Nghỉ việc mở Startup AI?"))}</button>
              <button type="button" class="saga-pill" onclick="loadBuilderPreset(1)">{esc(T("Preset 2: Borrow for Master’s?", "Mẫu 2: Vay tiền đi học Thạc sĩ?"))}</button>
              <button type="button" class="saga-pill" onclick="loadBuilderPreset(2)">{esc(T("Preset 3: Open Specialty Café?", "Mẫu 3: Góp vốn mở Quán Cà phê?"))}</button>
            </div>
          </div>

          <div style="margin-block-end:18px;">
            <label for="bldQuestion" style="font-family:var(--kicker);font-size:13.5px;font-weight:700;display:block;margin-block-end:6px;">
              {esc(T("Your Real-World Decision Question:", "Câu hỏi Quyết định Thực tế Của Bạn:"))}
            </label>
            <input id="bldQuestion" type="text"
                   value="{esc(T("Should I leave my stable engineering role to co-found a bootstrapped AI SaaS product?", "Có nên nghỉ công việc ổn định hiện tại để cùng bạn mở startup sản phẩm AI không?"))}"
                   oninput="updateDecisionBuilder()"
                   style="width:100%;padding:10px 14px;border-radius:10px;border:1.5px solid var(--line-2);background:var(--bg);font-weight:600;">
          </div>

          <div class="sim-grid">
            <div class="floor-detail">
              <div class="ctrl-row">
                <label for="bldS0"><span>1 · {esc(T("Ch. 1 Assumptions Audited (Fact vs. Wish)", "Ch. 1 Kiểm định Giả định ngầm (Thực tế vs. Ngộ nhận)"))}</span><strong id="bldV0">6/10</strong></label>
                <input id="bldS0" type="range" min="0" max="10" step="1" value="6" oninput="updateDecisionBuilder()">
              </div>
              <div class="ctrl-row">
                <label for="bldS1"><span>2 · {esc(T("Ch. 2 Pre-Mortem Inversion (Silent Graveyard)", "Ch. 2 Đảo ngược Pre-Mortem (Liệt kê kịch bản chết)"))}</span><strong id="bldV1">4/10</strong></label>
                <input id="bldS1" type="range" min="0" max="10" step="1" value="4" oninput="updateDecisionBuilder()">
              </div>
              <div class="ctrl-row">
                <label for="bldS2"><span>3 · {esc(T("Ch. 4 & 6 Root Structure vs. Symptom Fix", "Ch. 4 & 6 Giải quyết Gốc rễ & Độ trễ Hệ thống"))}</span><strong id="bldV2">7/10</strong></label>
                <input id="bldS2" type="range" min="0" max="10" step="1" value="7" oninput="updateDecisionBuilder()">
              </div>
              <div class="ctrl-row">
                <label for="bldS3"><span>4 · {esc(T("Ch. 8 Expected Value + Black-Swan Ruin Floor", "Ch. 8 Kỳ vọng EV Dương + Chốt chặn Không Phá sản"))}</span><strong id="bldV3">3/10</strong></label>
                <input id="bldS3" type="range" min="0" max="10" step="1" value="3" oninput="updateDecisionBuilder()">
              </div>
              <div class="ctrl-row" style="margin-block-end:0;">
                <label for="bldS4"><span>5 · {esc(T("Ch. 9 Cheap 7-Day Falsifiable Pilot Test", "Ch. 9 Thí nghiệm Nhỏ 7 Ngày Có Thể Bác Bỏ"))}</span><strong id="bldV4">5/10</strong></label>
                <input id="bldS4" type="range" min="0" max="10" step="1" value="5" oninput="updateDecisionBuilder()">
              </div>
            </div>

            <div class="floor-detail" style="background:var(--surface);">
              <svg id="builderRadarSvg" viewBox="0 0 420 300" role="img" aria-label="5-axis conscious decision readiness pentagon" style="width:100%;height:auto;background:var(--bg);border-radius:10px;border:1px solid var(--line);margin-block-end:12px;"></svg>
              <div id="builderVerdict" style="margin-block-end:12px;"></div>
              <div class="no-print" style="display:flex;gap:8px;flex-wrap:wrap;align-items:center;">
                <span class="copy-wrap">
                  <button type="button" class="btn-primary copy-btn" command="--copy" commandfor="memoPreviewBox">
                    <svg class="ic ic-copy" width="16" height="16" aria-hidden="true"><use href="#ic-copy"/></svg>
                    <svg class="ic ic-check" width="16" height="16" aria-hidden="true"><use href="#ic-check"/></svg>
                    <span>{esc(T("Copy Decision Memo", "Sao chép Bản Ghi Nhớ"))}</span>
                  </button>
                  <span class="copy-tip" role="status"></span>
                </span>
                <button type="button" class="btn-ghost" onclick="window.print()">
                  {ic_printer}
                  <span>{esc(T("Print / Save 1-Page PDF", "In / Lưu PDF 1 Trang"))}</span>
                </button>
              </div>
            </div>
          </div>

          <div class="sim-grid" style="margin-block-start:18px;">
            <div class="floor-detail">
              <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;">
                <h4 style="font-size:16.5px;">{esc(T("1 · Structured Decision Memo (Live Preview)", "1 · Bản Ghi Nhớ Quyết Định Có Cấu Trúc"))}</h4>
              </div>
              <pre id="memoPreviewBox" class="memo-code-box"></pre>
            </div>

            <div class="floor-detail">
              <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;">
                <div>
                  <span class="eyebrow" style="color:var(--c-prob);margin:0;">{esc(T("Preface p. 5 · AI as Socratic Partner, Never Crutch", "Lời nói đầu tr. 5 · Biến AI Thành Đối Tác Phản Biện"))}</span>
                  <h4 style="font-size:16.5px;">{esc(T("2 · Socratic AI Red-Team Prompt (Paste into Any AI)", "2 · Câu Lệnh AI Phản Biện Điểm Mù (Dán vào ChatGPT/Claude/Gemini)"))}</h4>
                </div>
                <span class="copy-wrap no-print">
                  <button type="button" class="tool-pill copy-btn" command="--copy" commandfor="socraticPromptBox">
                    <svg class="ic ic-copy" width="16" height="16" aria-hidden="true"><use href="#ic-copy"/></svg>
                    <svg class="ic ic-check" width="16" height="16" aria-hidden="true"><use href="#ic-check"/></svg>
                    <span>{esc(T("Copy AI Prompt", "Sao chép Lệnh AI"))}</span>
                  </button>
                  <span class="copy-tip" role="status"></span>
                </span>
              </div>
              <pre id="socraticPromptBox" class="memo-code-box"></pre>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================================================================
         VIEW 4: COGNITIVE BIASES, PROVERBS & FALLACIES
         ================================================================== -->
    <section id="view-traps" class="view-section" hidden>
      <span class="eyebrow" style="color:var(--c-trap);">{esc(T("System 1 Vulnerability Catalog · Chapters 1, 3 & 5", "Danh mục Điểm mù Nhận thức · Chương 1, 3 & 5"))}</span>
      <h2 id="heading-traps" tabindex="-1" style="font-size:28px;margin-block-end:6px;">{esc(T("10 Instinctive Biases (with Vietnamese Folk Wisdom) & 9 Fallacies", "10 Thiên kiến Bản năng (Gắn Tục ngữ Việt) & 9 Cái bẫy Ngụy biện – Thống kê"))}</h2>
      <p style="color:var(--ink-2);max-width:76ch;margin-block-end:20px;">{esc(T("Recognizing these patterns does not automatically erase them, yet naming a trap in real time is the first step to handing the wheel back to conscious method.", "Nhận diện tên gọi là bước đầu tiên để kéo phanh Hệ thống 1 và trao quyền kiểm soát lại cho phương pháp có kỷ luật."))}</p>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:16px;margin-block-end:28px;">
        {biases_html}
      </div>

      <div class="sec-card">
        <span class="eyebrow">{esc(T("Chapters 3 & 5 · Argument, Causal & Statistical Traps", "Chương 3 & 5 · Bẫy Ngụy biện, Nhân quả & Thống kê Thao túng"))}</span>
        <h3 style="font-size:22px;margin-block-end:14px;">{esc(T("Nine Classic Manipulation & Reasoning Errors in the Book", "Chín Lỗi Lập luận & Thống kê Điển hình Được Phân tích Trong Sách"))}</h3>
        <div class="cards-grid-4">{fallacies_html}</div>
      </div>
    </section>

    <!-- ==================================================================
         VIEW 5: BOOK ILLUSTRATION STUDIO (18 VECTOR PLATES + EDITORIAL REVIEW)
         ================================================================== -->
    <section id="view-plates" class="view-section" hidden>
      <span class="eyebrow">{esc(T("Book Illustration System · Print & Digital Companion", "Hệ thống Minh họa Sách · Bản vẽ Chuẩn Xuất bản & Tương tác"))}</span>
      <h2 id="heading-plates" tabindex="-1" style="font-size:28px;margin-block-end:6px;">{esc(T("24 Vector Illustrations & Story Plates for Học Tư Duy", "24 Bản vẽ Minh họa Sơ đồ & Chuyện kể Thiết kế cho Sách Học Tư Duy"))}</h2>
      <p style="color:var(--ink-2);max-width:80ch;margin-block-end:20px;">{esc(T("Includes 18 methodological plates plus 6 narrative story vignettes—all sharing one visual grammar and downloadable directly as crisp standalone SVGs for print layout.", "Bao gồm 18 bản vẽ cấu trúc phương pháp và 6 tranh kể chuyện ngụ ngôn—tuân thủ chung một ngôn ngữ thị giác của Systema Ratio và tải trực tiếp tệp .SVG sắc nét để dàn trang in sách."))}</p>

      <div class="teach-only sec-card" style="border-color:color-mix(in oklab, var(--c-prob) 40%, var(--line));">
        <span class="eyebrow" style="color:var(--c-prob);">{esc(T("Editorial & Proofreading Notes for the Print Manuscript", "Ghi chú Hiệu đính Biên tập Cho Bản thảo In (Tháng 1/2026)"))}</span>
        <h3 style="font-size:20px;margin-block-end:10px;">{esc(T("Helpful Polish Items Spotted Across the 171 Pages", "Một số Chi tiết Nhỏ Giúp Bản In Hoàn Thiện Hơn"))}</h3>
        <ul style="padding-inline-start:20px;font-size:14.5px;color:var(--ink-2);">{ed_notes_html}</ul>
      </div>

      {plates_html}
    </section>

    <!-- ==================================================================
         VIEW 6: 9-CHAPTER SPEC-BOARD READER & 29-TOOL MASTER TABLE
         ================================================================== -->
    <section id="view-reader" class="view-section" hidden>
      <span class="eyebrow">{esc(T("One Spec-Board That Repeats · All 9 Chapters & 29 Tools", "Cấu trúc 7 Phần Thống nhất · Trọn bộ 9 Chương & 29 Công cụ"))}</span>
      <h2 id="heading-reader" tabindex="-1" style="font-size:28px;margin-block-end:6px;">{esc(T("9-Chapter Illustrated Companion & Master Tool Directory", "Cẩm nang Minh họa 9 Chương & Bảng Tra cứu 29 Công cụ"))}</h2>
      <p style="color:var(--ink-2);margin-block-end:18px;">{esc(T("Every chapter follows Đào Minh Châu’s unified 7-part architecture paired with Minh’s real-world narrative thread.", "Tất cả các chương đều trình bày theo 7 mục thống nhất gắn liền với mạch truyện thực tế của Minh từ tuổi 22 đến 30."))}</p>

      <div class="reader-layout" style="margin-block-end:32px;">
        <nav class="reader-toc" aria-label="{esc(T("Chapters", "Mục lục Chương"))}">
          <div style="font-family:var(--mono);font-size:12px;font-weight:700;color:var(--ink-3);padding:4px 10px 8px;">
            {esc(T("Select Chapter (1–9)", "Chọn Chương Sách (1–9)"))}
          </div>
          {toc_btns}
        </nav>
        <div>{chapters_panes}</div>
      </div>

      <h3 style="font-size:22px;margin-block-end:10px;">{esc(T("Master Reference Table of All 29 Thinking Tools", "Bảng Tổng hợp Toàn bộ 29 Công cụ Thực hành Tư duy"))}</h3>
      <div tabindex="0" role="region" aria-labelledby="tools-table-caption" class="table-wrapper">
        <table class="tools-table" style="--lbl-ch:'{esc(T("Chapter", "Chương"))}';--lbl-when:'{esc(T("When to use", "Khi nào dùng"))}';--lbl-what:'{esc(T("Core mechanism", "Bản chất công cụ"))}';">
          <caption id="tools-table-caption">{esc(T("Click any row to open its step-by-step protocol and pitfalls", "Nhấn vào bất kỳ dòng công cụ nào để mở hướng dẫn từng bước và các lỗi cần tránh"))}</caption>
          <thead>
            <tr>
              <th scope="col">{esc(T("Tool", "Công cụ"))}</th>
              <th scope="col">{esc(T("Chapter & Pages", "Chương & Trang"))}</th>
              <th scope="col">{esc(T("When to Use", "Tình huống Áp dụng"))}</th>
              <th scope="col">{esc(T("How It Works", "Bản chất Vận hành"))}</th>
            </tr>
          </thead>
          <tbody>{table_rows}</tbody>
        </table>
      </div>

      <!-- FULL SUGGESTED BOOKSHELF DIRECTORY (23 LINKED CLASSICS) -->
      <div class="sec-card" id="sec-bookshelf" style="margin-block-start:28px;">
        <span class="eyebrow" style="color:var(--accent);">{esc(T("The Thinker’s Library · 23 Classic Books Cited Across Chapters 1–9", "Thư viện Người Học Tư Duy · 23 Tác phẩm Kinh điển Gợi ý Xuyên suốt 9 Chương"))}</span>
        <h3 style="font-size:24px;margin-block-end:6px;">{esc(T("Where to read deeper: Direct links to every recommended book", "Đọc sâu hơn sau cuốn sách này: Liên kết tra cứu trực tiếp từng tác phẩm"))}</h3>
        <p style="color:var(--ink-2);max-width:76ch;margin-block-end:14px;">{esc(T("Every title recommended by Đào Minh Châu—plus Karl Popper’s Preface touchstone—is linked below on Open Library and Google Books.", "Toàn bộ danh mục sách đọc thêm của tác giả Đào Minh Châu ở cuối 9 chương được tổng hợp kèm lời dẫn và liên kết trực tiếp tới Open Library & Google Books."))}</p>
        <div class="books-grid">{all_books_cards_html}</div>
      </div>
    </section>
  </main>

  <!-- THUMB-REACHABLE MOBILE BOTTOM NAVIGATION BAR (<= 1140px) -->
  <nav class="mobile-bottom-nav" aria-label="{esc(T("Mobile Primary Navigation", "Điều hướng di động"))}">
    <button type="button" class="mob-nav-btn" data-view="overview" aria-current="page" onclick="switchView('overview', null, true)">{ic_compass}<span>{mob_lbl_overview}</span></button>
    <button type="button" class="mob-nav-btn" data-view="cases" onclick="switchView('cases', null, true)">{ic_briefcase}<span>{mob_lbl_cases}</span></button>
    <button type="button" class="mob-nav-btn" data-view="atlas" onclick="switchView('atlas', null, true)">{ic_map}<span>{mob_lbl_atlas}</span></button>
    <button type="button" class="mob-nav-btn" data-view="labs" onclick="switchView('labs', null, true)">{ic_flask}<span>{mob_lbl_labs}</span></button>
    <button type="button" class="mob-nav-btn" data-view="traps" onclick="switchView('traps', null, true)">{ic_shield}<span>{mob_lbl_traps}</span></button>
    <button type="button" class="mob-nav-btn" data-view="reader" onclick="switchView('reader', null, true)">{ic_book}<span>{mob_lbl_reader}</span></button>
  </nav>

  <footer style="border-block-start:1px solid var(--line);padding:26px 20px;font-size:14px;color:var(--ink-3);">
    <div style="max-width:1440px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;">
      <div>
        <strong style="color:var(--ink);" lang="la">Systema Ratio</strong> · {esc(T("Illustrated & Interactive Architecture for", "Hệ thống Minh họa & Tương tác cho sách"))}
        <em>Học Tư Duy</em> · Đào Minh Châu (Hà Nội, 08/01/2026).
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <a href="index.html" class="tool-pill text-link" style="text-decoration:none;">{esc(T("Bilingual Portal", "Cổng Song ngữ"))}</a>
        <a href="{esc_raw(meta["other_href"])}" lang="{esc_raw(meta["other_lang"])}" class="tool-pill text-link" style="text-decoration:none;">{ic_globe}<span>{esc(meta["other_label"])}</span></a>
      </div>
    </div>
  </footer>

  <!-- Native Light-Dismiss Modal Dialog for Tool Dossiers -->
  <dialog id="toolDialog" class="sr-dialog" closedby="any" aria-labelledby="toolDialogTitle">
    <div id="toolDialogBody"></div>
  </dialog>

  <!-- Native Light-Dismiss Modal Dialog for Spin-a-Dilemma Roulette -->
  <dialog id="dilemmaDialog" class="sr-dialog" closedby="any" aria-labelledby="dilemmaDialogTitle">
    <div id="dilemmaDialogBody"></div>
  </dialog>

  <script>
  const SR = {payload_json};
  const EN = SR.lang === "en";
  const L = (e, v) => EN ? e : v;

  /* ========================================================================
     1. COLOR SCHEME TOGGLE (mwg `dark-mode-toggle` tri-state compliant)
     ======================================================================== */
  const metaScheme = document.querySelector('meta[name="color-scheme"]');
  const sysDarkMQ = window.matchMedia("(prefers-color-scheme: dark)");

  function getRenderedDark() {{
    const c = metaScheme.content;
    if (c === "dark") return true;
    if (c === "light") return false;
    return sysDarkMQ.matches;
  }}

  function syncThemeButton() {{
    const isDark = getRenderedDark();
    const btn = document.getElementById("themeBtn");
    const txt = document.getElementById("themeText");
    const useEl = document.getElementById("themeUse");
    const label = isDark ? SR.meta.theme_light : SR.meta.theme_dark;
    btn.setAttribute("aria-label", label);
    txt.textContent = label;
    if (useEl) useEl.setAttribute("href", isDark ? "#ic-sun" : "#ic-moon");
  }}

  function toggleColorScheme() {{
    const target = getRenderedDark() ? "light" : "dark";
    const sysCurrent = sysDarkMQ.matches ? "dark" : "light";
    if (target === sysCurrent) {{
      try {{ localStorage.removeItem("sr-color-scheme"); }} catch (e) {{}}
      metaScheme.content = "light dark";
    }} else {{
      try {{ localStorage.setItem("sr-color-scheme", target); }} catch (e) {{}}
      metaScheme.content = target;
    }}
    syncThemeButton();
  }}

  sysDarkMQ.addEventListener("change", syncThemeButton);
  window.addEventListener("storage", (ev) => {{
    if (ev.key === "sr-color-scheme") {{
      metaScheme.content = ev.newValue ?? "light dark";
      syncThemeButton();
    }}
  }});

  function announce(msg) {{
    const el = document.getElementById("srAnnouncer");
    if (el) el.textContent = msg;
  }}

  function toggleTeachMode() {{
    const on = document.body.classList.toggle("teach-mode");
    document.getElementById("teachBtn").setAttribute("aria-pressed", String(on));
    announce(on ? L("Educator & Editor lens enabled", "Đã bật góc nhìn Giảng dạy & Biên tập") : L("Standard reader lens", "Đã chuyển về chế độ đọc tiêu chuẩn"));
  }}

  const toolDialog = document.getElementById("toolDialog");
  const dilemmaDialog = document.getElementById("dilemmaDialog");
  [toolDialog, dilemmaDialog].forEach(dlg => {{
    if (dlg && !("closedBy" in HTMLDialogElement.prototype)) {{
      dlg.addEventListener("click", (event) => {{
        if (event.target !== dlg) return;
        const rect = dlg.getBoundingClientRect();
        const inside = rect.top <= event.clientY && event.clientY <= rect.top + rect.height &&
                       rect.left <= event.clientX && event.clientX <= rect.left + rect.width;
        if (!inside) dlg.close();
      }});
    }}
  }});

  /* ========================================================================
     1B. SCROLL PROGRESS FALLBACK (mwg `scroll-progress-indicator`)
     ======================================================================== */
  if (!CSS.supports("animation-timeline", "scroll()") &&
      window.matchMedia("(prefers-reduced-motion: no-preference)").matches) {{
    const progEl = document.getElementById("scrollProgress");
    if (progEl) {{
      window.addEventListener("scroll", () => {{
        const scrollable = document.documentElement.scrollHeight - window.innerHeight;
        const pct = scrollable > 0 ? Math.min(1, Math.max(0, window.scrollY / scrollable)) : 0;
        progEl.style.transform = `scaleX(${{pct}})`;
      }}, {{ passive: true }});
    }}
  }}

  /* ========================================================================
     2. DIRECTIONAL VIEW TRANSITIONS + TRUE URL HASH HISTORY (`hashchange`)
     ======================================================================== */
  const VIEWS = ["overview", "cases", "atlas", "labs", "traps", "plates", "reader"];
  const VIEW_HEADINGS = {{
    overview: "main-heading",
    cases: "heading-cases",
    atlas: "heading-atlas",
    labs: "heading-labs",
    traps: "heading-traps",
    plates: "heading-plates",
    reader: "heading-reader",
  }};
  let currentView = "overview";
  let currentChapter = "ch1";
  let suppressHashListener = false;

  function runDirectionalTransition(direction, updateFn, focusId) {{
    const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!document.startViewTransition || prefersReduced || !direction) {{
      updateFn();
      if (focusId) document.getElementById(focusId)?.focus({{ preventScroll: true }});
      return;
    }}
    try {{
      const transition = document.startViewTransition({{
        update: updateFn,
        types: [direction],
      }});
      transition.finished.finally(() => {{
        if (focusId) document.getElementById(focusId)?.focus({{ preventScroll: true }});
      }});
    }} catch (err) {{
      const transition = document.startViewTransition(updateFn);
      transition.finished.finally(() => {{
        if (focusId) document.getElementById(focusId)?.focus({{ preventScroll: true }});
      }});
    }}
  }}

  function applyViewDOM(v, sub) {{
    if (!VIEWS.includes(v)) v = "overview";
    currentView = v;
    for (const id of VIEWS) {{
      const sec = document.getElementById("view-" + id);
      if (sec) sec.hidden = (id !== v);
    }}
    document.querySelectorAll(".nav-link, .mob-nav-btn").forEach(btn => {{
      if (btn.dataset.view === v) btn.setAttribute("aria-current", "page");
      else btn.removeAttribute("aria-current");
    }});

    if (v === "cases") {{
      if (sub) {{
        if (SR.chapters[sub]) {{
          const chSel = document.getElementById("caseChFilter");
          if (chSel) chSel.value = sub;
          activeCaseCat = "all";
        }} else {{
          activeCaseCat = sub;
          const chSel = document.getElementById("caseChFilter");
          if (chSel) chSel.value = "all";
        }}
        document.querySelectorAll(".case-cat-pill").forEach(b => {{
          b.setAttribute("aria-pressed", String(b.dataset.cat === activeCaseCat));
        }});
      }}
      filterCasesVault();
    }}
    if (v === "atlas") {{
      if (sub && SR.tools.some(t => t.id === sub)) selectedToolId = sub;
      renderAtlasGraph();
    }}
    if (v === "labs" && sub) selectLab(sub, false);
    if (v === "reader") {{
      if (sub === "books") {{
        selectChapter(currentChapter, false);
        setTimeout(() => {{
          document.getElementById("sec-bookshelf")?.scrollIntoView({{ block: "start" }});
        }}, 45);
      }} else {{
        selectChapter(sub && SR.chapters[sub] ? sub : currentChapter, false);
      }}
    }}
    if (v === "plates" && sub) {{
      setTimeout(() => {{
        document.getElementById("plate-" + sub)?.scrollIntoView({{ block: "start" }});
      }}, 40);
    }}
    if (v === "overview" && sub === "floors") {{
      setTimeout(() => {{
        document.getElementById("sec-floors")?.scrollIntoView({{ block: "start" }});
      }}, 40);
    }}
  }}

  function switchView(v, sub, pushHistory = false, explicitDir = null) {{
    if (!VIEWS.includes(v)) v = "overview";
    const oldIdx = VIEWS.indexOf(currentView);
    const newIdx = VIEWS.indexOf(v);
    const dir = explicitDir || (newIdx > oldIdx ? "forward" : (newIdx < oldIdx ? "backward" : null));
    const newHash = "#" + v + (sub ? "/" + sub : "");

    if (location.hash !== newHash) {{
      suppressHashListener = true;
      if (pushHistory) history.pushState(null, "", newHash);
      else history.replaceState(null, "", newHash);
      setTimeout(() => {{ suppressHashListener = false; }}, 0);
    }}
    const sw = document.getElementById("langSwitchLink");
    if (sw) sw.href = "{esc(meta["other_href"])}" + newHash;

    const focusTarget = pushHistory ? VIEW_HEADINGS[v] : null;
    runDirectionalTransition(pushHistory ? dir : null, () => {{
      applyViewDOM(v, sub);
      if (!sub || v !== "plates") window.scrollTo({{ top: 0, behavior: "instant" }});
    }}, focusTarget);
  }}

  function syncFromHash() {{
    if (suppressHashListener) return;
    const raw = location.hash.replace(/^#/, "");
    if (!raw) {{
      applyViewDOM("overview", null);
      return;
    }}
    const [hv, hsub] = raw.split("/");
    if (VIEWS.includes(hv)) {{
      const oldIdx = VIEWS.indexOf(currentView);
      const newIdx = VIEWS.indexOf(hv);
      const dir = newIdx > oldIdx ? "forward" : (newIdx < oldIdx ? "backward" : null);
      const sw = document.getElementById("langSwitchLink");
      if (sw) sw.href = "{esc(meta["other_href"])}#" + raw;
      runDirectionalTransition(dir, () => applyViewDOM(hv, hsub), VIEW_HEADINGS[hv]);
    }}
  }}
  window.addEventListener("hashchange", syncFromHash);

  function jumpTarget(spec) {{
    const [v, sub] = spec.split(":");
    switchView(v, sub, true);
  }}

  /* ========================================================================
     3. COLD-OPEN SYSTEM 1 MIRROR TRAPS + PROTAGONIST TIMELINE + READING MEMORY
     ======================================================================== */
  const mirrorAnswers = {{}};
  function answerMirrorTrap(idx, kind) {{
    mirrorAnswers[idx] = kind;
    const tr = SR.traps[idx];
    document.querySelectorAll(`.quiz-opt[data-qidx="${{idx}}"]`).forEach(btn => {{
      if (btn.dataset.kind === kind) btn.setAttribute("data-picked", kind);
      else btn.removeAttribute("data-picked");
    }});
    const rev = document.getElementById("qrev-" + idx);
    if (rev) {{
      rev.hidden = false;
      const verdict = kind === "trap"
        ? `<strong style="color:var(--c-trap);display:block;margin-block-end:4px;">${{tr.caught}}</strong>`
        : `<strong style="color:var(--c-systems);display:block;margin-block-end:4px;">${{tr.passed}}</strong>`;
      rev.innerHTML = `
        ${{verdict}}
        <p style="color:var(--ink-2);margin-block-end:8px;">${{tr.explain}}</p>
        <button type="button" class="tool-pill" onclick="jumpTarget('${{tr.target}}')">${{tr.cta}} →</button>
      `;
    }}
    const tested = Object.keys(mirrorAnswers).length;
    const wiseCount = Object.values(mirrorAnswers).filter(v => v === "wise").length;
    const badge = document.getElementById("mirrorScoreBadge");
    if (badge) {{
      badge.textContent = L(
        `System 2 Reflex: ${{wiseCount}} / ${{tested}} Caught (${{tested}}/3 Tested)`,
        `Phản xạ Hệ thống 2: Tỉnh táo ${{wiseCount}} / ${{tested}} (${{tested}}/3 Đã thử)`
      );
    }}
  }}

  function selectMinhBeat(idx) {{
    document.querySelectorAll(".minh-stop").forEach(b => {{
      b.setAttribute("aria-pressed", String(Number(b.dataset.minh) === idx));
    }});
    const outEl = document.getElementById("minhStageOut");
    if (!outEl) return;
  }}

  function syncResumeButton() {{
    const btn = document.getElementById("resumeBtn");
    if (!btn) return;
    try {{
      const saved = localStorage.getItem("sr-last-ch");
      if (saved && SR.chapters[saved]) {{
        const c = SR.chapters[saved];
        btn.hidden = false;
        btn.textContent = L(`Resume Ch. ${{c.num}}: ${{c.title}} →`, `Đọc tiếp Ch. ${{c.num}}: ${{c.title}} →`);
      }}
    }} catch (e) {{}}
  }}

  function resumeLastChapter() {{
    try {{
      const saved = localStorage.getItem("sr-last-ch") || "ch1";
      switchView("reader", saved, true);
    }} catch (e) {{
      switchView("reader", "ch1", true);
    }}
  }}

  /* ========================================================================
     4. CROSS-VIEW GUIDED STORY WALKER (TOURS + LIFE SAGAS!)
     ======================================================================== */
  let journeyState = null; // {{ mode: 'tour'|'saga', id: string, stepIdx: number }}

  function startGuidedTour(tourId) {{
    journeyState = {{ mode: "tour", id: tourId, stepIdx: 0 }};
    syncJourneyStep(null);
  }}

  function syncJourneyStep(dir) {{
    const bar = document.getElementById("journeyBar");
    const inner = document.getElementById("journeyInner");
    if (!journeyState) {{
      bar.hidden = true;
      return;
    }}
    bar.hidden = false;

    if (journeyState.mode === "tour") {{
      const tr = SR.tours.find(x => x.id === journeyState.id);
      const st = tr.stops[journeyState.stepIdx];
      const dots = tr.stops.map((s, i) =>
        `<button type="button" class="j-step-dot" aria-current="${{i === journeyState.stepIdx ? 'step' : 'false'}}" onclick="goJourneyStep(${{i}})">${{i + 1}}</button>`
      ).join("");
      inner.innerHTML = `
        <div>
          <div class="journey-steps">
            <strong style="font-size:13px;color:var(--accent);margin-inline-end:6px;">${{tr.name}}:</strong>
            ${{dots}}
            <span style="font-size:13px;font-weight:700;margin-inline-start:4px;">${{st.label}}</span>
          </div>
          <p style="font-size:13.5px;color:var(--ink-2);">${{st.beat}}</p>
        </div>
        <div style="display:flex;gap:6px;flex-wrap:wrap;align-items:center;">
          <button type="button" class="tool-pill" ${{journeyState.stepIdx === 0 ? 'disabled style="opacity:0.45;cursor:not-allowed;"' : ''}} onclick="stepJourney(-1)">← ${{L("Prev", "Trước")}}</button>
          <button type="button" class="btn-primary" style="padding:8px 16px;font-size:13.5px;" onclick="stepJourney(1)">
            ${{journeyState.stepIdx < tr.stops.length - 1 ? L("Next Stop →", "Chặng Tiếp →") : L("Finish Tour ✓", "Hoàn thành ✓")}}
          </button>
          <button type="button" class="tool-pill" onclick="closeJourney()" aria-label="${{L("Exit guided story", "Đóng thanh dẫn chuyện")}}">✕</button>
        </div>
      `;
      switchView(st.view, st.sub, true, dir);
    }} else if (journeyState.mode === "saga") {{
      const sg = SR.pathways.find(x => x.id === journeyState.id);
      const st = sg.steps[journeyState.stepIdx];
      const tl = SR.tools.find(x => x.id === st.id);
      const dots = sg.steps.map((s, i) =>
        `<button type="button" class="j-step-dot" aria-current="${{i === journeyState.stepIdx ? 'step' : 'false'}}" onclick="goJourneyStep(${{i}})">${{i + 1}}</button>`
      ).join("");
      inner.innerHTML = `
        <div>
          <div class="journey-steps">
            <strong style="font-size:13px;color:${{sg.color}};margin-inline-end:6px;">${{sg.name}}:</strong>
            ${{dots}}
            <span style="font-size:13px;font-weight:700;margin-inline-start:4px;">${{tl.short_name}}</span>
          </div>
          <p style="font-size:13.5px;color:var(--ink-2);">${{st.beat}}</p>
        </div>
        <div style="display:flex;gap:6px;flex-wrap:wrap;align-items:center;">
          <button type="button" class="tool-pill" ${{journeyState.stepIdx === 0 ? 'disabled style="opacity:0.45;cursor:not-allowed;"' : ''}} onclick="stepJourney(-1)">← ${{L("Prev", "Trước")}}</button>
          <button type="button" class="tool-pill" onclick="jumpTarget('${{st.lab}}')">${{L("Open Lab / Ch. ↗", "Mở Thực hành ↗")}}</button>
          <button type="button" class="btn-primary" style="padding:8px 16px;font-size:13.5px;" onclick="stepJourney(1)">
            ${{journeyState.stepIdx < sg.steps.length - 1 ? L("Next Tool →", "Bước Tiếp →") : L("Done ✓", "Xong ✓")}}
          </button>
          <button type="button" class="tool-pill" onclick="closeJourney()" aria-label="${{L("Exit saga", "Thoát lộ trình")}}">✕</button>
        </div>
      `;
      selectedToolId = st.id;
      if (currentView !== "atlas") switchView("atlas", st.id, true, dir);
      else renderAtlasGraph();
    }}
  }}

  function goJourneyStep(idx) {{
    if (!journeyState) return;
    const dir = idx > journeyState.stepIdx ? "forward" : "backward";
    journeyState.stepIdx = idx;
    syncJourneyStep(dir);
  }}

  function stepJourney(delta) {{
    if (!journeyState) return;
    const len = journeyState.mode === "tour"
      ? SR.tours.find(x => x.id === journeyState.id).stops.length
      : SR.pathways.find(x => x.id === journeyState.id).steps.length;
    const next = journeyState.stepIdx + delta;
    if (next < 0) return;
    if (next >= len) {{
      closeJourney();
      return;
    }}
    journeyState.stepIdx = next;
    syncJourneyStep(delta > 0 ? "forward" : "backward");
  }}

  function closeJourney() {{
    if (journeyState && journeyState.mode === "saga") {{
      activeSaga = "all";
      document.querySelectorAll(".saga-pill[data-saga]").forEach(b => {{
        b.setAttribute("aria-pressed", String(b.dataset.saga === "all"));
      }});
      if (currentView === "atlas") renderAtlasGraph();
    }}
    journeyState = null;
    document.getElementById("journeyBar").hidden = true;
  }}

  /* ========================================================================
     5. OVERVIEW: FOUR FLOORS & SIX QUESTION THREADS
     ======================================================================== */
  function selectFloor(idx) {{
    const fl = SR.meta.floors[idx];
    document.querySelectorAll(".floor-btn").forEach(b => {{
      b.setAttribute("aria-pressed", String(Number(b.dataset.floor) === idx));
    }});
    const linksHtml = fl.links.map(([lbl, tgt]) =>
      `<button type="button" class="tool-pill" onclick="jumpTarget('${{tgt}}')">${{lbl}} →</button>`
    ).join(" ");
    document.getElementById("floorDetail").innerHTML = `
      <div style="font-family:var(--mono);font-size:12px;font-weight:700;color:var(--ink-3);margin-block-end:4px;">${{fl.num}} · ${{fl.badge}}</div>
      <h3 style="font-size:19px;margin-block-end:6px;">${{fl.name}}</h3>
      <p style="color:var(--ink-2);margin-block-end:12px;">${{fl.story}}</p>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">${{linksHtml}}</div>
    `;
  }}

  function selectThread(idx) {{
    const th = SR.meta.threads[idx];
    document.querySelectorAll(".thread-btn").forEach(b => {{
      b.setAttribute("aria-pressed", String(Number(b.dataset.thread) === idx));
    }});
    document.getElementById("threadOut").innerHTML = `
      <p style="margin-block-end:12px;">${{th.ans}}</p>
      <button type="button" class="tool-pill" onclick="jumpTarget('${{th.target}}')">${{th.cta}}</button>
    `;
  }}

  /* ========================================================================
     6. DOOR 2: INTERACTIVE METHOD ATLAS (ZERO TRUNCATION + MOBILE STAGE CARDS)
     ======================================================================== */
  let activeSaga = "all";
  let selectedToolId = "t-paul-elder-8";

  function setSaga(id) {{
    activeSaga = id;
    document.querySelectorAll(".saga-pill[data-saga]").forEach(b => {{
      b.setAttribute("aria-pressed", String(b.dataset.saga === id));
    }});
    if (id === "all") {{
      if (journeyState && journeyState.mode === "saga") {{
        journeyState = null;
        document.getElementById("journeyBar").hidden = true;
      }}
      renderAtlasGraph();
    }} else {{
      journeyState = {{ mode: "saga", id, stepIdx: 0 }};
      syncJourneyStep(null);
    }}
  }}

  function toggleMobileAtlasMode() {{
    const ws = document.getElementById("atlasWorkspace");
    const btn = document.getElementById("atlasMobModeBtn");
    const forceSvg = ws.classList.toggle("force-svg");
    btn.textContent = forceSvg
      ? L("Show Compact Cards", "Xem Danh sách Thẻ")
      : L("Show Vector Graph", "Xem Đồ thị Mạng lưới");
  }}

  function resetAtlasFilters() {{
    const s = document.getElementById("atlasSearch");
    const c = document.getElementById("atlasChFilter");
    if (s) s.value = "";
    if (c) c.value = "all";
    setSaga("all");
  }}

  function renderAtlasGraph() {{
    const svg = document.getElementById("atlasSvg");
    if (!svg) return;
    const q = (document.getElementById("atlasSearch")?.value || "").trim().toLowerCase();
    const chF = document.getElementById("atlasChFilter")?.value || "all";
    const sagaObj = SR.pathways.find(p => p.id === activeSaga);
    const sagaSet = sagaObj ? new Set(sagaObj.nodes) : null;

    const colX = {{ 1: 132, 2: 480, 3: 828 }};
    const stageTools = {{ 1: [], 2: [], 3: [] }};
    SR.tools.forEach(t => stageTools[t.stage].push(t));

    const pos = {{}};
    [1, 2, 3].forEach(st => {{
      const arr = stageTools[st];
      if (st === 1) {{
        arr.forEach((t, i) => {{ pos[t.id] = {{ x: colX[st], y: 340 + i * 168 }}; }});
      }} else if (st === 3) {{
        const topPad = 112, span = 676;
        const step = arr.length > 1 ? span / (arr.length - 1) : 0;
        arr.forEach((t, i) => {{ pos[t.id] = {{ x: colX[st], y: topPad + i * step }}; }});
      }} else {{
        const topPad = 80, span = 762;
        const step = arr.length > 1 ? span / (arr.length - 1) : 0;
        arr.forEach((t, i) => {{ pos[t.id] = {{ x: colX[st], y: topPad + i * step }}; }});
      }}
    }});

    const sel = SR.tools.find(t => t.id === selectedToolId) || SR.tools[1];
    const upSet = new Set(sel.rests_on);
    const dnSet = new Set(sel.powers);

    let matchCount = 0;
    SR.tools.forEach(t => {{
      const mQ = !q || t.name.toLowerCase().includes(q) || t.what.toLowerCase().includes(q) || t.short_name.toLowerCase().includes(q);
      const mC = chF === "all" || t.ch === chF;
      const mS = !sagaSet || sagaSet.has(t.id);
      if (mQ && mC && mS) matchCount++;
    }});

    const emptyEl = document.getElementById("atlasEmptyState");
    if (emptyEl) {{
      if (matchCount === 0) {{
        emptyEl.hidden = false;
        emptyEl.innerHTML = `
          <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;">
            <div>
              <strong style="display:block;font-size:16px;margin-block-end:2px;">${{L("No tools match your current filter.", "Không tìm thấy công cụ khớp bộ lọc hiện tại.")}}</strong>
              <span style="font-size:14px;color:var(--ink-2);">${{L("Try searching by problem symptom (e.g., 'delay', 'assumption', 'risk') or clear filters to see all 29 tools.", "Hãy thử tìm theo từ khóa khác (ví dụ: 'giả định', 'độ trễ', 'rủi ro') hoặc xóa bộ lọc để xem trọn bộ 29 công cụ.")}}</span>
            </div>
            <button type="button" class="btn-primary" onclick="resetAtlasFilters()">${{L("Reset All Filters", "Xóa Bộ lọc")}}</button>
          </div>
        `;
      }} else {{
        emptyEl.hidden = true;
      }}
    }}

    const halfW = 114;
    let out = `
      <rect x="18" y="12" width="228" height="38" rx="8" fill="var(--surface-2)" stroke="var(--line)"/>
      <text x="132" y="35" text-anchor="middle" font-size="12" font-weight="800" fill="var(--ink)">${{L("PART I · FOUNDATION (2)", "PHẦN I · NHẬP MÔN (2)")}}</text>
      <rect x="348" y="12" width="264" height="38" rx="8" fill="var(--surface-2)" stroke="var(--line)"/>
      <text x="480" y="35" text-anchor="middle" font-size="12" font-weight="800" fill="var(--ink)">${{L("PART II · CORE METHODS (18)", "PHẦN II · PHƯƠNG PHÁP CƠ BẢN (18)")}}</text>
      <rect x="714" y="12" width="228" height="38" rx="8" fill="var(--surface-2)" stroke="var(--line)"/>
      <text x="828" y="35" text-anchor="middle" font-size="12" font-weight="800" fill="var(--ink)">${{L("PART III · ADVANCED (9)", "PHẦN III · NÂNG CAO (9)")}}</text>
    `;

    // Edges
    SR.tools.forEach(src => {{
      src.powers.forEach(dstId => {{
        const p1 = pos[src.id], p2 = pos[dstId];
        if (!p1 || !p2) return;
        const isUp = (dstId === sel.id && upSet.has(src.id));
        const isDn = (src.id === sel.id && dnSet.has(dstId));
        const inSaga = sagaSet && sagaSet.has(src.id) && sagaSet.has(dstId);
        let stroke = "var(--line-2)", sw = 1.2, op = 0.3;
        if (isUp) {{ stroke = "var(--c-analytical)"; sw = 2.8; op = 0.95; }}
        else if (isDn) {{ stroke = "var(--c-creative)"; sw = 2.8; op = 0.95; }}
        else if (inSaga) {{ stroke = sagaObj.color; sw = 2.4; op = 0.88; }}
        else if (sagaSet) {{ op = 0.07; }}
        if (p1.x === p2.x) {{
          const archX = p1.x + (p1.x > 500 ? 124 : -124);
          out += `<path d="M ${{p1.x}},${{p1.y + (p2.y > p1.y ? 16 : -16)}} Q ${{archX}},${{(p1.y + p2.y)/2}} ${{p2.x}},${{p2.y + (p2.y > p1.y ? -16 : 16)}}" fill="none" stroke="${{stroke}}" stroke-width="${{sw}}" opacity="${{op}}"/>`;
        }} else {{
          const mx = (p1.x + p2.x) / 2;
          out += `<path d="M ${{p1.x + halfW}},${{p1.y}} C ${{mx}},${{p1.y}} ${{mx}},${{p2.y}} ${{p2.x - halfW}},${{p2.y}}" fill="none" stroke="${{stroke}}" stroke-width="${{sw}}" opacity="${{op}}"/>`;
        }}
      }});
    }});

    // Nodes (Full crisp short_name, zero ellipses!)
    SR.tools.forEach(t => {{
      const p = pos[t.id];
      const chInfo = SR.chapters[t.ch];
      const matchesQ = !q || t.name.toLowerCase().includes(q) || t.what.toLowerCase().includes(q) || t.short_name.toLowerCase().includes(q);
      const matchesCh = chF === "all" || t.ch === chF;
      const matchesSaga = !sagaSet || sagaSet.has(t.id);
      const active = matchesQ && matchesCh && matchesSaga;
      const isSel = t.id === sel.id;
      const isLinked = upSet.has(t.id) || dnSet.has(t.id);
      const op = isSel ? 1 : (active ? 0.96 : (isLinked ? 0.75 : 0.18));
      const bw = isSel ? 3 : (isLinked ? 2.2 : 1.5);
      out += `
        <g class="atlas-node" data-tid="${{t.id}}" transform="translate(${{p.x - halfW}}, ${{p.y - 17}})" opacity="${{op}}" style="cursor:pointer"
           onclick="selectTool('${{t.id}}')" tabindex="0" role="button" aria-label="${{t.name}}"
           onkeydown="handleAtlasKey(event, '${{t.id}}')">
          <rect x="0" y="0" width="${{halfW * 2}}" height="34" rx="8" fill="var(--surface)" stroke="${{isSel ? 'var(--ink)' : chInfo.color}}" stroke-width="${{bw}}"/>
          <circle cx="14" cy="17" r="5" fill="${{chInfo.color}}"/>
          <text x="26" y="21" font-size="12" font-weight="${{isSel ? '800' : '600'}}" fill="var(--ink)">${{t.short_name}}</text>
        </g>`;
    }});

    svg.innerHTML = out;
    renderMobileAtlasCards(stageTools, sel, q, chF, sagaSet);
    renderInspector(sel);
  }}

  function renderMobileAtlasCards(stageTools, sel, q, chF, sagaSet) {{
    const wrap = document.getElementById("atlasMobileCards");
    if (!wrap) return;
    const titles = {{
      1: L("Part I · Foundation (2)", "Phần I · Nhập môn (2)"),
      2: L("Part II · Core Methods (18)", "Phần II · Phương pháp Cơ bản (18)"),
      3: L("Part III · Advanced Syntheses (9)", "Phần III · Phương pháp Nâng cao (9)"),
    }};
    let htmlStr = "";
    [1, 2, 3].forEach(st => {{
      const items = stageTools[st].filter(t => {{
        const mQ = !q || t.name.toLowerCase().includes(q) || t.what.toLowerCase().includes(q) || t.short_name.toLowerCase().includes(q);
        const mC = chF === "all" || t.ch === chF;
        const mS = !sagaSet || sagaSet.has(t.id);
        return mQ && mC && mS;
      }});
      if (!items.length) return;
      const rows = items.map(t => {{
        const c = SR.chapters[t.ch];
        return `<button type="button" class="mob-tool-chip" aria-current="${{t.id === sel.id}}" onclick="selectTool('${{t.id}}', true)">
          <span style="width:9px;height:9px;border-radius:50%;background:${{c.color}};flex:none;" aria-hidden="true"></span>
          <span style="flex:1;">${{t.name}}</span>
          <span class="badge-mini">Ch.${{c.num}}</span>
        </button>`;
      }}).join("");
      htmlStr += `<div class="mob-stage-box"><h3 style="font-size:15.5px;margin-block-end:6px;">${{titles[st]}}</h3>${{rows}}</div>`;
    }});
    wrap.innerHTML = htmlStr;
  }}

  function handleAtlasKey(e, tid) {{
    if (e.key === "Enter" || e.key === " ") {{
      e.preventDefault();
      selectTool(tid);
      return;
    }}
    const cur = SR.tools.find(x => x.id === tid);
    if (!cur) return;
    let nextId = null;
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {{
      const col = SR.tools.filter(x => x.stage === cur.stage);
      const i = col.indexOf(cur);
      const ni = (i + (e.key === "ArrowDown" ? 1 : col.length - 1)) % col.length;
      nextId = col[ni].id;
    }} else if (e.key === "ArrowRight" && cur.powers.length) {{
      nextId = cur.powers[0];
    }} else if (e.key === "ArrowLeft" && cur.rests_on.length) {{
      nextId = cur.rests_on[0];
    }}
    if (nextId) {{
      e.preventDefault();
      selectTool(nextId);
      setTimeout(() => {{
        document.querySelector(`.atlas-node[data-tid="${{nextId}}"]`)?.focus();
      }}, 20);
    }}
  }}

  function selectTool(id, scrollMob = false) {{
    selectedToolId = id;
    if (journeyState && journeyState.mode === "saga") {{
      const sg = SR.pathways.find(x => x.id === journeyState.id);
      const idx = sg ? sg.nodes.indexOf(id) : -1;
      if (idx >= 0) {{
        journeyState.stepIdx = idx;
        syncJourneyStep(null);
      }}
    }}
    renderAtlasGraph();
    const newHash = "#atlas/" + id;
    if (currentView === "atlas" && location.hash !== newHash) {{
      suppressHashListener = true;
      history.pushState(null, "", newHash);
      setTimeout(() => {{ suppressHashListener = false; }}, 0);
    }}
    const t = SR.tools.find(x => x.id === id);
    if (t) announce(t.name);
    if (scrollMob && window.innerWidth <= 1080) {{
      document.getElementById("atlasInspector")?.scrollIntoView({{ behavior: "smooth", block: "start" }});
    }}
  }}

  function buildToolDossierHTML(t, inModal) {{
    const ch = SR.chapters[t.ch];
    const stepsHtml = t.steps.map(s => `<li style="margin-block-end:6px;">${{s}}</li>`).join("");
    const upHtml = t.rests_on.length
      ? t.rests_on.map(id => {{
          const o = SR.tools.find(x => x.id === id);
          const fn = inModal ? `openToolModal('${{id}}')` : `selectTool('${{id}}')`;
          return `<button type="button" class="tool-pill" onclick="${{fn}}">← ${{o.short_name}}</button>`;
        }}).join(" ")
      : `<span style="font-size:13.5px;color:var(--ink-3);">${{L("Foundational entry point", "Điểm khởi đầu nền tảng")}}</span>`;

    const dnHtml = t.powers.length
      ? t.powers.map(id => {{
          const o = SR.tools.find(x => x.id === id);
          const fn = inModal ? `openToolModal('${{id}}')` : `selectTool('${{id}}')`;
          return `<button type="button" class="tool-pill" onclick="${{fn}}">${{o.short_name}} →</button>`;
        }}).join(" ")
      : `<span style="font-size:13.5px;color:var(--ink-3);">${{L("Capstone synthesis", "Đỉnh hội tụ tổng hợp")}}</span>`;

    return `
      <span class="eyebrow" style="color:${{ch.color}};">${{L("Chapter", "Chương")}} ${{ch.num}} · ${{ch.title}} · p. ${{t.pages}}</span>
      <h3 id="${{inModal ? 'toolDialogTitle' : 'inspTitle'}}" style="font-size:22px;margin-block-end:6px;">${{t.name}}</h3>
      <p style="font-size:14px;font-weight:700;color:var(--accent);margin-block-end:8px;">${{L("When to deploy:", "Khi nào sử dụng:")}} ${{t.when}}</p>
      <p style="font-size:14.5px;color:var(--ink-2);">${{t.what}}</p>

      <div class="insp-sec">
        <h4 style="font-size:14.5px;margin-block-end:6px;">${{L("Step-by-Step Protocol", "Quy trình Thực hành")}}</h4>
        <ol style="padding-inline-start:18px;margin:0;font-size:14px;">${{stepsHtml}}</ol>
      </div>

      <div class="insp-sec">
        <div style="padding:11px 13px;border-radius:8px;background:color-mix(in oklab, var(--c-trap) 8%, var(--surface-2));border:1px solid color-mix(in oklab, var(--c-trap) 30%, var(--line));font-size:13.5px;">
          <strong style="color:var(--c-trap);">${{L("Common Trap:", "Lỗi Phổ biến Cần Tránh:")}}</strong> ${{t.pitfall}}
        </div>
      </div>

      <div class="insp-sec">
        <p style="font-size:14px;color:var(--ink-2);"><strong>${{L("Book Anchor:", "Ví dụ Điển hình Trong Sách:")}}</strong> ${{t.example}}</p>
      </div>

      <div class="insp-sec">
        <div style="font-size:12.5px;font-weight:700;color:var(--c-analytical);margin-block-end:6px;">${{L("Rests on (Prerequisites):", "Tựa trên nền tảng:")}}</div>
        <div style="display:flex;gap:6px;flex-wrap:wrap;margin-block-end:10px;">${{upHtml}}</div>
        <div style="font-size:12.5px;font-weight:700;color:var(--c-creative);margin-block-end:6px;">${{L("Powers (Downstream Unlocks):", "Mở khóa tiếp theo:")}}</div>
        <div style="display:flex;gap:6px;flex-wrap:wrap;">${{dnHtml}}</div>
      </div>
    `;
  }}

  function renderInspector(t) {{
    const el = document.getElementById("atlasInspector");
    if (el) el.innerHTML = buildToolDossierHTML(t, false) +
      `<div class="insp-sec"><button type="button" class="btn-ghost" style="width:100%;justify-content:center;" onclick="switchView('reader','${{t.ch}}', true)">${{L("Open Full Chapter", "Đọc Toàn bộ Chương")}} ${{SR.chapters[t.ch].num}} →</button></div>`;
  }}

  function openToolModal(id) {{
    const t = SR.tools.find(x => x.id === id);
    if (!t || !toolDialog) return;
    document.getElementById("toolDialogBody").innerHTML =
      buildToolDossierHTML(t, true) +
      `<div style="margin-block-start:16px;display:flex;justify-content:flex-end;gap:8px;">
         <button type="button" class="btn-primary" onclick="document.getElementById('toolDialog').close()">${{L("Close", "Đóng")}}</button>
       </div>`;
    toolDialog.showModal();
  }}

  /* ========================================================================
     7. DOOR 3: ACCESSIBLE LAB TABS + 7 LIVE COGNITIVE SIMULATORS
     ======================================================================== */
  const LABS = ["octagon", "wald", "systems", "games", "bayes", "science", "builder"];

  function selectLab(id, pushUrl = true) {{
    if (!LABS.includes(id)) id = "octagon";
    document.querySelectorAll('.lab-tablist [role="tab"]').forEach(tab => {{
      const sel = tab.dataset.lab === id;
      tab.setAttribute("aria-selected", String(sel));
      if (sel) {{
        try {{ tab.scrollIntoView({{ block: "nearest", inline: "nearest", container: "nearest" }}); }}
        catch (e) {{ tab.scrollIntoView({{ block: "nearest", inline: "nearest" }}); }}
      }}
    }});
    LABS.forEach(lid => {{
      const panel = document.getElementById("panel-" + lid);
      if (!panel) return;
      if (lid === id) panel.removeAttribute("hidden");
      else panel.setAttribute("hidden", "until-found");
    }});
    if (pushUrl && currentView === "labs") {{
      const h = "#labs/" + id;
      if (location.hash !== h) {{
        suppressHashListener = true;
        history.pushState(null, "", h);
        setTimeout(() => {{ suppressHashListener = false; }}, 0);
      }}
    }}
  }}

  LABS.forEach(lid => {{
    const panel = document.getElementById("panel-" + lid);
    if (panel) panel.addEventListener("beforematch", () => selectLab(lid, false));
  }});

  document.querySelector(".lab-tablist")?.addEventListener("keydown", (e) => {{
    if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
    const tabs = [...document.querySelectorAll('.lab-tablist [role="tab"]')];
    const idx = tabs.indexOf(document.activeElement);
    if (idx < 0) return;
    e.preventDefault();
    const next = tabs[(idx + (e.key === "ArrowRight" ? 1 : tabs.length - 1)) % tabs.length];
    next.focus();
    selectLab(next.dataset.lab);
  }});

  /* --- LAB 1: PAUL-ELDER OCTAGON --- */
  let octVertex = 3;
  const OCT_CASES = [
    {{
      ctx: L("University Senior · Tight Savings · Rising Job Market", "Sinh viên ĐH năm cuối · Tài chính hạn hẹp · Ngành cần kinh nghiệm"),
      els: [
        [L("1 · Purpose", "1 · Mục đích"), L("Make a career move aligned with my circumstances and 10-year goals.", "Đưa ra quyết định phù hợp nhất với hoàn cảnh và mục tiêu cá nhân.")],
        [L("2 · Key Question", "2 · Câu hỏi chính"), L("Should I enter a Master’s program immediately after graduation or work first?", "Học hay không học cao học ngay sau khi tốt nghiệp đại học?")],
        [L("3 · Point of View", "3 · Quan điểm"), L("Long-term professional capability & financial sustainability.", "Quan điểm phát triển nghề nghiệp dài hạn của bản thân.")],
        [L("4 · Assumptions", "4 · Giả định"), L("Hidden belief to test: ‘Having an M.A. automatically guarantees better jobs.’", "Tiền đề cần kiểm tra: “Có bằng cao học thì cơ hội nghề nghiệp mặc nhiên tốt hơn.”")],
        [L("5 · Information", "5 · Thông tin"), L("Actual employer hiring criteria, personal savings, feedback from early vs. late M.A. alumni.", "Yêu cầu thực tế của ngành, tài chính cá nhân, kinh nghiệm người học cao học sớm/muộn.")],
        [L("6 · Inference / Concepts", "6 · Suy luận"), L("Opportunity cost, experiential capital, cost–benefit analysis.", "Chi phí cơ hội, kinh nghiệm thực tiễn, phân tích chi phí – lợi ích.")],
        [L("7 · Conclusions", "7 · Kết luận"), L("Working 2–3 years before pursuing a targeted Master’s is the stronger move now.", "Đi làm vài năm tích lũy trước khi học cao học là lựa chọn hợp lý hơn lúc này.")],
        [L("8 · Implications", "8 · Hệ quả"), L("Proactively hunt learning-rich jobs; save tuition (+ accept risk of losing study momentum).", "Chủ động tìm môi trường giàu cọ xát; tiết kiệm học phí (+ chấp nhận rủi ro ngại đi học lại).")],
      ]
    }},
    {{
      ctx: L("Knowledge Worker · Rapid LLM Adoption (2026)", "Người lao động tri thức · Kỷ nguyên bùng nổ AI (2026)"),
      els: [
        [L("1 · Purpose", "1 · Mục đích"), L("Preserve human agency and career value while multiplying output with AI.", "Giữ vững vai trò con người và nâng cao năng lực cạnh tranh khi làm việc cùng AI.")],
        [L("2 · Key Question", "2 · Câu hỏi chính"), L("How do I use AI as a cognitive partner without letting my own thinking atrophy?", "Làm sao biến AI thành đối tác thay vì để AI nghĩ hộ làm thui chột tư duy?")],
        [L("3 · Point of View", "3 · Quan điểm"), L("Lifelong intellectual autonomy (Jensen Huang & Harari lens, p. 5).", "Tự chủ trí tuệ dài hạn (lăng kính Jensen Huang & Harari, tr. 5).")],
        [L("4 · Assumptions", "4 · Giả định"), L("Hidden trap: ‘Fast fluent AI text equals verified truth.’", "Giả định nguy hiểm: “Câu trả lời trôi chảy của AI đồng nghĩa với sự thật đúng đắn.”")],
        [L("5 · Information", "5 · Thông tin"), L("Primary sources, base-rate statistics, domain constraints AI cannot see.", "Dữ liệu gốc, xác suất cơ sở, bối cảnh thực địa mà AI không tự kiểm chứng được.")],
        [L("6 · Inference / Concepts", "6 · Suy luận"), L("Browne–Keeley critique, Popperian falsification, Systems leverage.", "Phản biện Browne–Keeley, kiểm chứng bác bỏ Popper, tư duy hệ thống.")],
        [L("7 · Conclusions", "7 · Kết luận"), L("Frame problems & audit assumptions myself first; use AI for divergent options & stress-testing.", "Tự mình định nghĩa vấn đề & kiểm định kết luận; dùng AI để mở rộng phương án và phản biện chéo.")],
        [L("8 · Implications", "8 · Hệ quả"), L("Slower first 5 minutes per task, vastly higher long-term skill compounding.", "Chậm hơn 5 phút đầu mỗi việc nhưng năng lực tư duy bản thân sắc bén dần theo thời gian.")],
      ]
    }},
    {{
      ctx: L("Urban Air Quality Policy · Millions of Low-Income Commuters (p. 59)", "Chính sách Giao thông Đô thị · Hàng triệu lao động thu nhập thấp (tr. 59)"),
      els: [
        [L("1 · Purpose", "1 · Mục đích"), L("Cut hazardous urban air pollution without crushing working-class livelihoods.", "Giảm ô nhiễm không khí đô thị mà không gây sốc sinh kế cho người dân.")],
        [L("2 · Key Question", "2 · Câu hỏi chính"), L("Should a city ban all petrol motorbikes immediately?", "Có nên bắt buộc chuyển đổi tất cả xe xăng sang xe điện ngay lập tức?")],
        [L("3 · Point of View", "3 · Quan điểm"), L("Whole-system public welfare (ecology + economics + social equity).", "Phúc lợi toàn hệ thống: Môi trường + Kinh tế + Công bằng xã hội.")],
        [L("4 · Assumptions", "4 · Giả định"), L("Unchecked assumption: ‘Petrol bikes are the #1 emission source and everyone can afford EVs.’", "Giả định thiếu kiểm chứng: “Xe xăng là nguồn ô nhiễm lớn nhất và ai cũng đủ tiền đổi xe ngay.”")],
        [L("5 · Information", "5 · Thông tin"), L("Source-apportionment air data, grid charging capacity, household income distribution.", "Tỷ trọng các nguồn gây ô nhiễm, hạ tầng trạm sạc, thu nhập của nhóm yếu thế.")],
        [L("6 · Inference / Concepts", "6 · Suy luận"), L("Conditional logic (‘If…then’), stakeholder impact analysis.", "Lập luận có điều kiện (“Nếu… thì…”), phân tích tác động xã hội.")],
        [L("7 · Conclusions", "7 · Kết luận"), L("IF petrol bikes are top source, phase out over 5 years WITH low-income credit subsidies.", "Nếu đúng là nguồn chính, thực hiện lộ trình 5 năm KÈM chính sách hỗ trợ tín dụng cho người nghèo.")],
        [L("8 · Implications", "8 · Hệ quả"), L("Cleaner air with public consent instead of economic shock and backlash.", "Giảm ô nhiễm bền vững, tránh phản kháng xã hội (Định luật hệ thống Senge).")],
      ]
    }}
  ];

  function renderOctagonLab() {{
    const idx = Number(document.getElementById("octPreset")?.value || 0);
    const cs = OCT_CASES[idx];
    const svg = document.getElementById("octSvg");
    const cx = 260, cy = 224, r = 122;
    const pts = Array.from({{length: 8}}, (_, i) => {{
      const a = (-112.5 + 45 * i) * Math.PI / 180;
      return [cx + r * Math.cos(a), cy + r * Math.sin(a), a];
    }});

    let s = `<rect x="14" y="14" width="492" height="392" rx="12" fill="none" stroke="var(--c-meta)" stroke-width="1.8" stroke-dasharray="5 3"/>
             <text x="28" y="38" font-size="12" font-weight="800" fill="var(--c-meta)">${{L("CONTEXT:", "HOÀN CẢNH:")}} ${{cs.ctx}}</text>`;
    for (let i = 0; i < 8; i++) {{
      for (let j = i + 1; j < 8; j++) {{
        const active = (i === octVertex || j === octVertex);
        s += `<line x1="${{pts[i][0].toFixed(1)}}" y1="${{pts[i][1].toFixed(1)}}" x2="${{pts[j][0].toFixed(1)}}" y2="${{pts[j][1].toFixed(1)}}"
                    stroke="${{active ? 'var(--accent)' : 'var(--line-2)'}}" stroke-width="${{active ? 2.3 : 1}}" opacity="${{active ? 0.9 : 0.35}}"/>`;
      }}
    }}
    pts.forEach(([px, py, a], i) => {{
      const sel = i === octVertex;
      const lx = cx + (r + 48) * Math.cos(a);
      const ly = cy + (r + 30) * Math.sin(a);
      const shortNm = cs.els[i][0].replace(/^\\d+\\s·\\s/, "");
      s += `<g style="cursor:pointer" onclick="octVertex=${{i}};renderOctagonLab()">
              <circle cx="${{px.toFixed(1)}}" cy="${{py.toFixed(1)}}" r="${{sel ? 20 : 16}}" fill="${{sel ? 'var(--accent)' : 'var(--c-meta)'}}" stroke="var(--surface)" stroke-width="2.5"/>
              <text x="${{px.toFixed(1)}}" y="${{(py + 4).toFixed(1)}}" text-anchor="middle" font-family="var(--mono)" font-size="12" font-weight="800" fill="var(--accent-ink)">${{i + 1}}</text>
              <text x="${{lx.toFixed(1)}}" y="${{(ly + 4).toFixed(1)}}" text-anchor="middle" font-size="12" font-weight="${{sel ? '800' : '600'}}" fill="var(--ink)">${{shortNm}}</text>
            </g>`;
    }});
    svg.innerHTML = s;

    const [vTitle, vBody] = cs.els[octVertex];
    document.getElementById("octDetail").innerHTML = `
      <span class="eyebrow" style="color:var(--accent);">${{L("Selected Vertex", "Thành tố Đang Chọn")}} (${{octVertex + 1}} / 8)</span>
      <h4 style="font-size:20px;margin-block-end:8px;">${{vTitle}}</h4>
      <p style="font-size:15px;margin-block-end:14px;">${{vBody}}</p>
      <hr style="border:none;border-block-start:1px solid var(--line);margin-block:12px;">
      <div style="display:grid;gap:6px;font-size:13.5px;">
        ${{cs.els.map(([t, b], k) => `<div style="cursor:pointer;padding:6px 10px;border-radius:6px;background:${{k===octVertex?'var(--surface)':'transparent'}};border:1px solid ${{k===octVertex?'var(--accent)':'transparent'}}" onclick="octVertex=${{k}};renderOctagonLab()"><strong>${{t}}:</strong> ${{b}}</div>`).join("")}}
      </div>`;
  }}

  /* --- LAB 2: ABRAHAM WALD WWII BOMBER --- */
  let waldMode = "wald";
  let waldZone = "engines";
  const WALD_ZONES = {{
    wings: {{
      title: L("Outer Wings & Fuselage Skin (Heavy Red Bullet Clusters)", "Cánh ngoài & Vỏ thân máy bay (Chi chít vết đạn đỏ)"),
      hits: L("High hit count on returning bombers", "Mật độ vết đạn RẤT CAO trên máy bay trở về"),
      naive: L("System 1 Mistake: ‘Look at all those holes—bolt heavy armor onto the wings!’", "Sai lầm Hệ thống 1: “Chỗ này trúng nhiều đạn nhất—phải bọc thép dày vào đây!”"),
      wald: L("Wald’s Truth: Planes riddled here STILL FLEW HOME. Wing skin can tolerate perforations—do NOT waste scarce armor weight here.", "Kết luận của Wald: Bị bắn thủng lỗ chỗ ở đây mà máy bay VẪN BAY VỀ ĐƯỢC -> Không nguy hiểm chí mạng, không cần bọc thép.")
    }},
    cockpit: {{
      title: L("Pilot Cockpit Canopy (Zero Bullet Holes on Survivors!)", "Buồng lái Phi công (Hầu như KHÔNG có vết đạn trên máy bay về đích!)"),
      hits: L("0–1 hits observed on returning bombers", "Gần như 0 vết đạn ghi nhận ở sân bay"),
      naive: L("System 1 Mistake: ‘The cockpit never gets hit—leave it unarmored.’", "Sai lầm Hệ thống 1: “Buồng lái chẳng mấy khi dính đạn—không cần gia cố.”"),
      wald: L("Wald’s Truth: Every bomber hit in the cockpit crashed into the sea and NEVER returned to be counted! ARMOR IMMEDIATELY.", "Kết luận của Wald: Máy bay trúng đạn vào buồng lái ĐÃ RƠI HẾT không về được để đếm! ĐÂY CHÍNH LÀ CHỖ PHẢI BỌC THÉP.")
    }},
    engines: {{
      title: L("Twin Engines & Fuel Pumps (Clean on Returning Planes!)", "Hai Động cơ Chính (Sạch bóng vết đạn trên máy bay sống sót!)"),
      hits: L("Near-zero hits on survivors", "Hầu như không có vết đạn trên máy bay trở về"),
      naive: L("System 1 Mistake: ‘Enemy flak rarely hits engines.’", "Sai lầm Hệ thống 1: “Đạn phòng không ít khi bắn trúng động cơ.”"),
      wald: L("Wald’s Truth: Flak hits uniformly—clean engines on survivors prove engine hits are FATAL. Highest-priority armor target!", "Kết luận của Wald: Đạn bắn ngẫu nhiên đều khắp—động cơ máy bay sống sót lành lặn chứng tỏ trúng đạn vào động cơ là RƠI NGAY! Ưu tiên bọc thép số 1.")
    }}
  }};

  function setWaldMode(m) {{
    waldMode = m;
    document.getElementById("waldMode1").setAttribute("aria-pressed", String(m === "naive"));
    document.getElementById("waldMode2").setAttribute("aria-pressed", String(m === "wald"));
    renderWaldLab();
  }}

  function renderWaldLab() {{
    const svg = document.getElementById("waldSvg");
    const armorW = waldMode === "wald";
    const dots = [[120,192],[142,202],[165,194],[184,207],[355,194],[378,205],[402,195],[420,206],[262,238],[276,254],[268,274],[244,338],[296,340]];
    svg.innerHTML = `
      <g onclick="waldZone='wings';renderWaldLab()" style="cursor:pointer">
        <path d="M 270,64 C 284,64 290,95 290,152 L 462,184 L 462,214 L 288,224 L 284,326 L 336,338 L 336,356 L 280,352 L 270,368 L 260,352 L 204,356 L 204,338 L 256,326 L 252,224 L 78,214 L 78,184 L 250,152 C 250,95 256,64 270,64 Z"
              fill="${{!armorW ? 'color-mix(in oklab, var(--m-trap) 18%, var(--surface-2))' : 'var(--surface-2)'}}" stroke="var(--ink)" stroke-width="2.2"/>
        ${{dots.map(([x,y]) => `<circle cx="${{x}}" cy="${{y}}" r="5" fill="var(--m-trap)"/>`).join("")}}
      </g>
      <g onclick="waldZone='engines';renderWaldLab()" style="cursor:pointer">
        <rect x="192" y="144" width="32" height="62" rx="7" fill="${{armorW ? 'color-mix(in oklab, var(--m-meta) 30%, var(--surface))' : 'var(--surface)'}}" stroke="var(--m-meta)" stroke-width="3"/>
        <rect x="316" y="144" width="32" height="62" rx="7" fill="${{armorW ? 'color-mix(in oklab, var(--m-meta) 30%, var(--surface))' : 'var(--surface)'}}" stroke="var(--m-meta)" stroke-width="3"/>
      </g>
      <g onclick="waldZone='cockpit';renderWaldLab()" style="cursor:pointer">
        <ellipse cx="270" cy="108" rx="15" ry="23" fill="${{armorW ? 'color-mix(in oklab, var(--m-meta) 30%, var(--surface))' : 'var(--surface)'}}" stroke="var(--m-meta)" stroke-width="3"/>
      </g>
      <text x="270" y="390" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink-2)">
        ${{L("Click Cockpit, Twin Engines, or Red-Dotted Wings to inspect", "Nhấn vào Buồng lái, Hai Động cơ hoặc Cánh nhiều chấm đỏ để phân tích")}}
      </text>`;

    const z = WALD_ZONES[waldZone];
    document.getElementById("waldDetail").innerHTML = `
      <span class="eyebrow" style="color:var(--c-creative);">${{z.hits}}</span>
      <h4 style="font-size:19px;margin-block-end:10px;">${{z.title}}</h4>
      <div style="padding:11px 13px;border-radius:8px;background:color-mix(in oklab, var(--m-trap) 10%, var(--surface-2));border:1px solid color-mix(in oklab, var(--m-trap) 35%, var(--line));margin-block-end:10px;font-size:14px;">${{z.naive}}</div>
      <div style="padding:11px 13px;border-radius:8px;background:color-mix(in oklab, var(--m-meta) 12%, var(--surface-2));border:1px solid color-mix(in oklab, var(--m-meta) 40%, var(--line));font-size:14px;font-weight:600;">${{z.wald}}</div>`;
  }}

  /* --- LAB 3: SYSTEMS DYNAMICS BOT SIMULATOR --- */
  let sysMode = "scurve";
  function setSysPreset(m) {{
    sysMode = m;
    document.querySelectorAll(".sys-preset").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.sp === m)));
    const g = document.getElementById("sysGain"), d = document.getElementById("sysDelay");
    if (m === "scurve") {{ g.value = 0.35; d.value = 1; }}
    if (m === "osc") {{ g.value = 0.45; d.value = 5; }}
    if (m === "runaway") {{ g.value = 0.25; d.value = 0; }}
    if (m === "symptom") {{ g.value = 0.40; d.value = 4; }}
    updateSysSim();
  }}

  function updateSysSim() {{
    const r = parseFloat(document.getElementById("sysGain").value);
    const tau = parseInt(document.getElementById("sysDelay").value, 10);
    document.getElementById("sysGainVal").textContent = r.toFixed(2);
    document.getElementById("sysDelayVal").textContent = tau;

    const N = 48;
    let y = new Array(N).fill(0);
    let rootDis = new Array(N).fill(0);
    if (sysMode === "scurve") {{
      y[0] = 6;
      for (let t = 1; t < N; t++) {{
        const yd = y[Math.max(0, t - 1 - tau)];
        y[t] = Math.max(0, Math.min(130, y[t - 1] + r * y[t - 1] * (1 - yd / 100)));
      }}
    }} else if (sysMode === "osc") {{
      y[0] = 35;
      for (let t = 1; t < N; t++) {{
        const yd = y[Math.max(0, t - 1 - tau)];
        y[t] = Math.max(5, Math.min(135, y[t - 1] + r * (70 - yd)));
      }}
    }} else if (sysMode === "runaway") {{
      y[0] = 6;
      for (let t = 1; t < N; t++) {{
        y[t] = Math.min(135, y[t - 1] * (1 + r * 0.32));
      }}
    }} else {{
      y[0] = 65; rootDis[0] = 18;
      for (let t = 1; t < N; t++) {{
        rootDis[t] = Math.min(135, rootDis[t - 1] * (1 + r * 0.14));
        const delayedRoot = t > tau * 3 ? rootDis[t - tau * 2] : 18;
        y[t] = Math.min(135, 22 * Math.exp(-0.25 * t) + delayedRoot * 0.88);
      }}
    }}

    const mapX = t => 54 + (t / (N - 1)) * 496;
    const mapY = v => 286 - (v / 140) * 236;
    const pathD = y.map((v, t) => `${{t === 0 ? 'M' : 'L'}} ${{mapX(t).toFixed(1)}},${{mapY(v).toFixed(1)}}`).join(" ");
    const eqY = sysMode === "osc" ? mapY(70) : mapY(100);

    let extraPath = "";
    if (sysMode === "symptom") {{
      const rdD = rootDis.map((v, t) => `${{t === 0 ? 'M' : 'L'}} ${{mapX(t).toFixed(1)}},${{mapY(v).toFixed(1)}}`).join(" ");
      extraPath = `<path d="${{rdD}}" fill="none" stroke="var(--m-trap)" stroke-width="2.2" stroke-dasharray="5 3"/>`;
    }}

    document.getElementById("sysBotSvg").innerHTML = `
      <line x1="54" y1="286" x2="554" y2="286" stroke="var(--ink-3)" stroke-width="1.6"/>
      <line x1="54" y1="36" x2="54" y2="286" stroke="var(--ink-3)" stroke-width="1.6"/>
      ${{sysMode !== 'runaway' && sysMode !== 'symptom' ? `<line x1="54" y1="${{eqY.toFixed(1)}}" x2="554" y2="${{eqY.toFixed(1)}}" stroke="var(--m-trap)" stroke-dasharray="4 4"/>` : ''}}
      ${{extraPath}}
      <path d="${{pathD}}" fill="none" stroke="var(--accent)" stroke-width="3.2"/>
      <text x="304" y="318" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink-2)">${{L("Horizontal Axis (Abscissa): Time t →", "Trục Hoành (Nằm ngang): Thời gian t →")}}</text>
      <text x="18" y="165" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink-2)" transform="rotate(-90 18 165)">${{L("System State", "Hành vi Hệ thống")}}</text>`;

    const notes = {{
      scurve: L("Reinforcing growth (R1) dominates early; Balancing limit (B1) takes over past the inflection point. Notice: cranking delay τ too high makes the S-curve overshoot and oscillate!", "Giai đoạn đầu vòng tăng cường R1 bùng nổ; sau điểm uốn vòng cân bằng B1 chiếm ưu thế. Hãy thử tăng Độ trễ τ lên cao: đường chữ S sẽ vọt lố qua ngưỡng cân bằng!"),
      osc: L("Balancing loop B tries to restore equilibrium (70), yet because of delay τ ('//'), corrective actions keep overshooting like a pendulum (p. 122). Lower τ toward 0 to stabilize!", "Vòng cân bằng B luôn kéo hệ thống về điểm cân bằng, nhưng vì có độ trễ τ ('//'), hệ thống cứ vọt quá đà như con lắc (tr. 122). Hãy kéo Độ trễ τ nhỏ lại để dập dao động!"),
      runaway: L("Unchecked Reinforcing loop R (bank-run panic or blame-driven error hiding, p. 123). Without introducing a Balancing loop early, exponential blowup is inevitable.", "Vòng phản hồi tăng cường R không có phanh hãm (như tin đồn rút tiền ngân hàng hay che giấu lỗi, tr. 123). Phải can thiệp từ sớm trước khi đường cong dựng đứng."),
      symptom: L("Senge’s Law #3 (‘Worse before better’ / Painkiller Trap, p. 118): Solid curve = visible symptom (drops briefly, then rebounds worse!); Dashed red curve = untreated root disease compounding silently.", "Bẫy chữa triệu chứng (Hình 6.7, tr. 118): Đường liền = triệu chứng giảm nhanh lúc đầu rồi bùng nặng hơn; Đường đứt nét đỏ = bệnh gốc không được điều trị âm thầm tăng vọt!")
    }};
    document.getElementById("sysExplain").innerHTML = notes[sysMode];
  }}

  /* --- LAB 4: STRATEGIC GAME THEORY ARENA --- */
  let curGame = "pd", curCell = [1, 1];
  const GAMES_DATA = {{
    pd: {{
      name: L("The Prisoner’s Dilemma (pp. 136–137)", "Thế Tiến thoái Lưỡng nan của Tù nhân (tr. 136–137)"),
      rows: [L("A: Stay Silent (Cooperate)", "A: Im lặng (Hợp tác)"), L("A: Confess (Defect)", "A: Thú tội (Phản bội)")],
      cols: [L("B: Stay Silent", "B: Im lặng"), L("B: Confess", "B: Thú tội")],
      cells: [
        [[L("2 yrs, 2 yrs", "2 năm, 2 năm"), "★ Pareto Best Joint Outcome", L("Both cooperate and serve only 2 years—requires mutual trust!", "Cả hai tin nhau cùng không nhận tội: tổng án nhẹ nhất (2 năm mỗi người).")],
         [L("5 yrs, 1 yr", "5 năm, 1 năm"), "Sucker’s Payoff for A", L("A stays loyal while B betrays A for a 1-year deal.", "A giữ im lặng bị B phản bội: A chịu 5 năm, B chỉ 1 năm.")]],
        [[L("1 yr, 5 yrs", "1 năm, 5 năm"), "Temptation for A", L("A betrays B—winning short-term at B’s expense.", "A thú tội phản bội B để hưởng án 1 năm, đẩy B vào 5 năm.")],
         [L("3 yrs, 3 yrs", "3 năm, 3 năm"), "Nash Equilibrium Trap", L("Self-protection pushes BOTH to confess—ending worse off (3y, 3y) than (2y, 2y)! Escape: binding pact + sanctioning betrayal.", "Vì nghi kỵ nhau, cả hai đều chọn thú tội và cùng chịu 3 năm tù! Giải pháp: thỏa thuận hợp tác kèm chế tài phạt kẻ phản bội.")]]
      ]
    }},
    chicken: {{
      name: L("The Chicken Game (p. 137)", "Trò chơi Gà — Đối đầu Trực diện (tr. 137)"),
      rows: [L("Driver A: Swerve (Yield)", "Lái xe A: Nhường đường"), L("Driver A: Drive Straight", "Lái xe A: Lao thẳng")],
      cols: [L("Driver B: Swerve", "B: Nhường đường"), L("Driver B: Straight", "B: Lao thẳng")],
      cells: [
        [[L("Safe, Safe", "An toàn, An toàn"), "★ Wise Mutual De-escalation", L("Both compromise proactively—nobody gets hurt and dignity stays intact.", "Hai bên chủ động thỏa hiệp: không ai bị thương, giữ được đại cục.")],
         [L("Safe (‘Chicken’), Pride Win", "Mất mặt, Thắng thế"), "Asymmetric Yield", L("A yields to save lives while B gloats.", "A nhường để tránh tai nạn nhưng bị gọi là 'gà'.")]],
        [[L("Pride Win, Safe (‘Chicken’)", "Thắng thế, Mất mặt"), "Asymmetric Yield", L("B yields while A pushes through.", "B nhường đường còn A lấn tới.")],
         [L("CRASH!, CRASH!", "TRỌNG THƯƠNG CẢ HAI!"), "Catastrophic Brinkmanship", L("Never push a rival into ‘nothing left to lose’—if pride outweighs life, both crash!", "Đừng bao giờ đẩy đàm phán vào thế không còn gì để mất—cả hai cùng lao thẳng sẽ thảm khốc!")]]
      ]
    }},
    sexes: {{
      name: L("Battle of the Sexes (p. 138)", "Cuộc chiến Giới tính — Vừa Thỏa hiệp Vừa Cạnh tranh (tr. 138)"),
      rows: [L("Wife: Music Concert", "Vợ: Đi nghe Ca nhạc"), L("Wife: Football Match", "Vợ: Đi xem Bóng đá")],
      cols: [L("Husband: Concert", "Chồng: Ca nhạc"), L("Husband: Football", "Chồng: Bóng đá")],
      cells: [
        [[L("Wife 5, Husband 3 (Sum=8)", "Vợ 5, Chồng 3 (Tổng=8)"), "★ Joint Optimum #1", L("Together at the concert! Total happiness = 8 (maximum). Take turns next weekend!", "Đi cùng nhau nghe nhạc! Tổng thỏa mãn đạt cực đại = 8. Tuần sau đổi lại đi xem bóng đá!")],
         [L("Wife 2, Husband 2 (Sum=4)", "Vợ 2, Chồng 2 (Tổng=4)"), "Worst Lonely Split", L("Each goes alone to their favorite event—losing the +3 joy of being together (Sum = 4).", "Mỗi người đi một nơi theo ý riêng—mất phần lợi lớn nhất là ở bên nhau (Tổng chỉ còn 4).")]],
        [[L("Wife 0, Husband 0", "Lệch pha (0, 0)"), "Miscoordination", L("Both sacrifice in opposite directions without talking!", "Thiếu giao tiếp dẫn tới lệch pha.")],
         [L("Wife 3, Husband 5 (Sum=8)", "Vợ 3, Chồng 5 (Tổng=8)"), "★ Joint Optimum #2", L("Together at the match! Total happiness = 8. Golden rule: reciprocal turn-taking over time.", "Cùng đi xem đá bóng! Tổng điểm vẫn đạt tối đa = 8. Chiến lược vàng: nguyên tắc có đi có lại dài hạn.")]]
      ]
    }},
    cake: {{
      name: L("Fair Cake-Cutting Protocol (p. 138)", "Trò chơi Chia Bánh Công bằng (tr. 138)"),
      rows: [L("Cutter A: Cut 50 / 50 Evenly", "Người cắt A: Chia đều 50 / 50"), L("Cutter A: Cut Unevenly 70 / 30", "Người cắt A: Cắt lệch 70 / 30")],
      cols: [L("Chooser B: Picks Larger Piece", "Người chọn B: Lấy phần lớn hơn"), L("Chooser B: Picks Polite Piece", "B: Lấy ngẫu nhiên")],
      cells: [
        [[L("A gets 50%, B gets 50%", "A nhận 50%, B nhận 50%"), "★ Self-Enforcing Fairness!", L("Because B chooses first, A’s own self-interest forces A to slice as close to 50/50 as humanly possible!", "Vì biết B được chọn trước, chính lợi ích cá nhân buộc A phải cắt chuẩn 50/50 công bằng tuyệt đối!")],
         [L("50%, 50%", "50%, 50%"), "Guaranteed Fair", L("Both slices are equal regardless.", "Hai phần bằng nhau nên chọn phần nào cũng công bằng.")]],
        [[L("A stuck with 30%, B takes 70%!", "A chỉ còn 30%, B lấy 70%!"), "Greed Backfires on Cutter", L("If A cuts a greedy giant slice, B immediately claims it—leaving A with the tiny piece!", "Nếu A tham cắt phần to phần nhỏ, B chọn ngay phần 70% khiến A tự nhận phần thiệt 30%!")],
         [L("70%, 30%", "70%, 30%"), "Unlikely", L("Rational Chooser B always picks the larger piece.", "Người có lý trí B sẽ luôn chọn phần lớn hơn.")]]
      ]
    }},
    rps: {{
      name: L("Zero-Sum Rock–Paper–Scissors (p. 139)", "Trò chơi Oẳn Tù Tỳ — Tổng Bằng Không (tr. 139)"),
      rows: [L("You: Rock / Paper / Scissors (Fixed Habit)", "Bạn: Đánh theo thói quen cố định"), L("You: Randomize 1/3 · 1/3 · 1/3", "Bạn: Ngẫu nhiên hóa 1/3 · 1/3 · 1/3")],
      cols: [L("Rival: Reads Pattern", "Đối thủ: Bắt bài quy luật"), L("Rival: Randomizes", "Đối thủ: Đánh ngẫu nhiên")],
      cells: [
        [[L("You Lose (−1, +1)", "Bạn Thua (−1, +1)"), "Exploited Predictability", L("In a zero-sum game with no dominant pure move, any habit gets decoded and beaten.", "Khi không nước đi nào mạnh tuyệt đối, mọi thói quen lặp lại đều bị đối phương bắt bài.")],
         [L("Even (0, 0)", "Hòa (0, 0)"), "Neutral", L("Unexploited only until rival notices your bias.", "Tạm cân bằng cho tới khi lộ quy luật.")]],
        [[L("Unexploitable (0, 0)", "Không thể bị bắt bài (0, 0)"), "★ Mixed-Strategy Shield!", L("Rotating Rock, Paper, Scissors unpredictably at 1/3 each makes it mathematically impossible for any rival to exploit you!", "Luân phiên 3 chiến lược hoàn toàn ngẫu nhiên không theo quy luật khiến đối phương không thể đoán trước!")],
         [L("Fair Equilibrium (0, 0)", "Cân bằng (0, 0)"), "★ Nash Mixed Equilibrium", L("Optimal play when interests are strictly zero-sum.", "Trạng thái cân bằng tối ưu của trò chơi tổng bằng không.")]]
      ]
    }}
  }};

  function selectGame(g) {{
    curGame = g; curCell = [0, 0];
    document.querySelectorAll(".gm-btn").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.gm === g)));
    renderGameLab();
  }}

  function renderGameLab() {{
    const g = GAMES_DATA[curGame];
    let tbl = `<table style="width:100%;border-collapse:collapse;background:var(--surface);border-radius:10px;overflow:hidden;border:1px solid var(--line);">
      <thead><tr><th style="padding:10px;border:1px solid var(--line);background:var(--surface-2);"></th>
      <th style="padding:10px;border:1px solid var(--line);background:var(--surface-2);">${{g.cols[0]}}</th>
      <th style="padding:10px;border:1px solid var(--line);background:var(--surface-2);">${{g.cols[1]}}</th></tr></thead><tbody>`;
    for (let r = 0; r < 2; r++) {{
      tbl += `<tr><th style="padding:12px;border:1px solid var(--line);background:var(--surface-2);text-align:start;">${{g.rows[r]}}</th>`;
      for (let c = 0; c < 2; c++) {{
        const sel = (curCell[0] === r && curCell[1] === c);
        const [pay, tag] = g.cells[r][c];
        tbl += `<td onclick="curCell=[${{r}},${{c}}];renderGameLab()" style="padding:14px;border:2px solid ${{sel ? 'var(--accent)' : 'var(--line)'}};background:${{sel ? 'color-mix(in oklab, var(--accent) 14%, var(--surface))' : 'var(--surface)'}};cursor:pointer;">
          <strong style="display:block;font-size:15px;">${{pay}}</strong>
          <span style="font-size:12.5px;color:var(--ink-2);">${{tag}}</span>
        </td>`;
      }}
      tbl += `</tr>`;
    }}
    tbl += `</tbody></table>`;
    document.getElementById("gameBoard").innerHTML = tbl;
    const [pay, tag, desc] = g.cells[curCell[0]][curCell[1]];
    document.getElementById("gameDetail").innerHTML = `
      <span class="eyebrow" style="color:var(--c-strategic);">${{g.name}}</span>
      <h4 style="font-size:19px;margin-block-end:6px;">${{pay}} · ${{tag}}</h4>
      <p style="font-size:14.5px;color:var(--ink-2);">${{desc}}</p>`;
  }}

  /* --- LAB 5: BAYESIAN 100-GRID & EXPECTED VALUE --- */
  function loadBayesPreset(p, s, fp) {{
    document.getElementById("byPrior").value = p;
    document.getElementById("bySens").value = s;
    document.getElementById("byFp").value = fp;
    updateBayes();
  }}

  function updateBayes() {{
    const priorPct = parseFloat(document.getElementById("byPrior").value);
    const sensPct = parseFloat(document.getElementById("bySens").value);
    const fpPct = parseFloat(document.getElementById("byFp").value);
    document.getElementById("byPriorVal").textContent = priorPct.toFixed(1) + "%";
    document.getElementById("bySensVal").textContent = sensPct.toFixed(0) + "%";
    document.getElementById("byFpVal").textContent = fpPct.toFixed(1) + "%";

    const pA = priorPct / 100, pBA = sensPct / 100, pBnotA = fpPct / 100;
    const tp = pA * pBA;
    const fp = (1 - pA) * pBnotA;
    const fn = pA * (1 - pBA);
    const post = (tp + fp) > 0 ? tp / (tp + fp) : 0;
    const mult = pA > 0 ? post / pA : 0;

    const nTp = Math.max(tp > 0 ? 1 : 0, Math.round(tp * 100));
    const nFp = Math.round(fp * 100);
    const nFn = Math.round(fn * 100);
    let g = "";
    for (let i = 0; i < 100; i++) {{
      const r = Math.floor(i / 10), c = i % 10;
      let fill = "var(--surface-2)", str = "var(--line-2)";
      if (i < nTp) {{ fill = "var(--m-trap)"; str = "var(--c-trap)"; }}
      else if (i < nTp + nFp) {{ fill = "var(--m-creative)"; str = "var(--c-creative)"; }}
      else if (i < nTp + nFp + nFn) {{ fill = "var(--m-prob)"; str = "var(--c-prob)"; }}
      g += `<rect x="${{24 + c * 27}}" y="${{20 + r * 27}}" width="22" height="22" rx="4" fill="${{fill}}" stroke="${{str}}"/>`;
    }}
    g += `
      <rect x="308" y="34" width="14" height="14" rx="3" fill="var(--m-trap)"/><text x="328" y="45" font-size="12" font-weight="700" fill="var(--ink)">${{L("True +", "Dương thật")}}: ${{(tp*100).toFixed(2)}}%</text>
      <rect x="308" y="64" width="14" height="14" rx="3" fill="var(--m-creative)"/><text x="328" y="75" font-size="12" font-weight="700" fill="var(--ink)">${{L("False +", "Dương giả")}}: ${{(fp*100).toFixed(2)}}%</text>
      <rect x="308" y="94" width="14" height="14" rx="3" fill="var(--m-prob)"/><text x="328" y="105" font-size="12" fill="var(--ink-2)">${{L("Missed −", "Âm giả")}}: ${{(fn*100).toFixed(2)}}%</text>
      <text x="308" y="152" font-family="var(--mono)" font-size="12" fill="var(--ink-2)">${{L("Updated Posterior:", "Xác suất Cập nhật:")}}</text>
      <text x="308" y="188" font-family="var(--display)" font-size="32" font-weight="800" fill="var(--c-prob)">${{(post*100).toFixed(1)}}%</text>
      <text x="308" y="214" font-size="12" font-weight="700" fill="var(--c-analytical)">${{mult.toFixed(1)}}× ${{L("vs. prior", "so với mức nền")}}</text>
    `;
    document.getElementById("bayesGridSvg").innerHTML = g;
    document.getElementById("bayesReadout").innerHTML = `
      <div style="font-family:var(--mono);font-size:13px;">P(A|B) = ${{(tp).toFixed(4)}} / (${{(tp).toFixed(4)}} + ${{(fp).toFixed(4)}}) = <strong>${{(post*100).toFixed(2)}}%</strong></div>`;

    const swan = document.getElementById("swanToggle").checked;
    document.getElementById("swanReadout").innerHTML = swan
      ? L("With a 1% Black Swan (−95% wipeout), mathematical EV is still +6.97%, YET 1-in-100 runs bankrupts you—proving p. 149’s warning: always pair EV with ruin protection!",
          "Dù có 1% Thiên nga đen (cháy −95% tài khoản), EV trung bình vẫn dương (+6,97%), NHƯNG 1 lần xảy ra là phá sản—chứng minh cảnh báo tr. 149: EV là cần nhưng chưa đủ trước rủi ro đuôi!")
      : L("Baseline Table 8.1 (pp. 146–147): EV = (5%×0.10) + (10%×0.15) + (15%×0.45) + (20%×0.05) − (5%×0.15) − (10%×0.10) = +8.00%.",
          "Bảng 8.1 gốc (tr. 146–147): EV = (5%×0,10) + (10%×0,15) + (15%×0,45) + (20%×0,05) − (5%×0,15) − (10%×0,10) = +8,00%.");
  }}

  /* --- LAB 6: SCIENTIFIC CONVERGENCE WHEEL --- */
  let sciStep = 3;
  const SCI_STEPS = [
    [L("1 · Active Observation", "1 · Quan sát Chủ động"), [L("Creative", "Sáng tạo")], L("Notice office fatigue every afternoon despite normal sleep and meals (p. 166).", "Nhận thấy cơ thể luôn mệt mỏi khi làm việc dù ăn ngủ hoàn toàn bình thường (tr. 166).")],
    [L("2 · Research Question", "2 · Đặt Câu hỏi Nghiên cứu"), [L("Creative", "Sáng tạo"), L("Logical", "Logic")], L("What specific mechanism causes afternoon fatigue during desk work?", "Đâu là nguyên nhân thực sự dẫn đến tình trạng mệt mỏi khi ngồi làm việc?")],
    [L("3 · Falsifiable Hypothesis", "3 · Đưa ra Giả thuyết"), [L("Creative", "Sáng tạo"), L("Logical", "Logic"), L("Critical", "Phản biện")], L("Prolonged sitting without movement causes the fatigue (testable & falsifiable—unlike ‘ghosts’!).", "Ngồi lâu thiếu vận động là nguyên nhân (có thể kiểm chứng & bác bỏ—khác hẳn giả thuyết “do ma ám”!).")],
    [L("4 · Controlled Experiment (Aim to Refute!)", "4 · Kiểm tra Giả thuyết (Cô lập Biến!)"), [L("Critical", "Phản biện"), L("Systems", "Hệ thống"), L("Strategic", "Chiến lược"), L("Logical", "Logic")], L("Every 60 mins of sitting, stand & move 5 mins for 7 days—holding coffee, sleep, and diet CONSTANT so variables don’t confound!", "Cứ ngồi 60 phút đứng lên vận động 5 phút suốt 1 tuần—GIỮ NGUYÊN lượng cà phê và ăn ngủ để không bị nhiễu biến (tr. 166–167)!")],
    [L("5 · Data Analysis", "5 · Phân tích Kết quả"), [L("Analytical", "Phân tích"), L("Probabilistic", "Xác suất"), L("Critical", "Phản biện")], L("Evaluate 7-day fatigue logs objectively against baseline.", "Phân tích nhật ký mức độ mệt mỏi 7 ngày một cách khách quan.")],
    [L("6 · Conclusion & Loop", "6 · Kết luận (Vòng lặp)"), [L("Logical", "Logic"), L("Critical", "Phản biện")], L("If fatigue persists, the hypothesis is FALSIFIED -> loop back to Step 3 for a rival hypothesis!", "Nếu hết mệt -> xác nhận giả thuyết; nếu vẫn mệt -> giả thuyết SAI, quay lại Bước 3 đặt giả thuyết khác!")],
    [L("7 · Peer Communication", "7 · Truyền thông & Phản biện Đồng đẳng"), [L("Critical", "Phản biện"), L("Systems", "Hệ thống")], L("Share protocol & results with colleagues so independent peers can replicate and critique.", "Chia sẻ quy trình và kết quả với đồng nghiệp để cộng đồng cùng kiểm chứng lại.")]
  ];

  function renderSciLab() {{
    const svg = document.getElementById("sciSvg");
    const cx = 260, cy = 195, r = 130;
    let s = `<circle cx="${{cx}}" cy="${{cy}}" r="${{r}}" fill="none" stroke="var(--line-2)" stroke-width="2" stroke-dasharray="4 4"/>
             <circle cx="${{cx}}" cy="${{cy}}" r="56" fill="var(--surface-2)" stroke="var(--c-science)" stroke-width="2"/>
             <text x="${{cx}}" y="${{cy - 4}}" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-science)">${{L("CH. 9", "CHƯƠNG 9")}}</text>
             <text x="${{cx}}" y="${{cy + 14}}" text-anchor="middle" font-size="12" fill="var(--ink-2)">${{L("8 Methods Unite", "8 Phương pháp")}}</text>`;
    SCI_STEPS.forEach(([nm], i) => {{
      const a = (-90 + (360 / 7) * i) * Math.PI / 180;
      const px = cx + r * Math.cos(a), py = cy + r * Math.sin(a);
      const sel = i === sciStep;
      const shortLbl = nm.replace(/^\\d+\\s·\\s/, "").slice(0, 18);
      s += `<g style="cursor:pointer" onclick="sciStep=${{i}};renderSciLab()">
              <circle cx="${{px.toFixed(1)}}" cy="${{py.toFixed(1)}}" r="${{sel ? 22 : 17}}" fill="${{sel ? 'var(--c-science)' : 'var(--surface)'}}" stroke="var(--c-science)" stroke-width="2.4"/>
              <text x="${{px.toFixed(1)}}" y="${{(py + 4).toFixed(1)}}" text-anchor="middle" font-family="var(--mono)" font-size="12" font-weight="800" fill="${{sel ? 'var(--accent-ink)' : 'var(--ink)'}}">${{i + 1}}</text>
              <text x="${{(cx + (r + 46) * Math.cos(a)).toFixed(1)}}" y="${{(cy + (r + 34) * Math.sin(a) + 4).toFixed(1)}}" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink)">${{shortLbl}}</text>
            </g>`;
    }});
    svg.innerHTML = s;
    const [stNm, mths, desc] = SCI_STEPS[sciStep];
    document.getElementById("sciDetail").innerHTML = `
      <span class="eyebrow" style="color:var(--c-science);">${{L("Scientific Method Stage", "Bước Phương pháp Khoa học")}} ${{sciStep + 1}} / 7</span>
      <h4 style="font-size:20px;margin-block-end:8px;">${{stNm}}</h4>
      <p style="font-size:15px;margin-block-end:14px;">${{desc}}</p>
      <div style="font-size:13px;font-weight:700;color:var(--ink-2);margin-block-end:6px;">${{L("Active Thinking Methods Recruited Here:", "Các Phương pháp Tư duy Phối hợp Ở Bước Này:")}}</div>
      <div style="display:flex;gap:6px;flex-wrap:wrap;">
        ${{mths.map(m => `<span class="pill-tag" style="margin:0;border-color:var(--c-science);color:var(--ink);">${{m}}</span>`).join("")}}
      </div>`;
  }}

  /* ========================================================================
     8. DOOR 6: CHAPTER SPEC-BOARD SWITCHER (DIRECTIONAL + LOCALSTORAGE)
     ======================================================================== */
  function selectChapter(chId, userAction = false) {{
    if (!SR.chapters[chId]) chId = "ch1";
    const oldNum = SR.chapters[currentChapter]?.num || 1;
    const newNum = SR.chapters[chId].num;
    const dir = newNum > oldNum ? "forward" : (newNum < oldNum ? "backward" : null);
    currentChapter = chId;

    const updateCh = () => {{
      document.querySelectorAll(".toc-btn").forEach(b => {{
        if (b.dataset.ch === chId) b.setAttribute("aria-current", "true");
        else b.removeAttribute("aria-current");
      }});
      document.querySelectorAll(".ch-pane").forEach(p => {{
        p.hidden = (p.id !== "pane-" + chId);
      }});
      try {{ localStorage.setItem("sr-last-ch", chId); }} catch (e) {{}}
      syncResumeButton();
    }};

    if (userAction) {{
      const h = "#reader/" + chId;
      if (location.hash !== h) {{
        suppressHashListener = true;
        history.pushState(null, "", h);
        setTimeout(() => {{ suppressHashListener = false; }}, 0);
      }}
      runDirectionalTransition(dir, () => {{
        updateCh();
        window.scrollTo({{ top: 0, behavior: "instant" }});
      }}, "heading-" + chId);
    }} else {{
      updateCh();
    }}
  }}

  function selectBookStory(idx) {{
    const st = SR.stories[idx];
    if (!st) return;
    const ch = SR.chapters[st.ch];
    document.querySelectorAll(".story-pick-btn").forEach(b => {{
      b.setAttribute("aria-pressed", String(Number(b.dataset.stidx) === idx));
    }});
    const stage = document.getElementById("storyTheaterStage");
    if (stage) {{
      stage.innerHTML = `
        <span class="eyebrow" style="color:${{ch.color}};">${{L("Chapter", "Chương")}} ${{ch.num}} · ${{ch.title}} · ${{st.pages}}</span>
        <h3 style="font-size:21px;margin-block-end:8px;">${{st.title}}</h3>
        <div class="plate-svg-wrap" style="margin-block-end:14px;">${{st.svg}}</div>
        <p style="font-size:15px;color:var(--ink);margin-block-end:10px;">${{st.hook}}</p>
        <div style="padding:12px 14px;border-radius:8px;background:var(--surface);border:1px solid var(--line);margin-block-end:12px;font-size:14.5px;">
          <strong style="color:var(--accent);">${{L("The Conscious Twist:", "Bước Ngoặt Tư Duy:")}}</strong> ${{st.twist}}
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button type="button" class="btn-primary" onclick="jumpTarget('${{st.target}}')">${{st.cta}} →</button>
          <button type="button" class="btn-ghost" onclick="switchView('plates', '${{st.plate_id}}', true)">${{L("Open Full Print Plate", "Xem Bản vẽ In ấn")}} →</button>
        </div>
      `;
    }}
  }}

  let dilemmaCursor = -1;
  function openDilemmaRoulette() {{
    if (!dilemmaDialog) return;
    dilemmaCursor = (dilemmaCursor + 1) % SR.dilemmas.length;
    renderDilemmaModal(null);
    if (!dilemmaDialog.open) dilemmaDialog.showModal();
  }}

  function renderDilemmaModal(picked) {{
    const dl = SR.dilemmas[dilemmaCursor];
    const body = document.getElementById("dilemmaDialogBody");
    if (!dl || !body) return;
    let feedbackHtml = "";
    if (picked) {{
      const ok = picked === dl.wise;
      const head = ok
        ? L("Sharp System 2 Call!", "Quyết định Hệ thống 2 Chuẩn xác!")
        : L("Caught by System 1 Impulse!", "Sập Bẫy Phản Xạ Hệ Thống 1!");
      const col = ok ? "var(--c-systems)" : "var(--c-trap)";
      feedbackHtml = `
        <div style="margin-block-start:14px;padding:14px;border-radius:10px;background:var(--surface-2);border:1px solid var(--line);">
          <strong style="display:block;color:${{col}};font-size:15.5px;margin-block-end:4px;">${{head}}</strong>
          <p style="font-size:14.5px;color:var(--ink-2);margin-block-end:12px;">${{dl.reveal}}</p>
          <button type="button" class="btn-primary" onclick="dilemmaDialog.close();jumpTarget('${{dl.target}}')">${{dl.cta}} →</button>
        </div>
      `;
    }}
    body.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-block-end:6px;">
        <span class="eyebrow" style="color:var(--c-strategic);margin:0;">${{dl.context}} (${{dilemmaCursor + 1}} / ${{SR.dilemmas.length}})</span>
        <button type="button" class="tool-pill" onclick="openDilemmaRoulette()">
          ↻ ${{L("Deal Next Scenario", "Đổi Tình huống Khác")}}
        </button>
      </div>
      <h3 id="dilemmaDialogTitle" style="font-size:20px;margin-block-end:12px;">${{dl.q}}</h3>
      <div class="quiz-choices">
        <button type="button" class="quiz-opt" data-picked="${{picked === 'a' ? (dl.wise === 'a' ? 'wise' : 'trap') : ''}}" onclick="renderDilemmaModal('a')">A · ${{dl.a}}</button>
        <button type="button" class="quiz-opt" data-picked="${{picked === 'b' ? (dl.wise === 'b' ? 'wise' : 'trap') : ''}}" onclick="renderDilemmaModal('b')">B · ${{dl.b}}</button>
      </div>
      ${{feedbackHtml}}
      <div style="margin-block-start:16px;display:flex;justify-content:flex-end;">
        <button type="button" class="btn-ghost" onclick="dilemmaDialog.close()">${{L("Close", "Đóng")}}</button>
      </div>
    `;
  }}

  /* ========================================================================
     9. SPLIT-SCREEN SCROLLYTELLING, 36-CASE VAULT & DECISION STRESS-TESTER
     ======================================================================== */
  let activeScrollyIdx = 0;

  function selectScrollyStep(idx) {{
    if (!SR.scrolly || !SR.scrolly[idx]) return;
    activeScrollyIdx = idx;
    const st = SR.scrolly[idx];
    document.querySelectorAll(".scrolly-step").forEach(el => {{
      el.classList.toggle("is-active", Number(el.dataset.scidx) === idx);
    }});
    document.querySelectorAll(".stage-beam-btn").forEach(btn => {{
      btn.setAttribute("aria-current", String(Number(btn.dataset.scbeam) === idx));
    }});
    document.querySelectorAll(".minh-stop").forEach(b => {{
      b.setAttribute("aria-pressed", String(Number(b.dataset.minh) === idx));
    }});
    const stageBox = document.getElementById("scrollyStickyStage");
    if (stageBox) stageBox.style.setProperty("--stage-col", st.color);
    const out = document.getElementById("scrollyStageContent");
    if (out) {{
      out.innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-block-end:6px;">
          <span class="eyebrow" style="color:${{st.color}};margin:0;">${{L("Active Prism Lens", "Lăng Kính Đang Chiếu")}} · Ch. ${{st.num}}: ${{st.title}}</span>
          <span class="badge-mini">${{st.metaphor}}</span>
        </div>
        <div class="plate-svg-wrap" style="margin-block-end:12px;">${{st.svg}}</div>
        <div style="padding:12px 14px;border-radius:10px;background:color-mix(in oklab, ${{st.color}} 9%, var(--surface-2));border:1px solid color-mix(in oklab, ${{st.color}} 34%, var(--line));margin-block-end:10px;">
          <div style="font-family:var(--mono);font-size:12px;font-weight:700;color:${{st.color}};margin-block-end:2px;">${{L("REAL-WORLD CASE FLASHPOINT", "HỒ SƠ THỰC CHIẾN TIÊU BIỂU")}}</div>
          <strong class="hd" style="display:block;font-size:16px;margin-block-end:4px;">${{st.case_title}}</strong>
          <p style="font-size:13.5px;color:var(--ink-2);margin-block-end:8px;">${{st.case_story}}</p>
          <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center;">
            <a class="ext-book-link" href="${{st.case_url}}" target="_blank" rel="noopener noreferrer"><span>${{st.case_src}}</span> ↗</a>
            <button type="button" class="tool-pill" onclick="jumpTarget('${{st.lab}}')">${{L("Try Matching Lab →", "Thử Mô phỏng →")}}</button>
          </div>
        </div>
        <div style="padding:10px 13px;border-radius:10px;background:var(--bg);border:1px solid var(--line);font-size:13.5px;">
          <strong style="color:var(--ink);">${{st.minh_age}} · ${{st.minh_head}}:</strong>
          <span style="color:var(--ink-2);"> ${{st.minh_story}}</span>
        </div>
      `;
    }}
  }}

  function scrollToScrollyStep(idx) {{
    selectScrollyStep(idx);
    const card = document.querySelector(`.scrolly-step[data-scidx="${{idx}}"]`);
    card?.scrollIntoView({{ behavior: "smooth", block: "center" }});
  }}

  function jumpToScrollyChapter(idx) {{
    if (currentView !== "overview") switchView("overview", null, false);
    setTimeout(() => scrollToScrollyStep(idx), 30);
  }}

  if ("IntersectionObserver" in window) {{
    const scObserver = new IntersectionObserver((entries) => {{
      let best = null;
      for (const en of entries) {{
        if (en.isIntersecting) {{
          if (!best || en.intersectionRatio > best.intersectionRatio) best = en;
        }}
      }}
      if (best) {{
        const idx = Number(best.target.dataset.scidx);
        if (!Number.isNaN(idx) && idx !== activeScrollyIdx) selectScrollyStep(idx);
      }}
    }}, {{ rootMargin: "-22% 0px -38% 0px", threshold: [0.25, 0.55, 0.8] }});
    document.querySelectorAll(".scrolly-step").forEach(el => scObserver.observe(el));
  }}

  /* --- 36 REAL-WORLD CASE STUDIES VAULT FILTER --- */
  let activeCaseCat = "all";

  function setCaseCategory(cat) {{
    activeCaseCat = cat;
    document.querySelectorAll(".case-cat-pill").forEach(b => {{
      b.setAttribute("aria-pressed", String(b.dataset.cat === cat));
    }});
    filterCasesVault(true);
  }}

  function resetCaseFilters() {{
    activeCaseCat = "all";
    document.querySelectorAll(".case-cat-pill").forEach(b => {{
      b.setAttribute("aria-pressed", String(b.dataset.cat === "all"));
    }});
    const s = document.getElementById("caseSearch");
    const c = document.getElementById("caseChFilter");
    if (s) s.value = "";
    if (c) c.value = "all";
    filterCasesVault(true);
  }}

  function filterCasesVault(syncUrl = false) {{
    const q = (document.getElementById("caseSearch")?.value || "").trim().toLowerCase();
    const chF = document.getElementById("caseChFilter")?.value || "all";
    if (syncUrl && currentView === "cases") {{
      const subPart = chF !== "all" ? "/" + chF : (activeCaseCat !== "all" ? "/" + activeCaseCat : "");
      const newHash = "#cases" + subPart;
      if (location.hash !== newHash) {{
        suppressHashListener = true;
        history.replaceState(null, "", newHash);
        setTimeout(() => {{ suppressHashListener = false; }}, 0);
      }}
      const sw = document.getElementById("langSwitchLink");
      if (sw) sw.href = "{esc_raw(meta["other_href"])}" + newHash;
    }}
    let shown = 0;
    const cards = document.querySelectorAll("#casesVaultGrid .case-card");
    cards.forEach(card => {{
      const mCat = activeCaseCat === "all" || card.dataset.cat === activeCaseCat;
      const mCh = chF === "all" || card.dataset.ch === chF;
      const mQ = !q || (card.dataset.search || "").includes(q);
      const vis = mCat && mCh && mQ;
      card.hidden = !vis;
      if (vis) shown++;
    }});
    const badge = document.getElementById("caseCountBadge");
    if (badge) {{
      badge.textContent = L(`Showing ${{shown}} / ${{cards.length}} Cases`, `Hiển thị ${{shown}} / ${{cards.length}} Hồ sơ`);
    }}
    const emptyEl = document.getElementById("caseEmptyState");
    if (emptyEl) {{
      if (shown === 0) {{
        emptyEl.hidden = false;
        emptyEl.innerHTML = `
          <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;">
            <div>
              <strong style="display:block;font-size:16px;margin-block-end:2px;">${{L("No case dossiers match that filter.", "Không tìm thấy hồ sơ khớp bộ lọc hiện tại.")}}</strong>
              <span style="font-size:14px;color:var(--ink-2);">${{L("Try searching ‘AI’, ‘Nobel’, ‘Hanoi’, ‘Boeing’, or reset filters to view all 36 cases.", "Hãy thử từ khóa như ‘AI’, ‘Nobel’, ‘Hà Nội’, ‘Boeing’ hoặc xóa bộ lọc để xem trọn bộ 36 hồ sơ.")}}</span>
            </div>
            <button type="button" class="btn-primary" onclick="resetCaseFilters()">${{L("Show All 36 Cases", "Xem Tất cả 36 Hồ sơ")}}</button>
          </div>
        `;
      }} else {{
        emptyEl.hidden = true;
      }}
    }}
  }}

  /* --- LAB 7: PERSONAL DECISION STRESS-TESTER & MEMO BUILDER --- */
  const BUILDER_PRESETS = [
    {{
      q: L("Should I leave my stable engineering role to co-found a bootstrapped AI SaaS product?",
           "Có nên nghỉ công việc kỹ sư ổn định hiện tại để cùng bạn mở startup sản phẩm AI không?"),
      scores: [6, 4, 7, 3, 5]
    }},
    {{
      q: L("Should I borrow $18,000 to enroll in a full-time Master’s degree immediately after graduation?",
           "Có nên vay 450 triệu đồng để đi học Thạc sĩ toàn thời gian ngay sau khi tốt nghiệp đại học?"),
      scores: [3, 5, 4, 4, 6]
    }},
    {{
      q: L("Should I invest 50% of my family savings to open a specialty coffee shop with a close friend?",
           "Có nên dồn 50% tiền tiết kiệm gia đình để góp vốn mở quán cà phê cùng bạn thân lúc này?"),
      scores: [4, 3, 5, 2, 4]
    }}
  ];

  const BUILDER_AXES = [
    {{ short: L("Assumptions", "Giả định"), full: L("Ch.1 Assumptions Audited", "Ch.1 Kiểm định Giả định"), lab: "labs:octagon" }},
    {{ short: L("Pre-Mortem", "Đảo ngược"), full: L("Ch.2 Pre-Mortem Inversion", "Ch.2 Đảo ngược Thất bại"), lab: "labs:wald" }},
    {{ short: L("Root Loops", "Gốc Hệ thống"), full: L("Ch.4 & 6 Root Structure", "Ch.4 & 6 Cấu trúc Hệ thống"), lab: "labs:systems" }},
    {{ short: L("Ruin Floor", "Chống Phá sản"), full: L("Ch.8 EV + Ruin Protection", "Ch.8 EV + Chốt chặn Đuôi"), lab: "labs:bayes" }},
    {{ short: L("7-Day Pilot", "Thử 7 Ngày"), full: L("Ch.9 Falsifiable Pilot", "Ch.9 Thí nghiệm Bác bỏ"), lab: "labs:science" }},
  ];

  function loadBuilderPreset(idx) {{
    const p = BUILDER_PRESETS[idx];
    if (!p) return;
    const qIn = document.getElementById("bldQuestion");
    if (qIn) qIn.value = p.q;
    p.scores.forEach((v, i) => {{
      const sl = document.getElementById("bldS" + i);
      if (sl) sl.value = v;
    }});
    updateDecisionBuilder();
  }}

  function updateDecisionBuilder() {{
    const svg = document.getElementById("builderRadarSvg");
    if (!svg) return;
    const vals = [0, 1, 2, 3, 4].map(i => {{
      const v = Number(document.getElementById("bldS" + i)?.value || 5);
      const lbl = document.getElementById("bldV" + i);
      if (lbl) lbl.textContent = v + "/10";
      return v;
    }});
    const total = vals.reduce((a, b) => a + b, 0);
    let minIdx = 0;
    vals.forEach((v, i) => {{ if (v < vals[minIdx]) minIdx = i; }});

    const cx = 210, cy = 156, maxR = 96;
    const rings = [0.25, 0.5, 0.75, 1.0].map(f => {{
      const pts = [0, 1, 2, 3, 4].map(i => {{
        const a = (-90 + 72 * i) * Math.PI / 180;
        return `${{(cx + maxR * f * Math.cos(a)).toFixed(1)}},${{(cy + maxR * f * Math.sin(a)).toFixed(1)}}`;
      }}).join(" ");
      return `<polygon points="${{pts}}" fill="none" stroke="var(--line-2)" stroke-width="1" opacity="0.55"/>`;
    }}).join("");

    const spokes = [0, 1, 2, 3, 4].map(i => {{
      const a = (-90 + 72 * i) * Math.PI / 180;
      const x2 = cx + maxR * Math.cos(a), y2 = cy + maxR * Math.sin(a);
      const lx = cx + (maxR + 34) * Math.cos(a), ly = cy + (maxR + 22) * Math.sin(a);
      return `<line x1="${{cx}}" y1="${{cy}}" x2="${{x2.toFixed(1)}}" y2="${{y2.toFixed(1)}}" stroke="var(--line-2)" stroke-width="1"/>
              <text x="${{lx.toFixed(1)}}" y="${{(ly + 4).toFixed(1)}}" text-anchor="middle" font-size="12" font-weight="700" fill="${{i === minIdx ? 'var(--c-trap)' : 'var(--ink)'}}">${{BUILDER_AXES[i].short}} (${{vals[i]}})</text>`;
    }}).join("");

    const dataPts = vals.map((v, i) => {{
      const a = (-90 + 72 * i) * Math.PI / 180;
      const r = maxR * Math.max(0.08, v / 10);
      return [cx + r * Math.cos(a), cy + r * Math.sin(a)];
    }});
    const polyStr = dataPts.map(([x, y]) => `${{x.toFixed(1)}},${{y.toFixed(1)}}`).join(" ");
    const dotsStr = dataPts.map(([x, y], i) =>
      `<circle cx="${{x.toFixed(1)}}" cy="${{y.toFixed(1)}}" r="${{i === minIdx ? 6 : 4.5}}" fill="${{i === minIdx ? 'var(--c-trap)' : 'var(--accent)'}}" stroke="var(--surface)" stroke-width="1.8"/>`
    ).join("");

    svg.innerHTML = `
      ${{rings}}
      ${{spokes}}
      <polygon points="${{polyStr}}" fill="color-mix(in oklab, var(--accent) 24%, transparent)" stroke="var(--accent)" stroke-width="2.6"/>
      ${{dotsStr}}
      <text x="16" y="24" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--ink-2)">${{L("READINESS SCORE:", "ĐIỂM KIỂM ĐỊNH:")}} ${{total}} / 50</text>
    `;

    let statusHead, statusCol, statusBody;
    if (total >= 38 && vals[minIdx] >= 6) {{
      statusHead = L("Ready for Controlled Execution", "Đủ Chín Muồi Để Triển Khai Có Kiểm Soát");
      statusCol = "var(--c-systems)";
      statusBody = L("All five conscious gates are solid. Lock in your pre-committed exit rules and run your pilot.",
                     "Cả 5 chốt chặn phương pháp đều vững vàng. Hãy chốt trước ngưỡng dừng lỗ và bắt đầu thí nghiệm thực tế.");
    }} else if (total >= 25) {{
      statusHead = L("Promising, Yet Vulnerable to a Blind Spot", "Có Triển Vọng Nhưng Còn Điểm Mù Nguy Hiểm");
      statusCol = "var(--c-creative)";
      statusBody = L("System 1 enthusiasm is ahead of your weakest safeguard. Strengthen the red axis before committing capital.",
                     "Sự hưng phấn đang đi trước khâu phòng vệ yếu nhất (màu đỏ). Hãy gia cố trục yếu nhất trước khi xuống tiền.");
    }} else {{
      statusHead = L("High System 1 Impulse Hazard: Pause & Pilot First!", "Báo Động Cảm Tính Hệ Thống 1: Khoan Tất Tay!");
      statusCol = "var(--c-trap)";
      statusBody = L("Do not make an irreversible bet yet. Convert this big leap into a cheap 7-day falsifiable experiment.",
                     "Chưa nên đặt cược một chiều lúc này! Hãy chuyển quyết định lớn thành một phép thử nhỏ 7 ngày chi phí thấp.");
    }}

    const weak = BUILDER_AXES[minIdx];
    const verdictEl = document.getElementById("builderVerdict");
    if (verdictEl) {{
      verdictEl.innerHTML = `
        <strong class="hd" style="display:block;font-size:18px;color:${{statusCol}};margin-block-end:4px;">${{total}}/50 · ${{statusHead}}</strong>
        <p style="font-size:14px;color:var(--ink-2);margin-block-end:10px;">${{statusBody}}</p>
        <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;padding:9px 12px;border-radius:8px;background:var(--surface-2);border:1px solid var(--line);font-size:13px;">
          <span><strong style="color:var(--c-trap);">${{L("Weakest Gate:", "Mắt xích yếu nhất:")}}</strong> ${{weak.full}} (${{vals[minIdx]}}/10)</span>
          <button type="button" class="tool-pill" onclick="jumpTarget('${{weak.lab}}')">${{L("Fix in Lab →", "Mở Lab Rèn luyện →")}}</button>
        </div>
      `;
    }}

    const q = document.getElementById("bldQuestion")?.value || "";
    const memoLines = [
      L("# SYSTEMA RATIO · CONSCIOUS DECISION MEMO", "# SYSTEMA RATIO · BẢN GHI NHỚ KIỂM ĐỊNH QUYẾT ĐỊNH"),
      L("Decision: ", "Câu hỏi quyết định: ") + q,
      L("Readiness Score: ", "Tổng điểm kiểm định: ") + total + "/50 (" + statusHead + ")",
      "────────────────────────────────────────",
      ...BUILDER_AXES.map((ax, i) => `• ${{ax.full}}: ${{vals[i]}}/10`),
      "────────────────────────────────────────",
      L("Priority Blind Spot: ", "Điểm mù ưu tiên xử lý: ") + weak.full + ` (${{vals[minIdx]}}/10)`
    ];
    const memoBox = document.getElementById("memoPreviewBox");
    if (memoBox) memoBox.textContent = memoLines.join("\\n");

    const socraticProbes = [
      L("1. Which hidden assumption am I treating as a guaranteed fact without primary evidence (Paul–Elder Vertex #4)?",
        "1. Giả định ngầm nào tôi đang mặc định là sự thật hiển nhiên mà chưa hề có bằng chứng gốc (Đỉnh #4 Paul–Elder)?"),
      L("2. Imagine it is 12 months from now and this decision failed catastrophically: what silent graveyard (Abraham Wald) did I ignore?",
        "2. Giả sử 12 tháng nữa quyết định này thất bại thảm hại: phần dữ liệu tử vong câm lặng nào (Abraham Wald) tôi đã bỏ sót?"),
      L("3. Am I solving the structural root cause (5-Whys) or applying a short-term symptom patch that triggers a delayed backlash loop (Senge)?",
        "3. Tôi đang giải quyết nguyên nhân gốc rễ hay chỉ vá triệu chứng ngắn hạn để rồi hứng chịu vòng phản hồi trễ (Định luật Senge)?"),
      L("4. Even if average Expected Value looks positive, what 1% Black Swan tail event could cause irreversible ruin—and what is my hard floor?",
        "4. Dù kỳ vọng trung bình có vẻ tốt, biến cố Thiên nga đen 1% nào có thể xóa sạch cuộc chơi—và đâu là ngưỡng dừng lỗ cứng của tôi?"),
      L("5. What 7-day, low-cost falsifiable experiment (Popper) could prove my favorite hypothesis WRONG before I commit all-in?",
        "5. Thí nghiệm nhỏ 7 ngày chi phí thấp nào (Karl Popper) có thể chứng minh giả thuyết tâm đắc của tôi là SAI trước khi tôi tất tay?")
    ];
    const socraticLines = [
      L("Act as my Socratic System-2 sparring partner (Đào Minh Châu, Học Tư Duy). DO NOT decide for me or give generic advice.",
        "Hãy đóng vai đối tác phản biện Socratic Hệ thống 2 (theo tinh thần sách Học Tư Duy của Đào Minh Châu). TUYỆT ĐỐI KHÔNG quyết định hộ hay khuyên chung chung."),
      L("My dilemma: “", "Câu hỏi quyết định của tôi: “") + q + "”",
      L("My weakest safeguard right now: ", "Khâu kiểm định yếu nhất của tôi hiện tại: ") + weak.full + ` (${{vals[minIdx]}}/10).`,
      "",
      L("Challenge me one question at a time, starting with:", "Hãy chất vấn tôi từng câu một để tôi tự suy nghĩ, bắt đầu từ:"),
      socraticProbes[minIdx],
      L("Wait for my answer, expose any Question Substitution or Confirmation Bias in my reasoning, and help me design a falsifiable next step.",
        "Hãy chờ tôi trả lời, chỉ ra nếu tôi mắc lỗi Thay thế câu hỏi hoặc Thiên kiến xác nhận, rồi cùng tôi thiết kế bước kiểm chứng thực tế.")
    ];
    const socBox = document.getElementById("socraticPromptBox");
    if (socBox) socBox.textContent = socraticLines.join("\\n");
  }}

  /* --- INVOKER-COMMAND COPY BUTTONS + ACCESSIBLE LIVE TIP (mwg `copy-button`) --- */
  const copyTimers = new WeakMap();
  let lastCopyAnnouncement = "";

  function legacyCopyText(text) {{
    const prevFocus = document.activeElement;
    const field = Object.assign(document.createElement("textarea"), {{ value: text }});
    field.setAttribute("readonly", "");
    field.style.cssText = "position:fixed;inset-block-start:0;opacity:0";
    document.body.append(field);
    field.select();
    try {{
      return document.execCommand("copy");
    }} finally {{
      field.remove();
      prevFocus?.focus({{ preventScroll: true }});
    }}
  }}

  function reportCopyStatus(button, ok) {{
    const tip = button.nextElementSibling;
    clearTimeout(copyTimers.get(button));
    button.removeAttribute("data-copied");
    button.removeAttribute("data-failed");
    let message = ok ? L("Copied!", "Đã chép!") : L("Copy failed", "Lỗi sao chép");
    if (message === lastCopyAnnouncement) message += "\\u00A0";
    lastCopyAnnouncement = message;
    if (tip) tip.textContent = "";
    void button.offsetWidth;
    button.setAttribute(ok ? "data-copied" : "data-failed", "");
    if (tip) requestAnimationFrame(() => {{ tip.textContent = message; }});
    copyTimers.set(button, setTimeout(() => {{
      button.removeAttribute("data-copied");
      button.removeAttribute("data-failed");
      if (tip) tip.textContent = "";
    }}, 2200));
  }}

  async function runCopyTarget(button, target) {{
    const text = target.matches("input, textarea") ? target.value : target.innerText.trim();
    if (!text) return;
    try {{
      await navigator.clipboard.writeText(text);
      reportCopyStatus(button, true);
    }} catch (err) {{
      if (legacyCopyText(text)) reportCopyStatus(button, true);
      else reportCopyStatus(button, false);
    }}
  }}

  if ("CommandEvent" in window) {{
    document.addEventListener("command", (event) => {{
      if (event.command && event.command.startsWith("--copy") && event.target) {{
        runCopyTarget(event.source, event.target);
      }}
    }}, true);
  }} else {{
    document.addEventListener("click", (event) => {{
      if (event.defaultPrevented) return;
      const button = event.target.closest('button[command^="--copy"]');
      if (!button) return;
      const target = document.getElementById(button.getAttribute("commandfor"));
      if (target) runCopyTarget(button, target);
    }});
  }}

  /* Boot everything cleanly */
  syncThemeButton();
  selectScrollyStep(0);
  selectFloor(3);
  selectMinhBeat(0);
  selectBookStory(0);
  selectThread(0);
  renderOctagonLab();
  renderWaldLab();
  updateSysSim();
  renderGameLab();
  updateBayes();
  renderSciLab();
  updateDecisionBuilder();
  filterCasesVault();
  renderAtlasGraph();
  syncResumeButton();

  const initHash = location.hash.replace(/^#/, "");
  if (initHash) {{
    const [hv, hsub] = initHash.split("/");
    if (VIEWS.includes(hv)) switchView(hv, hsub, false);
  }}

  window.addEventListener("keydown", (e) => {{
    if (e.key === "/" && !["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement?.tagName)) {{
      if (currentView === "atlas") {{
        e.preventDefault();
        document.getElementById("atlasSearch")?.focus();
      }} else if (currentView === "cases") {{
        e.preventDefault();
        document.getElementById("caseSearch")?.focus();
      }}
    }}
  }});
  </script>
</body>
</html>"""
