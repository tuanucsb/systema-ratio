# -*- coding: utf-8 -*-
"""Generates 18 publication-grade bilingual vector SVG Book Plates for Systema Ratio."""
import html
import math


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


STANDALONE_STYLE = """<style>
  svg { font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f5f6fb; color: #15172e; }
  .hd { font-family: 'Fraunces', Georgia, serif; font-weight: 800; }
  .mn { font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; }
</style>"""


def wrap_svg(vb_w: int, vb_h: int, title: str, body: str, standalone: bool = False) -> str:
    st = STANDALONE_STYLE if standalone else ""
    bg_rect = (
        f'<rect x="0" y="0" width="{vb_w}" height="{vb_h}" rx="12" fill="var(--bg, #f5f6fb)"/>'
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} {vb_h}" role="img" aria-label="{esc(title)}">'
        f"<title>{esc(title)}</title>{st}{bg_rect}{body}</svg>"
    )


def defs_arrows() -> str:
    return """<defs>
      <marker id="arInk" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M0,1 L9,5 L0,9 z" fill="var(--ink-2, #4a4f6a)"/>
      </marker>
      <marker id="arTeal" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M0,1 L9,5 L0,9 z" fill="#0d9488"/>
      </marker>
      <marker id="arRed" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M0,1 L9,5 L0,9 z" fill="#b81f2e"/>
      </marker>
      <marker id="arGreen" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M0,1 L9,5 L0,9 z" fill="#0b7547"/>
      </marker>
      <marker id="arBlue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M0,1 L9,5 L0,9 z" fill="#2458d3"/>
      </marker>
    </defs>"""


def build_plates(lang: str = "en", standalone: bool = False) -> list:
    en = lang == "en"
    T = lambda e, v: e if en else v
    plates = []

    # =========================================================================
    # PLATE 01: REDESIGNED BOOK COVER (SYSTEMA RATIO)
    # =========================================================================
    cov_title = T("LEARNING HOW TO THINK", "HỌC TƯ DUY")
    cov_sub = T("SYSTEMA RATIO · THE ARCHITECTURE OF CONSCIOUS REASON", "SYSTEMA RATIO · KIẾN TRÚC TƯ DUY CÓ Ý THỨC")
    cov_foot = T("3 Parts · 9 Methods · 29 Tools · Illustrated Edition", "3 Phần · 9 Phương pháp · 29 Công cụ · Ấn bản Minh họa")
    rays = [
        ("#ffd23f", T("2 · Creative", "2 · Sáng tạo"), 205),
        ("#5b8cff", T("3 · Critical", "3 · Phản biện"), 238),
        ("#38e0cf", T("4 · Analytical", "4 · Phân tích"), 271),
        ("#93a0ff", T("5 · Logical", "5 · Logic"), 304),
        ("#2dd490", T("6 · Systems", "6 · Hệ thống"), 337),
        ("#ff9a3d", T("7 · Strategic", "7 · Chiến lược"), 370),
        ("#a07fff", T("8 · Probabilistic", "8 · Xác suất"), 403),
        ("#ff5fa2", T("9 · Scientific", "9 · Khoa học"), 436),
    ]
    ray_svg = ""
    for col, lbl, yy in rays:
        ray_svg += f'<path d="M 332,320 C 390,320 420,{yy} 505,{yy}" fill="none" stroke="{col}" stroke-width="3.2"/>'
        ray_svg += f'<circle cx="508" cy="{yy}" r="4.5" fill="{col}"/>'
        ray_svg += f'<text x="520" y="{yy + 4}" font-size="12" font-weight="700" fill="{col}">{esc(lbl)}</text>'

    # Octagon prism center (275, 320), r=58
    oct_pts = " ".join(
        f"{275 + 58 * math.cos(math.radians(22.5 + 45 * k)):.1f},{320 + 58 * math.sin(math.radians(22.5 + 45 * k)):.1f}"
        for k in range(8)
    )
    oct_in = " ".join(
        f"{275 + 36 * math.cos(math.radians(22.5 + 45 * k)):.1f},{320 + 36 * math.sin(math.radians(22.5 + 45 * k)):.1f}"
        for k in range(8)
    )
    p01_body = f"""
    <rect x="20" y="16" width="600" height="588" rx="14" fill="#0e1022" stroke="#2a2f52" stroke-width="2"/>
    <rect x="34" y="30" width="572" height="560" rx="10" fill="none" stroke="#1f2342" stroke-width="1.2"/>
    <text x="320" y="72" text-anchor="middle" font-size="13" font-weight="700" letter-spacing="3" fill="#8d93b3">ĐÀO MINH CHÂU</text>
    <text x="320" y="118" text-anchor="middle" class="hd" font-size="34" font-weight="800" fill="#f3f4fb">{esc(cov_title)}</text>
    <text x="320" y="146" text-anchor="middle" class="mn" font-size="12" letter-spacing="0.8" fill="#2fc7e6">{esc(cov_sub)}</text>
    <line x1="120" y1="166" x2="520" y2="166" stroke="#2a2f52" stroke-width="1"/>

    <!-- Tangled System 1 input trajectories (left) -->
    <path d="M 62,255 C 115,215 135,375 217,315" fill="none" stroke="#ff5c6a" stroke-width="2.2" stroke-dasharray="4 3" opacity="0.85"/>
    <path d="M 62,320 C 125,365 150,260 217,320" fill="none" stroke="#ff5c6a" stroke-width="2.5" opacity="0.9"/>
    <path d="M 62,388 C 120,420 155,295 217,326" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3 3" opacity="0.8"/>
    <text x="64" y="230" font-size="12" font-weight="700" fill="#ff7a86">{esc(T("System 1 Noise", "Nhiễu Hệ thống 1"))}</text>
    <text x="64" y="248" font-size="12" fill="#b3b8d3">{esc(T("Biases & Impulse", "Bản năng & Thiên kiến"))}</text>

    <!-- 8-Sided Conscious Prism -->
    <polygon points="{oct_pts}" fill="#1f2342" stroke="#2fc7e6" stroke-width="2.6"/>
    <polygon points="{oct_in}" fill="none" stroke="#5b8cff" stroke-width="1.2" opacity="0.65"/>
    <text x="275" y="315" text-anchor="middle" font-size="12" font-weight="800" fill="#f3f4fb">{esc(T("CH. 1", "CHƯƠNG 1"))}</text>
    <text x="275" y="333" text-anchor="middle" font-size="12" fill="#2fc7e6">{esc(T("8 Elements", "8 Thành tố"))}</text>

    <!-- Refracted 8 Ordered Method Beams -->
    {ray_svg}

    <!-- Open Hand & Ascending Origami Bird (Epilogue emblem) -->
    <g transform="translate(275, 505)">
      <path d="M -56,22 Q -20,38 28,24 Q 52,16 66,4" fill="none" stroke="#b3b8d3" stroke-width="2.4" stroke-linecap="round"/>
      <path d="M -38,27 Q 0,42 46,24" fill="none" stroke="#656b87" stroke-width="1.6" stroke-linecap="round"/>
      <polygon points="-18,-6 8,-26 2,-2" fill="#2fc7e6"/>
      <polygon points="2,-2 8,-26 30,-14" fill="#5b8cff"/>
      <polygon points="-18,-6 2,-2 -8,10" fill="#ffd23f"/>
      <text x="45" y="-2" font-size="12" font-style="italic" fill="#d6daf0">{esc(T("“It lies in your hands.”", "“Nó nằm trong tay bạn.”"))}</text>
    </g>

    <text x="320" y="572" text-anchor="middle" class="mn" font-size="12" fill="#8d93b3">{esc(cov_foot)}</text>
    """
    plates.append({
        "id": "p01",
        "slug": "01-cover-systema-ratio",
        "ch": "Cover",
        "manuscript_ref": T("Replaces Cover (p. 1)", "Thay thế Bìa sách (tr. 1)"),
        "title": T("Plate 01 · Systema Ratio Cover Concept: The Prism & The Bird", "Bản vẽ 01 · Thiết kế Bìa mới: Lăng kính Lý trí & Cánh chim Tự chủ"),
        "say": T(
            "Conscious method (the 8-sided prism) refracts tangled System 1 impulse into eight disciplined beams of reason—placing agency back in the reader’s open hand.",
            "Tư duy có ý thức (lăng kính bát giác Chương 1) khúc xạ đám rối bản năng Hệ thống 1 thành 8 tia phương pháp kỷ luật—đặt sự tự chủ vào chính bàn tay người đọc."
        ),
        "rationale": T(
            "Replaces the draft’s neon-magenta outlined text over Picasso’s 1901 café portrait with an iconic architectural emblem uniting Chapter 1’s octagon, the 8 methods, and the Epilogue’s bird parable.",
            "Thay thế chữ viền tím hồng trên bức tranh quán rượu của Picasso bằng biểu tượng kiến trúc kết nối Bát giác Chương 1, 8 phương pháp Phần II–III và ẩn dụ Con chim ở Lời kết."
        ),
        "svg": wrap_svg(640, 620, cov_title, p01_body, standalone),
    })

    # =========================================================================
    # PLATE 02: DUAL-SYSTEM ARCHITECTURE & SIMON CONSOLIDATION LOOP (CH. 1)
    # =========================================================================
    p02_body = f"""{defs_arrows()}
    <rect x="24" y="22" width="852" height="396" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="46" y="54" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Two Systems of Thought & Herbert Simon’s Intuition Loop", "Hai Hệ thống Tư duy & Vòng Nâng cấp Trực giác của Herbert Simon"))}</text>
    <text x="46" y="75" font-size="13" fill="var(--ink-2, #4a4f6a)">{esc(T("System 1 proposes continuously; lazy System 2 rubber-stamps—unless awakened by conscious method.", "Hệ thống 1 liên tục gợi ý; Hệ thống 2 lười biếng dễ gật đầu—trừ khi được đánh thức bằng phương pháp có ý thức."))}</text>

    <!-- World Stimulus -->
    <rect x="46" y="138" width="136" height="118" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line-2, #cbd1e1)" stroke-width="1.5"/>
    <text x="114" y="175" text-anchor="middle" font-weight="700" font-size="13.5" fill="var(--ink, #15172e)">{esc(T("Complex Problem", "Vấn đề Thực tế"))}</text>
    <text x="114" y="196" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Signals & Context", "Tín hiệu & Hoàn cảnh"))}</text>
    <text x="114" y="222" text-anchor="middle" class="mn" font-size="10.5" fill="var(--ink-3, #656b87)">{esc(T("Snake? · 1234×17?", "Vật đen? · 1234×17?"))}</text>

    <!-- System 1 Box -->
    <rect x="226" y="102" width="256" height="142" rx="10" fill="rgba(229,51,63,0.08)" stroke="#b81f2e" stroke-width="2"/>
    <text x="244" y="129" font-weight="800" font-size="14.5" fill="var(--c-trap, #b81f2e)">{esc(T("SYSTEM 1 · Fast & Instinctive", "HỆ THỐNG 1 · Nhanh & Bản năng"))}</text>
    <text x="244" y="150" font-size="12" fill="var(--ink, #15172e)">{esc(T("• Automatic, effortless, never sleeps", "• Tự động, tức thì, hoạt động liên tục"))}</text>
    <text x="244" y="170" font-size="12" fill="var(--ink, #15172e)">{esc(T("• Driven by Memory + 3 Heuristics:", "• Dựa vào Trí nhớ + 3 mẹo Heuristic:"))}</text>
    <text x="256" y="190" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("1. Swap hard question for easy one", "1. Thay câu hỏi khó bằng câu hỏi dễ"))}</text>
    <text x="256" y="208" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("2. Fixed norms  ·  3. WYSIATI", "2. Chuẩn mực vội  ·  3. Thấy gì tin nấy"))}</text>
    <text x="244" y="230" font-size="11" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("⚠ Spawns 10 Systematic Biases", "⚠ Sinh ra 10 Thiên kiến mặc định"))}</text>

    <!-- System 2 Box -->
    <rect x="546" y="102" width="302" height="142" rx="10" fill="rgba(13,148,136,0.09)" stroke="#0d9488" stroke-width="2"/>
    <text x="564" y="129" font-weight="800" font-size="14.5" fill="var(--c-analytical, #0b7268)">{esc(T("SYSTEM 2 · Slow & Methodical", "HỆ THỐNG 2 · Chậm & Có ý thức"))}</text>
    <text x="564" y="150" font-size="12" fill="var(--ink, #15172e)">{esc(T("• Deliberate attention, agency & rules", "• Đòi hỏi nỗ lực chú ý, tập trung & quy tắc"))}</text>
    <text x="564" y="170" font-size="12" fill="var(--ink, #15172e)">{esc(T("• Chronic weakness: LAZY & easily tired", "• Điểm yếu chí mạng: LƯỜI BIẾNG, dễ thỏa hiệp"))}</text>
    <text x="564" y="193" font-size="11.5" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("Trap A: Rubber-stamps System 1", "Lỗi 1: Phó mặc hoàn toàn cho Hệ thống 1"))}</text>
    <text x="564" y="211" font-size="11.5" font-weight="700" fill="var(--c-creative, #946200)">{esc(T("Trap B: Wakes up, uses WRONG method", "Lỗi 2: Có can thiệp nhưng SAI phương pháp"))}</text>
    <text x="564" y="231" font-size="11.5" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("✓ Solution: 8 Elements + 8 Methods", "✓ Giải pháp: 8 Thành tố + 8 Phương pháp"))}</text>

    <!-- Connecting Arrows -->
    <line x1="182" y1="180" x2="220" y2="165" stroke="var(--ink-2, #4a4f6a)" stroke-width="2" marker-end="url(#arInk)"/>
    <line x1="482" y1="152" x2="540" y2="152" stroke="#b81f2e" stroke-width="2.2" marker-end="url(#arRed)"/>
    <text x="511" y="143" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("Hunches", "Gợi ý"))}</text>
    <line x1="546" y1="196" x2="488" y2="196" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arTeal)"/>
    <text x="514" y="214" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("Override", "Kiểm soát"))}</text>

    <!-- Herbert Simon Memory Consolidation Return Bar -->
    <rect x="226" y="286" width="622" height="96" rx="10" fill="rgba(37,99,235,0.08)" stroke="#2458d3" stroke-width="1.8" stroke-dasharray="6 4"/>
    <path d="M 700,244 L 700,286" fill="none" stroke="#2458d3" stroke-width="2.2" marker-end="url(#arBlue)"/>
    <path d="M 350,286 L 350,250" fill="none" stroke="#2458d3" stroke-width="2.2" marker-end="url(#arBlue)"/>
    <text x="537" y="316" text-anchor="middle" font-weight="800" font-size="13.5" fill="var(--c-critical, #2458d3)">{esc(T("HERBERT SIMON’S MEMORY CONSOLIDATION LOOP (p. 22)", "CHU TRÌNH CỦNG CỐ TRÍ NHỚ CỦA HERBERT SIMON (tr. 22)"))}</text>
    <text x="537" y="339" text-anchor="middle" font-size="12" fill="var(--ink, #15172e)">{esc(T("“Intuition is nothing more and nothing less than recognition from memory.”", "“Trực giác không gì khác hơn là sự nhận biết từ thông tin lưu trữ trong bộ nhớ.”"))}</text>
    <text x="537" y="361" text-anchor="middle" font-size="12" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("Disciplined System 2 practice today → Stored in Long-Term Memory → Smarter System 1 intuition tomorrow!", "Hệ thống 2 rèn đúng phương pháp hôm nay → Ghi vào Trí nhớ dài hạn → Nâng cấp trực giác Hệ thống 1 ngày mai!"))}</text>
    """
    plates.append({
        "id": "p02",
        "slug": "02-dual-system-simon-loop",
        "ch": "Ch. 1",
        "manuscript_ref": T("New figure for Ch. 1 (pp. 12–15, 22)", "Hình mới cho Chương 1 (tr. 12–15, 22)"),
        "title": T("Plate 02 · Kahneman’s Dual Systems & Simon’s Consolidation Loop", "Bản vẽ 02 · Hai Hệ thống Tư duy & Vòng Nâng cấp Trực giác"),
        "say": T(
            "System 2 not only catches System 1’s errors in the moment—its repeated methodical practice rewires long-term memory so intuition itself grows sharper.",
            "Hệ thống 2 không chỉ kiểm soát sai lầm tức thời của Hệ thống 1—khi thực hành đúng phương pháp đủ lâu, nó ghi vào trí nhớ để nâng cấp chính trực giác."
        ),
        "rationale": T(
            "Visualizes the core cognitive engine of Chapter 1 (currently 10 pages of pure text) and links p. 12’s dual-system conflict to p. 22’s closing insight.",
            "Trực quan hóa toàn bộ phần cốt lõi Chương 1 (hiện đang thuần chữ suốt 10 trang) và nối kết cơ chế Kahneman (tr. 12) với kết luận sâu sắc của Herbert Simon (tr. 22)."
        ),
        "svg": wrap_svg(900, 440, "Dual Systems & Simon Loop", p02_body, standalone),
    })

    # =========================================================================
    # PLATE 03: PAUL-ELDER 8 ELEMENTS OF CONSCIOUS THINKING (REDESIGN FIG 1.1)
    # =========================================================================
    el_labels = [
        T("1 · Purpose", "1 · Mục đích"),
        T("2 · Key Question", "2 · Câu hỏi chính"),
        T("3 · Point of View", "3 · Quan điểm"),
        T("4 · Assumptions", "4 · Giả định"),
        T("5 · Information", "5 · Thông tin"),
        T("6 · Inference / Method", "6 · Suy luận"),
        T("7 · Conclusions", "7 · Kết luận"),
        T("8 · Implications", "8 · Hệ quả"),
    ]
    cx, cy, r = 310, 254, 122
    pts = [
        (cx + r * math.cos(math.radians(-112.5 + 45 * i)), cy + r * math.sin(math.radians(-112.5 + 45 * i)))
        for i in range(8)
    ]
    k8_lines = ""
    for i in range(8):
        for j in range(i + 1, 8):
            is_edge = (j - i == 1) or (i == 0 and j == 7)
            sw = "2.4" if is_edge else "1.0"
            col = "#087087" if is_edge else "#8d93b3"
            op = "0.9" if is_edge else "0.35"
            k8_lines += f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>'

    node_svg = ""
    for i, (px, py) in enumerate(pts):
        ox = cx + (r + 44) * math.cos(math.radians(-112.5 + 45 * i))
        oy = cy + (r + 28) * math.sin(math.radians(-112.5 + 45 * i))
        node_svg += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="16" fill="#087087" stroke="#ffffff" stroke-width="2"/>'
        node_svg += f'<text x="{px:.1f}" y="{py + 4:.1f}" text-anchor="middle" class="mn" font-size="12" font-weight="700" fill="#ffffff">{i+1}</text>'
        node_svg += f'<text x="{ox:.1f}" y="{oy + 4:.1f}" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink, #15172e)">{esc(el_labels[i])}</text>'

    p03_body = f"""
    <rect x="24" y="20" width="852" height="420" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <!-- Context Frame -->
    <rect x="44" y="36" width="532" height="388" rx="14" fill="rgba(29,78,95,0.07)" stroke="#087087" stroke-width="2"/>
    <text x="64" y="62" font-weight="800" font-size="12" letter-spacing="0.6" fill="var(--c-meta, #087087)">{esc(T("CONTEXT (ECONOMIC · SOCIAL · HISTORICAL · PERSONAL)", "HOÀN CẢNH CỤ THỂ (KINH TẾ · XÃ HỘI · LỊCH SỬ · CÁ NHÂN)"))}</text>
    {k8_lines}
    {node_svg}
    <!-- Case Study Callout (Right) -->
    <rect x="596" y="42" width="260" height="376" rx="12" fill="var(--surface-2, #eef1f8)" stroke="var(--line-2, #cbd1e1)"/>
    <text x="614" y="72" class="hd" font-size="15.5" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Walkthrough (pp. 21–22)", "Ví dụ Thực hành (tr. 21–22)"))}</text>
    <text x="614" y="94" font-size="12" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("Grad School Now vs. Work First?", "Học Thạc sĩ ngay hay Đi làm trước?"))}</text>
    <text x="614" y="122" font-size="12" fill="var(--ink, #15172e)">{esc(T("1. Fit personal goals & finances", "1. Quyết định hợp hoàn cảnh cá nhân"))}</text>
    <text x="614" y="146" font-size="12" fill="var(--ink, #15172e)">{esc(T("2. Master’s right after B.A.?", "2. Học cao học ngay sau tốt nghiệp?"))}</text>
    <text x="614" y="170" font-size="12" fill="var(--ink, #15172e)">{esc(T("3. Long-term career trajectory", "3. Phát triển nghề nghiệp dài hạn"))}</text>
    <text x="614" y="194" font-size="12" fill="var(--c-trap, #b81f2e)">{esc(T("4. Assumption: M.A. = better jobs?", "4. Giả định: Có bằng cao học ắt tốt hơn?"))}</text>
    <text x="614" y="218" font-size="12" fill="var(--ink, #15172e)">{esc(T("5. Industry demand, savings, alumni", "5. Yêu cầu ngành, tài chính, người đi trước"))}</text>
    <text x="614" y="242" font-size="12" fill="var(--ink, #15172e)">{esc(T("6. Opportunity cost & cost–benefit", "6. Chi phí cơ hội & phân tích lợi ích"))}</text>
    <text x="614" y="266" font-size="12" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("7. Work 2–3 yrs before Master’s", "7. Đi làm vài năm trước khi học tiếp"))}</text>
    <text x="614" y="290" font-size="12" fill="var(--ink, #15172e)">{esc(T("8. Earn & learn (+ delay risk)", "8. Tích lũy thực tế (+ ngại học lại)"))}</text>
    <line x1="614" y1="316" x2="838" y2="316" stroke="var(--line-2, #cbd1e1)"/>
    <text x="614" y="340" font-size="12" font-style="italic" fill="var(--ink-2, #4a4f6a)">{esc(T("Non-linear: all 28 chords stay active", "Phi tuyến: cả 28 đường nối đều tương tác"))}</text>
    <text x="614" y="359" font-size="12" font-style="italic" fill="var(--ink-2, #4a4f6a)">{esc(T("as new facts reshape assumptions.", "động khi thông tin mới đổi giả định."))}</text>
    """
    plates.append({
        "id": "p03",
        "slug": "03-paul-elder-octagon",
        "ch": "Ch. 1",
        "manuscript_ref": T("Redesigned Fig. 1.1 (p. 20)", "Vẽ lại Hình 1.1 (tr. 20)"),
        "title": T("Plate 03 · The 8 Dynamic Elements of Conscious Thought in Context", "Bản vẽ 03 · Bát giác Động 8 Thành tố Tư duy trên Nền Hoàn cảnh"),
        "say": T(
            "Conscious thinking is neither linear nor isolated: every element cross-checks the other seven inside a concrete real-world context.",
            "Tư duy có ý thức không tuyến tính và không tách rời thực tại: cả 8 thành tố liên tục tương tác qua lại trên nền hoàn cảnh cụ thể."
        ),
        "rationale": T(
            "Upgrades Fig. 1.1’s bare numbered octagon (`1..8` on solid cyan) by naming all 8 vertices directly and pairing them side-by-side with p. 21’s graduate-school walkthrough.",
            "Nâng cấp Hình 1.1 (hiện chỉ có số 1..8 trên nền xanh đơn điệu) bằng nhãn trực tiếp tại 8 đỉnh kèm hộp đối chiếu ví dụ thực tế sinh viên năm cuối (tr. 21)."
        ),
        "svg": wrap_svg(900, 460, "Paul-Elder 8 Elements Octagon", p03_body, standalone),
    })

    # =========================================================================
    # PLATE 04: 10 COGNITIVE BIASES & VIETNAMESE PROVERBS (CH. 1)
    # =========================================================================
    b_rows = [
        ("1", T("Confirmation Bias", "Thiên kiến xác nhận"), "“Yêu nên tốt, ghét nên xấu”", T("Cherry-picking agreeable proof", "Chỉ gom bằng chứng hợp ý mình")),
        ("2", T("Anchoring Bias", "Hiệu ứng neo"), T("1M → 900k → 800k shirt", "Áo 1 triệu → 900k → 800k"), T("Trapped by the first number", "Bị con số đầu tiên neo nhận thức")),
        ("3", T("Availability Bias", "Thông tin sẵn có"), T("Plane crash headlines", "Tin tai nạn máy bay"), T("Vivid news ≠ high probability", "Thấy đưa tin nhiều tưởng nguy hiểm hơn")),
        ("4", T("Framing Effect", "Hiệu ứng đóng khung"), T("90% live vs. 10% die", "90% sống vs. 10% thất bại"), T("Swayed by packaging, not math", "Bị dẫn dắt bởi vỏ ngôn từ trình bày")),
        ("5", T("Sunk Cost Fallacy", "Lỗi chi phí chìm"), "“Đâm lao thì phải theo lao”", T("Throwing good time after bad", "Tiếc vé ngồi xem hết phim dở")),
        ("6", T("Loss Aversion", "Ám ảnh thua thiệt"), "“Con cá trượt là con cá to”", T("Loss hurts 1.5×–2.5× more", "Nỗi đau mất lớn gấp 1,5–2,5 lần niềm vui")),
        ("7", T("Bandwagon Effect", "Hiệu ứng đám đông"), "“A dua a tòng”", T("Outsourcing mind to the herd", "Tin và làm theo áp lực số đông")),
        ("8", T("Overconfidence", "Thiên kiến quá tự tin"), T("80% 'above-avg' riders", "80% tự nhận lái xe giỏi"), T("Inflated self-assessment", "Đánh giá năng lực vượt xa thực tế")),
        ("9", T("Affect Heuristic", "Quyết định cảm xúc"), "“Giận mất khôn”", T("Quitting job in a burst of anger", "Cảm xúc nhất thời đè bẹp lý trí")),
        ("10", T("Dunning–Kruger", "Hiệu ứng Dunning–Kruger"), "“Thùng rỗng kêu to”", T("Low skill → highest certainty", "Biết ít tự phụ, biết sâu khiêm nhường")),
    ]
    cards_svg = ""
    for idx, (num, nm, prov, sub) in enumerate(b_rows):
        col_i = idx % 2
        row_i = idx // 2
        bx = 42 + col_i * 416
        by = 92 + row_i * 70
        cards_svg += f'<rect x="{bx}" y="{by}" width="400" height="58" rx="8" fill="var(--surface-2, #eef1f8)" stroke="var(--line, #e1e5f0)"/>'
        cards_svg += f'<rect x="{bx}" y="{by}" width="34" height="58" rx="8" fill="#b81f2e"/>'
        cards_svg += f'<text x="{bx + 17}" y="{by + 34}" text-anchor="middle" class="mn" font-size="12" font-weight="800" fill="#ffffff">{num}</text>'
        cards_svg += f'<text x="{bx + 46}" y="{by + 23}" font-size="13" font-weight="700" fill="var(--ink, #15172e)">{esc(nm)}</text>'
        cards_svg += f'<text x="{bx + 390}" y="{by + 23}" text-anchor="end" font-size="11.5" font-style="italic" font-weight="700" fill="var(--c-strategic, #b34a00)">{esc(prov)}</text>'
        cards_svg += f'<text x="{bx + 46}" y="{by + 44}" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(sub)}</text>'

    p04_body = f"""
    <rect x="24" y="20" width="852" height="440" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="42" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("10 Instinctive Cognitive Biases Paired with Folk Proverbs (pp. 15–18)", "10 Thiên kiến Bản năng Phổ biến & Tục ngữ Dân gian Việt Nam (tr. 15–18)"))}</text>
    <text x="42" y="74" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("“Error in spontaneous thinking is not the exception—it is our default state.”", "“Sai lầm trong tư duy tự phát không phải là ngoại lệ, mà là trạng thái mặc định.”"))}</text>
    {cards_svg}
    """
    plates.append({
        "id": "p04",
        "slug": "04-ten-biases-folk-wisdom",
        "ch": "Ch. 1",
        "manuscript_ref": T("New figure for Ch. 1 (pp. 15–18)", "Hình mới cho Chương 1 (tr. 15–18)"),
        "title": T("Plate 04 · Atlas of the 10 Default Biases & Vietnamese Folk Proverbs", "Bản vẽ 04 · Bản đồ 10 Thiên kiến Mặc định & Ca dao Tục ngữ Việt"),
        "say": T(
            "Centuries before modern cognitive psychology, Vietnamese folk proverbs captured the exact instinctive traps of System 1.",
            "Hàng thế kỷ trước tâm lý học nhận thức hiện đại, tục ngữ dân gian Việt Nam đã đúc kết sắc sảo những cái bẫy bản năng của Hệ thống 1."
        ),
        "rationale": T(
            "Turns 4 pages of numbered text into a memorable cultural-scientific reference plate bridging APA definitions with Vietnamese folk wisdom.",
            "Chuyển hóa 4 trang liệt kê chữ thành bảng đối chiếu trực quan độc đáo giữa tâm lý học quốc tế và kho tàng tục ngữ Việt Nam."
        ),
        "svg": wrap_svg(900, 480, "10 Cognitive Biases and Proverbs", p04_body, standalone),
    })

    # =========================================================================
    # PLATE 05: CREATIVE DOUBLE DIAMOND & PROBLEM REDEFINITION (CH. 2)
    # =========================================================================
    p05_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="390" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Creative Thinking: Redefine First, Diverge Wide, Converge Deep", "Tư duy Sáng tạo: Định nghĩa lại Vấn đề · Phân kỳ Rộng · Hội tụ Sâu"))}</text>

    <!-- Diamond 1: Problem Space -->
    <polygon points="70,220 230,115 390,220 230,325" fill="rgba(217,119,6,0.10)" stroke="#946200" stroke-width="2.2"/>
    <line x1="230" y1="115" x2="230" y2="325" stroke="#946200" stroke-dasharray="4 4"/>
    <text x="230" y="102" text-anchor="middle" font-weight="800" font-size="12.5" fill="var(--c-creative, #946200)">{esc(T("1 · REDEFINE PROBLEM SPACE", "1 · TÁI ĐỊNH NGHĨA VẤN ĐỀ"))}</text>
    <text x="160" y="205" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("Narrow Trap:", "Đặt hẹp:"))}</text>
    <text x="160" y="222" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("“Zero-G ink pen?”", "“Bút mực không trọng lực?”"))}</text>
    <text x="302" y="205" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-systems, #0b7547)">{esc(T("Open Frame:", "Đặt mở:"))}</text>
    <text x="302" y="222" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("“Write in zero-G?” → Pencil!", "“Viết không trọng lực?” → Bút chì!"))}</text>
    <text x="230" y="352" text-anchor="middle" font-size="11" fill="var(--ink-3, #656b87)">{esc(T("Archimedes: Sphere = rotating 2D circle · Kapitsa: Stillness = motion at v=0", "Archimedes: Mặt cầu = hình tròn quay · Kapitsa: Đứng yên = chuyển động v=0"))}</text>

    <!-- Diamond 2: Solution Space (Diverge -> Converge) -->
    <polygon points="430,220 620,105 810,220 620,335" fill="rgba(13,148,136,0.10)" stroke="#0d9488" stroke-width="2.2"/>
    <line x1="620" y1="105" x2="620" y2="335" stroke="#0d9488" stroke-dasharray="4 4"/>
    <text x="535" y="96" text-anchor="middle" font-weight="800" font-size="12.5" fill="var(--c-creative, #946200)">{esc(T("2 · DIVERGE (Think Wide)", "2 · PHÂN KỲ (Nghĩ rộng)"))}</text>
    <text x="715" y="96" text-anchor="middle" font-weight="800" font-size="12.5" fill="var(--c-analytical, #0b7268)">{esc(T("3 · CONVERGE (Think Deep)", "3 · HỘI TỤ (Nghĩ sâu)"))}</text>
    <text x="530" y="206" text-anchor="middle" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("Defer ALL judgment", "Trì hoãn mọi phán xét"))}</text>
    <text x="530" y="225" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Brainstorm · Mind Map", "Động não · Sơ đồ tư duy"))}</text>
    <text x="530" y="242" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("SCAMPER · What-If?", "SCAMPER · Sẽ ra sao nếu?"))}</text>
    <text x="710" y="206" text-anchor="middle" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("Evaluate & Rank", "Phân tích & Chọn lọc"))}</text>
    <text x="710" y="225" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Novelty × Appropriateness", "Tính Mới lạ × Tính Phù hợp"))}</text>
    <text x="710" y="242" text-anchor="middle" font-size="11" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("→ Actionable Breakthrough", "→ Giải pháp Đột phá Khả thi"))}</text>

    <circle cx="390" cy="220" r="6" fill="#946200"/>
    <line x1="396" y1="220" x2="424" y2="220" stroke="var(--ink-2, #4a4f6a)" stroke-width="2" marker-end="url(#arInk)"/>
    <circle cx="810" cy="220" r="7" fill="#0d9488"/>
    """
    plates.append({
        "id": "p05",
        "slug": "05-creative-double-diamond",
        "ch": "Ch. 2",
        "manuscript_ref": T("New figure for Ch. 2 (pp. 25–29)", "Hình mới cho Chương 2 (tr. 25–29)"),
        "title": T("Plate 05 · Problem Redefinition & The Diverge–Converge Double Diamond", "Bản vẽ 05 · Tái định nghĩa Vấn đề & Mô hình Kim cương Kép Phân kỳ – Hội tụ"),
        "say": T(
            "Creativity stalls whenever we lock onto an old problem definition or mix premature critique into divergent ideation.",
            "Sáng tạo bị bóp nghẹt khi ta đóng khung vấn đề theo giải pháp cũ hoặc trộn lẫn phê phán quá sớm vào giai đoạn phân kỳ."
        ),
        "rationale": T(
            "Gives visual form to Chapter 2’s core principle ('Diverge then Converge', p. 26) and its famous Space Pen vs. Soviet Pencil & Archimedes stories.",
            "Hình tượng hóa nguyên lý cốt lõi “Phân kỳ rồi Hội tụ” (tr. 26) cùng giai thoại bút không gian, mặt cầu Archimedes và bài toán Kapitsa."
        ),
        "svg": wrap_svg(900, 430, "Creative Double Diamond", p05_body, standalone),
    })

    # =========================================================================
    # PLATE 06: ABRAHAM WALD WWII BOMBER SURVIVORSHIP BIAS (REDESIGN FIG 2.1)
    # =========================================================================
    dots = [
        (170, 196), (186, 204), (205, 195), (222, 208), (242, 198), (195, 214),
        (415, 196), (432, 206), (452, 197), (468, 209), (440, 216), (398, 208),
        (310, 232), (324, 245), (302, 258), (318, 272), (308, 288),
        (278, 342), (296, 348), (332, 344), (350, 350), (314, 152), (322, 162),
    ]
    dots_svg = "".join(f'<circle cx="{dx}" cy="{dy}" r="4.5" fill="#b81f2e"/>' for dx, dy in dots)
    p06_body = f"""
    <rect x="24" y="20" width="852" height="390" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Inversion Thinking: Abraham Wald’s Bomber Survivorship Map (p. 31)", "Tư duy Đảo ngược: Phân tích Vết đạn Máy bay của Abraham Wald (tr. 31)"))}</text>

    <!-- Twin-engine Bomber Silhouette -->
    <g>
      <!-- Fuselage & Wings -->
      <path d="M 314,88 C 326,88 332,115 332,165 L 495,192 L 495,218 L 330,226 L 326,332 L 372,344 L 372,360 L 322,356 L 314,372 L 306,356 L 256,360 L 256,344 L 302,332 L 298,226 L 133,218 L 133,192 L 296,165 C 296,115 302,88 314,88 Z"
            fill="var(--surface-2, #eef1f8)" stroke="var(--ink, #15172e)" stroke-width="2.2"/>
      <!-- Engines (UNSCATHED -> ARMOR HERE!) -->
      <rect x="242" y="156" width="28" height="54" rx="6" fill="rgba(13,148,136,0.22)" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="4 2"/>
      <rect x="358" y="156" width="28" height="54" rx="6" fill="rgba(13,148,136,0.22)" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="4 2"/>
      <!-- Cockpit (UNSCATHED -> ARMOR HERE!) -->
      <ellipse cx="314" cy="124" rx="13" ry="20" fill="rgba(13,148,136,0.22)" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="4 2"/>
      <!-- Center Rear Fuel/Tail Control -->
      <rect x="303" y="298" width="22" height="30" rx="5" fill="rgba(13,148,136,0.22)" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="4 2"/>
      {dots_svg}
    </g>

    <!-- Comparison Annotations (Right) -->
    <rect x="536" y="88" width="316" height="126" rx="10" fill="rgba(229,51,63,0.08)" stroke="#b81f2e" stroke-width="1.8"/>
    <text x="554" y="116" font-weight="800" font-size="13.5" fill="var(--c-trap, #b81f2e)">{esc(T("✗ Naive Engineer View (System 1)", "✗ Lập luận Xuôi Dễ Mắc Bẫy (Hệ thống 1)"))}</text>
    <text x="554" y="140" font-size="12" fill="var(--ink, #15172e)">{esc(T("Red dots = bullet holes on planes that RETURNED.", "Chấm đỏ = vết đạn trên máy bay ĐÃ TRỞ VỀ."))}</text>
    <text x="554" y="162" font-size="12" fill="var(--ink-2, #4a4f6a)">{esc(T("Proposal: “Armor the wings where the red dots", "Đề xuất sai: “Gia cố phần cánh/thân bị dính"))}</text>
    <text x="554" y="180" font-size="12" fill="var(--ink-2, #4a4f6a)">{esc(T("cluster!” (Victim of WYSIATI survivorship bias)", "nhiều đạn nhất!” (Mắc bẫy thiên kiến sống sót)"))}</text>

    <rect x="536" y="232" width="316" height="148" rx="10" fill="rgba(13,148,136,0.10)" stroke="#0d9488" stroke-width="2"/>
    <text x="554" y="260" font-weight="800" font-size="13.5" fill="var(--c-analytical, #0b7268)">{esc(T("✓ Abraham Wald’s Inversion (System 2)", "✓ Tư duy Đảo ngược của Wald (Hệ thống 2)"))}</text>
    <text x="554" y="284" font-size="12" fill="var(--ink, #15172e)">{esc(T("Planes hit in red zones SURVIVED the flight.", "Dính đạn ở vùng chấm đỏ mà máy bay VẪN VỀ ĐƯỢC."))}</text>
    <text x="554" y="306" font-size="12" fill="var(--ink, #15172e)">{esc(T("Fatal hits are on planes at the bottom of the sea!", "Vết đạn chí mạng nằm trên những chiếc ĐÃ RƠI!"))}</text>
    <text x="554" y="332" font-size="12" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("→ Armor the GREEN bullet-free zones: cockpit", "→ Phải gia cố vùng XANH KHÔNG CÓ VẾT ĐẠN:"))}</text>
    <text x="554" y="350" font-size="12" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("   & engines!", "   buồng lái và hai động cơ!"))}</text>
    """
    plates.append({
        "id": "p06",
        "slug": "06-abraham-wald-bomber",
        "ch": "Ch. 2",
        "manuscript_ref": T("Redesigned Fig. 2.1 (p. 31)", "Vẽ lại Hình 2.1 (tr. 31)"),
        "title": T("Plate 06 · Abraham Wald’s WWII Survivorship Inversion", "Bản vẽ 06 · Tư duy Đảo ngược & Thiên kiến Sống sót của Abraham Wald"),
        "say": T(
            "What is missing from your data is often deadlier than what is visible: armor where returning survivors were never hit.",
            "Phần khuyết thiếu không nhìn thấy thường chí mạng hơn phần hiện hữu: phải bọc thép những vùng máy bay sống sót không hề dính đạn."
        ),
        "rationale": T(
            "Enhances Fig. 2.1 by explicitly highlighting the unscathed green armor zones (cockpit & engines) alongside the System 1 vs. Wald comparison.",
            "Nâng cấp Hình 2.1 bằng cách khoanh rõ vùng xanh cần gia cố (buồng lái, động cơ) và đặt bảng đối chiếu trực tiếp Tư duy xuôi vs. Đảo ngược."
        ),
        "svg": wrap_svg(900, 430, "Abraham Wald Bomber Inversion", p06_body, standalone),
    })

    # =========================================================================
    # PLATE 07: SCAMPER (GIO VS RUOC) & SIX THINKING HATS (CH. 2)
    # =========================================================================
    hats = [
        ("#f3f4fb", "#2a2f52", T("White · Data", "Trắng · Sự thật"), T("What facts do we know?", "Dữ liệu khách quan là gì?")),
        ("#ef4444", "#ffffff", T("Red · Emotion", "Đỏ · Cảm xúc"), T("What does gut instinct say?", "Trực giác, cảm xúc ra sao?")),
        ("#1f2342", "#ffffff", T("Black · Risk", "Đen · Rủi ro"), T("What hazards loom?", "Rủi ro, hạn chế nào cần lưu ý?")),
        ("#facc15", "#1f2342", T("Yellow · Value", "Vàng · Lạc quan"), T("Where is the upside?", "Lợi ích & giá trị tích cực?")),
        ("#0b7547", "#ffffff", T("Green · Create", "Xanh lá · Sáng tạo"), T("What new options exist?", "Ý tưởng đột phá mới là gì?")),
        ("#2458d3", "#ffffff", T("Blue · Process", "Xanh dương · Điều phối"), T("How do we orchestrate?", "Quản lý quy trình tư duy")),
    ]
    hats_svg = ""
    for i, (bgc, fgc, hnm, hq) in enumerate(hats):
        hx = 480 + (i % 2) * 195
        hy = 104 + (i // 2) * 92
        hats_svg += f'<rect x="{hx}" y="{hy}" width="182" height="76" rx="9" fill="var(--surface-2, #eef1f8)" stroke="var(--line, #e1e5f0)"/>'
        hats_svg += f'<rect x="{hx + 10}" y="{hy + 10}" width="162" height="24" rx="5" fill="{bgc}" stroke="#656b87" stroke-width="0.8"/>'
        hats_svg += f'<text x="{hx + 91}" y="{hy + 26}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{fgc}">{esc(hnm)}</text>'
        hats_svg += f'<text x="{hx + 91}" y="{hy + 55}" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(hq)}</text>'

    p07_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="400" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Structured Creativity: SCAMPER Operators & Six Parallel Thinking Hats", "Công cụ Sáng tạo Có Cấu trúc: SCAMPER & Sáu Chiếc Mũ Tư duy Song song"))}</text>

    <!-- Left: SCAMPER + Gio vs Ruoc -->
    <rect x="44" y="80" width="412" height="316" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line-2, #cbd1e1)"/>
    <text x="62" y="108" font-weight="800" font-size="14" fill="var(--c-creative, #946200)">{esc(T("SCAMPER · 7 Transformation Prompts (pp. 39–41)", "SCAMPER · 7 Phép Biến đổi Sáng tạo (tr. 39–41)"))}</text>
    <text x="62" y="132" class="mn" font-size="11.5" fill="var(--ink, #15172e)">S · Substitute ({esc(T("Petrol → EV motor", "Động cơ xăng → điện"))})</text>
    <text x="62" y="152" class="mn" font-size="11.5" fill="var(--ink, #15172e)">C · Combine ({esc(T("Driver + Tour guide", "Lái xe + Hướng dẫn viên"))})</text>
    <text x="62" y="172" class="mn" font-size="11.5" fill="var(--ink, #15172e)">A · Adapt  |  M · Modify  |  P · Put to other use</text>
    <text x="62" y="192" class="mn" font-size="11.5" fill="var(--ink, #15172e)">E · Eliminate ({esc(T("Drop tire inner tube", "Bỏ ruột xe → lốp không săm"))})</text>
    <text x="62" y="212" class="mn" font-size="11.5" font-weight="700" fill="var(--c-strategic, #b34a00)">R · Rearrange / Reverse ({esc(T("Swap step order!", "Đảo ngược thứ tự bước!"))})</text>

    <rect x="62" y="228" width="376" height="150" rx="8" fill="var(--surface, #ffffff)" stroke="#946200" stroke-width="1.5"/>
    <text x="250" y="251" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-creative, #946200)">{esc(T("Vietnamese Culinary Proof of 'R' (Reverse Order, p. 41)", " Minh họa Kinh điển Chữ 'R' — Giò lụa & Ruốc (tr. 41)"))}</text>
    <text x="78" y="284" font-size="12" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Pork → [1. Pound raw] → [2. Boil]  =  GIÒ LỤA (Silky sausage)", "Thịt sống → [1. Giã nhuyễn] → [2. Luộc]  =  GIÒ LỤA"))}</text>
    <text x="78" y="320" font-size="12" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("Pork → [1. Boil first] → [2. Pound]  =  RUỐC (Fluffy floss)", "Thịt sống → [1. Luộc chín] → [2. Giã tơi]  =  RUỐC (Chà bông)"))}</text>
    <text x="250" y="356" text-anchor="middle" font-size="11" font-style="italic" fill="var(--ink-2, #4a4f6a)">{esc(T("Identical ingredients & operations—reversing order creates a new product!", "Cùng nguyên liệu và hai thao tác—chỉ đảo thứ tự đã tạo ra sản phẩm mới!"))}</text>

    <!-- Right: 6 Hats -->
    <text x="480" y="92" font-weight="800" font-size="14" fill="var(--c-critical, #2458d3)">{esc(T("Six Hats · Everyone Wears the SAME Hat Together", "Sáu Chiếc Mũ · Tất cả Đội CÙNG MỘT MŨ Cùng Lúc"))}</text>
    {hats_svg}
    <text x="666" y="392" text-anchor="middle" font-size="11" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("Rule: Parallel thinking—never assign 1 hat per person!", "Quy tắc cốt lõi: Tư duy song song—không chia vai mỗi người một mũ!"))}</text>
    """
    plates.append({
        "id": "p07",
        "slug": "07-scamper-six-hats",
        "ch": "Ch. 2",
        "manuscript_ref": T("New figure for Ch. 2 (pp. 39–44)", "Hình mới cho Chương 2 (tr. 39–44)"),
        "title": T("Plate 07 · SCAMPER Sequence Reversal (Giò vs. Ruốc) & Six Thinking Hats", "Bản vẽ 07 · SCAMPER (Ví dụ Giò & Ruốc) và Sáu Chiếc Mũ Tư duy"),
        "say": T(
            "Creativity thrives on structured operators: reversing two identical steps turns pork sausage into pork floss, while wearing six hats in parallel ends ego-driven argument.",
            "Sáng tạo bứt phá nhờ cấu trúc: chỉ đảo thứ tự giã – luộc đã biến giò thành ruốc, còn đội chung 6 chiếc mũ giúp xóa bỏ tranh cãi bản ngã."
        ),
        "rationale": T(
            "Illustrates Đào Minh Châu’s charming Vietnamese *giò vs. ruốc* SCAMPER insight (p. 41) alongside de Bono’s parallel-thinking rule (pp. 43–44).",
            "Minh họa ví dụ thuần Việt cực kỳ đắt giá về Giò và Ruốc của tác giả (tr. 41) cùng nguyên tắc “tư duy song song” của Sáu chiếc mũ (tr. 43–44)."
        ),
        "svg": wrap_svg(900, 440, "SCAMPER and Six Thinking Hats", p07_body, standalone),
    })

    # =========================================================================
    # PLATE 08: BROWNE-KEELEY 10-QUESTION CRITICAL FUNNEL (CH. 3)
    # =========================================================================
    bk_steps = [
        ("1–2", T("Issue, Conclusion & Reasons", "Vấn đề, Kết luận & Lý do"), "#2458d3", 740),
        ("3–4", T("Ambiguous Words & Hidden Assumptions (Value / Descriptive)", "Từ ngữ mơ hồ & Giả định ngầm (Giá trị / Mô tả)"), "#2458d3", 660),
        ("5", T("Logical Fallacies (Red herring, Equivocation, Circularity)", "Ngụy biện (Đánh lạc hướng, Đánh tráo khái niệm, Vòng vo)"), "#b81f2e", 580),
        ("6–7", T("Evidence Quality & Rival Causes (Correlation ≠ Causation)", "Độ tin cậy Bằng chứng & Quan hệ Nhân – Quả"), "#0d9488", 500),
        ("8–9", T("Deceptive Statistics & Omitted Counter-Information", "Số liệu Thống kê Lừa dối & Thông tin Quan trọng Bị Bỏ qua"), "#946200", 420),
        ("10", T("Nuanced Conditional Conclusions (“If…, then…”)", "Các Kết luận Hợp lý Có Điều kiện (“Nếu…, thì…”)"), "#0b7547", 340),
    ]
    bk_svg = ""
    for i, (num, txt, col, wd) in enumerate(bk_steps):
        fx = 450 - wd // 2
        fy = 88 + i * 54
        bk_svg += f'<rect x="{fx}" y="{fy}" width="{wd}" height="44" rx="8" fill="var(--surface-2, #eef1f8)" stroke="{col}" stroke-width="2"/>'
        bk_svg += f'<rect x="{fx}" y="{fy}" width="54" height="44" rx="8" fill="{col}"/>'
        bk_svg += f'<text x="{fx + 27}" y="{fy + 27}" text-anchor="middle" class="mn" font-size="12" font-weight="800" fill="#ffffff">Q{num}</text>'
        bk_svg += f'<text x="{fx + 68}" y="{fy + 27}" font-size="12.5" font-weight="700" fill="var(--ink, #15172e)">{esc(txt)}</text>'

    p08_body = f"""
    <rect x="24" y="20" width="852" height="420" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Critical Thinking Tier 1: Browne–Keeley 10-Question Sieve (pp. 52–60)", "Phản biện Tầng 1: Phễu Lọc 10 Câu hỏi Browne–Keeley (tr. 52–60)"))}</text>
    <text x="44" y="73" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("The mind’s immune system against manipulation, fake news, deceptive stats, and unverified AI claims.", "“Hệ thống miễn dịch” của trí óc trước tin giả, ngụy biện, thống kê thao túng và ảo giác AI."))}</text>
    {bk_svg}
    """
    plates.append({
        "id": "p08",
        "slug": "08-browne-keeley-funnel",
        "ch": "Ch. 3",
        "manuscript_ref": T("New figure for Ch. 3 (pp. 52–60)", "Hình mới cho Chương 3 (tr. 52–60)"),
        "title": T("Plate 08 · The Browne–Keeley 10-Question Argument Filter", "Bản vẽ 08 · Phễu Thẩm định Lập luận 10 Câu hỏi Browne–Keeley"),
        "say": T(
            "Raw claims enter wide at the top; only conditional, evidence-backed conclusions survive all ten diagnostic sieves.",
            "Mọi tuyên bố đi qua 10 tầng sàng lọc từ giả định, ngụy biện, thống kê đến thông tin bị giấu trước khi trở thành kết luận đáng tin."
        ),
        "rationale": T(
            "Chapter 3 currently has zero diagrams across 18 pages; this sieve gives readers a single visual map of all 10 Browne–Keeley questions.",
            "Chương 3 hiện chưa có bất kỳ hình vẽ nào suốt 18 trang; phễu lọc này giúp bạn đọc nắm trọn 10 bước phản biện lập luận chỉ trong một ánh nhìn."
        ),
        "svg": wrap_svg(900, 460, "Browne-Keeley 10 Questions Funnel", p08_body, standalone),
    })

    # =========================================================================
    # PLATE 09: PAUL-ELDER TIER-2 METACOGNITIVE ARCHITECTURE (CH. 3)
    # =========================================================================
    cols3 = [
        (
            "#087087",
            T("STEP 1 · ANALYZE", "BƯỚC 1 · PHÂN TÍCH"),
            T("8 Elements of Thought", "8 Thành tố Tư duy"),
            [
                T("1. Purpose", "1. Mục đích"),
                T("2. Key Question", "2. Câu hỏi chính"),
                T("3. Point of View", "3. Quan điểm"),
                T("4. Assumptions", "4. Giả định"),
                T("5. Information", "5. Thông tin"),
                T("6. Concepts & Inference", "6. Suy luận"),
                T("7. Conclusions", "7. Kết luận"),
                T("8. Implications", "8. Hệ quả"),
            ],
        ),
        (
            "#2458d3",
            T("STEP 2 · EVALUATE", "BƯỚC 2 · ĐÁNH GIÁ"),
            T("8 Universal Standards", "8 Tiêu chuẩn Trí tuệ"),
            [
                T("• Accuracy (True?)", "• Tính chính xác"),
                T("• Consistency / Precision", "• Tính nhất quán / cụ thể"),
                T("• Relevance", "• Tính thích đáng"),
                T("• Depth (Complexities)", "• Độ sâu"),
                T("• Breadth (Rival views)", "• Độ rộng"),
                T("• Logic (Coherence)", "• Tính logic"),
                T("• Significance", "• Tầm quan trọng"),
                T("• Fairness", "• Tính công bằng"),
            ],
        ),
        (
            "#0d9488",
            T("STEP 3 · IMPROVE", "BƯỚC 3 · CẢI THIỆN"),
            T("8 Intellectual Virtues", "8 Phẩm chất Trí tuệ"),
            [
                T("★ Intellectual Humility", "★ Khiêm tốn trí tuệ"),
                T("★ Intellectual Courage", "★ Dũng cảm trí tuệ"),
                T("★ Intellectual Empathy", "★ Đồng cảm trí tuệ"),
                T("★ Intellectual Autonomy", "★ Tự chủ trí tuệ"),
                T("★ Intellectual Integrity", "★ Chính trực trí tuệ"),
                T("★ Perseverance", "★ Kiên trì trí tuệ"),
                T("★ Confidence in Reason", "★ Niềm tin vào Lý trí"),
                T("★ Fairmindedness", "★ Công bằng"),
            ],
        ),
    ]
    pe_svg = ""
    for idx, (col, stp, sub, items) in enumerate(cols3):
        cx0 = 46 + idx * 280
        pe_svg += f'<rect x="{cx0}" y="96" width="248" height="296" rx="10" fill="var(--surface-2, #eef1f8)" stroke="{col}" stroke-width="2"/>'
        pe_svg += f'<rect x="{cx0}" y="96" width="248" height="52" rx="10" fill="{col}"/>'
        pe_svg += f'<text x="{cx0 + 124}" y="118" text-anchor="middle" class="mn" font-size="11" font-weight="800" fill="#ffffff">{esc(stp)}</text>'
        pe_svg += f'<text x="{cx0 + 124}" y="138" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">{esc(sub)}</text>'
        for k, it in enumerate(items):
            pe_svg += f'<text x="{cx0 + 18}" y="{174 + k * 26}" font-size="12" font-weight="600" fill="var(--ink, #15172e)">{esc(it)}</text>'
        if idx < 2:
            pe_svg += f'<line x1="{cx0 + 252}" y1="244" x2="{cx0 + 274}" y2="244" stroke="var(--ink-2, #4a4f6a)" stroke-width="2.4" marker-end="url(#arInk)"/>'

    p09_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="400" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="46" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Critical Thinking Tier 2: Paul–Elder Metacognitive Matrix (pp. 60–63)", "Phản biện Tầng 2: Tư duy về Chính Quá trình Tư duy Paul–Elder (tr. 60–63)"))}</text>
    <text x="46" y="74" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Apply the 8 Intellectual Standards to the 8 Elements of Thought to forge the 8 Intellectual Virtues.", "Áp dụng 8 Tiêu chuẩn Trí tuệ lên 8 Thành tố Tư duy nhằm bồi đắp 8 Phẩm chất của người tư duy công bằng."))}</text>
    {pe_svg}
    """
    plates.append({
        "id": "p09",
        "slug": "09-paul-elder-metacognition",
        "ch": "Ch. 3",
        "manuscript_ref": T("New figure for Ch. 3 (pp. 60–63)", "Hình mới cho Chương 3 (tr. 60–63)"),
        "title": T("Plate 09 · Paul–Elder 8 × 8 × 8 Metacognitive Architecture", "Bản vẽ 09 · Kiến trúc 3 Bước Tự Phản biện Tư duy (8 × 8 × 8)"),
        "say": T(
            "Critiquing others’ arguments is half the craft; applying identical standards to our own mind builds intellectual integrity.",
            "Phản biện lập luận bên ngoài mới là nửa chặng đường; áp dụng chuẩn mực nghiêm ngặt lên chính suy nghĩ của mình mới tạo nên sự chính trực trí tuệ."
        ),
        "rationale": T(
            "Distills 4 dense pages of bullet lists (pp. 60–63) into the classic 3-column Paul–Elder architecture.",
            "Cô đọng 4 trang danh sách dày đặc (tr. 60–63) thành sơ đồ 3 cột đối xứng 8 Thành tố → 8 Tiêu chuẩn → 8 Phẩm chất."
        ),
        "svg": wrap_svg(900, 440, "Paul-Elder Metacognitive Matrix", p09_body, standalone),
    })

    # =========================================================================
    # PLATE 10: ANALYTICAL TOOL CHAIN (FISHBONE -> 5 WHYS -> SWOT -> EISENHOWER)
    # =========================================================================
    p10_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="410" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Analytical Thinking Pipeline: How Core Tools Chain Together (p. 84)", "Chuỗi Liên hoàn Công cụ Tư duy Phân tích (tr. 71–84)"))}</text>
    <text x="44" y="73" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("“Analytical tools are rarely used in isolation—chain them from decomposition to prioritized action.”", "“Trong thực hành tư duy phân tích, các công cụ hiếm khi dùng độc lập mà kết hợp chặt chẽ với nhau.”"))}</text>

    <!-- 1. Fishbone -->
    <rect x="44" y="96" width="388" height="142" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#0d9488" stroke-width="1.8"/>
    <text x="60" y="120" font-weight="800" font-size="13" fill="var(--c-analytical, #0b7268)">{esc(T("1 · FISHBONE (Ishikawa 5M1E / 4S / 8P)", "1 · BIỂU ĐỒ XƯƠNG CÁ (Phân rã diện rộng)"))}</text>
    <line x1="68" y1="176" x2="346" y2="176" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arTeal)"/>
    <line x1="115" y1="138" x2="150" y2="176" stroke="#0d9488" stroke-width="1.8"/>
    <line x1="195" y1="138" x2="230" y2="176" stroke="#0d9488" stroke-width="1.8"/>
    <line x1="275" y1="138" x2="310" y2="176" stroke="#0d9488" stroke-width="1.8"/>
    <line x1="115" y1="216" x2="150" y2="176" stroke="#0d9488" stroke-width="1.8"/>
    <line x1="195" y1="216" x2="230" y2="176" stroke="#0d9488" stroke-width="1.8"/>
    <line x1="275" y1="216" x2="310" y2="176" stroke="#0d9488" stroke-width="1.8"/>
    <polygon points="350,154 418,176 350,198" fill="#0d9488"/>
    <text x="378" y="180" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">{esc(T("Problem", "Vấn đề"))}</text>
    <text x="112" y="134" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Machine", "Máy móc"))}</text>
    <text x="192" y="134" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Method", "Quy trình"))}</text>
    <text x="275" y="134" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Material", "Vật liệu"))}</text>
    <text x="112" y="231" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("People", "Con người"))}</text>
    <text x="192" y="231" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Measure", "Đo lường"))}</text>
    <text x="275" y="231" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Environ.", "Môi trường"))}</text>

    <!-- 2. 5 Whys -->
    <rect x="468" y="96" width="388" height="142" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#2458d3" stroke-width="1.8"/>
    <text x="484" y="120" font-weight="800" font-size="13" fill="var(--c-critical, #2458d3)">{esc(T("2 · 5 WHYS DRILL (Ohno’s Robot Example)", "2 · 5 CÂU HỎI TẠI SAO (Đào tới gốc rễ)"))}</text>
    <text x="484" y="144" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("Why 1: Circuit overloaded & fuse blew", "Tại sao 1: Quá tải mạch, đứt cầu chì"))}</text>
    <text x="498" y="163" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("↳ Why 2–3: Bearing dry ← Oil pump weak", "↳ Tại sao 2–3: Kẹt vòng bi ← Bơm thiếu dầu"))}</text>
    <text x="512" y="182" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("↳ Why 4: Intake clogged by metal shavings", "↳ Tại sao 4: Cửa hút tắc vụn kim loại"))}</text>
    <text x="526" y="203" font-size="12" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("↳ Why 5 (Root): Pump lacks a strainer! [Verify]", "↳ Tại sao 5 (Gốc): Bơm thiếu bộ lọc! [Xác minh]"))}</text>

    <!-- 3. SWOT -->
    <rect x="44" y="258" width="388" height="150" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#946200" stroke-width="1.8"/>
    <text x="60" y="282" font-weight="800" font-size="13" fill="var(--c-creative, #946200)">{esc(T("3 · SWOT + WEIGHTED COMPARISON", "3 · MA TRẬN SWOT & SO SÁNH TRỌNG SỐ"))}</text>
    <rect x="60" y="294" width="174" height="46" rx="6" fill="rgba(21,128,61,0.12)"/>
    <text x="147" y="321" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-systems, #0b7547)">{esc(T("S · Strengths (Internal)", "S · Điểm mạnh (Nội tại)"))}</text>
    <rect x="242" y="294" width="174" height="46" rx="6" fill="rgba(229,51,63,0.10)"/>
    <text x="329" y="321" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("W · Weaknesses (Internal)", "W · Điểm yếu (Nội tại)"))}</text>
    <rect x="60" y="346" width="174" height="46" rx="6" fill="rgba(37,99,235,0.10)"/>
    <text x="147" y="373" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-critical, #2458d3)">{esc(T("O · Opportunities (External)", "O · Cơ hội (Bên ngoài)"))}</text>
    <rect x="242" y="346" width="174" height="46" rx="6" fill="rgba(217,119,6,0.14)"/>
    <text x="329" y="373" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-strategic, #b34a00)">{esc(T("T · Threats (External)", "T · Thách thức (Bên ngoài)"))}</text>

    <!-- 4. Eisenhower (Upgrades blurry Fig 4.3!) -->
    <rect x="468" y="258" width="388" height="150" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#3346e0" stroke-width="1.8"/>
    <text x="484" y="282" font-weight="800" font-size="13" fill="var(--c-logical, #3346e0)">{esc(T("4 · EISENHOWER EXECUTION MATRIX (p. 80)", "4 · MA TRẬN ƯU TIÊN EISENHOWER (tr. 80)"))}</text>
    <rect x="484" y="294" width="174" height="46" rx="6" fill="rgba(229,51,63,0.12)" stroke="#b81f2e"/>
    <text x="571" y="314" text-anchor="middle" font-size="11" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("Q1 · Urgent + Important", "Ô 1 · Khẩn cấp + Quan trọng"))}</text>
    <text x="571" y="330" text-anchor="middle" font-size="10.5" fill="var(--ink, #15172e)">{esc(T("Do Immediately", "Thực hiện ngay"))}</text>
    <rect x="666" y="294" width="174" height="46" rx="6" fill="rgba(13,148,136,0.15)" stroke="#0d9488" stroke-width="2"/>
    <text x="753" y="314" text-anchor="middle" font-size="11" font-weight="800" fill="var(--c-analytical, #0b7268)">{esc(T("Q2 · Not Urgent + Important", "Ô 2 · Không khẩn + Quan trọng"))}</text>
    <text x="753" y="330" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("Schedule & Invest Early ★", "Lên lịch chuẩn bị sớm ★"))}</text>
    <rect x="484" y="346" width="174" height="46" rx="6" fill="var(--surface, #ffffff)" stroke="var(--line-2, #cbd1e1)"/>
    <text x="571" y="366" text-anchor="middle" font-size="11" font-weight="700" fill="var(--ink-2, #4a4f6a)">{esc(T("Q3 · Urgent + Not Imp.", "Ô 3 · Khẩn + Không quan trọng"))}</text>
    <text x="571" y="382" text-anchor="middle" font-size="10.5" fill="var(--ink-3, #656b87)">{esc(T("Delegate", "Ủy nhiệm"))}</text>
    <rect x="666" y="346" width="174" height="46" rx="6" fill="var(--surface, #ffffff)" stroke="var(--line-2, #cbd1e1)"/>
    <text x="753" y="366" text-anchor="middle" font-size="11" font-weight="700" fill="var(--ink-3, #656b87)">{esc(T("Q4 · Neither", "Ô 4 · Không khẩn + Không QT"))}</text>
    <text x="753" y="382" text-anchor="middle" font-size="10.5" fill="var(--ink-3, #656b87)">{esc(T("Eliminate", "Cần loại bỏ"))}</text>
    """
    plates.append({
        "id": "p10",
        "slug": "10-analytical-tool-chain",
        "ch": "Ch. 4",
        "manuscript_ref": T("Upgrades Figs. 4.1, 4.2 & 4.3 (pp. 72–84)", "Nâng cấp Hình 4.1, 4.2 & 4.3 (tr. 72–84)"),
        "title": T("Plate 10 · The Integrated Analytical Tool Chain", "Bản vẽ 10 · Chuỗi Phối hợp 4 Công cụ Phân tích Cốt lõi"),
        "say": T(
            "Fishbone widens cause categories, 5 Whys drills to the root, SWOT maps internal vs. external forces, and Eisenhower protects Quadrant 2 execution.",
            "Xương cá mở rộng nhánh nguyên nhân, 5 Tại sao khoan tới gốc rễ, SWOT định vị nội – ngoại lực, và Eisenhower bảo vệ Ô 2 chiến lược."
        ),
        "rationale": T(
            "Replaces the blurry low-resolution Eisenhower JPEG (Fig. 4.3, p. 80) and plain SWOT box with a crisp vector suite illustrating p. 84’s synthesis.",
            "Thay thế ảnh chụp Ma trận Eisenhower bị mờ vỡ hạt (Hình 4.3, tr. 80) và bảng thô bằng đồ họa vector sắc nét tích hợp đúng tinh thần trang 84."
        ),
        "svg": wrap_svg(900, 450, "Analytical Thinking Tool Chain", p10_body, standalone),
    })

    # =========================================================================
    # PLATE 11: LOGICAL THINKING — 4 LAWS & 4 INFERENCE ENGINES (CH. 5)
    # =========================================================================
    laws = [
        ("A ≡ A", T("1. Identity", "1. Đồng nhất"), T("Keep term meaning fixed", "Giữ nguyên nghĩa khái niệm")),
        ("¬(A ∧ ¬A)", T("2. Non-Contradiction", "2. Không mâu thuẫn"), T("Not true & false in same respect", "Không vừa đúng vừa sai cùng nghĩa")),
        ("A ∨ ¬A", T("3. Excluded Middle", "3. Loại trừ trung gian"), T("No murky third state", "Không có trạng thái lơ lửng")),
        ("P ⇒ Q", T("4. Sufficient Reason", "4. Đủ lý do"), T("Every claim needs ground", "Mọi kết luận phải đủ căn cứ")),
    ]
    law_svg = ""
    for i, (sym, lnm, lds) in enumerate(laws):
        lx = 44 + i * 206
        law_svg += f'<rect x="{lx}" y="86" width="194" height="78" rx="8" fill="rgba(79,70,229,0.08)" stroke="#3346e0" stroke-width="1.6"/>'
        law_svg += f'<text x="{lx + 97}" y="110" text-anchor="middle" class="mn" font-size="13" font-weight="800" fill="var(--c-logical, #3346e0)">{esc(sym)}</text>'
        law_svg += f'<text x="{lx + 97}" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink, #15172e)">{esc(lnm)}</text>'
        law_svg += f'<text x="{lx + 97}" y="150" text-anchor="middle" font-size="10.5" fill="var(--ink-2, #4a4f6a)">{esc(lds)}</text>'

    infs = [
        ("#3346e0", T("DEDUCTION (Top-Down)", "DIỄN DỊCH (Từ trên xuống)"), T("General Rule → Specific Case", "Tiền đề chung → Cụ thể"), T("100% Certain (if premises hold)", "Chắc chắn 100% (nếu tiền đề đúng)"), T("Trap: Whale ≠ Fish; Undistributed middle", "Bẫy: Cá voi ≠ cá; Sai bao hàm tập hợp")),
        ("#0d9488", T("INDUCTION (Bottom-Up)", "QUY NẠP (Từ dưới lên)"), T("Specific Cases → Pattern Law", "Quan sát cụ thể → Quy luật"), T("Probabilistic (revisable)", "Mang tính xác suất (cập nhật)"), T("Trap: Small sample; 1697 Black Swan", "Bẫy: Mẫu nhỏ; Thiên nga đen 1697")),
        ("#946200", T("CAUSAL (5 Criteria)", "NHÂN QUẢ (5 Yếu tố)"), T("Time + Corr + No-3rd + Mech", "Thời gian + Tương quan + Cơ chế"), T("Explains WHY X produces Y", "Giải thích cơ chế A sinh ra B"), T("Trap: Ice cream & sunglasses (Sun!)", "Bẫy: Kem & kính râm (do trời nắng!)")),
        ("#bd1e68", T("ANALOGY (Loại suy)", "TƯƠNG TỰ (Loại suy)"), T("A & B share c,d,e → B has f?", "A, B chung c,d,e → B có f?"), T("Probabilistic structural transfer", "Xác suất theo chiều sâu tương đồng"), T("Trap: Shark vs. Tiger; Piano equivocation", "Bẫy: Cá mập – hổ; Đặng Thái Sơn")),
    ]
    inf_svg = ""
    for i, (col, inm, dir_s, cert, trp) in enumerate(infs):
        ix = 44 + (i % 2) * 412
        iy = 186 + (i // 2) * 114
        inf_svg += f'<rect x="{ix}" y="{iy}" width="400" height="100" rx="9" fill="var(--surface-2, #eef1f8)" stroke="{col}" stroke-width="1.8"/>'
        inf_svg += f'<text x="{ix + 16}" y="{iy + 24}" font-size="13" font-weight="800" fill="{col}">{esc(inm)}</text>'
        inf_svg += f'<text x="{ix + 16}" y="{iy + 46}" font-size="11.5" font-weight="700" fill="var(--ink, #15172e)">{esc(dir_s)}  ·  {esc(cert)}</text>'
        inf_svg += f'<text x="{ix + 16}" y="{iy + 72}" font-size="11" fill="var(--c-trap, #b81f2e)">{esc(trp)}</text>'

    p11_body = f"""
    <rect x="24" y="20" width="852" height="404" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Logical Thinking: The 4 Classical Laws & 4 Inference Engines (pp. 88–98)", "Tư duy Logic: 4 Nguyên lý Gốc & 4 Công cụ Suy luận (tr. 88–98)"))}</text>
    <text x="44" y="72" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Logic is the grammar of all reasoning—distinguishing 100% deductive entailment from probabilistic induction and analogy.", "Logic là ngữ pháp của mọi lập luận—phân định rạch ròi suy luận chắc chắn 100% với suy luận xác suất."))}</text>
    {law_svg}
    {inf_svg}
    """
    plates.append({
        "id": "p11",
        "slug": "11-logical-laws-and-inferences",
        "ch": "Ch. 5",
        "manuscript_ref": T("New figure for Ch. 5 (pp. 88–98)", "Hình mới cho Chương 5 (tr. 88–98)"),
        "title": T("Plate 11 · Grammar of Logic: 4 Laws & 4 Reasoning Modes", "Bản vẽ 11 · Ngữ pháp của Suy luận: 4 Nguyên lý & 4 Phương thức Logic"),
        "say": T(
            "Only Deduction from true universal premises guarantees certainty; Induction, Causality, and Analogy demand sample size, mechanism, and structural depth.",
            "Chỉ Diễn dịch từ tiền đề phổ quát đúng mới cho sự chắc chắn tuyệt đối; Quy nạp, Nhân quả và Loại suy luôn đòi hỏi cỡ mẫu, cơ chế và chiều sâu bản chất."
        ),
        "rationale": T(
            "Chapter 5 currently has zero illustrations across 14 pages; this blueprint maps all 4 laws and 4 inference tools onto one comparative board.",
            "Chương 5 hiện chưa có hình minh họa nào; bản vẽ này hệ thống hóa trọn vẹn 4 nguyên lý logic cổ điển và 4 công cụ suy luận trên một mặt phẳng."
        ),
        "svg": wrap_svg(900, 444, "Logical Laws and Inference Engines", p11_body, standalone),
    })

    # =========================================================================
    # PLATE 12: SYSTEMS THINKING — BLAME LOOP (R1/R2) -> LEARNING CULTURE (B1/B2)
    # =========================================================================
    p12_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="400" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Systems Leverage: Flipping Blame Spirals (R) into Learning Loops (B) (pp. 114–115)", "Điểm Đòn bẩy Hệ thống: Chuyển Vòng Xoáy Giấu Lỗi (R) Thành Học Tập (B) (tr. 114–115)"))}</text>

    <!-- Left: Vicious R1/R2 Blame Loop -->
    <rect x="44" y="78" width="392" height="320" rx="10" fill="rgba(229,51,63,0.06)" stroke="#b81f2e" stroke-width="1.8"/>
    <text x="240" y="104" text-anchor="middle" font-weight="800" font-size="13.5" fill="var(--c-trap, #b81f2e)">{esc(T("BEFORE · Blame Culture (Runaway Errors R1 & R2)", "TRƯỚC · Văn hóa Đổ lỗi & Trừng phạt (Vòng R1 & R2)"))}</text>
    <circle cx="240" cy="242" r="92" fill="none" stroke="#b81f2e" stroke-width="2.2" stroke-dasharray="5 3"/>
    <text x="240" y="238" text-anchor="middle" font-weight="800" font-size="18" fill="var(--c-trap, #b81f2e)">R1 · R2 (+)</text>
    <text x="240" y="258" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Errors Spiral Upward", "Lỗi ngày càng lan rộng"))}</text>
    <rect x="180" y="124" width="120" height="30" rx="6" fill="#b81f2e"/>
    <text x="240" y="143" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">{esc(T("Punitive Blame (+)", "Quy trách nhiệm (+)"))}</text>
    <text x="366" y="210" text-anchor="middle" font-size="11" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Fear & Hiding (+)", "Lo sợ & Che giấu (+)"))}</text>
    <text x="240" y="362" text-anchor="middle" font-size="11" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Truth Blindness & Zero Innovation (−)", "Mù thông tin & Ngại đổi mới (−)"))}</text>
    <text x="112" y="210" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("More Errors (+)", "Lỗi Tăng Lên (+)"))}</text>

    <!-- Right: Virtuous B1/B2 Learning Loop -->
    <rect x="464" y="78" width="392" height="320" rx="10" fill="rgba(21,128,61,0.07)" stroke="#0b7547" stroke-width="2"/>
    <text x="660" y="104" text-anchor="middle" font-weight="800" font-size="13.5" fill="var(--c-systems, #0b7547)">{esc(T("AFTER · Leverage Point Swap (Self-Correcting B1 & B2)", "SAU · Can thiệp Điểm Đòn bẩy (Vòng Cân bằng B1 & B2)"))}</text>
    <circle cx="660" cy="242" r="92" fill="none" stroke="#0b7547" stroke-width="2.4"/>
    <text x="660" y="238" text-anchor="middle" font-weight="800" font-size="18" fill="var(--c-systems, #0b7547)">B1 · B2 (−)</text>
    <text x="660" y="258" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Errors Self-Correct", "Lỗi tự điều chỉnh giảm dần"))}</text>
    <rect x="582" y="122" width="156" height="32" rx="6" fill="#0b7547"/>
    <text x="660" y="142" text-anchor="middle" font-size="11" font-weight="800" fill="#ffffff">{esc(T("★ Learning Opportunity (+)", "★ Cơ hội Học tập (+)"))}</text>
    <text x="786" y="210" text-anchor="middle" font-size="11" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Less Fear & Hiding (−)", "Giảm lo & Giấu lỗi (−)"))}</text>
    <text x="660" y="362" text-anchor="middle" font-size="11" font-weight="700" fill="var(--c-systems, #0b7547)">{esc(T("Open Data + Safe Experimentation (+)", "Đủ thông tin + Dám đổi mới (+)"))}</text>
    <text x="532" y="210" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-systems, #0b7547)">{esc(T("Errors Fall (−)", "Lỗi Giảm Đi (−)"))}</text>
    """
    plates.append({
        "id": "p12",
        "slug": "12-systems-cld-leverage-pivot",
        "ch": "Ch. 6",
        "manuscript_ref": T("Upgrades Figs. 6.3 & 6.4 (pp. 114–115)", "Vẽ lại đồng bộ Hình 6.3 & 6.4 (tr. 114–115)"),
        "title": T("Plate 12 · Causal Loop Leverage: From Error Hiding (R) to Learning (B)", "Bản vẽ 12 · Đòn bẩy Vòng Phản hồi: Từ Che giấu Lỗi (R) sang Học tập (B)"),
        "say": T(
            "Changing a single structural rule—treating errors as learning data instead of punishable sins—flips two destructive reinforcing loops into self-correcting balancing loops.",
            "Chỉ đổi một mắt xích cấu trúc—coi lỗi là cơ hội học tập thay vì trừng phạt—đã đảo chiều 2 vòng xoáy phá hủy (R) thành 2 vòng tự cân bằng bền vững (B)."
        ),
        "rationale": T(
            "Unifies Figs. 6.1–6.7 (currently low-res screenshots with mixed `s/o` and `+/-` fonts) into a clean side-by-side vector comparison.",
            "Chuẩn hóa loạt ảnh chụp mờ Hình 6.1–6.7 (vốn lệch phông chữ và ký hiệu) thành đồ họa đối chiếu trực quan chuẩn mực."
        ),
        "svg": wrap_svg(900, 440, "Systems Thinking CLD Pivot", p12_body, standalone),
    })

    # =========================================================================
    # PLATE 13: BEHAVIOR OVER TIME (BOT) — 3 SYSTEMIC CURVES (CH. 6)
    # =========================================================================
    p13_body = f"""
    <rect x="24" y="20" width="852" height="380" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Behavior Over Time (BOT): Three Signature Dynamic Regimes (pp. 120–123)", "Đồ thị Hành vi Theo Thời gian: 3 Mẫu hình Động học Điển hình (tr. 120–123)"))}</text>

    <!-- 1. S-Curve -->
    <rect x="44" y="80" width="258" height="292" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line, #e1e5f0)"/>
    <text x="60" y="106" font-weight="800" font-size="13" fill="var(--c-analytical, #0b7268)">{esc(T("1 · Logistic S-Curve", "1 · Hành vi Hình chữ S"))}</text>
    <line x1="68" y1="142" x2="278" y2="142" stroke="#b81f2e" stroke-width="1.4" stroke-dasharray="4 3"/>
    <line x1="68" y1="278" x2="280" y2="278" stroke="var(--ink-3, #656b87)" stroke-width="1.5"/>
    <line x1="68" y1="128" x2="68" y2="278" stroke="var(--ink-3, #656b87)" stroke-width="1.5"/>
    <path d="M 72,270 C 135,268 155,235 174,205 C 193,175 215,145 276,144" fill="none" stroke="#0d9488" stroke-width="3"/>
    <circle cx="174" cy="205" r="5" fill="#946200"/>
    <text x="174" y="193" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--c-creative, #946200)">{esc(T("Inflection", "Điểm uốn"))}</text>
    <text x="60" y="308" font-size="11" fill="var(--ink, #15172e)">{esc(T("Phase 1: R dominates (takeoff)", "Pha 1: Vòng R thống trị (bùng nổ)"))}</text>
    <text x="60" y="326" font-size="11" fill="var(--ink, #15172e)">{esc(T("Phase 2: B dominates (saturation)", "Pha 2: Vòng B thống trị (bão hòa)"))}</text>
    <text x="60" y="350" font-size="10.5" fill="var(--ink-3, #656b87)">{esc(T("Ex: Product adoption, viral spread", "VD: Tăng trưởng sản phẩm, dịch tễ"))}</text>

    <!-- 2. Delayed Oscillation -->
    <rect x="321" y="80" width="258" height="292" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line, #e1e5f0)"/>
    <text x="337" y="106" font-weight="800" font-size="13" fill="var(--c-critical, #2458d3)">{esc(T("2 · Delayed Oscillation", "2 · Hành vi Dao động (do Trễ)"))}</text>
    <line x1="345" y1="205" x2="555" y2="205" stroke="#b81f2e" stroke-width="1.4" stroke-dasharray="4 3"/>
    <line x1="345" y1="278" x2="557" y2="278" stroke="var(--ink-3, #656b87)" stroke-width="1.5"/>
    <line x1="345" y1="128" x2="345" y2="278" stroke="var(--ink-3, #656b87)" stroke-width="1.5"/>
    <path d="M 348,248 Q 378,132 408,205 T 468,205 T 528,205 L 552,165" fill="none" stroke="#2458d3" stroke-width="3"/>
    <text x="337" y="308" font-size="11" fill="var(--ink, #15172e)">{esc(T("Balancing loop B + Time Delay (//)", "Vòng cân bằng B + Độ trễ (//)"))}</text>
    <text x="337" y="326" font-size="11" font-weight="700" fill="var(--c-critical, #2458d3)">{esc(T("Fix: Shorten feedback delay τ!", "Giải pháp: Thu hẹp độ trễ thời gian!"))}</text>
    <text x="337" y="350" font-size="10.5" fill="var(--ink-3, #656b87)">{esc(T("Ex: Business & inventory cycles", "VD: Chu kỳ kinh tế, tồn kho"))}</text>

    <!-- 3. Runaway Exponential -->
    <rect x="598" y="80" width="258" height="292" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line, #e1e5f0)"/>
    <text x="614" y="106" font-weight="800" font-size="13" fill="var(--c-trap, #b81f2e)">{esc(T("3 · Unchecked Runaway", "3 · Tăng Không Giới hạn (Khủng hoảng)"))}</text>
    <line x1="622" y1="278" x2="834" y2="278" stroke="var(--ink-3, #656b87)" stroke-width="1.5"/>
    <line x1="622" y1="128" x2="622" y2="278" stroke="var(--ink-3, #656b87)" stroke-width="1.5"/>
    <path d="M 626,272 C 695,270 755,252 818,134" fill="none" stroke="#b81f2e" stroke-width="3"/>
    <text x="614" y="308" font-size="11" fill="var(--ink, #15172e)">{esc(T("Pure Reinforcing loop R unchecked", "Vòng tăng cường R lấn át hoàn toàn"))}</text>
    <text x="614" y="326" font-size="11" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("Fix: Intervene early to cap R!", "Giải pháp: Hãm vòng R ngay từ sớm!"))}</text>
    <text x="614" y="350" font-size="10.5" fill="var(--ink-3, #656b87)">{esc(T("Ex: Contagious bank-run panic", "VD: Rút tiền hàng loạt sụp đổ ngân hàng"))}</text>
    """
    plates.append({
        "id": "p13",
        "slug": "13-bot-three-archetypes",
        "ch": "Ch. 6",
        "manuscript_ref": T("Upgrades Figs. 6.8, 6.9 & 6.10 (pp. 121–123)", "Vẽ lại Hình 6.8, 6.9 & 6.10 (tr. 121–123)"),
        "title": T("Plate 13 · Three Signature Behavior-Over-Time (BOT) Curves", "Bản vẽ 13 · Ba Đồ thị Diễn biến Hành vi Hệ thống Điển hình"),
        "say": T(
            "Every curve over time reveals the hidden loop structure underneath—and corrects p. 120’s abscissa/ordinate axis labels.",
            "Hình dáng đường cong theo trục hoành thời gian phơi bày cấu trúc vòng lặp ẩn phía sau và chuẩn hóa lại trục hoành / trục tung ở tr. 120."
        ),
        "rationale": T(
            "Replaces three pixelated cropped curves (Figs. 6.8–6.10) with a unified triptych linking each curve directly to its R/B loop mechanism.",
            "Thay 3 ảnh cắt mờ (Hình 6.8–6.10) bằng bộ ba đồ thị vector chuẩn xác đối chiếu trực tiếp từng dạng đường cong với cơ chế vòng R/B."
        ),
        "svg": wrap_svg(900, 420, "Behavior Over Time Graphs", p13_body, standalone),
    })

    # =========================================================================
    # PLATE 14: STRATEGIC ARCHITECTURE — PESTLE -> TOWS -> SCENARIO WORLDS (CH. 7)
    # =========================================================================
    p14_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="390" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Strategic Architecture: From Macro Radar to Resilient Scenarios (pp. 130–135)", "Kiến trúc Tư duy Chiến lược: Từ PESTLE & TOWS Đến Kịch bản Tương lai (tr. 130–135)"))}</text>

    <!-- Col 1: PESTLE -->
    <rect x="44" y="84" width="224" height="296" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#b34a00" stroke-width="1.8"/>
    <text x="156" y="110" text-anchor="middle" font-weight="800" font-size="13" fill="var(--c-strategic, #b34a00)">{esc(T("1 · PESTLE RADAR", "1 · QUÉT VĨ MÔ PESTLE"))}</text>
    <text x="62" y="142" font-size="12" font-weight="700" fill="var(--ink, #15172e)">P · Political ({esc(T("Policy", "Chính sách"))})</text>
    <text x="62" y="172" font-size="12" font-weight="700" fill="var(--ink, #15172e)">E · Economic ({esc(T("Inflation/Rates", "Lạm phát/Lãi"))})</text>
    <text x="62" y="202" font-size="12" font-weight="700" fill="var(--ink, #15172e)">S · Social ({esc(T("Demographics", "Nhân khẩu"))})</text>
    <text x="62" y="232" font-size="12" font-weight="700" fill="var(--ink, #15172e)">T · Tech ({esc(T("AI & Automation", "AI & Tự động"))})</text>
    <text x="62" y="262" font-size="12" font-weight="700" fill="var(--ink, #15172e)">L · Legal ({esc(T("Statutes", "Luật định"))})</text>
    <text x="62" y="292" font-size="12" font-weight="700" fill="var(--ink, #15172e)">E · Ecological ({esc(T("Climate", "Khí hậu"))})</text>
    <text x="156" y="346" text-anchor="middle" font-size="11" font-style="italic" fill="var(--ink-2, #4a4f6a)">{esc(T("Pick ≤ 3 key uncertainties", "Chọn ≤ 3 bất định then chốt"))}</text>

    <line x1="272" y1="232" x2="298" y2="232" stroke="var(--ink-2, #4a4f6a)" stroke-width="2.2" marker-end="url(#arInk)"/>

    <!-- Col 2: TOWS -->
    <rect x="304" y="84" width="256" height="296" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#0d9488" stroke-width="1.8"/>
    <text x="432" y="110" text-anchor="middle" font-weight="800" font-size="13" fill="var(--c-analytical, #0b7268)">{esc(T("2 · TOWS ACTION MATRIX", "2 · MA TRẬN HÀNH ĐỘNG TOWS"))}</text>
    <rect x="320" y="128" width="108" height="96" rx="7" fill="rgba(21,128,61,0.12)"/>
    <text x="374" y="160" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-systems, #0b7547)">SO</text>
    <text x="374" y="182" text-anchor="middle" font-size="10.5" fill="var(--ink, #15172e)">{esc(T("Strength × Opp.", "Mạnh × Cơ hội"))}</text>
    <rect x="436" y="128" width="108" height="96" rx="7" fill="rgba(37,99,235,0.12)"/>
    <text x="490" y="160" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-critical, #2458d3)">ST</text>
    <text x="490" y="182" text-anchor="middle" font-size="10.5" fill="var(--ink, #15172e)">{esc(T("Strength × Threat", "Mạnh × Nguy cơ"))}</text>
    <rect x="320" y="232" width="108" height="96" rx="7" fill="rgba(217,119,6,0.12)"/>
    <text x="374" y="264" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-creative, #946200)">WO</text>
    <text x="374" y="286" text-anchor="middle" font-size="10.5" fill="var(--ink, #15172e)">{esc(T("Cure Weakness", "Mượn O bù Yếu"))}</text>
    <rect x="436" y="232" width="108" height="96" rx="7" fill="rgba(229,51,63,0.12)"/>
    <text x="490" y="264" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-trap, #b81f2e)">WT</text>
    <text x="490" y="286" text-anchor="middle" font-size="10.5" fill="var(--ink, #15172e)">{esc(T("Knee → Swim!", "Đau gối → Đi bơi!"))}</text>
    <text x="432" y="356" text-anchor="middle" font-size="11" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("SWOT is input; TOWS is action!", "SWOT là đầu vào; kết hợp mới là chiến lược!"))}</text>

    <line x1="564" y1="232" x2="590" y2="232" stroke="var(--ink-2, #4a4f6a)" stroke-width="2.2" marker-end="url(#arInk)"/>

    <!-- Col 3: Scenario Planning -->
    <rect x="596" y="84" width="260" height="296" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#6835f0" stroke-width="1.8"/>
    <text x="726" y="110" text-anchor="middle" font-weight="800" font-size="13" fill="var(--c-prob, #6835f0)">{esc(T("3 · SCENARIO PLAYBOOKS", "3 · CHIẾN LƯỢC KỊCH BẢN"))}</text>
    <rect x="614" y="132" width="224" height="88" rx="8" fill="rgba(229,51,63,0.10)" stroke="#b81f2e"/>
    <text x="628" y="156" font-size="11.5" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("Scenario 1: Inflation > Deposit Rate", "Kịch bản 1: Lạm phát > Lãi gửi NH"))}</text>
    <text x="628" y="178" font-size="11" fill="var(--ink, #15172e)">{esc(T("→ Rotate cash into gold / real assets", "→ Chuyển sang vàng / bất động sản"))}</text>
    <text x="628" y="198" font-size="10.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Rule: Never collapse in the bad world!", "Chuẩn bị để không sụp đổ ở kịch bản xấu!"))}</text>

    <rect x="614" y="238" width="224" height="88" rx="8" fill="rgba(21,128,61,0.10)" stroke="#0b7547"/>
    <text x="628" y="262" font-size="11.5" font-weight="800" fill="var(--c-systems, #0b7547)">{esc(T("Scenario 2: Inflation < Deposit Rate", "Kịch bản 2: Lạm phát < Lãi gửi NH"))}</text>
    <text x="628" y="284" font-size="11" fill="var(--ink, #15172e)">{esc(T("→ Compound bank deposits safely", "→ Tiếp tục giữ tiền gửi hưởng lãi thực"))}</text>
    <text x="628" y="304" font-size="10.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Adapt dynamically—don’t forecast 1 line", "Thích ứng linh hoạt thay vì đoán mò 1 hướng"))}</text>
    """
    plates.append({
        "id": "p14",
        "slug": "14-strategic-pestle-tows-scenarios",
        "ch": "Ch. 7",
        "manuscript_ref": T("New figure for Ch. 7 (pp. 130–135)", "Hình mới cho Chương 7 (tr. 130–135)"),
        "title": T("Plate 14 · Strategic Pipeline: PESTLE → TOWS → Scenario Worlds", "Bản vẽ 14 · Chuỗi Hoạch định Chiến lược: PESTLE → TOWS → Kịch bản"),
        "say": T(
            "Analysis audits today’s board, TOWS turns traits into postures, and Scenario Planning prepares resilient moves across multiple uncertain futures.",
            "PESTLE quét biến động vĩ mô, TOWS kết hợp nội – ngoại lực thành hành động, còn Kịch bản giữ ta đứng vững dù tương lai rẽ sang hướng nào."
        ),
        "rationale": T(
            "Chapter 7 currently has zero figures across 15 pages; Plate 14 and Plate 15 bring its strategic frameworks and game-theory matrices to life.",
            "Chương 7 hiện chưa có hình minh họa nào suốt 15 trang; Bản vẽ 14 và 15 trực quan hóa toàn bộ quy trình chiến lược và Lý thuyết trò chơi."
        ),
        "svg": wrap_svg(900, 430, "Strategic Pipeline PESTLE TOWS Scenarios", p14_body, standalone),
    })

    # =========================================================================
    # PLATE 15: GAME THEORY — 5 ARCHETYPAL GAMES (CH. 7)
    # =========================================================================
    games = [
        ("#b81f2e", T("1 · Prisoner’s Dilemma", "1 · Tiến thoái Lưỡng nan Tù nhân"), T("Silent/Silent = (2y, 2y) ★ Best joint", "Im lặng/Im lặng = (2 năm, 2 năm) ★"), T("Confess/Confess = (3y, 3y) Trap!", "Thú tội/Thú tội = (3 năm, 3 năm) Bẫy!"), T("Lesson: Binding trust + punish betrayal", "Bài học: Thỏa thuận hợp tác + phạt phản bội")),
        ("#946200", T("2 · Chicken Game", "2 · Trò chơi Gà (Đối đầu)"), T("Swerve/Swerve = Safe compromise", "Cùng nhường = Cả hai an toàn"), T("Straight/Straight = Fatal crash!", "Không ai nhường = Đâm nhau thảm khốc!"), T("Lesson: Never corner rivals with 0 to lose", "Bài học: Đừng dồn đối phương vào chân tường")),
        ("#0d9488", T("3 · Fair Cake-Cutting", "3 · Chia Bánh Công bằng"), T("Player A cuts into 2 pieces", "Người A cắt bánh làm 2 phần"), T("Player B chooses their slice first", "Người B được quyền chọn phần trước"), T("Lesson: Self-enforcing fairness mechanism", "Bài học: Cơ chế tự bảo đảm sự công bằng")),
        ("#2458d3", T("4 · Battle of the Sexes", "4 · Cuộc chiến Giới tính"), T("Together at Concert (5,3) or Match (3,5)", "Đi chung: Ca nhạc (5,3) / Bóng đá (3,5)"), T("Go alone = (2,2) Worst total (4 < 8)!", "Đi riêng = (2,2) Tổng thỏa mãn thấp nhất!"), T("Lesson: Reciprocal turn-taking over time", "Bài học: Thỏa hiệp có đi có lại dài hạn")),
        ("#6835f0", T("5 · Rock–Paper–Scissors", "5 · Oẳn tù tỳ (Tổng bằng 0)"), T("Rock > Scissors > Paper > Rock", "Đá thắng Kéo > Giấy > Đá"), T("Any predictable pattern gets exploited", "Mọi quy luật lặp lại đều bị bắt bài"), T("Lesson: Randomize equally across moves", "Bài học: Luân phiên ngẫu nhiên không quy luật")),
    ]
    g_svg = ""
    for i, (col, gnm, l1, l2, les) in enumerate(games):
        gx = 44 + (i % 3) * 276 if i < 3 else 182 + (i - 3) * 288
        gy = 86 if i < 3 else 248
        g_svg += f'<rect x="{gx}" y="{gy}" width="262" height="142" rx="10" fill="var(--surface-2, #eef1f8)" stroke="{col}" stroke-width="2"/>'
        g_svg += f'<text x="{gx + 14}" y="{gy + 26}" font-size="12.5" font-weight="800" fill="{col}">{esc(gnm)}</text>'
        g_svg += f'<text x="{gx + 14}" y="{gy + 54}" font-size="11" fill="var(--ink, #15172e)">{esc(l1)}</text>'
        g_svg += f'<text x="{gx + 14}" y="{gy + 76}" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(l2)}</text>'
        g_svg += f'<line x1="{gx + 14}" y1="{gy + 94}" x2="{gx + 248}" y2="{gy + 94}" stroke="var(--line-2, #cbd1e1)"/>'
        g_svg += f'<text x="{gx + 14}" y="{gy + 118}" font-size="11" font-weight="700" fill="{col}">{esc(les)}</text>'

    p15_body = f"""
    <rect x="24" y="20" width="852" height="400" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Strategic Game Theory: Five Archetypes of Human Interaction (pp. 136–139)", "Lý thuyết Trò chơi: 5 Mô hình Tương tác Chiến lược Kinh điển (tr. 136–139)"))}</text>
    <text x="44" y="72" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Your outcome depends on everyone’s choices—diagnose which game you are in before making a move.", "Kết quả của mỗi bên phụ thuộc vào lựa chọn của tất cả các bên—hãy nhận diện đúng trò chơi trước khi hành động."))}</text>
    {g_svg}
    """
    plates.append({
        "id": "p15",
        "slug": "15-five-game-theory-archetypes",
        "ch": "Ch. 7",
        "manuscript_ref": T("New figure for Ch. 7 (pp. 136–139)", "Hình mới cho Chương 7 (tr. 136–139)"),
        "title": T("Plate 15 · The Five Classic Game-Theory Models", "Bản vẽ 15 · Năm Mô hình Lý thuyết Trò chơi Phổ biến Trong Đời sống"),
        "say": T(
            "Whether facing pollution races, brinkmanship, fair division, family compromises, or zero-sum rivals, Game Theory turns conflict into structured strategy.",
            "Từ xả thải môi trường, đàm phán căng thẳng, chia phần công bằng đến nhường nhịn vợ chồng—mỗi tình huống đều có chiến lược giải mã tối ưu."
        ),
        "rationale": T(
            "Visualizes all five Game Theory subsections of Chapter 7 onto clean payoff cards for rapid recall.",
            "Trực quan hóa trọn vẹn 5 mục Lý thuyết trò chơi của Chương 7 thành 5 thẻ cấu trúc rõ ràng, dễ nhớ, dễ áp dụng."
        ),
        "svg": wrap_svg(900, 440, "Five Game Theory Archetypes", p15_body, standalone),
    })

    # =========================================================================
    # PLATE 16: PROBABILITY TREE & EXPECTED VALUE (REDESIGN FIGS 8.1-8.3)
    # =========================================================================
    leaves = [
        (102, "#0b7547", T("Gain +5%", "Lãi 5%"), "0.20", "0.75 × 0.20 = 0.150"),
        (162, "#0b7547", T("Gain +10%", "Lãi 10%"), "0.70", "0.75 × 0.70 = 0.525"),
        (222, "#0b7547", T("Gain +20%", "Lãi 20%"), "0.10", "0.75 × 0.10 = 0.075"),
        (302, "#b81f2e", T("Loss −5%", "Lỗ 5%"), "0.60", "0.25 × 0.60 = 0.150"),
        (362, "#b81f2e", T("Loss −15%", "Lỗ 15%"), "0.40", "0.25 × 0.40 = 0.100"),
    ]
    lf_svg = ""
    for i, (ly, col, lnm, p2, prod) in enumerate(leaves):
        sy = 162 if i < 3 else 332
        lf_svg += f'<line x1="258" y1="{sy}" x2="390" y2="{ly}" stroke="{col}" stroke-width="2" marker-end="url(#arInk)"/>'
        lf_svg += f'<text x="322" y="{(sy + ly)//2 - 5}" text-anchor="middle" class="mn" font-size="11" font-weight="700" fill="{col}">{p2}</text>'
        lf_svg += f'<rect x="398" y="{ly - 17}" width="106" height="34" rx="6" fill="var(--surface-2, #eef1f8)" stroke="{col}" stroke-width="1.6"/>'
        lf_svg += f'<text x="451" y="{ly + 4}" text-anchor="middle" font-size="12" font-weight="700" fill="{col}">{esc(lnm)}</text>'
        lf_svg += f'<text x="518" y="{ly + 4}" class="mn" font-size="11.5" fill="var(--ink, #15172e)">({prod})</text>'

    p16_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="390" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Probabilistic Thinking: Investment Tree & Expected Value (pp. 146–152)", "Cây Xác suất Đầu tư & Giá trị Kỳ vọng EV (tr. 146–152)"))}</text>

    <!-- Root -->
    <rect x="48" y="224" width="96" height="44" rx="8" fill="#6835f0"/>
    <text x="96" y="251" text-anchor="middle" font-size="13" font-weight="800" fill="#ffffff">{esc(T("Invest", "Đầu tư"))}</text>

    <!-- Stage 1 -->
    <line x1="144" y1="240" x2="196" y2="162" stroke="#0b7547" stroke-width="2.4" marker-end="url(#arGreen)"/>
    <text x="160" y="192" class="mn" font-size="11.5" font-weight="700" fill="var(--c-systems, #0b7547)">0.75</text>
    <rect x="202" y="145" width="56" height="34" rx="6" fill="rgba(21,128,61,0.14)" stroke="#0b7547" stroke-width="1.8"/>
    <text x="230" y="167" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-systems, #0b7547)">{esc(T("Gain", "Lãi"))}</text>

    <line x1="144" y1="252" x2="196" y2="332" stroke="#b81f2e" stroke-width="2.4" marker-end="url(#arRed)"/>
    <text x="160" y="308" class="mn" font-size="11.5" font-weight="700" fill="var(--c-trap, #b81f2e)">0.25</text>
    <rect x="202" y="315" width="56" height="34" rx="6" fill="rgba(229,51,63,0.12)" stroke="#b81f2e" stroke-width="1.8"/>
    <text x="230" y="337" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("Loss", "Lỗ"))}</text>

    {lf_svg}

    <!-- Right Summary Card -->
    <rect x="676" y="88" width="182" height="290" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#6835f0" stroke-width="1.8"/>
    <text x="767" y="116" text-anchor="middle" font-weight="800" font-size="13" fill="var(--c-prob, #6835f0)">{esc(T("GOLDEN RULES", "QUY TẮC CÂY & EV"))}</text>
    <text x="690" y="144" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("1. Node fan sums = 1.00", "1. Tổng nhánh con = 1,00"))}</text>
    <text x="690" y="166" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("2. Leaf P = path product", "2. Nút cuối = tích dọc nhánh"))}</text>
    <text x="690" y="188" class="mn" font-size="11" font-weight="700" fill="var(--c-systems, #0b7547)">Σ P_leaf = 1.000 ✓</text>
    <line x1="690" y1="206" x2="844" y2="206" stroke="var(--line-2, #cbd1e1)"/>
    <text x="690" y="230" font-size="11.5" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Expected Value (Tree):", "Kỳ vọng EV (Cây 8.3):"))}</text>
    <text x="690" y="252" class="mn" font-size="13" font-weight="800" fill="var(--c-prob, #6835f0)">EV = +5.25%</text>
    <text x="690" y="280" font-size="11.5" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Table 8.1 Portfolio EV:", "Bảng 8.1 Đầu tư:"))}</text>
    <text x="690" y="302" class="mn" font-size="13" font-weight="800" fill="var(--c-systems, #0b7547)">EV = +8.00%</text>
    <text x="690" y="336" font-size="10.5" font-style="italic" fill="var(--c-trap, #b81f2e)">{esc(T("+ Guard against Taleb’s", "+ Luôn kiểm tra thêm rủi ro"))}</text>
    <text x="690" y="352" font-size="10.5" font-style="italic" fill="var(--c-trap, #b81f2e)">{esc(T("  Black Swan tail ruin!", "  Thiên nga đen (tr. 149)!"))}</text>
    """
    plates.append({
        "id": "p16",
        "slug": "16-probability-tree-expected-value",
        "ch": "Ch. 8",
        "manuscript_ref": T("Redesigned Figs. 8.1–8.3 & Table 8.1 (pp. 146–152)", "Vẽ lại Hình 8.1–8.3 & Bảng 8.1 (tr. 146–152)"),
        "title": T("Plate 16 · Multi-Stage Probability Tree & Expected Value", "Bản vẽ 16 · Cây Xác suất Đa Tầng & Giá trị Kỳ vọng (EV)"),
        "say": T(
            "Probability trees enforce conservation of probability (Σ = 1.000) and turn fuzzy risk into explicit Expected Value.",
            "Cây xác suất giữ tổng khả năng bằng 1,000 ở mọi nút rẽ và biến cảm giác mơ hồ về rủi ro thành Giá trị kỳ vọng minh bạch."
        ),
        "rationale": T(
            "Replaces Word-drawn screenshots (Figs. 8.1–8.3) that captured red spellcheck squiggles under 'Lỗ' with crisp vector typography.",
            "Thay thế các ảnh chụp Word Hình 8.1–8.3 bị dính gạch chân đỏ kiểm tra chính tả dưới chữ “Lỗ” bằng sơ đồ vector chuẩn xuất bản."
        ),
        "svg": wrap_svg(900, 430, "Probability Tree and Expected Value", p16_body, standalone),
    })

    # =========================================================================
    # PLATE 17: BAYESIAN 1% BASE-RATE MEDICAL PARADOX (100-CELL VISUAL PROOF)
    # =========================================================================
    cells_svg = ""
    for r_i in range(10):
        for c_i in range(10):
            idx = r_i * 10 + c_i
            gx = 54 + c_i * 28
            gy = 104 + r_i * 28
            if idx == 0:
                fill_c, str_c = "#b81f2e", "#991b1b"  # 1 True Positive (~0.99)
            elif idx in (1, 2):
                fill_c, str_c = "#f59e0b", "#946200"  # 2 False Positives (~1.98)
            else:
                fill_c, str_c = "var(--surface-2, #eef1f8)", "var(--line-2, #cbd1e1)"
            cells_svg += f'<rect x="{gx}" y="{gy}" width="23" height="23" rx="4" fill="{fill_c}" stroke="{str_c}" stroke-width="1.2"/>'

    p17_body = f"""
    <rect x="24" y="20" width="852" height="396" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Why a 99%-Accurate Test Means Only a 33% Chance of Disease (pp. 154–155)", "Vì Sao Xét Nghiệm Chính Xác 99% Dương Tính Chỉ Có 33% Mắc Bệnh? (tr. 154–155)"))}</text>
    <text x="44" y="74" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Visualizing 100 random people when Base Rate P(b) = 1%, Sensitivity = 99%, False-Positive Rate = 2%.", "Hình dung 100 người bất kỳ khi Tỷ lệ mắc bệnh nền P(b) = 1%, Độ nhạy = 99%, Dương tính giả = 2%."))}</text>

    {cells_svg}
    <text x="190" y="402" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--ink-2, #4a4f6a)">{esc(T("100 Random People Screened", "100 Người Bất kỳ Đi Xét nghiệm"))}</text>

    <!-- Explanation & Formula (Right) -->
    <rect x="366" y="104" width="486" height="282" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#6835f0" stroke-width="1.8"/>
    <rect x="386" y="124" width="18" height="18" rx="4" fill="#b81f2e"/>
    <text x="414" y="138" font-size="12.5" font-weight="700" fill="var(--ink, #15172e)">{esc(T("1 Truly Sick Person → Tests Positive (0.99 ≈ 1 red square)", "1 Người Mắc bệnh Thật → Dương tính thật (0,99 ≈ 1 ô đỏ)"))}</text>

    <rect x="386" y="156" width="18" height="18" rx="4" fill="#f59e0b"/>
    <text x="414" y="170" font-size="12.5" font-weight="700" fill="var(--ink, #15172e)">{esc(T("2 Healthy People → False Positives! (99 × 2% = 1.98 ≈ 2 amber)", "2 Người Khỏe mạnh → Dương tính giả! (99 × 2% = 1,98 ≈ 2 ô vàng)"))}</text>

    <rect x="386" y="188" width="18" height="18" rx="4" fill="var(--surface, #ffffff)" stroke="var(--line-2, #cbd1e1)"/>
    <text x="414" y="202" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("97 Healthy People → True Negatives", "97 Người Khỏe mạnh → Âm tính thật"))}</text>

    <line x1="386" y1="222" x2="832" y2="222" stroke="var(--line-2, #cbd1e1)"/>
    <text x="386" y="250" class="mn" font-size="13" font-weight="800" fill="var(--c-prob, #6835f0)">P(b | d) = 0.0099 / (0.0099 + 0.0198) = 1 / 3 ≈ 33.3%</text>
    <text x="386" y="280" font-size="12" fill="var(--ink, #15172e)">{esc(T("• Out of ~3 people who get a positive slip, only 1 is truly sick (33%)!", "• Trong ~3 người nhận phiếu dương tính, chỉ có 1 người bệnh thật (33%)!"))}</text>
    <text x="386" y="304" font-size="12" fill="var(--ink, #15172e)">{esc(T("• If prevalence is 1 in 1,000 (0.001), true risk drops to just 3.3%!", "• Nếu tỷ lệ bệnh nền chỉ 1/1.000 (0,001), xác suất bệnh thật chỉ còn 3,3%!"))}</text>
    <text x="386" y="332" font-size="12" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("• Yet the test still matters: your risk rose 33× above the 1% prior!", "• Nhưng xét nghiệm vẫn rất giá trị: nguy cơ đã tăng gấp 33 lần mức nền 1%!"))}</text>
    <text x="386" y="362" font-size="11" font-style="italic" fill="var(--ink-2, #4a4f6a)">{esc(T("Never update beliefs without anchoring on Base Rate P(A) first.", "Bài học cốt tử: Không bao giờ quên Xác suất cơ sở P(A) khi cập nhật niềm tin."))}</text>
    """
    plates.append({
        "id": "p17",
        "slug": "17-bayesian-base-rate-grid",
        "ch": "Ch. 8",
        "manuscript_ref": T("New visual proof for Ch. 8 (pp. 154–155)", "Hình minh họa trực quan mới cho Chương 8 (tr. 154–155)"),
        "title": T("Plate 17 · The 100-Person Visual Proof of Bayes’ Theorem", "Bản vẽ 17 · Chứng minh Trực quan Định lý Bayes qua Lưới 100 Người"),
        "say": T(
            "Counting 1 red true-positive square beside 2 amber false-positive squares makes Bayes’ 33% medical result unforgettable without algebra anxiety.",
            "Nhìn trực tiếp 1 ô đỏ bệnh thật đặt cạnh 2 ô vàng dương tính giả giúp người đọc hiểu tức khắc con số 33% mà không sợ công thức toán."
        ),
        "rationale": T(
            "Addresses p. 156’s barrier #2 ('probability concepts are counter-intuitive') by turning conditional probability into natural frequencies.",
            "Giải quyết triệt để rào cản số 2 ở tr. 156 (“khái niệm xác suất không trực quan”) bằng phương pháp lưới tần suất tự nhiên."
        ),
        "svg": wrap_svg(900, 436, "Bayesian Base Rate 100-Person Grid", p17_body, standalone),
    })

    # =========================================================================
    # PLATE 18: GRAND SCIENTIFIC CONVERGENCE & EPILOGUE BIRD IN HAND (CH. 9 + EPILOGUE)
    # =========================================================================
    sci_steps = [
        ("1", T("Observe", "Quan sát"), T("Creative curiosity", "Sáng tạo")),
        ("2", T("Question", "Đặt câu hỏi"), T("Creative + Logical", "Sáng tạo + Logic")),
        ("3", T("Hypothesis", "Giả thuyết"), T("Falsifiable! (Popper)", "Có thể bác bỏ!")),
        ("4", T("Controlled Test", "Kiểm tra"), T("Aim to REFUTE · Systems/Strat.", "Nhằm BÁC BỎ · Hệ thống")),
        ("5", T("Analyze Data", "Phân tích"), T("Analytical + Probabilistic", "Phân tích + Xác suất")),
        ("6", T("Conclude", "Kết luận"), T("If refuted → loop to #3!", "Nếu sai → quay lại #3!")),
        ("7", T("Share / Peer Review", "Truyền thông"), T("Open community critique", "Đồng đẳng phản biện")),
    ]
    sc_svg = ""
    for i, (sn, stt, mth) in enumerate(sci_steps):
        sy = 92 + i * 44
        col = "#bd1e68" if sn in ("3", "4") else "#087087"
        sc_svg += f'<rect x="52" y="{sy}" width="416" height="36" rx="7" fill="var(--surface-2, #eef1f8)" stroke="{col}" stroke-width="1.6"/>'
        sc_svg += f'<rect x="52" y="{sy}" width="34" height="36" rx="7" fill="{col}"/>'
        sc_svg += f'<text x="69" y="{sy + 23}" text-anchor="middle" class="mn" font-size="11.5" font-weight="800" fill="#ffffff">{sn}</text>'
        sc_svg += f'<text x="98" y="{sy + 23}" font-size="12.5" font-weight="800" fill="var(--ink, #15172e)">{esc(stt)}</text>'
        sc_svg += f'<text x="456" y="{sy + 23}" text-anchor="end" font-size="11" font-weight="700" fill="{col}">{esc(mth)}</text>'

    p18_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="404" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Grand Synthesis: The Scientific Loop (p. 166) & The Bird in Your Hand (p. 171)", "Đỉnh Hội tụ Phương pháp Khoa học (tr. 166) & Con Chim Trong Tay Bạn (tr. 171)"))}</text>

    {sc_svg}
    <!-- Falsification Feedback Loop Arrow (#6 back to #3) -->
    <path d="M 468,330 L 504,330 L 504,198 L 474,198" fill="none" stroke="#b81f2e" stroke-width="2.2" marker-end="url(#arRed)"/>
    <text x="512" y="268" font-size="10.5" font-weight="800" fill="#b81f2e" transform="rotate(-90 512 268)">{esc(T("Refuted → Revise!", "Bị bác bỏ → Sửa giả thuyết!"))}</text>

    <!-- Epilogue Card (Right) -->
    <rect x="546" y="92" width="308" height="308" rx="12" fill="#0e1022" stroke="#2a2f52" stroke-width="2"/>
    <text x="700" y="124" text-anchor="middle" class="mn" font-size="10.5" letter-spacing="1.5" fill="#2fc7e6">{esc(T("EPILOGUE · PAGE 171", "LỜI KẾT · TRANG 171"))}</text>
    <text x="700" y="152" text-anchor="middle" class="hd" font-size="18" font-weight="700" fill="#f3f4fb">{esc(T("Alive or Dead?", "Chim Sống hay Chết?"))}</text>

    <g transform="translate(700, 226)">
      <circle cx="0" cy="-8" r="44" fill="rgba(47,199,230,0.10)" stroke="#2fc7e6" stroke-dasharray="3 3"/>
      <polygon points="-24,-6 10,-32 4,-2" fill="#2fc7e6"/>
      <polygon points="4,-2 10,-32 36,-16" fill="#5b8cff"/>
      <polygon points="-24,-6 4,-2 -10,12" fill="#ffd23f"/>
      <path d="M -62,28 Q -18,46 34,30 Q 58,22 72,8" fill="none" stroke="#d6daf0" stroke-width="2.6" stroke-linecap="round"/>
    </g>

    <text x="700" y="298" text-anchor="middle" font-size="12" font-style="italic" fill="#d6daf0">{esc(T("“The book decides nothing for you.", "“Cuốn sách không quyết định điều gì thay bạn."))}</text>
    <text x="700" y="318" text-anchor="middle" font-size="12" font-style="italic" fill="#d6daf0">{esc(T("Whether the bird lives or dies", "Con chim sống hay chết"))}</text>
    <text x="700" y="338" text-anchor="middle" font-size="12.5" font-weight="700" fill="#2fc7e6">{esc(T("lies in your hands.”", "nằm trong tay bạn.”"))}</text>
    <text x="700" y="374" text-anchor="middle" font-size="11" fill="#8d93b3">{esc(T("Practice thinking → Escape suffering", "Thực hành tư duy → Thành công & Thoát khổ"))}</text>
    """
    plates.append({
        "id": "p18",
        "slug": "18-scientific-convergence-epilogue",
        "ch": "Ch. 9 & Epilogue",
        "manuscript_ref": T("Upgrades Fig. 9.1 (p. 166) + Epilogue (p. 171)", "Nâng cấp Hình 9.1 (tr. 166) + Minh họa Lời kết (tr. 171)"),
        "title": T("Plate 18 · The 7-Step Scientific Convergence & The Bird in Your Hand", "Bản vẽ 18 · Vòng Hội tụ Khoa học 7 Bước & Ẩn dụ Con Chim Trong Tay"),
        "say": T(
            "Every method in the book converges inside the falsifiable loop of Science—and comes alive only when practiced by the reader’s own hands.",
            "Cả 8 phương pháp hội tụ trọn vẹn trong chu trình kiểm chứng khoa học—và chỉ thực sự sống dậy khi bạn tự mình thực hành mỗi ngày."
        ),
        "rationale": T(
            "Upgrades Fig. 9.1’s plain Word boxes by mapping which thinking method powers each scientific step, paired with the closing parable plate.",
            "Nâng cấp sơ đồ khối Hình 9.1 bằng cách gắn rõ các phương pháp tư duy vào từng bước khoa học, đặt cạnh bản vẽ kết sách đầy dư âm."
        ),
        "svg": wrap_svg(900, 444, "Scientific Convergence and Epilogue Bird", p18_body, standalone),
    })

    # =========================================================================
    # PLATE 19: STORY ILLUSTRATION — COILED ROPE IN GRASS & 3-SHOP SHIRT ANCHOR
    # =========================================================================
    p19_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="380" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <!-- Left Scene: Dusk Grass Coil (Survival Reflex) -->
    <rect x="44" y="42" width="390" height="336" rx="10" fill="#171a33" stroke="#2a2f52" stroke-width="1.5"/>
    <text x="64" y="72" class="mn" font-size="11.5" font-weight="700" fill="#2fc7e6">{esc(T("STORY I · CH. 1 (p. 12)", "CHUYỆN KỂ I · CHƯƠNG 1 (tr. 12)"))}</text>
    <text x="64" y="98" class="hd" font-size="18" font-weight="700" fill="#f3f4fb">{esc(T("The Dark Coil at Dusk", "Vật Đen Loằn Ngoằn Trong Bóng Chiều"))}</text>
    <!-- Moon & grass blades -->
    <circle cx="384" cy="84" r="20" fill="#fef08a" opacity="0.85"/>
    <path d="M 60,296 Q 72,250 82,296 M 92,296 Q 100,242 112,296 M 330,296 Q 344,248 354,296 M 364,296 Q 378,255 388,296" fill="none" stroke="#2a2f52" stroke-width="2.2"/>
    <line x1="56" y1="296" x2="416" y2="296" stroke="#3a4070" stroke-width="2"/>
    <!-- Coiled rope looking like a viper -->
    <path d="M 164,282 C 194,256 254,256 270,278 C 284,296 200,300 214,272 C 224,252 276,254 294,264" fill="none" stroke="#ff5c6a" stroke-width="7" stroke-linecap="round"/>
    <circle cx="297" cy="264" r="4" fill="#fef08a"/>
    <!-- Jump trajectory arc -->
    <path d="M 148,268 Q 104,170 76,228" fill="none" stroke="#5b8cff" stroke-width="2.5" stroke-dasharray="5 3" marker-end="url(#arTeal)"/>
    <text x="72" y="168" font-size="12" font-weight="700" fill="#93a0ff">{esc(T("System 1 leaps in 0.2s!", "Hệ thống 1 nhảy vọt sau 0,2 giây!"))}</text>
    <text x="64" y="330" font-size="12" fill="#b3b8d3">{esc(T("Saves your life in the jungle—when ‘false alarm’ beats venom.", "Cứu mạng nơi rừng rậm—thà nhầm dây thừng còn hơn rắn cắn."))}</text>
    <text x="64" y="352" font-size="12" font-weight="700" fill="#ff7a86">{esc(T("Yet fails catastrophically on modern pricing & contracts →", "Nhưng lại sập bẫy ngay giữa phố thị hiện đại →"))}</text>

    <!-- Right Scene: Three Shirt Shops Street (Anchoring Trap p. 15) -->
    <rect x="456" y="42" width="398" height="336" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line-2, #cbd1e1)"/>
    <text x="476" y="72" class="mn" font-size="11.5" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("STORY II · CH. 1 (pp. 15–16)", "CHUYỆN KỂ II · CHƯƠNG 1 (tr. 15–16)"))}</text>
    <text x="476" y="98" class="hd" font-size="18" font-weight="700" fill="var(--ink, #15172e)">{esc(T("The Three Shirt Shops & The 1,000k Anchor", "Ba Cửa Hiệu Áo Sơ-mi & Cái Cọc 1 Triệu"))}</text>

    <!-- 3 Shop awnings -->
    <rect x="476" y="126" width="112" height="136" rx="8" fill="var(--surface, #ffffff)" stroke="#b81f2e" stroke-width="2"/>
    <path d="M 476,148 L 588,148" stroke="#b81f2e" stroke-width="2"/>
    <text x="532" y="142" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("SHOP 1 · ANCHOR", "TIỆM 1 · MỎ NEO"))}</text>
    <text x="532" y="192" text-anchor="middle" class="hd" font-size="20" font-weight="800" fill="var(--ink, #15172e)">1,000k</text>
    <text x="532" y="216" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Drops first number", "Đóng cọc giá đầu"))}</text>
    <text x="532" y="242" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("“Too pricey”", "“Hơi đắt, đi tiếp”"))}</text>

    <rect x="600" y="126" width="112" height="136" rx="8" fill="rgba(229,51,63,0.09)" stroke="#b81f2e" stroke-width="2.4"/>
    <path d="M 600,148 L 712,148" stroke="#b81f2e" stroke-width="2"/>
    <text x="656" y="142" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("SHOP 2 · TRAP!", "TIỆM 2 · SẬP BẪY!"))}</text>
    <text x="656" y="192" text-anchor="middle" class="hd" font-size="20" font-weight="800" fill="var(--c-trap, #b81f2e)">900k</text>
    <text x="656" y="216" text-anchor="middle" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("Feels −100k cheap!", "Tưởng rẻ được 100k!"))}</text>
    <text x="656" y="242" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("System 1 Buys!", "Mua vội ngay!"))}</text>

    <rect x="724" y="126" width="112" height="136" rx="8" fill="rgba(13,148,136,0.1)" stroke="#0d9488" stroke-width="2" stroke-dasharray="5 3"/>
    <path d="M 724,148 L 836,148" stroke="#0d9488" stroke-width="2"/>
    <text x="780" y="142" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-analytical, #0b7268)">{esc(T("SHOP 3 · MISSED", "TIỆM 3 · BỎ LỠ"))}</text>
    <text x="780" y="192" text-anchor="middle" class="hd" font-size="20" font-weight="800" fill="var(--c-analytical, #0b7268)">800k</text>
    <text x="780" y="216" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("True market value", "Giá chuẩn thị trường"))}</text>
    <text x="780" y="242" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-analytical, #0b7268)">{esc(T("Never checked", "Chưa kịp bước tới"))}</text>

    <text x="476" y="302" font-size="12.5" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Lesson: Anchors turn a 100k overpayment into a ‘bargain’.", "Bài học: Mỏ neo đầu tiên biến cái giá đắt hơn 100 ngàn thành ‘món hời’."))}</text>
    <text x="476" y="326" font-size="12" fill="var(--ink-2, #4a4f6a)">{esc(T("Survey independent benchmarks (Ch. 4) before judging any single quote.", "Luôn khảo sát mặt bằng độc lập (Chương 4) trước khi tin vào con số đầu tiên."))}</text>
    """
    plates.append({
        "id": "p19",
        "slug": "19-story-snake-coil-and-shirt-anchor",
        "ch": "Ch. 1 Story",
        "manuscript_ref": T("Narrative Plate for Ch. 1 (pp. 12–16)", "Tranh Kể chuyện Chương 1 (tr. 12–16)"),
        "title": T("Plate 19 · Story Vignette: The Dusk Coil & The Three Shirt Shops", "Bản vẽ 19 · Minh họa Chuyện kể: Vật Đen Trong Cỏ & Ba Cửa Hiệu Áo Sơ-mi"),
        "say": T(
            "The exact survival reflex that leaps away from a rope in dusk grass gets tricked ten minutes later by a 1,000k price tag.",
            "Chính phản xạ nhảy vọt cứu mạng trước sợi dây thừng trong cỏ tối lại dễ dàng bị lừa mười phút sau trước tấm bảng giá 1 triệu đồng."
        ),
        "rationale": T(
            "Pairs the book’s two vivid opening parables side-by-side to show why System 1 is evolutionary genius in nature yet costly in modern life.",
            "Đặt song song hai câu chuyện mở đầu sống động nhất của Chương 1 để thấy sự đối lập giữa bản năng sinh tồn và bẫy thị trường hiện đại."
        ),
        "svg": wrap_svg(900, 420, "Dusk Coil and Three Shirt Shops", p19_body, standalone),
    })

    # =========================================================================
    # PLATE 20: STORY ILLUSTRATION — ARCHIMEDES, ZERO-G PEN & BARRY MARSHALL
    # =========================================================================
    p20_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="380" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Three Stories of Reframing: Breaking Hidden Assumptions (Ch. 2, pp. 27–29)", "Ba Câu chuyện Định nghĩa lại Vấn đề: Phá Vỡ Giả định Ngầm (Chương 2, tr. 27–29)"))}</text>

    <!-- Panel 1: Archimedes -->
    <rect x="44" y="76" width="264" height="298" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#946200" stroke-width="1.8"/>
    <text x="62" y="104" font-size="12" font-weight="800" fill="var(--c-creative, #946200)">{esc(T("1 · ARCHIMEDES’ SPHERE", "1 · MẶT CẦU ARCHIMEDES"))}</text>
    <line x1="176" y1="122" x2="176" y2="254" stroke="var(--ink-3, #656b87)" stroke-width="1.8" stroke-dasharray="4 3"/>
    <circle cx="176" cy="188" r="52" fill="rgba(245,158,11,0.12)" stroke="#946200" stroke-width="2.2"/>
    <ellipse cx="176" cy="188" rx="52" ry="18" fill="none" stroke="#0d9488" stroke-width="1.8" stroke-dasharray="4 3"/>
    <ellipse cx="176" cy="188" rx="22" ry="52" fill="none" stroke="#946200" stroke-width="1.6"/>
    <path d="M 152,126 C 172,114 196,114 202,128" fill="none" stroke="#0d9488" stroke-width="2" marker-end="url(#arTeal)"/>
    <text x="176" y="282" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink, #15172e)">{esc(T("2D Circle + Rotation = 3D Sphere", "Hình tròn 2D quay quanh đường kính"))}</text>
    <text x="176" y="304" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Dynamic generative definition", "Định nghĩa động mở ra hình học mới"))}</text>
    <text x="176" y="344" text-anchor="middle" class="mn" font-size="11.5" fill="var(--c-analytical, #0b7268)">{esc(T("+ Kapitsa: Stillness is motion at v = 0", "+ Kapitsa: Đứng yên là chuyển động v = 0"))}</text>

    <!-- Panel 2: Space Pen vs Writing Tool -->
    <rect x="328" y="76" width="264" height="298" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#0d9488" stroke-width="1.8"/>
    <text x="346" y="104" font-size="12" font-weight="800" fill="var(--c-analytical, #0b7268)">{esc(T("2 · ZERO-GRAVITY ORBIT", "2 · BÚT VIẾT KHÔNG TRỌNG LỰC"))}</text>
    <rect x="348" y="128" width="224" height="58" rx="8" fill="rgba(229,51,63,0.09)" stroke="#b81f2e"/>
    <text x="460" y="150" text-anchor="middle" font-size="12" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("Narrow Frame: ‘Ballpoint Ink Pen’", "Khung hẹp: ‘Làm bút bi chảy mực’"))}</text>
    <text x="460" y="171" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Locks mind inside pressurized ink", "Trói tư duy vào ống mực nén khí tốn kém"))}</text>
    <line x1="460" y1="190" x2="460" y2="214" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arTeal)"/>
    <rect x="348" y="220" width="224" height="72" rx="8" fill="rgba(13,148,136,0.12)" stroke="#0d9488" stroke-width="2"/>
    <text x="460" y="244" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-analytical, #0b7268)">{esc(T("Wider Frame: ‘Zero-G Writing Tool’", "Khung rộng: ‘Dụng cụ viết trên vũ trụ’"))}</text>
    <text x="460" y="268" text-anchor="middle" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("Unlocks grease pencils, styluses, dry media", "Mở ra bút chì sáp, bút khô, bảng cảm ứng"))}</text>
    <text x="460" y="344" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--ink-2, #4a4f6a)">{esc(T("Never bake an old tool into the question", "Đừng gài sẵn công cụ cũ vào câu hỏi"))}</text>

    <!-- Panel 3: Marshall & Warren Nobel Ulcer Story -->
    <rect x="612" y="76" width="244" height="298" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#bd1e68" stroke-width="1.8"/>
    <text x="630" y="104" font-size="12" font-weight="800" fill="var(--c-science, #bd1e68)">{esc(T("3 · NOBEL ULCER DOGMA", "3 · GIẢI NOBEL VI KHUẨN DẠ DÀY"))}</text>
    <!-- Beaker / Flask illustration -->
    <path d="M 716,132 L 752,132 M 724,132 L 724,162 L 694,220 Q 688,234 704,234 L 764,234 Q 780,234 774,220 L 744,162 L 744,132" fill="rgba(190,24,93,0.12)" stroke="#bd1e68" stroke-width="2.4"/>
    <path d="M 702,208 Q 734,200 766,208 L 772,222 Q 776,230 764,230 L 704,230 Q 692,230 696,222 Z" fill="#f472b6" opacity="0.55"/>
    <circle cx="724" cy="218" r="3" fill="#bd1e68"/><circle cx="742" cy="222" r="3" fill="#bd1e68"/><circle cx="734" cy="212" r="2.5" fill="#bd1e68"/>
    <text x="734" y="264" text-anchor="middle" font-size="12" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("Old Dogma: ‘Acid kills all bacteria’", "Định kiến cũ: ‘Axit diệt mọi vi khuẩn’"))}</text>
    <text x="734" y="288" text-anchor="middle" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("Marshall drank H. pylori culture,", "Bác sĩ Marshall tự uống vi khuẩn HP,"))}</text>
    <text x="734" y="308" text-anchor="middle" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("got gastritis, cured it with antibiotics!", "chứng minh loét dạ dày chữa khỏi bằng"))}</text>
    <text x="734" y="344" text-anchor="middle" font-size="12" font-weight="800" fill="var(--c-science, #bd1e68)">{esc(T("2005 Nobel Prize in Medicine", "kháng sinh → Giải Nobel Y học 2005!"))}</text>
    """
    plates.append({
        "id": "p20",
        "slug": "20-story-archimedes-space-pen-marshall",
        "ch": "Ch. 2 Story",
        "manuscript_ref": T("Narrative Plate for Ch. 2 (pp. 27–29)", "Tranh Kể chuyện Chương 2 (tr. 27–29)"),
        "title": T("Plate 20 · Story Triptych: Archimedes’ Sphere, Zero-G Writing & Marshall’s Flask", "Bản vẽ 20 · Bộ ba Chuyện kể Sáng tạo: Mặt cầu, Bút Vũ trụ & Cốc Vi khuẩn HP"),
        "say": T(
            "Breakthroughs begin not by brainstorming harder inside an old box, but by shattering the false assumption hidden inside the question.",
            "Đột phá sáng tạo bắt đầu không phải bằng cách cố nghĩ thêm giải pháp trong chiếc hộp cũ, mà bằng cách đập vỡ giả định sai đang trói câu hỏi."
        ),
        "rationale": T(
            "Brings Chapter 2’s three historical vignettes to life as a memorable visual triptych.",
            "Chuyển thể 3 giai thoại khoa học nổi bật nhất ở đầu Chương 2 thành bức tranh ba ngăn giàu sức gợi."
        ),
        "svg": wrap_svg(900, 420, "Three Stories of Creative Reframing", p20_body, standalone),
    })

    # =========================================================================
    # PLATE 21: STORY ILLUSTRATION — TAIICHI OHNO'S 5-WHYS FACTORY ROBOT
    # =========================================================================
    p21_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="360" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Taiichi Ohno’s Toyota Shop-Floor Story: Drilling 5 Whys Past the Fuse (Ch. 4, p. 76)", "Chuyện Xưởng Toyota của Taiichi Ohno: Khoan 5 Câu Hỏi Tại Sao Tới Tận Lưới Lọc (Chương 4, tr. 76)"))}</text>
    <text x="44" y="74" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Replacing the blown fuse restarts the robot in 5 minutes—and guarantees it breaks again tomorrow.", "Chỉ thay cầu chì mới giúp máy chạy lại sau 5 phút—nhưng chắc chắn ngày mai máy lại cháy tiếp."))}</text>

    <!-- 5 Connected Mechanical Stations -->
    <rect x="44" y="112" width="144" height="148" rx="10" fill="rgba(229,51,63,0.09)" stroke="#b81f2e" stroke-width="2"/>
    <text x="116" y="138" text-anchor="middle" class="mn" font-size="11.5" font-weight="800" fill="var(--c-trap, #b81f2e)">WHY 1 · SYMPTOM</text>
    <text x="116" y="166" text-anchor="middle" font-size="14" font-weight="800" fill="var(--ink, #15172e)">{esc(T("Blown Fuse", "Đứt Cầu Chì"))}</text>
    <text x="116" y="192" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Motor overloaded", "Động cơ bị quá tải"))}</text>
    <text x="116" y="236" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-trap, #b81f2e)">{esc(T("✗ Lazy fix stops here", "✗ Chữa cháy dừng ở đây"))}</text>

    <line x1="188" y1="186" x2="210" y2="186" stroke="var(--ink-2, #4a4f6a)" stroke-width="2.2" marker-end="url(#arInk)"/>

    <rect x="214" y="112" width="144" height="148" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line-2, #cbd1e1)" stroke-width="1.8"/>
    <text x="286" y="138" text-anchor="middle" class="mn" font-size="11.5" font-weight="800" fill="var(--ink-2, #4a4f6a)">WHY 2</text>
    <text x="286" y="166" text-anchor="middle" font-size="14" font-weight="800" fill="var(--ink, #15172e)">{esc(T("Seized Bearing", "Khô Vòng Bi"))}</text>
    <text x="286" y="192" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Insufficient oil", "Thiếu dầu bôi trơn"))}</text>
    <text x="286" y="212" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("at high friction", "khi quay tốc độ cao"))}</text>

    <line x1="358" y1="186" x2="380" y2="186" stroke="var(--ink-2, #4a4f6a)" stroke-width="2.2" marker-end="url(#arInk)"/>

    <rect x="384" y="112" width="144" height="148" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line-2, #cbd1e1)" stroke-width="1.8"/>
    <text x="456" y="138" text-anchor="middle" class="mn" font-size="11.5" font-weight="800" fill="var(--ink-2, #4a4f6a)">WHY 3</text>
    <text x="456" y="166" text-anchor="middle" font-size="14" font-weight="800" fill="var(--ink, #15172e)">{esc(T("Weak Oil Pump", "Bơm Dầu Yếu"))}</text>
    <text x="456" y="192" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Pump shaft worn", "Bơm không hút đủ"))}</text>
    <text x="456" y="212" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("and sputtering", "lưu lượng thiết kế"))}</text>

    <line x1="528" y1="186" x2="550" y2="186" stroke="var(--ink-2, #4a4f6a)" stroke-width="2.2" marker-end="url(#arInk)"/>

    <rect x="554" y="112" width="144" height="148" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line-2, #cbd1e1)" stroke-width="1.8"/>
    <text x="626" y="138" text-anchor="middle" class="mn" font-size="11.5" font-weight="800" fill="var(--ink-2, #4a4f6a)">WHY 4</text>
    <text x="626" y="166" text-anchor="middle" font-size="14" font-weight="800" fill="var(--ink, #15172e)">{esc(T("Clogged Intake", "Kẹt Vụn Kim Loại"))}</text>
    <text x="626" y="192" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Metal shavings", "Mạt sắt lọt thẳng"))}</text>
    <text x="626" y="212" text-anchor="middle" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("jammed inside", "vào ống hút dầu"))}</text>

    <line x1="698" y1="186" x2="720" y2="186" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arTeal)"/>

    <rect x="724" y="106" width="132" height="160" rx="10" fill="rgba(13,148,136,0.14)" stroke="#0d9488" stroke-width="2.6"/>
    <text x="790" y="134" text-anchor="middle" class="mn" font-size="11.5" font-weight="800" fill="var(--c-analytical, #0b7268)">WHY 5 · ROOT!</text>
    <text x="790" y="164" text-anchor="middle" font-size="14.5" font-weight="800" fill="var(--c-analytical, #0b7268)">{esc(T("No Strainer!", "Thiếu Lưới Lọc!"))}</text>
    <text x="790" y="192" text-anchor="middle" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("Install $2 mesh", "Lắp bộ lọc đầu vào"))}</text>
    <text x="790" y="212" text-anchor="middle" font-size="11.5" fill="var(--ink, #15172e)">{esc(T("→ Permanent cure", "→ Trị dứt điểm gốc rễ"))}</text>
    <text x="790" y="244" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-analytical, #0b7268)">{esc(T("✓ Verified Root", "✓ Gốc rễ đã kiểm chứng"))}</text>

    <text x="450" y="318" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Rule (p. 77): At every ‘Why’, verify empirically on the floor—never invent armchair guesses!", "Nguyên tắc vàng (tr. 77): Mỗi bước ‘Tại sao’ đều phải kiểm chứng thực tế tại hiện trường, tuyệt đối không đoán mò!"))}</text>
    """
    plates.append({
        "id": "p21",
        "slug": "21-story-ohno-toyota-five-whys",
        "ch": "Ch. 4 Story",
        "manuscript_ref": T("Narrative Plate for Ch. 4 (pp. 76–77)", "Tranh Kể chuyện Chương 4 (tr. 76–77)"),
        "title": T("Plate 21 · Story Cutaway: Taiichi Ohno’s Halted Robot & The Missing Strainer", "Bản vẽ 21 · Chuyện kể Xưởng Toyota: Cỗ Máy Dừng Đột Ngột & Chiếc Lưới Lọc Bị Quên"),
        "say": T(
            "Fixing Why #1 (the fuse) treats the loud symptom; drilling empirically to Why #5 (the missing strainer) cures the machine forever.",
            "Thay cầu chì ở Tại sao #1 chỉ dập phần ngọn; khoan thực chứng tới Tại sao #5 (thiếu lưới lọc) mới chữa lành hệ thống vĩnh viễn."
        ),
        "rationale": T(
            "Turns p. 76’s classic Toyota factory dialogue into a sequential mechanical cutaway.",
            "Chuyển đoạn đối thoại kinh điển tại xưởng máy Toyota (tr. 76) thành chuỗi mặt cắt kỹ thuật trực quan."
        ),
        "svg": wrap_svg(900, 400, "Taiichi Ohno Five Whys Cutaway", p21_body, standalone),
    })

    # =========================================================================
    # PLATE 22: STORY ILLUSTRATION — THE SAVANNA PENDULUM (LIONS, GAZELLES, GRASS)
    # =========================================================================
    p22_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="380" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <text x="44" y="52" class="hd" font-size="19" font-weight="700" fill="var(--ink, #15172e)">{esc(T("The Savanna Ecosystem Story: Why ‘Saving’ Gazelles Starved the Herd (Ch. 6, pp. 114, 122)", "Chuyện Hệ Sinh Thái Đồng Cỏ: Vì Sao ‘Cứu’ Linh Dương Lại Khiến Cả Đàn Chết Đói (Chương 6, tr. 114, 122)"))}</text>
    <text x="44" y="74" font-size="12.5" fill="var(--ink-2, #4a4f6a)">{esc(T("Linear thinking sees predator vs. prey; Systems thinking sees the delayed balancing web keeping the prairie alive.", "Tư duy tuyến tính chỉ thấy thú dữ ăn thịt con mồi; Tư duy hệ thống thấy vòng cân bằng có độ trễ giữ đồng cỏ xanh tươi."))}</text>

    <!-- Left Ecological Web -->
    <rect x="44" y="96" width="388" height="276" rx="10" fill="var(--surface-2, #eef1f8)" stroke="#0b7547" stroke-width="1.8"/>
    <circle cx="238" cy="146" r="36" fill="rgba(229,51,63,0.12)" stroke="#b81f2e" stroke-width="2"/>
    <text x="238" y="144" text-anchor="middle" font-size="13" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("Lions", "Sư tử"))}</text>
    <text x="238" y="162" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Predators", "Thú săn mồi"))}</text>

    <circle cx="128" cy="286" r="38" fill="rgba(217,119,6,0.14)" stroke="#946200" stroke-width="2"/>
    <text x="128" y="284" text-anchor="middle" font-size="13" font-weight="800" fill="var(--c-creative, #946200)">{esc(T("Gazelles", "Linh dương"))}</text>
    <text x="128" y="302" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Herbivores", "Đàn ăn cỏ"))}</text>

    <circle cx="348" cy="286" r="38" fill="rgba(21,128,61,0.14)" stroke="#0b7547" stroke-width="2"/>
    <text x="348" y="284" text-anchor="middle" font-size="13" font-weight="800" fill="var(--c-systems, #0b7547)">{esc(T("Grassland", "Thảm cỏ"))}</text>
    <text x="348" y="302" text-anchor="middle" font-size="11" fill="var(--ink-2, #4a4f6a)">{esc(T("Carrying Base", "Nguồn thức ăn"))}</text>

    <path d="M 206,168 Q 148,205 138,246" fill="none" stroke="#0b7547" stroke-width="2.2" marker-end="url(#arGreen)"/>
    <text x="148" y="204" font-size="11.5" font-weight="800" fill="var(--c-systems, #0b7547)">− (B1)</text>
    <path d="M 166,286 L 306,286" fill="none" stroke="#b81f2e" stroke-width="2.2" marker-end="url(#arRed)"/>
    <text x="238" y="276" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("Overgrazing − //", "Ăn trụi cỏ − //"))}</text>
    <path d="M 332,250 Q 308,192 272,162" fill="none" stroke="#0d9488" stroke-width="1.8" stroke-dasharray="4 3" marker-end="url(#arTeal)"/>
    <text x="238" y="352" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Emergence: Health belongs to the whole loop", "Tính hợp trội: Sức sống nằm ở toàn mạng lưới"))}</text>

    <!-- Right Delayed Collapse Wave -->
    <rect x="456" y="96" width="398" height="276" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line-2, #cbd1e1)"/>
    <text x="476" y="124" font-size="13" font-weight="800" fill="var(--ink, #15172e)">{esc(T("When Humans Wipe Out Predators at t = 1:", "Khi Con Người Diệt Hết Thú Săn Mồi Ở t = 1:"))}</text>
    <line x1="484" y1="306" x2="828" y2="306" stroke="var(--ink-3, #656b87)" stroke-width="1.6"/>
    <line x1="484" y1="144" x2="484" y2="306" stroke="var(--ink-3, #656b87)" stroke-width="1.6"/>
    <!-- Gazelle boom & bust -->
    <path d="M 488,256 C 530,254 560,150 612,152 C 664,154 700,294 820,298" fill="none" stroke="#946200" stroke-width="3.2"/>
    <!-- Grass collapse -->
    <path d="M 488,186 C 540,186 585,220 645,282 C 690,302 750,302 820,300" fill="none" stroke="#0b7547" stroke-width="2.4" stroke-dasharray="5 3"/>
    <text x="612" y="144" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-creative, #946200)">{esc(T("Gazelle Boom!", "Đàn bùng nổ!"))}</text>
    <text x="742" y="274" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("Grass Gone → Mass Famine", "Đất trơ trụi → Đói hàng loạt"))}</text>
    <text x="656" y="346" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink-2, #4a4f6a)">{esc(T("Senge’s Law #1 & #3: Today’s problems come from yesterday’s ‘solutions’", "Định luật Senge: Vấn đề hôm nay bắt nguồn từ chính ‘giải pháp’ hôm qua"))}</text>
    """
    plates.append({
        "id": "p22",
        "slug": "22-story-savanna-lions-gazelles-delay",
        "ch": "Ch. 6 Story",
        "manuscript_ref": T("Narrative Plate for Ch. 6 (pp. 114, 122)", "Tranh Kể chuyện Chương 6 (tr. 114, 122)"),
        "title": T("Plate 22 · Ecological Parable: Lions, Gazelles & Delayed Overshoot", "Bản vẽ 22 · Ngụ ngôn Sinh thái: Sư tử, Linh dương & Cú Sập Do Độ Trễ"),
        "say": T(
            "Removing a balancing constraint triggers euphoric short-term growth followed by catastrophic resource collapse.",
            "Xóa sổ vòng cân bằng tự nhiên tạo ra cơn bùng nổ ngắn hạn rồi dẫn tới sự sụp đổ toàn diện của nguồn sống."
        ),
        "rationale": T(
            "Illustrates Chapter 6’s savanna ecosystem example in the classic natural-history spirit of Systema Intelligentiae.",
            "Minh họa câu chuyện đồng cỏ Chương 6 theo phong cách bản vẽ tự nhiên học kinh điển."
        ),
        "svg": wrap_svg(900, 420, "Savanna Lions Gazelles and Grassland Loop", p22_body, standalone),
    })

    # =========================================================================
    # PLATE 23: STORY ILLUSTRATION — KAHNEMAN'S MIDNIGHT HIT-AND-RUN CAB (P. 157)
    # =========================================================================
    p23_body = f"""
    <rect x="24" y="20" width="852" height="380" rx="12" fill="var(--surface, #ffffff)" stroke="var(--line, #e1e5f0)"/>
    <!-- Left Noir Scene -->
    <rect x="44" y="42" width="376" height="336" rx="10" fill="#0e1022" stroke="#2a2f52" stroke-width="1.6"/>
    <text x="64" y="72" class="mn" font-size="11.5" font-weight="700" fill="#a07fff">{esc(T("CHAPTER 8 MYSTERY · PAGE 157", "BÀI TOÁN TRINH THÁM CHƯƠNG 8 · TRANG 157"))}</text>
    <text x="64" y="98" class="hd" font-size="18" font-weight="700" fill="#f3f4fb">{esc(T("The Midnight Hit-and-Run Witness", "Nhân Chứng Đêm Mưa & Chiếc Taxi Gây Tai Nạn"))}</text>
    <!-- Streetlamp cone of light -->
    <polygon points="224,118 112,296 336,296" fill="rgba(250,204,21,0.12)"/>
    <circle cx="224" cy="118" r="8" fill="#fde047"/>
    <!-- Cab silhouette -->
    <rect x="168" y="246" width="112" height="34" rx="8" fill="#5b8cff" opacity="0.85"/>
    <path d="M 186,246 L 202,224 L 250,224 L 266,246 Z" fill="#f43f5e" opacity="0.75"/>
    <circle cx="192" cy="282" r="10" fill="#b3b8d3"/><circle cx="256" cy="282" r="10" fill="#b3b8d3"/>
    <text x="224" y="268" text-anchor="middle" class="mn" font-size="11.5" font-weight="800" fill="#0e1022">{esc(T("GREEN or RED?", "XANH hay ĐỎ?"))}</text>
    <text x="64" y="326" font-size="12" fill="#d6daf0">{esc(T("• City fleet: 60% Green cabs, 40% Red cabs (p. 157)", "• Thành phố có: 60% Taxi Xanh, 40% Taxi Đỏ (tr. 157)"))}</text>
    <text x="64" y="348" font-size="12" fill="#b3b8d3">{esc(T("• Dusk witness accuracy: 85% right, 15% color mix-up", "• Nhân chứng nhìn đúng màu 85%, nhìn nhầm 15%"))}</text>
    <text x="64" y="368" font-size="12" font-weight="700" fill="#ff7a86">{esc(T("Witness testifies: ‘The cab was RED!’", "Nhân chứng khai: ‘Chiếc xe bỏ chạy màu ĐỎ!’"))}</text>

    <!-- Right Bayes Breakdown -->
    <rect x="440" y="42" width="414" height="336" rx="10" fill="var(--surface-2, #eef1f8)" stroke="var(--line-2, #cbd1e1)"/>
    <text x="462" y="74" class="hd" font-size="17" font-weight="700" fill="var(--ink, #15172e)">{esc(T("Book Exercise Question: P(Actually Green | ‘Red’)?", "Câu hỏi Bài tập Sách: Xác suất Xe Thật Là XANH?"))}</text>
    <rect x="462" y="96" width="370" height="72" rx="8" fill="rgba(16,185,129,0.12)" stroke="#0d9488" stroke-width="1.8"/>
    <text x="478" y="122" font-size="12.5" font-weight="800" fill="var(--c-analytical, #0b7268)">{esc(T("Branch 1: Cab was GREEN (0.60) × Misread as ‘Red’ (0.15)", "Nhánh 1: Xe thật là XANH (0,60) × Nhìn nhầm thành ‘Đỏ’ (0,15)"))}</text>
    <text x="478" y="148" class="mn" font-size="13.5" font-weight="800" fill="var(--ink, #15172e)">0.60 × 0.15 = 0.090 (9.0% of all cases)</text>

    <rect x="462" y="182" width="370" height="72" rx="8" fill="rgba(229,51,63,0.1)" stroke="#b81f2e" stroke-width="1.8"/>
    <text x="478" y="208" font-size="12.5" font-weight="800" fill="var(--c-trap, #b81f2e)">{esc(T("Branch 2: Cab was RED (0.40) × Seen rightly as ‘Red’ (0.85)", "Nhánh 2: Xe thật là ĐỎ (0,40) × Nhìn đúng là ‘Đỏ’ (0,85)"))}</text>
    <text x="478" y="234" class="mn" font-size="13.5" font-weight="800" fill="var(--ink, #15172e)">0.40 × 0.85 = 0.340 (34.0% of all cases)</text>

    <rect x="462" y="270" width="370" height="90" rx="8" fill="var(--surface, #ffffff)" stroke="#6835f0" stroke-width="2.2"/>
    <text x="478" y="296" font-size="12.5" font-weight="700" fill="var(--c-prob, #6835f0)">{esc(T("Bayes’ Posterior for Green = 0.09 / (0.09 + 0.34):", "Định lý Bayes cho Xe Xanh = 0,09 / (0,09 + 0,34):"))}</text>
    <text x="478" y="324" class="hd" font-size="22" font-weight="800" fill="var(--c-prob, #6835f0)">{esc(T("20.9% Green  (79.1% Red — NOT 85%!)", "20,9% là Taxi Xanh  (chứ không phải chỉ 15%!)"))}</text>
    <text x="478" y="348" font-size="11.5" fill="var(--ink-2, #4a4f6a)">{esc(T("And if Green cabs are 85% of town (Kahneman), ‘Red’ is wrong 41% of the time!", "Nếu Taxi Xanh chiếm 85% thành phố (Kahneman), lời khai ‘Đỏ’ sai tới 41%!"))}</text>
    """
    plates.append({
        "id": "p23",
        "slug": "23-story-midnight-taxi-bayes-mystery",
        "ch": "Ch. 8 Story",
        "manuscript_ref": T("Illustrates Exercise #3 (p. 157)", "Minh họa Bài tập #3 Taxi Xanh – Đỏ (tr. 157)"),
        "title": T("Plate 23 · Detective Vignette: The Midnight Hit-and-Run Cab Paradox", "Bản vẽ 23 · Chuyện kể Trinh thám: Vụ Tai Nạn Lúc Chạng Vạng & Chiếc Taxi Xanh – Đỏ"),
        "say": T(
            "Eyewitness testimony never stands alone—its true weight shifts dramatically with the city’s underlying fleet base rate.",
            "Lời khai nhân chứng không bao giờ đứng độc lập—độ tin cậy thực sự của nó phụ thuộc chặt chẽ vào tỷ lệ nền của đội xe trong thành phố."
        ),
        "rationale": T(
            "Solves and illustrates Chapter 8’s signature p. 157 hit-and-run taxi problem step-by-step.",
            "Giải tường minh và minh họa trực quan bài toán Taxi Xanh – Đỏ đặc sắc nhất cuối Chương 8 (tr. 157)."
        ),
        "svg": wrap_svg(900, 420, "Midnight Taxi Bayes Detective Story", p23_body, standalone),
    })

    # =========================================================================
    # PLATE 24: EPILOGUE PARABLE — THE BOY, THE WISE TEACHER & THE LIVING BIRD
    # =========================================================================
    p24_body = f"""{defs_arrows()}
    <rect x="24" y="20" width="852" height="360" rx="14" fill="#0e1022" stroke="#2a2f52" stroke-width="2"/>
    <text x="450" y="56" text-anchor="middle" class="mn" font-size="11.5" letter-spacing="1.6" fill="#2fc7e6">{esc(T("CLOSING FABLE · PAGE 171 · THE BIRD IN YOUR HAND", "NGỤ NGÔN KHÉP LẠI CUỐN SÁCH · TRANG 171 · CON CHIM TRONG TAY BẠN"))}</text>
    <text x="450" y="88" text-anchor="middle" class="hd" font-size="22" font-weight="800" fill="#f3f4fb">{esc(T("“Teacher—is the bird in my hands alive or dead?”", "“Thưa cô, đố cô biết con chim trong tay em sống hay chết?”"))}</text>

    <!-- Left Trap Binary Box -->
    <rect x="54" y="118" width="248" height="218" rx="10" fill="#1f2342" stroke="#ff5c6a" stroke-width="1.6"/>
    <text x="178" y="146" text-anchor="middle" font-size="12.5" font-weight="800" fill="#ff7a86">{esc(T("THE BOY’S BINARY TRAP", "CÁI BẪY NHỊ NGUYÊN CỦA CẬU BÉ"))}</text>
    <text x="72" y="180" font-size="12" fill="#d6daf0">{esc(T("• If Teacher says ‘Dead’:", "• Nếu cô đoán ‘Chim chết’:"))}</text>
    <text x="84" y="200" font-size="11.5" fill="#8d93b3">{esc(T("He opens his hands and lets it fly.", "Cậu mở tay cho chim bay đi → Cô sai."))}</text>
    <text x="72" y="236" font-size="12" fill="#d6daf0">{esc(T("• If Teacher says ‘Alive’:", "• Nếu cô đoán ‘Chim sống’:"))}</text>
    <text x="84" y="256" font-size="11.5" fill="#8d93b3">{esc(T("He crushes it quietly → Dead.", "Cậu âm thầm bóp chặt → Chim chết."))}</text>
    <text x="178" y="306" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff7a86">{esc(T("Rigged ‘Either / Or’ Frame", "Khung câu hỏi gài bẫy ‘Đúng / Sai’"))}</text>

    <!-- Center Emblem: Open Hands & Rising Bird -->
    <g transform="translate(450, 224)">
      <circle cx="0" cy="-10" r="78" fill="rgba(47,199,230,0.08)" stroke="#2fc7e6" stroke-width="1.6" stroke-dasharray="4 4"/>
      <polygon points="-34,-8 14,-46 6,-2" fill="#2fc7e6"/>
      <polygon points="6,-2 14,-46 48,-22" fill="#5b8cff"/>
      <polygon points="-34,-8 6,-2 -14,18" fill="#ffd23f"/>
      <path d="M -78,36 Q -22,58 42,38 Q 72,28 88,10" fill="none" stroke="#f3f4fb" stroke-width="3" stroke-linecap="round"/>
      <path d="M -54,44 Q 0,64 62,38" fill="none" stroke="#8d93b3" stroke-width="1.8" stroke-linecap="round"/>
    </g>

    <!-- Right Reframing Box -->
    <rect x="598" y="118" width="248" height="218" rx="10" fill="#1f2342" stroke="#2fc7e6" stroke-width="2"/>
    <text x="722" y="146" text-anchor="middle" font-size="12.5" font-weight="800" fill="#2fc7e6">{esc(T("THE TEACHER’S REFRAMING", "CÂU TRẢ LỜI BẰNG TƯ DUY"))}</text>
    <text x="722" y="184" text-anchor="middle" font-size="13" font-style="italic" fill="#f3f4fb">{esc(T("“If you want it to live, it lives.", "“Em muốn nó sống thì nó sống."))}</text>
    <text x="722" y="206" text-anchor="middle" font-size="13" font-style="italic" fill="#f3f4fb">{esc(T("If you want it to die, it dies.", "Em muốn nó chết thì nó chết."))}</text>
    <text x="722" y="232" text-anchor="middle" font-size="13.5" font-weight="800" fill="#ffd23f">{esc(T("It lies in your hands.”", "Nó nằm trong tay em.”"))}</text>
    <line x1="628" y1="254" x2="816" y2="254" stroke="#2a2f52"/>
    <text x="722" y="280" text-anchor="middle" font-size="11.5" fill="#b3b8d3">{esc(T("“How did you read my mind?”", "“Sao cô đoán được ý nghĩ của em?”"))}</text>
    <text x="722" y="304" text-anchor="middle" font-size="12.5" font-weight="800" fill="#2fc7e6">{esc(T("— “Through thinking!”", "— “Bằng tư duy!”"))}</text>
    """
    plates.append({
        "id": "p24",
        "slug": "24-epilogue-fable-the-bird-in-your-hand",
        "ch": "Epilogue",
        "manuscript_ref": T("Full Epilogue Plate (p. 171)", "Bản vẽ Lời kết (tr. 171)"),
        "title": T("Plate 24 · Closing Fable: The Boy, The Teacher & The Living Bird", "Bản vẽ 24 · Ngụ ngôn Khép sách: Cậu Học Trò, Cô Giáo & Con Chim Sống"),
        "say": T(
            "Stepping outside a rigged binary question restores moral and intellectual responsibility to the person holding the choice.",
            "Bước ra khỏi cái bẫy nhị nguyên định sẵn để trả lại quyền tự chủ và trách nhiệm cho chính bàn tay người lựa chọn."
        ),
        "rationale": T(
            "Gives the manuscript’s unforgettable final page its own full ceremonial illustration.",
            "Dành riêng một bản vẽ trang trọng cho câu chuyện ngụ ngôn khép lại trang 171 của cuốn sách."
        ),
        "svg": wrap_svg(900, 400, "Epilogue Fable The Bird in Your Hand", p24_body, standalone),
    })

    return plates
