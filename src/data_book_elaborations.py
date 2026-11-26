# -*- coding: utf-8 -*-
"""Deep, page-cited method elaborations, sub-method protocols, and authentic original examples extracted directly from Đào Minh Châu's book Học Tư Duy (Learning How to Think, Hà Nội, 08/01/2026, 171 pp.)."""

BOOK_AUTHOR_META = {
    "en": {
        "banner_kicker": "Official Interactive Companion to the Book",
        "book_title": "Học Tư Duy (Learning How to Think)",
        "author_line": "Written by Author Đào Minh Châu · Hà Nội, January 8, 2026 · 171 Pages",
        "about_book_title": "About Đào Minh Châu’s Book Học Tư Duy",
        "about_book_body": (
            "Originating from executive and university capacity-building courses taught by Đào Minh Châu since 2010, "
            "Học Tư Duy bridges Karl Popper’s insight (“All life is problem solving”) and Buddhist wisdom (“Life is suffering”) "
            "into a practical, learnable 3-Part architecture: Part I awakens conscious supervision over System 1 instinct (Chapter 1); "
            "Part II builds the four foundational thinking instruments—Creative, Critical, Analytical, and Logical Thinking (Chapters 2–5); "
            "and Part III synthesizes them into four advanced lenses—Systems, Strategic, Probabilistic, and Scientific Thinking (Chapters 6–9)."
        ),
        "parts_breakdown": [
            ("Preface & Epilogue", "pp. 5–8, 171", "Why we must think for ourselves in the age of AI—and the closing parable of the living bird in your hands."),
            ("Part I · Foundation", "Ch. 1 · pp. 10–22", "What thinking is, Kahneman’s System 1 vs. System 2, 10 cognitive biases with Vietnamese proverbs, and Paul & Elder’s 8-element conscious frame."),
            ("Part II · 4 Basic Methods", "Ch. 2–5 · pp. 23–100", "Creative Thinking (generate options), Critical Thinking (verify truth), Analytical Thinking (dissect structure), and Logical Thinking (valid inference)."),
            ("Part III · 4 Advanced Methods", "Ch. 6–9 · pp. 101–170", "Systems Thinking (feedback loops & delays), Strategic Thinking (scenarios & game theory), Probabilistic Thinking (EV & Bayes), and Scientific Thinking (falsifiable synthesis)."),
        ],
    },
    "vi": {
        "banner_kicker": "Ấn Bản Tương Tác & Minh Họa Dựa Trên Sách Nguyên Bản",
        "book_title": "Học Tư Duy",
        "author_line": "Tác giả: Đào Minh Châu · Hà Nội, 08/01/2026 · 171 trang",
        "about_book_title": "Giới thiệu cuốn sách Học Tư Duy của tác giả Đào Minh Châu",
        "about_book_body": (
            "Khởi nguồn từ các khóa đào tạo nâng cao năng lực do tác giả Đào Minh Châu trực tiếp giảng dạy từ năm 2010, "
            "cuốn sách Học Tư Duy kết nối triết lý nhà Phật (“Đời là bể khổ”) với mệnh đề của Karl Popper (“Cả cuộc đời là giải quyết vấn đề”): "
            "muốn giải quyết vấn đề để thoát khổ và làm chủ kỷ nguyên AI, con người phải học cách tư duy có phương pháp. "
            "Sách được kiến thiết chặt chẽ thành 3 Phần, 9 Chương: Phần I đánh thức tư duy có ý thức (Chương 1); "
            "Phần II trang bị 4 phương pháp tư duy cơ bản—Sáng tạo, Phản biện, Phân tích, Logic (Chương 2–5); "
            "và Phần III tích hợp thành 4 phương pháp tư duy nâng cao—Hệ thống, Chiến lược, Xác suất, Khoa học (Chương 6–9)."
        ),
        "parts_breakdown": [
            ("Lời nói đầu & Lời kết", "tr. 5–8, 171", "Vì sao càng có AI càng phải tự tư duy—và câu chuyện ngụ ngôn con chim sống hay chết nằm trong tay bạn."),
            ("Phần I · Nhập môn", "Chương 1 · tr. 10–22", "Bản chất tư duy, Hệ thống 1 & Hệ thống 2 (Kahneman), 10 thiên kiến gắn với tục ngữ Việt Nam và khung 8 thành tố Paul–Elder."),
            ("Phần II · 4 Phương pháp Cơ bản", "Chương 2–5 · tr. 23–100", "Tư duy Sáng tạo (mở rộng giải pháp), Phản biện (thẩm định đúng sai), Phân tích (mổ xẻ cấu trúc) và Logic (ngữ pháp suy luận)."),
            ("Phần III · 4 Phương pháp Nâng cao", "Chương 6–9 · tr. 101–170", "Tư duy Hệ thống (vòng phản hồi & độ trễ), Chiến lược (kịch bản & lý thuyết trò chơi), Xác suất (EV & Bayes) và Khoa học (kiểm chứng thực nghiệm)."),
        ],
    },
}


BOOK_ELABORATIONS = {
    # =========================================================================
    # CHAPTER 1 · OVERVIEW OF THINKING (pp. 10–22)
    # =========================================================================
    "ch1": {
        "en": {
            "lead_summary": (
                "Đào Minh Châu opens Part I (pp. 10–22) by showing why human beings err by default: automatic System 1 runs nonstop on memory shortcuts, "
                "while lazy System 2 either stays asleep or rationalizes impulses unless anchored inside Paul & Elder’s 8-element conscious framework."
            ),
            "book_spotlight_example": {
                "title": "Book Example (pp. 12 & 15–16): The Dark Coil in Grass & The Three Shirt Shops",
                "pages": "pp. 12, 15–16",
                "body": (
                    "Spotting a dark, wiggly shape near your foot at dusk, System 1 leaps sideways in 0.2 seconds—saving your life if it is a viper. "
                    "Yet minutes later on a shopping street, Shop 1 quotes 1,000,000 VND for a shirt, Shop 2 asks 900,000 VND, and you buy it feeling ‘clever’—never walking "
                    "twenty steps to Shop 3 where the identical shirt costs 800,000 VND. The same fast heuristic that saves you in the bush traps you in modern pricing."
                ),
                "takeaway": "Slowing down alone is insufficient; System 2 needs explicit 8-element checkpoints to override anchoring and question substitution.",
            },
            "deep_elaboration": [
                "Synthesizing the Oxford Dictionary of Philosophy and the American Psychological Association (pp. 10–11), Đào Minh Châu defines thinking as a hidden, symbolic cognitive rehearsal: before speaking or acting in reality, the human mind manipulates concepts, images, and propositions to uncover underlying regularities rather than reacting by blind instinct.",
                "Drawing on Daniel Kahneman’s Nobel-winning research (pp. 12–14), Chapter 1 explains how our mind operates via two modes: System 1 (fast, automatic, effortless, always on) and System 2 (slow, deliberate, effortful, and chronically lazy). Quoting Herbert Simon’s famous insight—“Intuition is nothing more and nothing less than recognition” (p. 14)—the author clarifies that System 1 thinks through stored memory patterns and shortcuts (heuristics) such as Question Substitution and WYSIATI (‘What You See Is All There Is’).",
                "Crucially, Đào Minh Châu warns on pages 18–19 that ‘thinking slowly’ does NOT guarantee right answers: errors happen both when System 2 fails to intervene AND when System 2 wakes up without a sound method. Therefore, Chapter 1 introduces Elder & Paul’s 8 Elements of Conscious Thought (pp. 19–21) situated inside real socio-historical Context—and closes with the Simon Consolidation Loop (p. 22): practicing conscious methods in Parts II–III gradually rewrites better instincts into System 1.",
            ],
            "sub_methods": [
                {
                    "name": "1. Defining Thinking: Symbolic Rehearsal & Rationality",
                    "pages": "pp. 10–11",
                    "desc": "Distinguishes human rational thought from reflex: thinking is covert (invisible from outside) and symbolic (manipulating mental representations, words, and models before acting).",
                    "steps": "Identify the problem → Pause physical reaction → Rehearse alternative actions mentally → Judge consequences against objective reality.",
                    "book_example": "Oxford Philosophy definition cited on p. 11: thinking is ‘mental trial and rehearsal of what to say or do’ prior to irreversible action.",
                },
                {
                    "name": "2. Dual-System Dynamics & Heuristic Shortcuts (Kahneman & Simon)",
                    "pages": "pp. 12–14",
                    "desc": "Maps the division of labor between effortless System 1 and effort-heavy System 2, showing how heuristics trade strict accuracy for survival speed.",
                    "steps": "Spot high-complexity or unfamiliar stakes → Detect Question Substitution (swapping a hard question for an easy feeling) → Wake System 2 deliberately.",
                    "book_example": "Leaping away from a dark rope-like object near your foot uses System 1; computing 17 × 24 in your head forces System 2 to allocate scarce working memory (p. 12).",
                },
                {
                    "name": "3. Diagnostic Audit of the 10 Instinctive Biases",
                    "pages": "pp. 15–18",
                    "desc": "Catalogs the ten recurring System 1 traps—uniquely paired by Đào Minh Châu with traditional Vietnamese proverbs so readers recognize them in everyday life.",
                    "steps": "Name the active bias (Confirmation, Anchoring, Availability, Framing, Sunk Cost, Loss Aversion, Bandwagon, Overconfidence, Affect, Dunning–Kruger) → Apply its conscious counter-question.",
                    "book_example": "Plane crashes dominate TV news so travelers fear flying more than driving despite road accidents being far deadlier (Availability, p. 16); ‘90% lean meat’ outsells ‘10% fat meat’ (Framing, p. 16); quitting a good job in a burst of anger at a colleague illustrates ‘Giận mất khôn’ / Affect bias (p. 18).",
                },
                {
                    "name": "4. Elder & Paul’s 8-Element Conscious Thinking Architecture",
                    "pages": "pp. 19–21",
                    "desc": "Makes thinking visible, controllable, and auditable by decomposing any reasoning act into eight interdependent elements inside a real Context.",
                    "steps": "State (1) Purpose → Formulate (2) Key Question → Surface (3) Assumptions & (4) Point of View → Gather (5) Information → Apply (6) Concepts → Draw (7) Inferences/Conclusions → Trace (8) Implications & Consequences.",
                    "book_example": "Deciding whether to pursue graduate school or start working (pp. 20–21): changing your Point of View (short-term income vs. 10-year capability) or testing hidden Assumptions (‘a Master’s degree guarantees higher pay’) completely reshapes the conclusion.",
                },
            ],
        },
        "vi": {
            "lead_summary": (
                "Mở đầu Phần I (tr. 10–22), tác giả Đào Minh Châu lý giải vì sao sai lầm là trạng thái mặc định khi ta suy nghĩ theo bản năng: "
                "Hệ thống 1 chạy tự động bằng trí nhớ và mẹo tắt, còn Hệ thống 2 vốn lười biếng sẽ chỉ hợp thức hóa cảm tính nếu thiếu khung 8 thành tố có ý thức của Paul & Elder."
            ),
            "book_spotlight_example": {
                "title": "Ví dụ Nguyên bản Trong Sách (tr. 12 & 15–16): Vật Đen Trong Cỏ & Ba Cửa Hiệu Áo Sơ-mi",
                "pages": "tr. 12, 15–16",
                "body": (
                    "Bất chợt thấy vật màu đen dài loằn ngoằn gần chân, bạn nhảy vọt sang bên trong tích tắc nhờ Hệ thống 1—cứu mạng nếu đó là rắn độc. "
                    "Nhưng khi đi mua áo sơ-mi: Tiệm 1 hét 1 triệu đồng, sang Tiệm 2 báo 900 ngàn là bạn mừng rỡ mua ngay vì tưởng ‘rẻ được 100 ngàn’—mà không đi thêm vài bước sang Tiệm 3 nơi chiếc áo y hệt có giá chuẩn 800 ngàn!"
                ),
                "takeaway": "Chỉ suy nghĩ chậm lại thôi chưa đủ; Hệ thống 2 cần khung kiểm định 8 thành tố để bẻ gãy mỏ neo và sự thay thế câu hỏi.",
            },
            "deep_elaboration": [
                "Tổng hợp từ Từ điển Triết học Oxford và Hiệp hội Tâm lý học Hoa Kỳ (APA, tr. 10–11), tác giả Đào Minh Châu chỉ rõ hai đặc trưng cốt tử của tư duy: tính ẩn giấu và tính biểu tượng. Tư duy chính là ‘sự tập dượt trong tâm trí về những gì cần nói hoặc cần làm’ bằng khái niệm, hình ảnh và lập luận duy lý trước khi hành động ngoài đời thực.",
                "Dựa trên công trình đoạt giải Nobel của Daniel Kahneman (tr. 12–14), Chương 1 phân tích cơ chế phối hợp giữa Hệ thống 1 (nhanh, tự động, không tốn sức, chạy liên tục không bao giờ nghỉ) và Hệ thống 2 (chậm, có ý thức, tốn nhiều năng lượng và rất ‘lười biếng’). Dẫn lời Herbert Simon—‘Trực giác không gì khác hơn là sự nhận biết’ (tr. 14)—sách giải thích rằng Hệ thống 1 dựa vào kho trí nhớ và các mẹo tắt (heuristic) như Thay thế câu hỏi hay chỉ nhìn cái có trước mắt.",
                "Điểm nhấn sắc sảo của Đào Minh Châu ở trang 18–19 là chỉ ra hai nguồn gốc của sai lầm: (1) Hệ thống 2 lười biếng để mặc Hệ thống 1 tự tung tự tác, và (2) Hệ thống 2 đã vào cuộc nhưng lại dùng phương pháp sai. Vì vậy, Chương 1 trao cho người đọc khung 8 thành tố tư duy có ý thức của Elder & Paul đặt trong Bối cảnh cụ thể (tr. 19–21), đồng thời mở ra vòng lặp rèn luyện: khi Hệ thống 2 thực hành nhuần nhuyễn các phương pháp ở Phần II và Phần III, tri thức đúng sẽ lắng vào trí nhớ để nâng cấp chính trực giác Hệ thống 1 (tr. 22).",
            ],
            "sub_methods": [
                {
                    "name": "1. Bản chất của Tư duy: Tập dượt Biểu tượng & Tính Duy lý",
                    "pages": "tr. 10–11",
                    "desc": "Phân biệt tư duy của con người với phản xạ bản năng: tư duy thao tác trên các ý tưởng, khái niệm và mô hình tinh thần để xuyên qua bề nổi, nắm bắt quy luật khách quan.",
                    "steps": "Nhận diện vấn đề → Tạm dừng phản ứng bốc đồng → Tập dượt các phương án trong tâm trí → Đối chiếu hệ quả với thực tế khách quan.",
                    "book_example": "Định nghĩa của Từ điển Triết học Oxford (tr. 11): biểu hiện rõ nhất của tính duy lý ở con người là tập dượt trước trong đầu điều định nói hoặc định làm.",
                },
                {
                    "name": "2. Hai Hệ thống Tư duy & Các Mẹo tắt Heuristic (Kahneman & Simon)",
                    "pages": "tr. 12–14",
                    "desc": "Giải mã sự phân công giữa Hệ thống 1 (trực giác dựa trên nhận biết trí nhớ) và Hệ thống 2 (kiểm soát có ý thức), cùng cơ chế các mẹo tắt đánh đổi độ chính xác lấy tốc độ.",
                    "steps": "Nhận biết tình huống phức tạp vượt khỏi kinh nghiệm quen thuộc → Phát hiện lúc Hệ thống 1 tự ý ‘thay câu hỏi khó bằng câu hỏi dễ’ → Chủ động kích hoạt Hệ thống 2.",
                    "book_example": "Nhảy tránh vật đen loằn ngoằn gần chân là Hệ thống 1; thực hiện phép nhân 17 × 24 trong đầu buộc Hệ thống 2 phải dồn sự chú ý và quy tắc toán học (tr. 12).",
                },
                {
                    "name": "3. Nhận diện 10 Lỗi Bản năng (Thiên kiến Nhận thức) Qua Tục ngữ Việt",
                    "pages": "tr. 15–18",
                    "desc": "Hệ thống hóa 10 thiên kiến phổ biến nhất của Hệ thống 1, được tác giả đối chiếu sinh động với kho tàng ca dao, tục ngữ Việt Nam để người đọc nhớ ngay và tự soi chiếu.",
                    "steps": "Gọi đúng tên thiên kiến đang chi phối (Xác nhận, Mỏ neo, Sẵn có, Đóng khung, Chi phí chìm, Ám ảnh thua thiệt, Đám đông, Quá tự tin, Cảm xúc, Dunning–Kruger) → Đặt câu hỏi kiểm chứng ngược lại.",
                    "book_example": "Tin tức tai nạn máy bay dồn dập làm nhiều người sợ đi máy bay hơn đi bộ/xe máy dù thống kê thực tế ngược hẳn (Thiên kiến sẵn có, tr. 16); nhãn ‘90% thịt nạc’ hấp dẫn hơn ‘10% mỡ’ (Đóng khung, tr. 16); vì một cơn bực tức với đồng nghiệp mà nộp đơn bỏ công việc tốt—ứng với câu ‘Giận mất khôn’ (Thiên kiến cảm xúc, tr. 18).",
                },
                {
                    "name": "4. Quá trình Tư duy Có Ý thức 8 Thành tố (Elder & Paul)",
                    "pages": "tr. 19–21",
                    "desc": "Biến quá trình suy nghĩ vô hình thành cấu trúc 8 thành tố tường minh đặt trong một Bối cảnh kinh tế – văn hóa – lịch sử xác định để tự kiểm soát và nâng cấp chất lượng tư duy.",
                    "steps": "Làm rõ (1) Mục đích → Đặt (2) Câu hỏi chính → Rà soát (3) Giả định & (4) Quan điểm góc nhìn → Thu thập (5) Thông tin → Vận dụng (6) Khái niệm → Thực hiện (7) Suy luận/Kết luận → Lường trước (8) Hệ quả.",
                    "book_example": "Bài toán chọn học tiếp cao học hay đi làm ngay (tr. 20–21): khi soi kỹ Giả định ngầm và đổi Góc nhìn dài hạn – ngắn hạn, quyết định trở nên sáng tỏ thay vì chạy theo số đông.",
                },
            ],
        },
    },

    # =========================================================================
    # CHAPTER 2 · CREATIVE THINKING (pp. 24–48)
    # =========================================================================
    "ch2": {
        "en": {
            "lead_summary": (
                "Chapter 2 (pp. 24–48) demystifies creativity as a disciplined habit combining Novelty and Appropriateness (Amabile), "
                "equipping readers with 7 concrete tools—Problem Redefinition, Inversion, Brainstorming, Mind Mapping, SCAMPER, Six Hats, and ‘What If’ questions."
            ),
            "book_spotlight_example": {
                "title": "Book Example (pp. 25, 31–33): Repurposing a Water Glass, Wald’s Bombers & Mastering English via Inversion",
                "pages": "pp. 25, 30–33",
                "body": (
                    "Creativity begins right on your desk: repurposing an ordinary drinking glass as a stand, a rice-measuring scoop, or a flower vase (p. 25). "
                    "At strategic scale, Đào Minh Châu walks step-by-step through Inversion Thinking (pp. 30–33): from Abraham Wald armoring the unhit engines of WWII bombers "
                    "to flipping ‘How do I master English in 12 months?’ into ‘How do I guarantee failing at English in 12 months?’ (never speaking out of shyness, studying sporadically)—then eliminating each failure trigger systematically."
                ),
                "takeaway": "Separate divergent generation (‘think wide without judgment’) from convergent selection (‘filter for real-world fit’).",
            },
            "deep_elaboration": [
                "Opening Part II (Basic Thinking Methods), Đào Minh Châu cites Teresa Amabile’s dual criterion (pp. 24–25): an idea is truly creative only when it possesses both Novelty (distinctive, non-routine) and Appropriateness (useful, feasible for the problem at hand). Wild eccentricity without utility is mere fantasy; routine utility without novelty is habit.",
                "Pages 25–26 establish five core principles of creative thought: (1) dare to challenge entrenched assumptions (such as medical dogma before Barry Marshall proved bacteria cause stomach ulcers, pp. 29–30), (2) question outdated human-made rules (illustrated by Vietnam’s historic reform legalizing the private sector, p. 26), (3) cross-pollinate unrelated domains (combining a coffeehouse + bookstore into a book-café, p. 26), (4) treat failed attempts as informative feedback rather than shame, and (5) alternate Divergent Thinking (expanding options) with Convergent Thinking (selecting the best).",
                "Across pages 27–46, the book provides detailed step-by-step manuals—complete with common mistakes to avoid—for seven practical creative instruments, before diagnosing personal barriers (fear of failure, perfectionism) and organizational barriers (rigid hierarchy, premature criticism) and prescribing daily drills like the 3-minute ‘Brick’ exercise (pp. 47–48).",
            ],
            "sub_methods": [
                {
                    "name": "1. Problem Identification & Redefinition (Định nghĩa lại vấn đề)",
                    "pages": "pp. 27–30",
                    "desc": "How we state a problem dictates—and often cages—which solutions we can see. Redefining shifts static attributes into dynamic processes or strips away embedded tool assumptions.",
                    "steps": "Write down the default problem statement → Strip out any pre-assumed tool → Restate the core functional need in 3–5 distinct ways from broader angles.",
                    "book_example": "Archimedes redefined a static 3D sphere dynamically as ‘the shape traced by rotating a 2D circle around its diameter’ (p. 27); the NASA space-pen parable locked into ‘How do we make a ballpoint pen flow in zero gravity?’ whereas asking ‘What writes in zero gravity?’ immediately reveals a pencil (p. 29); Barry Marshall & Robin Warren won the 2005 Nobel Prize by redefining stomach ulcers from ‘chronic stress acid’ to ‘curable H. pylori bacterial infection’ (pp. 29–30).",
                },
                {
                    "name": "2. Inversion Thinking (Tư duy Đảo ngược)",
                    "pages": "pp. 30–33",
                    "desc": "Instead of asking only how to achieve success—or staring only at visible data—flip the question upside down: ask what guarantees failure, what is missing, or what never changes.",
                    "steps": "State your goal → Invert: ‘How could I guarantee complete failure at this goal?’ → List every concrete failure cause → Design specific preventive actions against each cause.",
                    "book_example": "Abraham Wald armored the spotless engines and cockpit of returning WWII bombers (Fig. 2.1, p. 31); Jeff Bezos built Amazon around ‘What will NOT change in 10 years?’ (low prices, fast delivery, p. 31); and Đào Minh Châu works out a full 4-step plan on pp. 32–33 inverting ‘Master English in 12 months’ into ‘How to fail at English in 12 months.’",
                },
                {
                    "name": "3. Brainstorming & Mind Mapping (Động não & Sơ đồ tư duy)",
                    "pages": "pp. 33–39",
                    "desc": "Brainstorming unlocks group quantity by suspending all critique during generation; Tony Buzan’s Mind Map (Figs. 2.2–2.3) externalizes radiant associative thinking with keywords, branches, and colors.",
                    "steps": "Brainstorming: Define clear focus → Set a bold quota (e.g., 100 ideas in 60 minutes, p. 35) → Zero criticism during divergence → Cluster & evaluate afterward. Mind Map: Central topic → Main branches → Sub-branches using concise keywords (content before pretty decoration, p. 39).",
                    "book_example": "Figure 2.3 (p. 38) maps the entire Artificial Intelligence ecosystem—Machine Learning, Deep Learning, NLP, Computer Vision, Robotics, and Hardware—onto a single visual Mind Map.",
                },
                {
                    "name": "4. SCAMPER’s 7 Transformation Lenses",
                    "pages": "pp. 40–42",
                    "desc": "A systematic checklist of seven action verbs to innovate upon an existing product, service, or workflow when a blank page feels intimidating.",
                    "steps": "Substitute → Combine → Adapt → Modify / Magnify / Minimize → Put to another use → Eliminate → Reverse / Rearrange.",
                    "book_example": "Substitute a gasoline engine with an electric motor to create EVs and e-scooters (p. 40); Modify shoe sole materials and geometry for running, walking, summer, or winter conditions (p. 41).",
                },
                {
                    "name": "5. De Bono’s Six Thinking Hats & ‘What If…’ Counterfactuals",
                    "pages": "pp. 43–46",
                    "desc": "Six Thinking Hats ends ego-driven debate by having everyone wear the same cognitive lens simultaneously; ‘What If…’ shatters industry orthodoxy with bold hypotheticals.",
                    "steps": "Six Hats: White (neutral facts), Red (gut feelings), Black (risks/caution), Yellow (value/optimism), Green (new alternatives), Blue (process control). What-If: Pick an industry rule → Ask ‘What if the exact opposite held?’ → Trace business implications.",
                    "book_example": "Netflix asked ‘What if people watched movies anytime over the internet instead of renting physical DVDs?’ (p. 45), and Airbnb asked ‘What if travelers stayed in locals’ spare rooms for less than hotels?’ (pp. 45–46).",
                },
            ],
        },
        "vi": {
            "lead_summary": (
                "Chương 2 (tr. 24–48) xóa bỏ ngộ nhận rằng sáng tạo là năng khiếu bẩm sinh huyền bí: sáng tạo là thói quen làm việc kết hợp Tính mới lạ và Tính phù hợp (Amabile), "
                "được rèn luyện qua 7 công cụ thực hành từ Định nghĩa lại vấn đề, Tư duy Đảo ngược, Brainstorming, Mind Map đến SCAMPER, Sáu chiếc mũ và câu hỏi ‘Sẽ ra sao nếu’."
            ),
            "book_spotlight_example": {
                "title": "Ví dụ Nguyên bản Trong Sách (tr. 25, 31–33): Cái Cốc Uống Nước, Máy Bay Wald & Học Tiếng Anh Ngược",
                "pages": "tr. 25, 30–33",
                "body": (
                    "Tư duy sáng tạo bắt đầu ngay từ vật bình thường nhất: dùng chiếc cốc uống nước để kê đồ vật, làm dụng cụ đong gạo hay lọ cắm hoa (tr. 25). "
                    "Ở tầm phương pháp, tác giả hướng dẫn chi tiết Tư duy Đảo ngược (tr. 30–33): từ Abraham Wald bọc thép phần động cơ lành lặn trên máy bay Thế chiến II "
                    "đến bài thực hành lật ngược mục tiêu ‘Làm sao thành thạo tiếng Anh trong 12 tháng?’ thành ‘Làm sao để chắc chắn thất bại việc học tiếng Anh sau 12 tháng?’—từ đó triệt tiêu từng nguyên nhân gây thất bại."
                ),
                "takeaway": "Tuyệt đối tách bạch giai đoạn Tư duy Phân kỳ (mở rộng tối đa ý tưởng, không phán xét) với giai đoạn Tư duy Hội tụ (chọn lọc giải pháp khả thi).",
            },
            "deep_elaboration": [
                "Mở đầu Phần II (Các phương pháp tư duy cơ bản), tác giả Đào Minh Châu dẫn định nghĩa kinh điển của Teresa Amabile (tr. 24–25): một ý tưởng chỉ thực sự sáng tạo khi thỏa mãn đồng thời hai tiêu chuẩn—Tính mới lạ (khác biệt, độc đáo) và Tính phù hợp (giải quyết được vấn đề, mang lại giá trị thực tế).",
                "Trang 25–26 xác lập 5 nguyên lý nền tảng của tư duy sáng tạo: (1) dám thách thức các giả định cố hữu (như định kiến loét dạ dày do căng thẳng trước khi Marshall & Warren tìm ra vi khuẩn HP, tr. 29–30), (2) đặt câu hỏi lại với các quy tắc do con người đặt ra khi bối cảnh đã đổi thay (ví dụ thực tiễn Việt Nam đổi mới thừa nhận và phát triển kinh tế tư nhân, tr. 26), (3) kết hợp những lĩnh vực tưởng chừng không liên quan (quán cà phê + hiệu sách = cà phê sách, tr. 26), (4) không sợ sai lầm mà coi thất bại là dữ liệu học hỏi, và (5) nhịp nhàng giữa Tư duy Phân kỳ và Tư duy Hội tụ.",
                "Xuyên suốt trang 27–46, cuốn sách cầm tay chỉ việc từng bước thực hiện kèm danh mục ‘Các lỗi phổ biến cần tránh’ cho 7 công cụ sáng tạo, đồng thời mổ xẻ các rào cản cá nhân (sợ bị chê cười, cầu toàn quá sớm) lẫn rào cản tổ chức, khép lại bằng bài tập 3 phút nghĩ công dụng của ‘Viên gạch’ (tr. 47–48).",
            ],
            "sub_methods": [
                {
                    "name": "1. Xác định hay Định nghĩa lại Vấn đề",
                    "pages": "tr. 27–30",
                    "desc": "Cách chúng ta phát biểu vấn đề quyết định (và thường giam hãm) không gian giải pháp. Định nghĩa lại vấn đề giúp tháo bỏ rào cản khái niệm và tránh gắn cứng vấn đề vào một công cụ có sẵn.",
                    "steps": "Viết ra cách hiểu mặc định → Gỡ bỏ công cụ/giả định bị gài sẵn trong câu hỏi → Diễn đạt lại bản chất nhu cầu dưới 3–5 góc nhìn động khác nhau.",
                    "book_example": "Archimedes định nghĩa lại mặt cầu tĩnh thành ‘hình tạo ra khi quay một đường tròn quanh đường kính của nó’ (tr. 27); giai thoại bút viết vũ trụ của Mỹ tốn công làm mực chảy không trọng lực trong khi hỏi ‘Cái gì viết được khi không trọng lực?’ sẽ dẫn ngay tới bút chì (tr. 29); hai nhà khoa học Marshall & Warren định nghĩa lại bệnh loét dạ dày là bệnh nhiễm khuẩn và đoạt Nobel Y học 2005 (tr. 29–30).",
                },
                {
                    "name": "2. Tư duy Đảo ngược (Inversion Thinking)",
                    "pages": "tr. 30–33",
                    "desc": "Thay vì chỉ hỏi làm sao thành công hoặc chỉ nhìn phần dữ liệu hiện hữu, hãy lật ngược chiều suy nghĩ: điều gì dẫn tới thất bại, phần dữ liệu nào đang vắng mặt, hay điều gì không bao giờ thay đổi?",
                    "steps": "Nêu mục tiêu cần đạt → Đảo ngược: ‘Làm thế nào để đảm bảo mục tiêu này thất bại hoàn toàn?’ → Liệt kê mọi tác nhân gây thất bại → Xây dựng biện pháp khắc phục từng tác nhân đó.",
                    "book_example": "Nhà toán học Abraham Wald chỉ đạo bọc thép vùng không có lỗ đạn trên máy bay ném bom (Hình 2.1, tr. 31); Jeff Bezos hỏi ‘10 năm nữa điều gì KHÔNG thay đổi?’ để xây dựng đế chế Amazon (tr. 31); và bài hướng dẫn chi tiết đảo ngược mục tiêu thành thạo tiếng Anh trong 12 tháng ở trang 32–33.",
                },
                {
                    "name": "3. Brainstorming (Động não) & Mind Map (Sơ đồ Tư duy)",
                    "pages": "tr. 33–39",
                    "desc": "Brainstorming giải phóng số lượng ý tưởng tập thể bằng kỷ luật ‘cấm phê phán khi đang phát ý tưởng’; Sơ đồ tư duy (Hình 2.2–2.3) mô phỏng cấu trúc liên tưởng tỏa nhánh tự nhiên của bộ não.",
                    "steps": "Brainstorming: Nêu rõ đích → Đặt chỉ tiêu cụ thể (ví dụ 100 ý tưởng trong 60 phút, tr. 35) → Tuyệt đối chưa phán xét → Gom nhóm & sàng lọc sau. Mind Map: Chủ đề trung tâm → Nhánh chính → Nhánh phụ bằng từ khóa ngắn gọn (ưu tiên nội dung trước hình thức, tr. 39).",
                    "book_example": "Hình 2.3 (tr. 38) minh họa toàn bộ Hệ sinh thái Trí tuệ Nhân tạo (AI) trên một sơ đồ tư duy trực quan từ Học máy, Học sâu, Xử lý ngôn ngữ tự nhiên đến Thị giác máy tính và Phần cứng.",
                },
                {
                    "name": "4. Công cụ SCAMPER (7 Thấu kính Biến đổi)",
                    "pages": "tr. 40–42",
                    "desc": "Bộ 7 câu hỏi gợi mở có hệ thống giúp cải tiến sản phẩm, dịch vụ hoặc quy trình hiện hữu mà không phải chờ cảm hứng ngẫu nhiên.",
                    "steps": "Substitute (Thay thế) → Combine (Kết hợp) → Adapt (Thích nghi) → Modify (Sửa đổi/Phóng đại/Thu nhỏ) → Put to another use (Dùng vào việc khác) → Eliminate (Loại bỏ) → Reverse (Đảo ngược/Sắp xếp lại).",
                    "book_example": "Thay thế động cơ xăng bằng động cơ điện tạo ra ô tô, xe máy điện (tr. 40); Sửa đổi cấu trúc đế giày cho phù hợp giày chạy bộ, giày đi bộ, giày mùa hè hay mùa đông (tr. 41).",
                },
                {
                    "name": "5. Sáu Chiếc Mũ Tư Duy (De Bono) & Câu hỏi ‘Sẽ ra sao nếu’ (What If)",
                    "pages": "tr. 43–46",
                    "desc": "Sáu chiếc mũ giúp cuộc họp thoát cảnh cãi vã bảo vệ cái tôi bằng cách cùng đội một màu mũ tại một thời điểm; câu hỏi ‘Sẽ ra sao nếu…’ phá vỡ lối mòn ngành nghề.",
                    "steps": "6 mũ: Trắng (dữ liệu), Đỏ (cảm xúc), Đen (rủi ro), Vàng (lợi ích), Xanh lá (ý tưởng mới), Xanh lam (điều phối). What-If: Nêu quy ước hiển nhiên → Hỏi ‘Sẽ ra sao nếu quy ước ấy đảo ngược?’ → Khai phá mô hình mới.",
                    "book_example": "Netflix khởi sinh từ câu hỏi ‘Sẽ ra sao nếu người dùng xem phim trực tuyến mọi lúc thay vì ra tiệm thuê băng đĩa?’ (tr. 45), còn Airbnb hỏi ‘Sẽ ra sao nếu du khách thuê phòng trống nhà dân rẻ hơn khách sạn?’ (tr. 45–46).",
                },
            ],
        },
    },

    # =========================================================================
    # CHAPTER 3 · CRITICAL THINKING (pp. 49–66)
    # =========================================================================
    "ch3": {
        "en": {
            "lead_summary": (
                "Chapter 3 (pp. 49–66) builds the mind’s two-tier immune system: first auditing external claims via Browne & Keeley’s 10 critical questions, "
                "then turning the scalpel inward to audit our own reasoning through Paul & Elder’s Intellectual Standards and Intellectual Virtues."
            ),
            "book_spotlight_example": {
                "title": "Book Example (pp. 58–59 & 64): The Deceptive Average Income, Banning Gas Cars & Aristotle’s Teeth Count",
                "pages": "pp. 58–59, 64",
                "body": (
                    "Suppose a report claims: ‘Average income of our 10-person group rose 20%—everyone is better off!’ Đào Minh Châu shows (p. 58) that if 1 wealthy member’s income tripled while 9 members earned 0% more, the average lies about the group. "
                    "Similarly, on p. 64 he recalls Bertrand Russell’s famous quip: Aristotle asserted women have fewer teeth than men—without ever asking Mrs. Aristotle to open her mouth so he could count! Intelligence without critical habit still falls for dogma."
                ),
                "takeaway": "Critical thinking is NOT hostile nitpicking; it is objective, evidence-based evaluation applied equally to others’ claims and our own cherished beliefs.",
            },
            "deep_elaboration": [
                "Citing Michael Scriven and Richard Paul (p. 50), Đào Minh Châu defines Critical Thinking as the intellectually disciplined process of actively conceptualizing, analyzing, synthesizing, and evaluating information gathered from observation, experience, reflection, or communication as a guide to belief and action. Above all, it refuses automatic acceptance of what we hear, read, or even think ourselves.",
                "Pages 51–52 establish core principles: demand objective evidence before accepting claims (rejecting unverified viral assertions like ‘fasting cures cancer’ or prejudices like ‘meeting a woman at the alley gate brings bad luck,’ p. 51), recognize that knowledge evolves as better evidence arrives (from geocentrism to heliocentrism, p. 52), and generate multiple rival explanations for any event (why a candidate failed a job interview, p. 52).",
                "Uniquely, Đào Minh Châu organizes practical critical tools into a Two-Tier Architecture: Tier 1 (pp. 53–60) applies Browne & Keeley’s 10-question checklist to dissect external arguments, fallacies, evidence types, and misleading statistics; Tier 2 (pp. 61–63) applies Paul & Elder’s 3-part metacognitive framework—Elements of Thought, Universal Intellectual Standards, and Intellectual Virtues (Humility, Courage, Empathy, Integrity)—to critique our OWN mind.",
            ],
            "sub_methods": [
                {
                    "name": "1. Isolating the Issue, Conclusion, Reasons & Hidden Assumptions",
                    "pages": "pp. 53–54",
                    "desc": "You cannot critique an argument until you separate its topic (Issue), what the speaker wants you to accept (Conclusion), the supporting pillars (Reasons), and unspoken beliefs holding them together (Assumptions).",
                    "steps": "Find the Conclusion first → List the explicit Reasons → Surface both Value Assumptions (what ought to matter) and Descriptive Assumptions (how the world supposedly works).",
                    "book_example": "‘Effects of social media on children’ is merely a topic, NOT a conclusion until someone claims ‘Children under 13 should be barred from social media’ (p. 53).",
                },
                {
                    "name": "2. Detecting Ambiguity, Emotional Manipulation & Fallacies",
                    "pages": "pp. 54–55",
                    "desc": "Audits key terms that shift meaning mid-sentence and flags rhetorical tricks—personal attacks, false dilemmas, bandwagon pressure, emotional labels, and circular reasoning.",
                    "steps": "Demand precise definitions of abstract words → Strip away loaded emotional adjectives → Check whether reasons actually prove the conclusion rather than repeating it.",
                    "book_example": "Shaming morning walkers who didn’t post red-profile photos on the 80th National Day as ‘unpatriotic’ is an emotional manipulation fallacy (p. 55); saying ‘Sleep is vital for the brain because the brain really needs sleep’ is empty circular reasoning (p. 55).",
                },
                {
                    "name": "3. Auditing Evidence Quality, Rival Causes & Deceptive Statistics",
                    "pages": "pp. 56–58",
                    "desc": "Evaluates the reliability of intuition, personal anecdotes, testimonials, authority appeals, observational studies, and statistical summaries.",
                    "steps": "Check sample representativeness → Distinguish Mean, Median, and Mode → Spot surrogate/mismatched statistics → Hunt for confounding third variables.",
                    "book_example": "‘A is a math teacher, therefore A must be brilliant at math’ confuses formal title with verified competence (p. 57); ice cream sales and sunglasses sales rise together because of hot summer sun, not because ice cream makes people buy sunglasses (p. 57); mean vs. median income distortion (p. 58).",
                },
                {
                    "name": "4. Checking Omitted Information & Reasonable Alternative Conclusions",
                    "pages": "pp. 59–60",
                    "desc": "Almost every persuasive pitch highlights convenient facts while omitting trade-offs, transition costs, and viable middle-ground options.",
                    "steps": "Ask ‘What crucial data is missing here?’ → Map economic, technical, and social knock-on effects → Formulate nuanced ‘if–then’ conclusions instead of rigid ‘yes/no’ binaries.",
                    "book_example": "Evaluating ‘Gasoline cars emit CO2, so ban all gas cars immediately!’ (p. 59): critical thinking asks about battery grid capacity, disposal pollution, commuter livelihoods, and phased transition timelines.",
                },
                {
                    "name": "5. Self-Critique via Paul & Elder’s Intellectual Standards & Virtues",
                    "pages": "pp. 61–64",
                    "desc": "Applies Clarity, Accuracy, Precision, Relevance, Consistency, Logic, Depth, Breadth, and Fairness to our own beliefs to cultivate Intellectual Humility and Courage.",
                    "steps": "Audit your own thought across the 8 Elements → Test against the 9 Intellectual Standards → Practice Intellectual Humility (admitting what you don’t know) and Fair-mindedness.",
                    "book_example": "Aristotle’s unverified claim about women’s teeth (p. 64) shows why even history’s greatest logician erred whenever he failed to turn empirical skepticism onto his own assumptions.",
                },
            ],
        },
        "vi": {
            "lead_summary": (
                "Chương 3 (tr. 49–66) xây dựng ‘hệ miễn dịch nhận thức’ hai tầng: Tầng 1 dùng bộ 10 câu hỏi của Browne & Keeley để thẩm định lập luận, bằng chứng và số liệu bên ngoài; "
                "Tầng 2 dùng chuẩn mực và phẩm chất trí tuệ của Paul & Elder để tự phản biện chính suy nghĩ của bản thân."
            ),
            "book_spotlight_example": {
                "title": "Ví dụ Nguyên bản Trong Sách (tr. 58–59 & 64): Bẫy Thu Nhập Trung Bình, Cấm Xe Xăng & Chiếc Răng Của Aristotle",
                "pages": "tr. 58–59, 64",
                "body": (
                    "Khi nghe báo cáo ‘Thu nhập trung bình của nhóm 10 người tăng 20%’, đừng vội tin cả nhóm đều khấm khá: nếu 1 người giàu tăng vọt thu nhập còn 9 người kia dậm chân tại chỗ, số trung bình cộng đã che mờ thực tế (tr. 58). "
                    "Ở trang 64, tác giả nhắc lại câu chuyện kinh điển: đại triết gia Aristotle từng khẳng định đàn ông nhiều răng hơn phụ nữ—mà không hề bảo vợ mở miệng ra đếm thử! Thiếu thói quen phản biện, người cực kỳ thông minh vẫn sập bẫy định kiến."
                ),
                "takeaway": "Tư duy phản biện KHÔNG phải là bắt bẻ hay công kích cá nhân, mà là thẩm định khách quan dựa trên bằng chứng đối với cả người khác lẫn chính mình.",
            },
            "deep_elaboration": [
                "Dẫn định nghĩa của Scriven & Paul (tr. 50), tác giả Đào Minh Châu làm rõ: Tư duy phản biện là quá trình rèn luyện kỷ luật trí tuệ nhằm chủ động phân tích, tổng hợp và đánh giá thông tin thu nhận được từ quan sát, trải nghiệm hay giao tiếp để làm kim chỉ nam cho niềm tin và hành động—không bao giờ tin ngay một cách thụ động.",
                "Trang 51–52 nêu bật các nguyên lý cốt lõi: mọi khẳng định đều phải có bằng chứng khách quan kiểm chứng (bác bỏ tin đồn vô căn cứ như ‘nhịn ăn chữa ung thư’ hay định kiến ‘ra ngõ gặp gái là xui xẻo’, tr. 51); tri thức luôn vận động cập nhật khi có bằng chứng mới (như Thuyết Nhật tâm thay thế Thuyết Địa tâm, tr. 52); và luôn tìm nhiều cách giải thích hợp lý khác nhau cho cùng một hiện tượng (như một ứng viên trượt phỏng vấn xin việc có thể do nhiều nguyên nhân chứ không hẳn vì kém năng lực, tr. 52).",
                "Điểm đặc sắc nhất của Chương 3 là cấu trúc 2 công cụ lớn bổ trợ trọn vẹn cho nhau: (1) Bộ 10 câu hỏi phản biện của Browne & Keeley (tr. 53–60) giúp mổ xẻ lập luận của người khác từ giả định ngầm, ngụy biện đến thống kê lập lờ; và (2) Khung tự phản biện 3 phần của Paul & Elder (tr. 61–63)—gồm 8 Thành tố tư duy, Các Tiêu chuẩn Trí tuệ Phổ quát và Các Phẩm chất Trí tuệ (Khiêm tốn trí tuệ, Dũng cảm trí tuệ, Chính trực trí tuệ).",
            ],
            "sub_methods": [
                {
                    "name": "1. Bóc tách Vấn đề, Kết luận, Lý lẽ & Giả định Ngầm",
                    "pages": "tr. 53–54",
                    "desc": "Không thể phản biện khi chưa xác định rõ người nói đang muốn thuyết phục ta kết luận điều gì, dựa trên những lý lẽ nào và ẩn chứa giả định không nói ra nào.",
                    "steps": "Tìm Kết luận trước → Liệt kê các Lý lẽ nâng đỡ → Chỉ ra cả Giả định giá trị (coi điều gì đáng quý hơn) và Giả định mô tả (niềm tin ngầm về cách thế giới vận hành).",
                    "book_example": "‘Ảnh hưởng của mạng xã hội đến trẻ em’ mới chỉ là chủ đề bàn luận, chưa phải kết luận để phản biện cho tới khi ai đó khẳng định cụ thể cần cấm hay cho phép như thế nào (tr. 53).",
                },
                {
                    "name": "2. Phát hiện Từ ngữ Mơ hồ, Đánh tráo Cảm xúc & Ngụy biện",
                    "pages": "tr. 54–55",
                    "desc": "Kiểm tra các khái niệm đa nghĩa và vạch trần các chiêu thức ngụy biện: công kích cá nhân, gán nhãn cảm xúc, dựa vào đám đông, đánh lạc hướng hay lập luận vòng quanh.",
                    "steps": "Yêu cầu định nghĩa rõ từ khóa trừu tượng → Tách bỏ tính từ kích động cảm xúc → Kiểm tra xem lý lẽ có thực sự chứng minh cho kết luận không.",
                    "book_example": "Quy chụp những người đi bộ tập thể dục không đổi ảnh đại diện màu đỏ dịp kỷ niệm 80 năm Quốc khánh là ‘không yêu nước’ là ngụy biện gán nhãn cảm xúc (tr. 55); nói ‘Giấc ngủ rất cần cho não vì não rất cần ngủ’ là lập luận vòng quanh vô nghĩa (tr. 55).",
                },
                {
                    "name": "3. Thẩm định Độ tin cậy Bằng chứng, Nguyên nhân Thay thế & Thống kê Lập lờ",
                    "pages": "tr. 56–58",
                    "desc": "Phân biệt sức nặng giữa trực giác, lời kể cá nhân, lời chứng thực, uy quyền chuyên gia, nghiên cứu khoa học và vạch trần các con số thống kê đánh lừa.",
                    "steps": "Xét tính đại diện của mẫu → Phân biệt Trung bình cộng (Mean), Trung vị (Median) và Yếu vị (Mode) → Cảnh giác ‘thống kê chứng minh một đằng, kết luận một nẻo’.",
                    "book_example": "‘Vì A là giáo viên toán nên A giỏi toán’ là suy diễn uy quyền chưa kiểm chứng (tr. 57); lượng kem và kính râm cùng tăng vì trời nắng nóng chứ không gây ra nhau (tr. 57); bẫy thu nhập trung bình cộng (tr. 58).",
                },
                {
                    "name": "4. Truy tìm Thông tin Bị Bỏ sót & Các Kết luận Hợp lý Khác",
                    "pages": "tr. 59–60",
                    "desc": "Mọi lập luận thuyết phục một chiều đều giấu bớt chi phí chuyển đổi, tác động phụ và các phương án dung hòa khả thi hơn.",
                    "steps": "Đặt câu hỏi mở ‘Thông tin quan trọng nào đã bị lược bỏ?’ → Đánh giá tác động kinh tế, hạ tầng, xã hội → Đề xuất các kết luận có điều kiện linh hoạt.",
                    "book_example": "Trước lập luận ‘Xe xăng thải CO2 gây ô nhiễm nên phải cấm ngay lập tức!’ (tr. 59), tư duy phản biện đòi hỏi dữ liệu về sinh kế người dân, hạ tầng điện, xử lý pin thải và lộ trình chuyển đổi.",
                },
                {
                    "name": "5. Tự Phản biện qua Tiêu chuẩn & Phẩm chất Trí tuệ (Paul & Elder)",
                    "pages": "tr. 61–64",
                    "desc": "Áp dụng bộ tiêu chuẩn Rõ ràng, Chính xác, Cụ thể, Liên quan, Nhất quán, Logic, Sâu sắc, Toàn diện, Công bằng để tự gạn đục khơi trong chính nhận thức của mình.",
                    "steps": "Phân tích suy nghĩ của mình theo 8 Thành tố → Đo bằng các Tiêu chuẩn Trí tuệ → Rèn luyện Khiêm tốn trí tuệ (biết giới hạn hiểu biết của mình) và Dũng cảm trí tuệ.",
                    "book_example": "Câu chuyện Aristotle không đếm răng (tr. 64) nhắc nhở: rào cản lớn nhất không phải thiếu trí thông minh mà là sự kiêu ngạo chủ quan và lệ thuộc uy quyền.",
                },
            ],
        },
    },

    # =========================================================================
    # CHAPTER 4 · ANALYTICAL THINKING (pp. 68–86)
    # =========================================================================
    "ch4": {
        "en": {
            "lead_summary": (
                "Chapter 4 (pp. 68–86) teaches Analytical Thinking—disassembling complex tangles like a watchmaker to expose components, linkages, and root causes "
                "using five workhorse tools: SWOT, Taiichi Ohno’s 5 Whys, Ishikawa Fishbone (6M/4S/8P), the Eisenhower Matrix, and 6-Step Comparative Analysis."
            ),
            "book_spotlight_example": {
                "title": "Book Example (pp. 74–75): Taiichi Ohno’s Stopped Factory Robot (5 Whys)",
                "pages": "pp. 74–75",
                "body": (
                    "On a Toyota production floor, a welding robot suddenly halts (p. 74). A hasty technician just swaps the blown fuse—and the robot breaks again tomorrow. "
                    "Taiichi Ohno asks ‘Why?’ five times: (1) Why did it stop? Overload blew the fuse. (2) Why overload? Bearing lacked lubrication. "
                    "(3) Why insufficient oil? Pump wasn’t circulating enough. (4) Why? Pump shaft was worn and rattling. (5) Why did it wear out? No metal strainer was fitted, letting metal shavings enter! Attaching a strainer cures the failure permanently."
                ),
                "takeaway": "Analysis peels back symptoms layer by layer until it hits an actionable structural root cause.",
            },
            "deep_elaboration": [
                "Opening with P. S. Baber’s aphorism—“Analysis is the art of creation through destruction” (p. 68)—Đào Minh Châu defines Analytical Thinking (p. 69) as breaking a complex whole into constituent parts to inspect both the nature of each part and the structural linkages connecting parts to the whole, exactly like disassembling a mechanical watch to see how its gears interlock.",
                "Pages 70–71 articulate core analytical principles: systematic decomposition (avoiding overwhelming lumps), structural-relational focus, strict factual grounding (separating verified data from opinion or wishful guessing), and pairing deductive top-down trees with inductive data pattern-finding.",
                "Pages 71–84 walk step-by-step through five practical analytical frameworks—SWOT (Fig. 4.1), 5 Whys, Ishikawa Fishbone Diagrams across Manufacturing (6M), Services (4S), and Marketing (8P) (Fig. 4.2), the Eisenhower Urgent–Important Matrix (Fig. 4.3), and 6-Step Comparative Analysis—noting on p. 84 that in real practice, master analysts combine these tools sequentially (e.g., Fishbone to map all candidate branches, then 5 Whys to drill down each suspect branch).",
            ],
            "sub_methods": [
                {
                    "name": "1. SWOT Analysis (Internal Capabilities × External Environment)",
                    "pages": "pp. 71–73",
                    "desc": "Decomposes a person’s, project’s, or organization’s position across four structured quadrants: internal Strengths & Weaknesses (controllable) vs. external Opportunities & Threats (contextual).",
                    "steps": "Audit internal tangible assets (equipment, capital) & intangible assets (brand, know-how, team) → Scan external technological, economic & competitive shifts → Synthesize priorities.",
                    "book_example": "Figure 4.1 (pp. 72–73): separating internal factory/human-resource capabilities from external forces such as rapid AI disruption so teams stop confusing internal weaknesses with external threats.",
                },
                {
                    "name": "2. Taiichi Ohno’s 5 Whys Root-Cause Drilling",
                    "pages": "pp. 74–76",
                    "desc": "Pioneered in the Toyota Production System, asking ‘Why?’ iteratively (~5 layers, flexibly fewer or more) drills past surface symptoms to the underlying physical or process root cause.",
                    "steps": "State the observable failure precisely → Ask ‘Why did this happen?’ grounded in verified fact (never speculation) → Repeat on each answer until fixing that link prevents recurrence.",
                    "book_example": "Ohno’s stopped factory robot (pp. 74–75): Fuse blew → Bearing dry → Oil pump weak → Shaft worn → Missing intake strainer allowing metal chips in.",
                },
                {
                    "name": "3. Ishikawa Fishbone Diagram (6M, 4S & 8P Taxonomies)",
                    "pages": "pp. 76–79",
                    "desc": "When a complex problem has multiple interacting causes rather than a single linear chain, the Fishbone diagram (Fig. 4.2) maps main causal ribs and sub-branches visually.",
                    "steps": "Place the Problem at the fish head → Draw major category ribs: 6M for manufacturing (Manpower, Machine, Material, Method, Measurement, Mother Nature), 4S for service (Surrounding, Supplier, System, Skill), or 8P for marketing → Brainstorm sub-causes → Weight & verify.",
                    "book_example": "Pages 77–79 show how switching category skeletons (6M on a factory line vs. 4S in a hospital/hotel vs. 8P in commercial launch) prevents blind spots.",
                },
                {
                    "name": "4. The Eisenhower Priority Matrix (Important vs. Urgent)",
                    "pages": "pp. 80–81",
                    "desc": "Human System 1 chronically confuses ‘noisy/urgent’ tasks with ‘genuinely important’ goals. Figure 4.3 splits all tasks into four actionable quadrants to protect scarce time.",
                    "steps": "Quadrant 1 (Important + Urgent): Do immediately → Quadrant 2 (Important + Not Urgent): Schedule deep time → Quadrant 3 (Not Important + Urgent): Delegate/automate → Quadrant 4 (Neither): Eliminate.",
                    "book_example": "Pages 80–81 warn against spending all day trapped in Quadrant 3 interruptions while neglecting Quadrant 2 capability-building, health, and long-term planning.",
                },
                {
                    "name": "5. Six-Step Comparative Analysis Framework",
                    "pages": "pp. 82–84",
                    "desc": "Replaces gut-feel ‘apples-to-oranges’ choices with a transparent, weighted multi-criteria matrix across competing candidates, strategies, or investments.",
                    "steps": "(1) Define objective & core question → (2) Select comparable subjects → (3) Establish measurable criteria → (4) Collect symmetrical data across all options → (5) Analyze patterns objectively → (6) Draw actionable recommendations.",
                    "book_example": "Evaluating competing job offers, suppliers, or technology stacks (pp. 82–84) without cherry-picking criteria to favor a pre-chosen favorite.",
                },
            ],
        },
        "vi": {
            "lead_summary": (
                "Chương 4 (tr. 68–86) rèn luyện Tư duy Phân tích—nghệ thuật ‘tháo chiếc đồng hồ’ thành từng bánh răng và mối liên kết để chiếu rọi nguyên nhân gốc rễ "
                "bằng 5 công cụ chủ lực: SWOT, 5 Câu hỏi Tại sao (Taiichi Ohno), Biểu đồ Xương cá (6M/4S/8P), Ma trận Eisenhower và Phân tích So sánh 6 bước."
            ),
            "book_spotlight_example": {
                "title": "Ví dụ Nguyên bản Trong Sách (tr. 74–75): Con Robot Đột Ngột Dừng Hoạt Động Của Taiichi Ohno",
                "pages": "tr. 74–75",
                "body": (
                    "Tại xưởng Toyota, một robot hàn đột ngột đứng máy (tr. 74). Nếu chỉ thay cầu chì mới, hôm sau máy lại hỏng! "
                    "Taiichi Ohno truy 5 câu hỏi Tại sao: (1) Sao robot dừng? Quá tải làm đứt cầu chì. (2) Sao quá tải? Vòng bi thiếu dầu bôi trơn. "
                    "(3) Sao thiếu dầu? Bơm dầu hút không đủ. (4) Sao bơm yếu? Trục bơm bị mòn rơ. (5) Sao trục mòn? Không có lưới lọc ở đầu hút nên mạt sắt lọt vào! Lắp lưới lọc mới trị dứt điểm gốc rễ."
                ),
                "takeaway": "Phân tích là bóc từng lớp vỏ triệu chứng bằng dữ kiện thực tế cho tới khi chạm đúng mắt xích gốc có thể xử lý triệt để.",
            },
            "deep_elaboration": [
                "Mở đầu bằng châm ngôn của P. S. Baber—‘Phân tích là nghệ thuật sáng tạo thông qua sự phá hủy’ (tr. 68)—tác giả Đào Minh Châu định nghĩa Tư duy phân tích (tr. 69) là chia nhỏ một vấn đề phức tạp thành các bộ phận hợp thành để hiểu rõ bản chất từng phần và cách chúng tương tác với tổng thể, giống như người thợ tháo chiếc đồng hồ cơ để thấy rõ từng bánh răng ăn khớp.",
                "Trang 70–71 đúc kết các nguyên lý cốt lõi: chia nhỏ có hệ thống, tập trung vào cấu trúc và mối liên hệ, định hướng thực tế nghiêm ngặt (tách dữ liệu kiểm chứng khỏi cảm tính hay suy đoán), đồng thời kết hợp nhuần nhuyễn cả diễn dịch lẫn quy nạp.",
                "Từ trang 71 đến 84, tác giả hướng dẫn chi tiết từng bước và chỉ rõ các lỗi sai thường gặp cho 5 công cụ phổ biến nhất: Phân tích SWOT (Hình 4.1), 5 Câu hỏi Tại sao, Biểu đồ Xương cá 6M/4S/8P (Hình 4.2), Ma trận quản trị ưu tiên Eisenhower (Hình 4.3) và Khung Phân tích So sánh 6 bước—đồng thời nhấn mạnh các công cụ này phát huy sức mạnh cao nhất khi phối hợp cùng nhau (tr. 84).",
            ],
            "sub_methods": [
                {
                    "name": "1. Phân tích SWOT (Nội lực Bên trong × Bối cảnh Bên ngoài)",
                    "pages": "tr. 71–73",
                    "desc": "Bóc tách vị thế của cá nhân hay tổ chức thành 4 ô rành mạch: Điểm mạnh (S) & Điểm yếu (W) thuộc nội tại kiểm soát được; Cơ hội (O) & Thách thức (T) thuộc môi trường khách quan.",
                    "steps": "Rà soát tài sản hữu hình (nhà xưởng, thiết bị, vốn) & vô hình (nhân lực, thương hiệu, bí quyết) → Quét biến động bên ngoài (công nghệ AI, thị trường, pháp lý) → Tổng hợp trọng tâm.",
                    "book_example": "Hình 4.1 (tr. 72–73) phân biệt rõ các yếu tố nội tại của doanh nghiệp với làn sóng công nghệ AI từ bên ngoài để không nhầm lẫn giữa điểm yếu chủ quan và thách thức khách quan.",
                },
                {
                    "name": "2. Phân tích 5 Câu hỏi ‘Tại sao’ (5 Whys — Taiichi Ohno)",
                    "pages": "tr. 74–76",
                    "desc": "Công cụ trứ danh của Hệ thống Sản xuất Toyota: hỏi liên tiếp ‘Tại sao?’ (linh hoạt 3–7 vòng tùy độ sâu) dựa trên hiện trường thực tế để vượt qua triệu chứng bề mặt tới nguyên nhân gốc.",
                    "steps": "Phát biểu rõ sự cố → Hỏi ‘Tại sao điều này xảy ra?’ dựa trên sự thật quan sát được (không đoán mò hay đổ lỗi cá nhân) → Lặp lại tới khi tìm ra giải pháp ngăn tái diễn.",
                    "book_example": "Ví dụ kinh điển của Taiichi Ohno về robot dừng máy do thiếu lưới lọc mạt sắt ở bơm dầu (tr. 74–75).",
                },
                {
                    "name": "3. Biểu đồ Xương Cá Ishikawa (Khung 6M, 4S & 8P)",
                    "pages": "tr. 76–79",
                    "desc": "Khi sự cố do nhiều nhóm nguyên nhân đan xen gây ra, Biểu đồ Xương cá (Hình 4.2) giúp hệ thống hóa toàn diện các nhánh chính và nhánh phụ mà không bỏ sót.",
                    "steps": "Đặt Vấn đề ở đầu cá → Vẽ các xương chính theo ngành: 6M cho sản xuất (Nhân lực, Máy móc, Nguyên liệu, Phương pháp, Đo lường, Môi trường), 4S cho dịch vụ, hoặc 8P cho marketing → Truy nhánh phụ → Xếp trọng số ưu tiên.",
                    "book_example": "Trang 77–79 chỉ rõ cách chọn bộ khung xương cá phù hợp (6M, 4S hay 8P) và lỗi phổ biến là liệt kê tràn lan nhưng quên xếp thứ tự ưu tiên nguyên nhân trọng yếu.",
                },
                {
                    "name": "4. Ma trận Quản lý Ưu tiên Eisenhower (Quan trọng × Khẩn cấp)",
                    "pages": "tr. 80–81",
                    "desc": "Con người rất dễ nhầm việc ‘khẩn cấp trước mắt’ là việc ‘quan trọng dài hạn’. Hình 4.3 phân loại công việc thành 4 ô để phân bổ quỹ thời gian hữu hạn một cách tỉnh táo.",
                    "steps": "Ô 1 (Quan trọng + Khẩn cấp): Làm ngay → Ô 2 (Quan trọng + Không khẩn cấp): Lên lịch đầu tư sâu → Ô 3 (Không quan trọng + Khẩn cấp): Ủy quyền/tối giản → Ô 4 (Cả hai đều không): Loại bỏ.",
                    "book_example": "Trang 80–81 cảnh báo lỗi sa lầy cả ngày vào các việc vặt khẩn cấp ở Ô 3 và giải trí vô bổ Ô 4 mà bỏ bê việc học tập, rèn luyện và hoạch định tương lai ở Ô 2.",
                },
                {
                    "name": "5. Khung Phân tích So sánh 6 Bước",
                    "pages": "tr. 82–84",
                    "desc": "Đặt các phương án lựa chọn lên cùng một hệ quy chiếu tiêu chí đo lường được để ra quyết định khách quan thay vì cảm tính.",
                    "steps": "(1) Xác định mục tiêu & câu hỏi cốt lõi → (2) Chọn đối tượng tương đồng để so sánh → (3) Thiết lập bộ tiêu chí đo lường → (4) Thu thập dữ liệu đồng nhất → (5) Phân tích & diễn giải khách quan → (6) Kết luận & khuyến nghị.",
                    "book_example": "Áp dụng khi so sánh chọn trường, chọn việc làm, chọn nhà cung cấp hay phương án đầu tư (tr. 82–84), tránh thiên kiến xác nhận làm lệch tiêu chí.",
                },
            ],
        },
    },

    # =========================================================================
    # CHAPTER 5 · LOGICAL THINKING (pp. 87–100)
    # =========================================================================
    "ch5": {
        "en": {
            "lead_summary": (
                "Closing Part II, Chapter 5 (pp. 87–100) establishes Logical Thinking as ‘the grammar of all reasoning’—anchoring valid thought on the 4 Laws of Logic "
                "and four inference engines: Deductive, Inductive, Causal, and Analogical reasoning."
            ),
            "book_spotlight_example": {
                "title": "Book Example (pp. 89, 92 & 98): The Phở Equivocation, The Whale Syllogism & Shark-vs.-Tiger Analogy",
                "pages": "pp. 89, 92, 98",
                "body": (
                    "Đào Minh Châu illustrates how subtle logical slips wreck everyday arguments: (1) ‘Vietnamese people love phở; he holds Vietnamese citizenship → he must love phở’ violates the Law of Identity by shifting ‘Vietnamese’ from cultural habit to legal passport (p. 89); "
                    "(2) ‘All fish breathe with gills; whales are fish → whales breathe with gills’ has valid deductive structure but fails because Premise 2 is false—whales are mammals (p. 92); "
                    "(3) ‘Sharks and tigers are both fierce carnivores; sharks live underwater → tigers live underwater’ exposes false analogy ignoring gills/fins vs. lungs/legs (p. 98)."
                ),
                "takeaway": "Because every other thinking method relies on inference, logic is the universal grammar keeping Creative, Critical, Analytical, and Scientific thought coherent (p. 100).",
            },
            "deep_elaboration": [
                "Opening with Arthur Conan Doyle’s Sherlock Holmes (p. 87), Đào Minh Châu defines Logical Thinking as rigorous, rule-governed reasoning that moves from verified premises to necessary or well-supported conclusions without contradiction, ambiguity, or emotional distortion.",
                "Pages 88–90 lay down the four classical pillars of formal logic: the Law of Identity (a concept must keep the exact same meaning throughout an argument), the Law of Non-Contradiction (a statement and its negation cannot both be true in the same respect at the same time), the Law of Excluded Middle (between P and not-P there is no vague third truth value), and Leibniz’s Principle of Sufficient Reason (every claim requires adequate objective grounds).",
                "Pages 91–99 then equip readers with four practical inference tools—Deductive Syllogisms, Inductive Generalization, 5-Criterion Causal Verification, and Aristotle’s 4-Condition Analogical Reasoning—before warning against Gustave Le Bon’s crowd-psychology trap (p. 99), where group emotion overrides individual logic.",
            ],
            "sub_methods": [
                {
                    "name": "1. The Four Fundamental Laws of Logic",
                    "pages": "pp. 88–90",
                    "desc": "The constitutional guardrails of coherent thought: Identity, Non-Contradiction, Excluded Middle, and Sufficient Reason.",
                    "steps": "Lock definitions from start to finish (Identity) → Reject self-contradictory claims (Non-Contradiction) → Eliminate evasive vagueness (Excluded Middle) → Demand evidence/mechanism (Sufficient Reason).",
                    "book_example": "Equivocating between cultural ‘Vietnamese’ and legal nationality in the phở example violates Identity (p. 89); ‘It is raining’ at one exact spot and moment is either true or false (Excluded Middle, p. 90).",
                },
                {
                    "name": "2. Deductive Reasoning (General Rule → Guaranteed Specific Case)",
                    "pages": "pp. 91–92",
                    "desc": "Moves top-down from universal premises to a specific conclusion. Sound deduction requires BOTH a valid logical form AND factually true premises.",
                    "steps": "Verify Major Premise is universally true → Verify Minor Premise accurately classifies the case → Check syllogistic structure (avoiding affirming the consequent or denying the antecedent).",
                    "book_example": "‘All fish breathe through gills; whales are fish → whales breathe through gills’ (p. 92) demonstrates how a false premise produces a false conclusion despite neat form.",
                },
                {
                    "name": "3. Inductive Reasoning (Specific Observations → General Pattern)",
                    "pages": "pp. 93–94",
                    "desc": "Moves bottom-up from empirical observations to broader generalizations and scientific hypotheses—powerful for discovery, but probabilistic rather than 100% certain.",
                    "steps": "Gather a sufficiently large, diverse sample → Identify recurring patterns → Avoid Hasty Generalization (small sample) and Over-Extrapolation beyond observed boundaries.",
                    "book_example": "Meeting 3 rude people from one locality and concluding ‘everyone from that province is rude in public’ commits the small-sample fallacy (p. 94); assuming a PhD in one narrow specialty is an authority on every topic commits over-extrapolation (p. 94).",
                },
                {
                    "name": "4. Five-Criterion Causal Inference (Suy luận Nhân quả)",
                    "pages": "pp. 95–96",
                    "desc": "Prevents confusing coincidence or co-variation with true cause-and-effect by testing five strict conditions.",
                    "steps": "Verify (1) Correlation, (2) Temporal precedence (cause before effect), (3) Plausible physical/social mechanism, (4) Elimination of third-factor confounders, and (5) Contextual boundary conditions.",
                    "book_example": "Hot weather precedes rising household electricity use via the mechanism of air-conditioner demand (p. 95); when 4 partygoers suffer food poisoning after all drinking water, water may just be an innocent shared accompaniment rather than the toxin (p. 96).",
                },
                {
                    "name": "5. Analogical Reasoning & Aristotle’s Four Conditions",
                    "pages": "pp. 97–98",
                    "desc": "Transfers knowledge from familiar domain A to target domain B based on shared attributes—strong only when similarities are causally relevant to the inferred property.",
                    "steps": "Audit Aristotle’s 4 rules (p. 97): (1) Number of shared traits, (2) Causal relevance of shared traits to the conclusion, (3) Absence of disqualifying differences, and (4) Depth over surface appearance.",
                    "book_example": "Shark vs. Tiger analogy (p. 98): sharing ‘fierce meat-eating predator’ is irrelevant to breathing underwater, while ignoring fins/gills vs. legs/lungs invalidates the transfer.",
                },
            ],
        },
        "vi": {
            "lead_summary": (
                "Khép lại Phần II, Chương 5 (tr. 87–100) xác lập Tư duy Logic là ‘ngữ pháp của mọi sự suy luận’—đặt nền móng trên 4 Nguyên lý Logic cơ bản "
                "cùng 4 công cụ suy luận cốt lõi: Diễn dịch, Quy nạp, Nhân quả và Tương tự."
            ),
            "book_spotlight_example": {
                "title": "Ví dụ Nguyên bản Trong Sách (tr. 89, 92 & 98): Bẫy ‘Người Việt Thích Phở’, Tam Đoạn Luận Cá Voi & Cá Mập – Hổ",
                "pages": "tr. 89, 92, 98",
                "body": (
                    "Tác giả Đào Minh Châu nêu 3 ví dụ cực kỳ dễ nhớ cho các lỗi logic thường gặp: (1) ‘Người Việt thích ăn phở; anh ấy có quốc tịch Việt Nam → anh ấy thích ăn phở’ vi phạm Luật Đồng nhất vì đánh tráo khái niệm văn hóa với khái niệm pháp lý (tr. 89); "
                    "(2) ‘Đã là cá thì thở bằng mang; cá voi là cá → cá voi thở bằng mang’ sai ngay từ tiền đề 2 vì cá voi là thú có vú thở bằng phổi (tr. 92); "
                    "(3) ‘Cá mập và hổ đều là thú dữ ăn thịt; cá mập sống dưới nước → hổ cũng sống dưới nước’ phơi bày lỗi so sánh khập khiễng bỏ qua khác biệt vây/mang và chân/phổi (tr. 98)."
                ),
                "takeaway": "Vì suy luận là công cụ của mọi phương pháp tư duy khác, logic chính là bộ ngữ pháp giữ cho toàn bộ hệ thống lý trí mạch lạc và chặt chẽ (tr. 100).",
            },
            "deep_elaboration": [
                "Mở đầu bằng câu nói nổi tiếng của thám tử Sherlock Holmes (Arthur Conan Doyle, tr. 87), tác giả Đào Minh Châu định nghĩa Tư duy logic là quá trình suy luận tuân thủ các quy tắc khách quan nhằm đi từ tiền đề xác thực tới kết luận hợp lệ, không mâu thuẫn, không nhập nhằng và không bị cảm xúc đám đông dẫn dắt.",
                "Trang 88–90 trình bày 4 nguyên lý nền tảng của logic hình thức: Nguyên lý Đồng nhất (khái niệm phải giữ nguyên một nghĩa xuyên suốt lập luận), Nguyên lý Không mâu thuẫn (hai mệnh đề đối lập không thể cùng đúng một lúc trong cùng mối quan hệ), Nguyên lý Loại trừ cái thứ ba (giữa đúng và sai không có trạng thái lấp lửng thứ ba) và Nguyên lý Đủ lý do (mọi kết luận đều phải có căn cứ xác đáng).",
                "Trang 91–99 đi sâu vào cách vận hành và các bẫy sai lầm của 4 công cụ suy luận—Diễn dịch, Quy nạp, Nhân quả và Tương tự—trước khi cảnh báo rào cản ‘Tâm lý học đám đông’ của Gustave Le Bon (tr. 99), nơi con người dễ đánh mất lý trí cá nhân khi hòa vào cảm xúc bầy đàn.",
            ],
            "sub_methods": [
                {
                    "name": "1. Bốn Nguyên lý Nền tảng của Tư duy Logic",
                    "pages": "tr. 88–90",
                    "desc": "Bốn trụ cột hiến pháp bảo vệ sự trong sáng của lập luận: Đồng nhất, Không mâu thuẫn, Loại trừ trung gian và Đủ lý do.",
                    "steps": "Giữ nhất quán nội hàm khái niệm (Đồng nhất) → Bác bỏ hai khẳng định trái ngược nhau (Không mâu thuẫn) → Tránh lập lờ nước đôi (Loại trừ trung gian) → Đòi hỏi bằng chứng đủ mạnh (Đủ lý do).",
                    "book_example": "Đánh tráo ‘người Việt’ gốc văn hóa với người mang hộ chiếu Việt Nam trong câu chuyện ăn phở vi phạm Luật Đồng nhất (tr. 89); mệnh đề ‘Trời đang mưa’ tại một thời điểm và địa điểm xác định chỉ có thể đúng hoặc sai (tr. 90).",
                },
                {
                    "name": "2. Suy luận Diễn dịch (Từ Quy tắc Chung → Trường hợp Cụ thể)",
                    "pages": "tr. 91–92",
                    "desc": "Đi từ tiền đề tổng quát xuống kết luận cụ thể. Một suy luận diễn dịch chỉ vững chắc khi ĐỒNG THỜI có cấu trúc hợp lệ VÀ các tiền đề ban đầu đúng sự thật.",
                    "steps": "Kiểm tra tính chân xác của Đại tiền đề → Kiểm tra Tiểu tiền đề → Rà soát cấu trúc tam đoạn luận để không mắc lỗi hình thức.",
                    "book_example": "Tam đoạn luận ‘Cá thở bằng mang; cá voi là cá → cá voi thở bằng mang’ (tr. 92) minh họa việc tiền đề sai dẫn thẳng tới kết luận sai dù hình thức có vẻ hợp lý.",
                },
                {
                    "name": "3. Suy luận Quy nạp (Từ Quan sát Cụ thể → Quy luật Khái quát)",
                    "pages": "tr. 93–94",
                    "desc": "Đi từ các dữ kiện riêng lẻ để phát hiện mẫu hình và hình thành giả thuyết rộng hơn—là động lực tạo tri thức mới nhưng luôn mang tính xác suất chứ không tuyệt đối.",
                    "steps": "Thu thập mẫu đủ lớn và đa dạng → Nhận diện quy luật lặp lại → Tránh tuyệt đối ‘Lỗi mẫu nhỏ’ (vơ đũa cả nắm) và ‘Ngoại suy quá giới hạn quan sát’.",
                    "book_example": "Gặp 3 người từ một địa phương cư xử thô bạo nơi công cộng rồi kết luận cả vùng đó đều thô bạo là lỗi mẫu nhỏ (tr. 94); thấy tiến sĩ giỏi chuyên môn hẹp rồi tin tiến sĩ phán lĩnh vực nào cũng đúng là ngoại suy quá đà (tr. 94).",
                },
                {
                    "name": "4. Suy luận Nhân quả 5 Tiêu chuẩn",
                    "pages": "tr. 95–96",
                    "desc": "Giúp phân biệt mối quan hệ nguyên nhân – kết quả thực sự với sự trùng hợp ngẫu nhiên hoặc tương quan giả tạo.",
                    "steps": "Kiểm tra đủ 5 yếu tố: (1) Tương quan, (2) Trật tự thời gian trước–sau, (3) Cơ chế tác động hợp lý, (4) Loại trừ yếu tố thứ ba gây nhiễu, và (5) Điều kiện bối cảnh.",
                    "book_example": "Trời nóng → bật điều hòa quạt mát → tiêu thụ điện tăng có đầy đủ trật tự thời gian và cơ chế (tr. 95); 4 người bạn dự tiệc cùng uống nước lọc rồi bị ngộ độc thì nước lọc có thể chỉ là yếu tố đi kèm chứ chưa chắc là thủ phạm (tr. 96).",
                },
                {
                    "name": "5. Suy luận Tương tự & 4 Điều kiện của Aristotle",
                    "pages": "tr. 97–98",
                    "desc": "Chuyển giao hiểu biết từ đối tượng A sang đối tượng B dựa trên các nét tương đồng—chỉ đáng tin khi điểm giống nhau gắn chặt với bản chất thuộc tính cần suy ra.",
                    "steps": "Đối chiếu 4 điều kiện Aristotle (tr. 97): (1) Số lượng điểm tương đồng, (2) Mức độ liên quan bản chất tới kết luận, (3) Không bỏ sót điểm khác biệt cốt tử, (4) Độ sâu sắc thay vì bề nổi.",
                    "book_example": "Ví dụ Cá mập và Hổ cùng là thú dữ ăn thịt nên suy ra hổ sống dưới nước (tr. 98) vi phạm cả tính liên quan lẫn việc bỏ sót điểm khác biệt sống còn (mang/vây so với phổi/chân).",
                },
            ],
        },
    },

    # =========================================================================
    # CHAPTER 6 · SYSTEMS THINKING (pp. 102–125)
    # =========================================================================
    "ch6": {
        "en": {
            "lead_summary": (
                "Opening Part III (Advanced Methods), Chapter 6 (pp. 102–125) shifts our lens from isolated snapshots to interconnected wholes—teaching Emergence, "
                "Peter Senge’s 11 Laws, Causal Loop Diagrams (CLD), Behavior-Over-Time (BOT) curves, and high-leverage structural interventions."
            ),
            "book_spotlight_example": {
                "title": "Book Example (pp. 115–118 & 123): Error-Hiding Teams, Startup Saturation, Painkillers & Bank Runs",
                "pages": "pp. 115–118, 123",
                "body": (
                    "Đào Minh Châu builds three full Causal Loop case studies (Figs. 6.3–6.7): (1) When managers punish mistakes, employees hide errors, killing organizational learning so defects surge—whereas treating errors as learning signals flips the loop so defects fall (pp. 115–116); "
                    "(2) Startup booms stall when market saturation (loop B1) overtakes entrepreneurial contagion (loop R1) unless policy expands technological innovation (pp. 116–117); "
                    "(3) Swallowing painkillers masks pain fast while the underlying illness worsens and fosters drug dependence (p. 118)."
                ),
                "takeaway": "To change a system’s behavior permanently, stop pushing harder on symptoms—redesign its feedback loops, delays, and incentives.",
            },
            "deep_elaboration": [
                "Launching Part III on page 101, Đào Minh Châu emphasizes that ‘Advanced Thinking Methods’ are NOT reserved for ivory-tower elites—everyone needs them daily, and anyone can master them once Parts I–II are in place. Quoting Ludwig von Bertalanffy and Donella Meadows (pp. 102–105), Chapter 6 defines a system as an organized, interdependent set of elements interacting toward a purpose over time, generating Emergent properties (‘tính trồi’) possessed by none of its isolated parts—just as life and consciousness belong to the living human body, never to a detached hand or organ (p. 105).",
                "Pages 106–110 synthesize 8 core systems principles into Peter Senge’s 11 Laws of the Fifth Discipline, illustrated with vivid everyday examples: banning a book or film makes more people hunt for it (‘the harder you push, the harder the system pushes back,’ p. 108); painkillers make behavior look better before getting worse (p. 108); a delicious restaurant expanding tables faster than kitchen capacity destroys the very quality that made it popular (p. 109); and inside a system, ‘there is no outside blame’ (p. 110).",
                "Pages 111–124 provide complete step-by-step blueprints for building Causal Loop Diagrams (Balancing loops ‘B’ like lions and gazelles in Fig. 6.1; Reinforcing loops ‘R’ like compound bank interest in Fig. 6.2; Delays ‘//’) and reading the three canonical Behavior-Over-Time graphs: S-shaped bounded growth (Fig. 6.8), delay-driven oscillation (Fig. 6.9), and runaway exponential collapse such as a bank run (Fig. 6.10, p. 123).",
            ],
            "sub_methods": [
                {
                    "name": "1. System Anatomy, Hierarchy & Emergence (Tính trồi)",
                    "pages": "pp. 103–105",
                    "desc": "Every system comprises Elements, Interconnections, Organization, Boundary, Environment, and Purpose—and every system is simultaneously made of subsystems and nested inside a suprasystem.",
                    "steps": "Draw an appropriate system boundary → Identify tangible & intangible elements → Ask what Emergent property arises strictly from their interaction.",
                    "book_example": "The human body (p. 105): circulatory, respiratory, and nervous subsystems interact to create living consciousness—yet the person is simultaneously one member inside a family and society.",
                },
                {
                    "name": "2. Peter Senge’s 11 Laws of Systems Thinking",
                    "pages": "pp. 106–110",
                    "desc": "Diagnostic laws explaining why linear common sense chronically backfires inside complex organizations, markets, and families.",
                    "steps": "Check whether today’s problem came from yesterday’s ‘fix’ → Look for compensating feedback → Respect natural growth limits → Separate distant causes from local symptoms → Abandon blame.",
                    "book_example": "Censoring a movie fuels curiosity (p. 108); taking painkillers hides worsening pathology (p. 108); an overcrowded restaurant ruins its own food quality (p. 109).",
                },
                {
                    "name": "3. Causal Loop Diagrams (CLD): Balancing (B), Reinforcing (R) & Delays (//)",
                    "pages": "pp. 111–119",
                    "desc": "Maps directional causal arrows (‘+’ same direction, ‘−’ opposite direction) to reveal self-correcting Balancing loops (B) and self-amplifying Reinforcing loops (R), plus time delays.",
                    "steps": "(1) Define the dynamic problem clearly → (2) Map all variables, ‘+ / −’ polarities, R/B loops, and time delays → (3) Locate high-leverage structural changes.",
                    "book_example": "Lions & gazelles population balance (Fig. 6.1, p. 112); compound savings account interest (Fig. 6.2, p. 113); plus the 3 full worked CLDs on error-hiding vs. learning (Figs. 6.3–6.4), startup ecosystems (Figs. 6.5–6.6), and symptom-patching (Fig. 6.7). Also notes on p. 120 why ‘Price → Revenue’ must be unpacked into Price → Demand → Revenue!",
                },
                {
                    "name": "4. Behavior-Over-Time (BOT) Graphs & Three System Archetypes",
                    "pages": "pp. 120–124",
                    "desc": "Plots system state on the vertical axis against time on the horizontal axis so teams read multi-year trajectories instead of reacting to single-day noise.",
                    "steps": "Plot historical trajectory over a wide time horizon → Classify curve shape (S-curve, Oscillation, or Runaway Exponential) → Infer which R/B loops and delays are dominating.",
                    "book_example": "Fig. 6.8 S-curve (human height growth or product adoption hitting saturation, p. 121); Fig. 6.9 Pendulum oscillation caused by delayed feedback (p. 122); Fig. 6.10 Runaway bank run collapse when depositor panic triggers further withdrawals (p. 123).",
                },
            ],
        },
        "vi": {
            "lead_summary": (
                "Mở đầu Phần III (Phương pháp Nâng cao), Chương 6 (tr. 102–125) chuyển tầm nhìn từ các lát cắt rời rạc sang chỉnh thể tương tác—làm chủ Tính trồi, "
                "11 Định luật của Peter Senge, Sơ đồ Vòng phản hồi Nhân quả (CLD) và Đồ thị Diễn biến Hành vi Theo Thời gian (BOT)."
            ),
            "book_spotlight_example": {
                "title": "Ví dụ Nguyên bản Trong Sách (tr. 115–118 & 123): Văn Hóa Giấu Lỗi, Khởi Nghiệp, Thuốc Giảm Đau & Đổ Vỡ Ngân Hàng",
                "pages": "tr. 115–118, 123",
                "body": (
                    "Tác giả Đào Minh Châu giải chi tiết 3 bài toán Vòng phản hồi (Hình 6.3–6.7): (1) Khi sếp trừng phạt lỗi, nhân viên giấu lỗi làm mất cơ hội học hỏi khiến lỗi ngày càng phình to—ngược lại, coi lỗi là bài học sẽ đảo chiều vòng lặp giúp lỗi giảm dần (tr. 115–116); "
                    "(2) Phong trào khởi nghiệp chững lại khi vòng bão hòa thị trường B1 lấn át vòng lan tỏa R1 nếu thiếu đổi mới công nghệ mở rộng thị trường (tr. 116–117); "
                    "(3) Uống thuốc giảm đau chỉ dập triệu chứng tạm thời trong khi căn bệnh gốc âm thầm nặng thêm và gây lệ thuộc thuốc (tr. 118)."
                ),
                "takeaway": "Muốn thay đổi hành vi của hệ thống một cách bền vững, đừng cố ép triệu chứng—hãy thiết kế lại cấu trúc vòng phản hồi, độ trễ và điểm đòn bẩy.",
            },
            "deep_elaboration": [
                "Ngay trang mở đầu Phần III (tr. 101), tác giả Đào Minh Châu khẳng định: ‘Phương pháp tư duy nâng cao’ không phải thứ cao siêu chỉ dành cho giới học giả, mà là công cụ thiết yếu hàng ngày ai cũng học được khi đã nắm vững các phương pháp cơ bản ở Phần II. Dẫn lời Ludwig von Bertalanffy và Donella Meadows (tr. 102–105), Chương 6 chỉ rõ đặc trưng cốt tử của hệ thống là Tính trồi (Emergence): cơ thể người có sự sống và ý thức nhờ các cơ quan tương tác với nhau—tách rời từng bộ phận thì không bộ phận nào tự có sự sống (tr. 105).",
                "Trang 106–110 cụ thể hóa 8 nguyên lý hệ thống thành 11 Định luật của Peter Senge với các ví dụ đời thường sắc sảo: sách/phim càng cấm càng đông người lùng xem (tr. 108); uống thuốc giảm đau làm bệnh tưởng đỡ trước khi nặng hơn (tr. 108); quán ăn ngon đông khách vội mở rộng quá sức khiến chất lượng sụt giảm và mất khách (tr. 109); và nguyên tắc ‘Không có sự đổ lỗi ra bên ngoài’ (tr. 110).",
                "Trang 111–124 hướng dẫn từng bước vẽ Sơ đồ Vòng phản hồi Nhân quả (Vòng cân bằng B như sư tử – nai ở Hình 6.1; Vòng tăng cường R như lãi kép tiền gửi tiết kiệm ở Hình 6.2) và cách đọc 3 dạng Đồ thị Diễn biến Theo Thời gian (BOT): đường chữ S (Hình 6.8), dao động do độ trễ như con lắc (Hình 6.9) và tăng trưởng bùng nổ dẫn tới sụp đổ như hiện tượng rút tiền hàng loạt ở ngân hàng (Hình 6.10, tr. 123).",
            ],
            "sub_methods": [
                {
                    "name": "1. Cấu trúc Hệ thống, Phân cấp & Tính trồi (Emergence)",
                    "pages": "tr. 103–105",
                    "desc": "Mọi hệ thống đều gồm Phần tử, Tương tác, Tổ chức, Ranh giới, Môi trường và Mục đích; mỗi bộ phận bản thân nó lại là một hệ thống con và toàn hệ thống nằm trong hệ thống lớn hơn.",
                    "steps": "Xác định ranh giới hệ thống hợp lý → Nhận diện cả yếu tố hữu hình và vô hình → Chỉ ra thuộc tính mới (tính trồi) sinh ra từ sự tương tác.",
                    "book_example": "Cơ thể con người (tr. 105): hệ tuần hoàn, hô hấp, thần kinh phối hợp tạo nên sự sống; bàn tay vừa là bộ phận của cơ thể vừa là hệ thống con, còn mỗi con người lại là phần tử của xã hội.",
                },
                {
                    "name": "2. Mười một Định luật Tư duy Hệ thống của Peter Senge",
                    "pages": "tr. 106–110",
                    "desc": "Bộ quy luật chẩn đoán vì sao các giải pháp tuyến tính ‘mì ăn liền’ luôn gây tác dụng ngược trong quản trị, chính sách và đời sống.",
                    "steps": "Kiểm tra xem vấn đề hôm nay có sinh ra từ ‘giải pháp’ hôm qua không → Tìm phản hồi bù trừ → Tôn trọng nhịp độ tăng trưởng tối ưu → Không đổ lỗi cá nhân rời rạc.",
                    "book_example": "Phim/sách bị cấm lại càng kích thích tò mò (tr. 108); thuốc giảm đau che lấp căn nguyên bệnh (tr. 108); quán ăn phát triển nóng quá ngưỡng phục vụ tự đánh mất uy tín (tr. 109).",
                },
                {
                    "name": "3. Sơ đồ Vòng Phản hồi Nhân quả (CLD): Cân bằng (B), Tăng cường (R) & Độ trễ",
                    "pages": "tr. 111–119",
                    "desc": "Vẽ mũi tên nhân quả thuận chiều (+) và ngược chiều (−) để nhận diện vòng tự điều chỉnh cân bằng (B), vòng khuếch đại tăng cường (R) và khoảng trễ thời gian.",
                    "steps": "(1) Phát biểu rõ vấn đề động → (2) Xác định biến số, chiều tác động (+/−), vòng lặp R/B và độ trễ → (3) Tác động vào điểm đòn bẩy làm đổi chiều hệ thống.",
                    "book_example": "Sư tử và nai trên đồng cỏ (Hình 6.1, tr. 112); tiền gửi tiết kiệm lãi mẹ đẻ lãi con (Hình 6.2, tr. 113); 3 ví dụ thực hành chi tiết về Giấu lỗi vs. Học từ lỗi (Hình 6.3–6.4), Hệ sinh thái khởi nghiệp (Hình 6.5–6.6), Chữa triệu chứng vs. Chữa gốc (Hình 6.7), cùng lưu ý tách mối quan hệ ‘Giá → Cầu → Doanh thu’ ở tr. 120.",
                },
                {
                    "name": "4. Đồ thị Diễn biến Hành vi Theo Thời gian (BOT — 3 Mẫu hình Kinh điển)",
                    "pages": "tr. 120–124",
                    "desc": "Biểu diễn biến số hệ thống trên trục tung và thời gian trên trục hoành để nhìn thấu xu hướng cấu trúc thay vì phản ứng giật cục theo sự kiện.",
                    "steps": "Chọn khung thời gian đủ dài → Vẽ đường diễn biến thực tế → Đối chiếu 3 mẫu hình (Chữ S, Dao động, Tăng vọt không giới hạn) để tìm cơ chế vòng lặp bên dưới.",
                    "book_example": "Hình 6.8 tăng trưởng chữ S (chiều cao con người, sản phẩm mới chạm ngưỡng bão hòa, tr. 121); Hình 6.9 dao động con lắc do độ trễ phản hồi (tr. 122); Hình 6.10 vòng xoáy rút tiền hàng loạt làm sụp đổ ngân hàng (tr. 123).",
                },
            ],
        },
    },

    # =========================================================================
    # CHAPTER 7 · STRATEGIC THINKING (pp. 127–141)
    # =========================================================================
    "ch7": {
        "en": {
            "lead_summary": (
                "Chapter 7 (pp. 127–141) elevates thinking onto a dynamic, multi-year, multi-actor chessboard—combining Dynamic SWOT/TOWS, PESTLE macro-scanning, "
                "Scenario Planning under uncertainty, and five Game Theory archetypes (including Fair Cake-Cutting and Rock–Paper–Scissors)."
            ),
            "book_spotlight_example": {
                "title": "Book Example (pp. 134–135 & 138): Protecting Bank Savings Against Inflation & The Fair Cake-Cutting Rule",
                "pages": "pp. 134–135, 138",
                "body": (
                    "How should an ordinary saver protect cash sitting in a bank account over the next 3 years? Đào Minh Châu walks through Scenario Planning (pp. 134–135): "
                    "isolating the 2 critical uncertainties—Inflation Rate and Deposit Interest Rate—to prepare distinct asset allocations ahead of time rather than guessing one forecast. "
                    "And on p. 138, he illustrates Game Theory’s elegance through Fair Cake-Cutting: when two children share a cake, ‘Person A cuts, Person B chooses first’ guarantees fairness without an outside referee!"
                ),
                "takeaway": "Strategic thinking shapes the future proactively—aligning scarce resources, anticipating rivals, and designing smart rules.",
            },
            "deep_elaboration": [
                "Opening with Leon Trotsky (“You may not be interested in strategy, but strategy is interested in you”) and Michael Porter (“Sound strategy starts with having the right goal,” p. 127), Đào Minh Châu traces strategy from Sun Tzu and Clausewitz to modern life and organizational leadership (pp. 128–129): strategy is a coherent master plan bridging today’s reality to a long-term vision amid resource constraints and uncertain environments.",
                "Pages 129–130 set out four strategic principles: (1) keep eyes on the overarching purpose (never win tactical skirmishes that lose the war), (2) combine long-term foresight with proactive shaping rather than passive prediction, (3) stay agile—abandoning obsolete assumptions and turning crises into openings, and (4) iterate continuously through reflection.",
                "Pages 130–140 present four interlocking strategic toolkits: action-oriented SWOT pairing, PESTLE 6-factor environmental scanning, 6-step Scenario Strategy construction, and five classic Game Theory models—Prisoner’s Dilemma, Chicken, Fair Cake-Cutting, Battle of the Sexes, and Rock–Paper–Scissors—showing readers how to identify *which* game they are actually playing before choosing a move (p. 141).",
            ],
            "sub_methods": [
                {
                    "name": "1. Action-Oriented Strategic SWOT / TOWS Pairing",
                    "pages": "pp. 130–131",
                    "desc": "Upgrades Chapter 4’s static diagnostic SWOT into dynamic strategic moves by actively cross-pairing internal Strengths/Weaknesses against external Opportunities/Threats.",
                    "steps": "Leverage Strengths to capture Opportunities → Use Strengths to shield against Threats → Fix Weaknesses to unlock Opportunities → Mitigate Weaknesses exposed to Threats.",
                    "book_example": "Using your strong digital/AI proficiency (Strength) to insulate your career against industry layoffs (Threat), or organizations pivoting to online operations during pandemic lockdowns (p. 131).",
                },
                {
                    "name": "2. PESTLE Macro-Environment Scanning",
                    "pages": "pp. 131–133",
                    "desc": "Prevents strategic tunnel vision by scanning six macro-forces before committing multi-year capital or career bets.",
                    "steps": "Scan Political, Economic (inflation, interest rates), Social (demographics, lifestyle), Technological (AI, automation), Legal (regulations, IP), and Environmental trends → Quantify impact → Integrate into strategy.",
                    "book_example": "Assessing how inflation, interest-rate shifts, demographic aging, and environmental rules reshape financial and project sustainability (p. 132).",
                },
                {
                    "name": "3. Six-Step Scenario Strategy Construction",
                    "pages": "pp. 133–135",
                    "desc": "Because single-line forecasts fail in volatile times, Scenario Planning maps plausible alternative futures around 2–3 critical uncertainties and prepares robust playbooks for each.",
                    "steps": "(1) Set time horizon (1, 3, 5, or 10 years) & goal → (2) Identify macro drivers → (3) Isolate <= 3 top uncertainties → (4) Construct plausible scenarios → (5) Design resilient actions for each → (6) Track early-warning signposts.",
                    "book_example": "Worked 3-year personal finance example (pp. 134–135): preserving the real value of bank deposits across combinations of high/low inflation and high/low interest rates.",
                },
                {
                    "name": "4. Game Theory’s Five Strategic Archetypes",
                    "pages": "pp. 136–139",
                    "desc": "Models interdependent decisions where your outcome depends directly on what other rational actors choose—teaching cooperation, deterrence, fair division, coordination, and unpredictability.",
                    "steps": "Identify players, options & payoffs → Diagnose which of the 5 games applies → Choose equilibrium or change the rules of the game.",
                    "book_example": "All 5 games taught in the book: (4.1) Prisoner’s Dilemma—factories dumping waste or rival ad wars (pp. 136–137); (4.2) Chicken—head-on brinkmanship where pride destroys both (p. 137); (4.3) Fair Cake-Cutting—‘one cuts, the other chooses’ (p. 138); (4.4) Battle of the Sexes—spouses coordinating weekend outings via turn-taking (pp. 138–139); (4.5) Rock–Paper–Scissors—mixed unpredictability when any predictable habit gets exploited (p. 139).",
                },
            ],
        },
        "vi": {
            "lead_summary": (
                "Chương 7 (tr. 127–141) nâng tầm tư duy lên bàn cờ dài hạn nhiều biến số và nhiều người chơi—kết hợp SWOT hành động, quét vĩ mô PESTLE, "
                "Xây dựng Chiến lược theo Kịch bản và 5 mô hình Lý thuyết Trò chơi (từ Song đề Tù nhân đến Chia bánh công bằng & Oẳn tù tỳ)."
            ),
            "book_spotlight_example": {
                "title": "Ví dụ Nguyên bản Trong Sách (tr. 134–135 & 138): Bảo Toàn Tiền Gửi Ngân Hàng & Luật ‘Chia Bánh Công Bằng’",
                "pages": "tr. 134–135, 138",
                "body": (
                    "Làm sao bảo toàn giá trị khoản tiền gửi tiết kiệm trong 3 năm tới? Tác giả Đào Minh Châu hướng dẫn từng bước Xây dựng Kịch bản (tr. 134–135): "
                    "lọc ra 2 yếu tố bất định then chốt nhất—Tỷ lệ lạm phát và Mức lãi suất—để chuẩn bị sẵn phương án phân bổ tài sản cho từng kịch bản thay vì đoán mò một con số. "
                    "Và ở trang 138, tác giả minh họa vẻ đẹp của Lý thuyết Trò chơi qua bài toán Chia bánh: quy tắc ‘Một người cắt, người kia chọn phần trước’ tự động buộc người cắt phải chia đều nhất có thể!"
                ),
                "takeaway": "Tư duy chiến lược không thụ động đoán tương lai mà chủ động định hình vị thế, phân bổ nguồn lực và nhận diện đúng luật chơi.",
            },
            "deep_elaboration": [
                "Mở đầu bằng câu nói của Leon Trotsky (‘Bạn có thể không quan tâm tới chiến lược, nhưng chiến lược quan tâm tới bạn’) và Michael Porter (‘Chiến lược có cơ sở bắt đầu từ mục đích đúng’, tr. 127), tác giả Đào Minh Châu dẫn dắt từ Tôn Tử, Clausewitz đến quản trị hiện đại (tr. 128–129): chiến lược là kế hoạch tổng thể nhất quán kết nối nguồn lực hiện tại với đích đến dài hạn trong môi trường đầy biến động.",
                "Trang 129–130 nêu 4 nguyên lý chủ chốt: (1) luôn bám sát bức tranh lớn và mục đích tối hậu, (2) tầm nhìn xa chủ động định hình tương lai thay vì phản ứng bị động, (3) linh hoạt thích ứng—dám từ bỏ giả định lỗi thời, và (4) suy ngẫm, đánh giá lặp lại thường xuyên.",
                "Trang 130–140 trang bị 4 nhóm công cụ sắc bén: SWOT định hướng hành động, Phân tích vĩ mô PESTLE, Quy trình 6 bước xây dựng chiến lược theo Kịch bản, và 5 trò chơi chiến lược kinh điển (Song đề tù nhân, Trò chơi Gà, Chia bánh công bằng, Cuộc chiến giới tính, Oẳn tù tỳ)—khép lại bằng lời dặn ở tr. 141: trước mọi nước đi, hãy tự hỏi mình đang ở trong trò chơi nào!",
            ],
            "sub_methods": [
                {
                    "name": "1. SWOT Chiến lược (Kết hợp Chủ động 4 Chiều)",
                    "pages": "tr. 130–131",
                    "desc": "Nâng cấp ma trận SWOT tĩnh ở Chương 4 thành các mũi giáp công chiến lược bằng cách ghép chéo Điểm mạnh/Điểm yếu nội tại với Cơ hội/Nguy cơ bên ngoài.",
                    "steps": "Dùng Điểm mạnh chớp Cơ hội → Dùng Điểm mạnh hóa giải Nguy cơ → Khắc phục Điểm yếu để đón Cơ hội → Thu hẹp Điểm yếu trước Nguy cơ.",
                    "book_example": "Dùng năng lực công nghệ tốt của bản thân (Điểm mạnh) để giảm thiểu nguy cơ bị sa thải (Nguy cơ); hoặc tổ chức tận dụng công nghệ số (Cơ hội) duy trì hoạt động giữa đại dịch phong tỏa (tr. 131).",
                },
                {
                    "name": "2. Phân tích Môi trường Vĩ mô PESTLE (6 Chiều)",
                    "pages": "tr. 131–133",
                    "desc": "Quét toàn diện 6 lực đẩy vĩ mô để chiến lược cá nhân hay doanh nghiệp không bị bất ngờ trước các cơn sóng lớn của thời cuộc.",
                    "steps": "Phân tích Chính trị (Political), Kinh tế (Economic), Xã hội (Social), Công nghệ (Technological), Pháp lý (Legal) và Môi trường (Environmental) → Định lượng tác động → Tích hợp vào kế hoạch.",
                    "book_example": "Đánh giá tác động của lạm phát, lãi suất, xu hướng tiêu dùng xã hội và tiêu chuẩn bền vững môi trường lên tính khả thi tài chính của dự án (tr. 132).",
                },
                {
                    "name": "3. Xây dựng Chiến lược Theo Kịch bản (Scenario Planning)",
                    "pages": "tr. 133–135",
                    "desc": "Thay vì đặt cược toàn bộ tương lai vào một dự báo duy nhất dễ sai, hãy xây dựng các kịch bản khả thi xoay quanh tối đa 2–3 yếu tố bất định then chốt nhất.",
                    "steps": "(1) Chọn khung thời gian (1, 3, 5, 10 năm) & mục tiêu → (2) Xác định động lực thay đổi → (3) Chọn <= 3 bất định then chốt → (4) Dựng các kịch bản → (5) Thiết kế đối sách cho từng kịch bản → (6) Theo dõi tín hiệu sớm.",
                    "book_example": "Bài toán thực tế trang 134–135: xây dựng chiến lược bảo toàn giá trị tiền gửi ngân hàng trong 3 năm trước hai ẩn số lớn nhất là tỷ lệ lạm phát và mức lãi suất.",
                },
                {
                    "name": "4. Năm Mô hình Lý thuyết Trò chơi Kinh điển",
                    "pages": "tr. 136–139",
                    "desc": "Phân tích các tình huống tương tác chiến lược nơi kết quả của bạn phụ thuộc trực tiếp vào lựa chọn của đối tác hoặc đối thủ.",
                    "steps": "Xác định người chơi, lựa chọn & lợi ích → Nhận diện đúng dạng trò chơi trong 5 mẫu hình → Chọn chiến lược hợp tác, nhượng bộ, chia phần hay biến hóa.",
                    "book_example": "Đủ 5 trò chơi nguyên bản trong sách: (4.1) Tiến thoái lưỡng nan của tù nhân—nhà máy xả thải, chạy đua quảng cáo (tr. 136–137); (4.2) Trò chơi Gà—đối đầu sát ván (tr. 137); (4.3) Chia bánh công bằng—người cắt không được chọn trước (tr. 138); (4.4) Cuộc chiến giới tính—hai vợ chồng chọn lịch cuối tuần và lần lượt nhượng bộ dài hạn (tr. 138–139); (4.5) Oẳn tù tỳ—chiến lược hỗn hợp tránh bị bắt bài (tr. 139).",
                },
            ],
        },
    },

    # =========================================================================
    # CHAPTER 8 · PROBABILISTIC THINKING (pp. 143–159)
    # =========================================================================
    "ch8": {
        "en": {
            "lead_summary": (
                "Chapter 8 (pp. 143–159) replaces our evolutionary craving for ‘100% certainty’ with Probabilistic Thinking—teaching Probability Distributions, "
                "Expected Value (EV) with Black-Swan ruin protection, Investment Probability Trees, Bayes’ Theorem, and core probability laws."
            ),
            "book_spotlight_example": {
                "title": "Book Example (pp. 151–155 & 157): The Investment Tree, The 99%-Accurate Medical Test & The Midnight Cab",
                "pages": "pp. 151–155, 157",
                "body": (
                    "A patient tests positive on a diagnostic test that is 99% sensitive with only a 2% false-positive rate, for a disease affecting 1% of the population (p. 154). "
                    "System 1 panics: ‘99% sure I’m sick!’ Đào Minh Châu works out Bayes’ Theorem step-by-step (p. 155): P(True Positive) = 0.01 × 0.99 = 0.0099, while P(False Positive) = 0.99 × 0.02 = 0.0198. "
                    "Total positives = 0.0297, so your actual chance of illness is 0.0099 / 0.0297 = 33.3%—two out of three positive results are false alarms!"
                ),
                "takeaway": "Thinking in calibrated probabilities won’t make every single bet win, but it guarantees fewer catastrophic errors over a lifetime (p. 148).",
            },
            "deep_elaboration": [
                "Quoting Bertrand Russell (“Uncertainty, in the presence of vivid hopes and fears, is painful, must be endured if we wish to live without the support of comforting myths”) and Voltaire (p. 143), Đào Minh Châu explains why humans struggle with uncertainty: System 1 evolved for split-second binary ‘safe vs. danger’ reactions, whereas modern finance, medicine, careers, and AI operate in shades of likelihood.",
                "Pages 144–149 build the conceptual foundation step-by-step: Theoretical, Empirical, and Subjective probability ($P(\\text{Heads}) + P(\\text{Tails}) = 1$); Probability Distributions across all mutually exclusive outcomes; and Mathematical Expected Value ($EV(X) = X_1 P_1 + X_2 P_2 + \\dots + X_n P_n$, p. 147). Crucially, on page 149, the author highlights Nassim Taleb’s caveat: a positive $EV$ is necessary but NOT sufficient—if any low-probability ‘Black Swan’ branch causes irreversible ruin or bankruptcy, you must reject or hedge the bet!",
                "Pages 150–159 provide two step-by-step calculation tools—Probability Trees (worked investment tree in Figs. 8.1–8.3) and Bayesian Updating (worked medical screening proof on pp. 154–155)—plus exercises including the famous Hit-and-Run Green/Red Cab mystery (p. 157) and a mathematical Appendix of addition/multiplication laws for independent and conditional events (pp. 158–159).",
            ],
            "sub_methods": [
                {
                    "name": "1. Theoretical, Empirical & Subjective Probability",
                    "pages": "pp. 144–146",
                    "desc": "Clarifies the three legitimate ways we assign numbers between 0 and 1 to uncertain future events.",
                    "steps": "Use symmetry/combinatorics for Theoretical probability → Use historical frequencies for Empirical probability → Use calibrated domain evidence & logic for Subjective probability.",
                    "book_example": "Flipping a fair coin ($P = 0.5$, theoretical, p. 145) vs. assessing that Football Team A has a 60% chance of beating Team B based on form, injuries, and tactics (subjective, p. 146).",
                },
                {
                    "name": "2. Probability Distributions, Expected Value (EV) & Black-Swan Protection",
                    "pages": "pp. 146–149",
                    "desc": "Weighs every possible payoff by its likelihood ($EV = \\sum X_i P_i$) while enforcing a hard survival floor against low-probability, catastrophic tail losses.",
                    "steps": "List all outcomes $X_1..X_n$ whose probabilities sum to 1 → Compute $EV = \\sum X_i P_i$ → Audit the worst-case branch: if loss causes ruin, decline or cap exposure even if $EV > 0$!",
                    "book_example": "Investment distribution analysis on pp. 147–149: why long-run positive EV wins over repeated trials, yet a single ruinous tail event overrides average math.",
                },
                {
                    "name": "3. Multi-Stage Probability Trees (Cây xác suất)",
                    "pages": "pp. 150–153",
                    "desc": "Maps sequential uncertain branches visually from top to bottom (or left to right), multiplying conditional probabilities along each path so every branch remains transparent.",
                    "steps": "Draw root decision/event → Branch Stage 1 outcomes (probabilities summing to 1) → Branch Stage 2 sub-outcomes from each node → Multiply along branches to get terminal path probabilities.",
                    "book_example": "Figures 8.1–8.3 (pp. 151–152): an ‘Invest’ root node splits into Profit (0.75) and Loss (0.25); Profit then splits into +5%, +10%, and +20% return tiers to compute exact joint probabilities.",
                },
                {
                    "name": "4. Bayesian Updating & Base-Rate Discipline (Suy luận Bayes)",
                    "pages": "pp. 153–159",
                    "desc": "Mathematically updates prior belief $P(A)$ when new evidence $B$ arrives via $P(A|B) = \\frac{P(A)P(B|A)}{P(B)}$, curing human Base-Rate Neglect.",
                    "steps": "Anchor on the objective Base Rate $P(b)$ first → Compute True Positives $P(b)P(d|b)$ → Compute False Positives $P(\\neg b)P(d|\\neg b)$ → Divide True Positives by ALL Positives.",
                    "book_example": "Full worked diagnostic proof on pp. 154–155 ($1\\%$ disease base rate, $99\\%$ sensitivity, $2\\%$ false positive $\\Rightarrow 33.3\\%$ posterior) + Exercise #3 on p. 157 (60% Green cabs / 40% Red cabs with an 85%-accurate witness reporting ‘Red’ $\\Rightarrow 20.9\\%$ chance the cab was actually Green!).",
                },
            ],
        },
        "vi": {
            "lead_summary": (
                "Chương 8 (tr. 143–159) giúp ta vượt qua cơn khát ‘chắc chắn 100%’ của bản năng bằng Tư duy Xác suất—làm chủ Phân bổ xác suất, "
                "Giá trị Kỳ vọng (EV) gắn với phòng vệ Thiên nga đen, Cây xác suất, Suy luận Bayes và Phụ lục công thức xác suất cốt lõi."
            ),
            "book_spotlight_example": {
                "title": "Ví dụ Nguyên bản Trong Sách (tr. 151–155 & 157): Cây Xác Suất Đầu Tư, Xét Nghiệm 99% & Chiếc Taxi Đêm Mưa",
                "pages": "tr. 151–155, 157",
                "body": (
                    "Một căn bệnh có tỷ lệ mắc nền trong dân số là 1% ($P(b)=0,01$). Xét nghiệm có độ nhạy phát hiện bệnh tới 99% và tỷ lệ dương tính giả chỉ 2% (tr. 154). "
                    "Khi cầm tờ kết quả dương tính, trực giác tưởng chắc chắn 99% đã mắc bệnh! Nhưng tác giả Đào Minh Châu tính tường minh bằng Bayes (tr. 155): Dương tính thật = $0,01 \\times 0,99 = 0,0099$; Dương tính giả = $0,99 \\times 0,02 = 0,0198$. "
                    "Xác suất thực sự mắc bệnh chỉ là $0,0099 / 0,0297 \\approx 33\\%$—tức cứ 3 người dương tính thì có tới 2 người khỏe mạnh!"
                ),
                "takeaway": "Tư duy xác suất không biến ta thành nhà tiên tri biết chắc mọi chuyện, nhưng giúp ta ít sai lầm hơn hẳn theo thời gian dài hạn (tr. 148).",
            },
            "deep_elaboration": [
                "Mở đầu bằng lời của Bertrand Russell và Voltaire—‘Sự nghi ngờ không phải là một trạng thái dễ chịu, nhưng sự chắc chắn là một điều lố bịch’ (tr. 143)—tác giả Đào Minh Châu chỉ rõ rào cản tâm lý lớn nhất: bộ não tiến hóa ưa câu trả lời nhị nguyên ‘có/không’, trong khi thế giới thực vận hành bằng các mức độ khả năng.",
                "Trang 144–149 xây dựng nền tảng khái niệm mạch lạc từ 3 dạng xác suất (Lý thuyết, Thực nghiệm, Chủ quan), Phân bổ xác suất đến công thức Giá trị Kỳ vọng ($EV(X) = X_1 P_1 + X_2 P_2 + \\dots + X_n P_n$, tr. 147). Đặc biệt ở trang 149, tác giả nhấn mạnh nguyên tắc sống còn: EV dương là điều kiện cần nhưng CHƯA ĐỦ—nếu có một kịch bản xác suất rất nhỏ (‘Thiên nga đen’) gây hậu quả sụp đổ không thể gượng dậy, ta tuyệt đối không đánh cược mù quáng!",
                "Trang 150–159 hướng dẫn chi tiết hai công cụ tính toán trực quan—Cây xác suất (ví dụ đầu tư Hình 8.1–8.3) và Suy luận Bayes (bài toán chẩn đoán y khoa tr. 154–155)—kèm bài tập trinh thám Taxi Xanh – Đỏ nổi tiếng (tr. 157) và Phụ lục hệ thống hóa toàn bộ công thức cộng, nhân xác suất có điều kiện (tr. 158–159).",
            ],
            "sub_methods": [
                {
                    "name": "1. Ba Dạng Xác suất: Lý thuyết, Thực nghiệm & Chủ quan",
                    "pages": "tr. 144–146",
                    "desc": "Phân biệt rõ cơ sở định lượng khả năng xảy ra của sự kiện trong toán học, thống kê dữ liệu lịch sử và đánh giá chuyên gia.",
                    "steps": "Dùng tính đối xứng cho Xác suất lý thuyết → Dùng tần suất quan sát lặp lại cho Xác suất thực nghiệm → Dùng thông tin nền & lập luận logic cho Xác suất chủ quan.",
                    "book_example": "Tung đồng xu cân đối ($P(\\text{ngửa}) + P(\\text{sấp}) = 1$, lý thuyết, tr. 145) so với đánh giá đội bóng A có 60% khả năng thắng đội B dựa trên phong độ và đội hình (chủ quan, tr. 146).",
                },
                {
                    "name": "2. Phân bổ Xác suất, Giá trị Kỳ vọng (EV) & Phòng vệ Thiên nga Đen",
                    "pages": "tr. 146–149",
                    "desc": "Liệt kê đầy đủ các kịch bản thành – bại cùng trọng số xác suất để tính kỳ vọng toán học, đồng thời kiểm soát rủi ro phá sản ở đuôi phân phối.",
                    "steps": "Liệt kê đủ các phương án kết quả $X_1..X_n$ (tổng xác suất = 1) → Tính $EV = \\sum X_i P_i$ → Kiểm tra kịch bản xấu nhất: nếu vượt sức chịu đựng thì không đầu tư dù $EV > 0$.",
                    "book_example": "Phân tích quyết định đầu tư ở tr. 147–149: cập nhật lại xác suất linh hoạt khi có phản hồi mới từ khách hàng hoặc thị trường.",
                },
                {
                    "name": "3. Cây Xác suất Đa tầng (Probability Tree)",
                    "pages": "tr. 150–153",
                    "desc": "Sơ đồ hóa chuỗi sự kiện nhiều giai đoạn giúp nhìn rõ toàn bộ các nhánh kết quả và tính chính xác xác suất tích của từng nhánh.",
                    "steps": "Vẽ nút gốc hành động → Tách các nhánh bước 1 (ghi xác suất trên mũi tên, tổng = 1) → Tách tiếp các nhánh con bước 2 → Nhân dọc theo đường đi để ra xác suất cuối.",
                    "book_example": "Hình 8.1–8.3 (tr. 151–152): từ nút gốc ‘Đầu tư’ tách nhánh ‘Lãi’ (0,75) và ‘Lỗ’ (0,25); từ nút ‘Lãi’ tách tiếp 3 mức lãi 5%, 10%, 20% để tính kỳ vọng toàn diện.",
                },
                {
                    "name": "4. Suy luận Bayes & Kỷ luật Tỷ lệ Nền (Base Rate)",
                    "pages": "tr. 153–159",
                    "desc": "Công thức toán học cập nhật niềm tin ban đầu $P(A)$ khi xuất hiện bằng chứng mới $B$, giúp khắc phục lỗi bỏ quên xác suất cơ sở.",
                    "steps": "Xác định Tỷ lệ nền $P(b)$ trước tiên → Tính nhánh Dương tính thật $P(b)P(d|b)$ → Tính nhánh Dương tính giả $P(\\neg b)P(d|\\neg b)$ → Lấy Dương tính thật chia cho Tổng mọi ca dương tính.",
                    "book_example": "Lời giải chi tiết bài toán xét nghiệm bệnh ra kết quả 33,3% (tr. 154–155) và Bài tập #3 trang 157 (Thành phố có 60% Taxi Xanh, 40% Taxi Đỏ, nhân chứng nhìn đúng 85% khai xe gây tai nạn màu Đỏ $\\Rightarrow$ vẫn có 20,9% khả năng xe thật là màu Xanh!).",
                },
            ],
        },
    },

    # =========================================================================
    # CHAPTER 9 · SCIENTIFIC THINKING (pp. 160–171)
    # =========================================================================
    "ch9": {
        "en": {
            "lead_summary": (
                "Capstone Chapter 9 (pp. 160–170) & the Epilogue (p. 171) unite ALL eight previous thinking methods inside the 7-Step Scientific Method—turning empirical observation, "
                "Popperian falsifiability, and controlled experimentation into an everyday life discipline."
            ),
            "book_spotlight_example": {
                "title": "Book Example (pp. 163, 166–167 & 171): Explaining Early Readers, Solving Office Fatigue & The Bird in Your Hand",
                "pages": "pp. 163, 166–167, 171",
                "body": (
                    "Scientific thinking works right at your desk (pp. 166–167): suppose you feel exhausted at work despite normal sleep and meals. "
                    "Saying ‘a ghost cursed my desk’ fails Popper’s falsifiability test (p. 167). Instead, you formulate testable hypotheses (stuffy CO2 in the room, dehydration, unbroken screen glare), "
                    "change ONE controlled variable for a week while keeping others constant, measure afternoon energy, and revise if refuted! "
                    "Then on page 171, the wise teacher answers the boy’s ‘Is the bird alive or dead?’ trap: ‘Whether it lives or dies lies in your hands.’"
                ),
                "takeaway": "Science is the grand convergence where Creative hypotheses, Critical skepticism, Analytical dissection, Logical deduction, Systems context, Strategic design, and Probabilistic testing work as one.",
            },
            "deep_elaboration": [
                "Opening with Carl Sagan (“Science is a way of thinking much more than it is a body of knowledge”), P. J. O’Rourke, and Bertrand Russell (p. 160), Đào Minh Châu dispels the myth that scientific thinking belongs only to laboratory researchers: treating science as a daily cognitive method empowers anyone to distinguish fact from fiction, overcome superstition, and solve practical problems on solid evidence (p. 161).",
                "Pages 162–163 organize scientific principles into Foundational Principles—Empiricism (astronomy proving Earth orbits the Sun rather than myth, p. 162), Objectivity, Falsifiability (why ‘we are reincarnations of past lives’ cannot be tested or refuted, p. 163), and Replicability (a new cancer drug is valid only when independent labs reproduce the result, p. 163)—and Methodological Principles such as generating multiple competing hypotheses (e.g., explaining why some children read early via genetics, home reading environment, pedagogy, or media exposure, p. 163).",
                "Pages 164–167 unveil the book’s architectural climax (Figure 9.1): as you step through the 7 stages of the Scientific Method, Đào Minh Châu explicitly maps how Creative, Critical, Analytical, Logical, Systems, Strategic, and Probabilistic thinking each power specific stages of the loop—before closing on page 171 with the unforgettable parable of the bird in the reader’s own hands.",
            ],
            "sub_methods": [
                {
                    "name": "1. Empiricism, Falsifiability (Popper) & Independent Replication",
                    "pages": "pp. 162–163",
                    "desc": "Separates genuine testable claims from unfalsifiable dogma, superstition, and one-off flukes.",
                    "steps": "Ask ‘What conceivable observation would prove this claim wrong?’ (Falsifiability) → Demand empirical measurement over anecdote → Verify independent replication & alternative hypotheses.",
                    "book_example": "‘Past-life reincarnation’ or ‘work fatigue caused by ghosts’ cannot be falsified by any experiment (pp. 163, 167); early childhood reading requires testing rival hypotheses rather than jumping to one story (p. 163).",
                },
                {
                    "name": "2. The 7-Step Scientific Method & Grand Convergence of All 8 Methods",
                    "pages": "pp. 164–166",
                    "desc": "Figure 9.1 unites every chapter of Đào Minh Châu’s book into one self-correcting feedback cycle.",
                    "steps": "(1) Purposeful Observation → (2) Question [Creative + Critical] → (3) Falsifiable Hypothesis [Creative + Logical] → (4) Controlled Experiment Design [Strategic + Systems + Logical] → (5) Data Analysis [Analytical + Probabilistic + Logical + Systems] → (6) Conclusion / Revise Hypothesis if Refuted → (7) Peer Communication & Critique [Critical].",
                    "book_example": "Pages 164–166 explicitly annotate which chapters from Parts II and III activate at each of the 7 steps—proving the nine chapters form one integrated organism.",
                },
                {
                    "name": "3. Everyday Controlled Experimentation (Solving Work Fatigue)",
                    "pages": "pp. 166–167",
                    "desc": "Applies controlled variable testing to personal productivity, health, management, or teaching without needing a laboratory.",
                    "steps": "Observe anomaly → Formulate concrete testable hypothesis → Change ONE factor while holding sleep/diet constant → Measure outcome → Keep if supported, revise hypothesis if refuted.",
                    "book_example": "Full everyday walkthrough on pp. 166–167 diagnosing unexplained daytime fatigue at work and avoiding the 4 common experimental errors (unfalsifiable claims, uncontrolled confounders, biased interpretation, skipping peer feedback).",
                },
                {
                    "name": "4. Epilogue Synthesis: The Boy, The Teacher & The Bird in Your Hand",
                    "pages": "p. 171",
                    "desc": "Reframes a rigged binary trap and hands agency back to the reader: methods on paper live only through conscious daily practice.",
                    "steps": "Spot rigged ‘Either/Or’ traps → Step up to the causal agent’s level → Practice the 9 methods in real decisions until they become second nature.",
                    "book_example": "A mischievous schoolboy cups a live bird behind his back to trap his teacher (‘Alive or dead?’). She answers: ‘If you want it to live, it lives; if you want it to die, it dies—it lies in your hands’—through thinking! (p. 171).",
                },
            ],
        },
        "vi": {
            "lead_summary": (
                "Chương 9 (tr. 160–170) cùng Lời kết (tr. 171) là đỉnh hội tụ của toàn bộ cuốn sách: tích hợp cả 8 phương pháp tư duy trước đó vào Quy trình Phương pháp Khoa học 7 bước—"
                "biến tính khả bác bỏ (Popper) và thực nghiệm có kiểm soát thành thói quen giải quyết vấn đề hàng ngày."
            ),
            "book_spotlight_example": {
                "title": "Ví dụ Nguyên bản Trong Sách (tr. 163, 166–167 & 171): Trẻ Biết Đọc Sớm, Chứng Mệt Mỏi Khi Làm Việc & Con Chim Trong Tay",
                "pages": "tr. 163, 166–167, 171",
                "body": (
                    "Tư duy khoa học vận hành ngay trong đời sống hàng ngày (tr. 166–167): bạn thấy mệt mỏi khi làm việc dù ăn ngủ bình thường. "
                    "Nếu phán ‘do ma ám’ thì không cách nào kiểm chứng hay bác bỏ được (tr. 167). Thay vào đó, bạn đặt giả thuyết kiểm chứng được (phòng bí thiếu oxy, ngồi nhìn màn hình liên tục, thiếu nước), "
                    "thử nghiệm thay đổi TỪNG yếu tố trong khi giữ nguyên các yếu tố khác, đo kết quả và sẵn sàng sửa giả thuyết nếu sai! "
                    "Khép lại ở trang 171 là câu trả lời bất hủ của cô giáo trước cái bẫy của cậu học trò: ‘Con chim sống hay chết nằm trong tay em—bằng tư duy!’"
                ),
                "takeaway": "Phương pháp khoa học là nơi Sáng tạo, Phản biện, Phân tích, Logic, Hệ thống, Chiến lược và Xác suất hợp lực thành một chu trình tự sửa sai hoàn chỉnh.",
            },
            "deep_elaboration": [
                "Mở đầu bằng châm ngôn của Carl Sagan—‘Khoa học là một cách tư duy hơn là một khối kiến thức’ (tr. 160)—tác giả Đào Minh Châu xóa bỏ định kiến rằng tư duy khoa học chỉ dành cho nhà nghiên cứu trong phòng thí nghiệm: coi khoa học là phương pháp tư duy giúp mỗi người tự phân biệt sự thật với hư cấu, vượt qua mê tín và nâng cao chất lượng quyết định trong mọi lĩnh vực đời sống (tr. 161).",
                "Trang 162–163 chia hệ nguyên lý thành hai nhóm chặt chẽ: Nguyên lý Nền tảng gồm Thực nghiệm (nhờ quan sát thiên văn mới biết Trái Đất quay quanh Mặt Trời, tr. 162), Khách quan, Khả năng bị bác bỏ (Falsifiability—ví dụ khẳng định ‘chúng ta là tái sinh của kiếp trước’ không có cách nào kiểm chứng bác bỏ nên không mang tính khoa học, tr. 163) và Khả năng tái lập (thuốc trị ung thư mới phải được các phòng thí nghiệm độc lập lặp lại kết quả, tr. 163); cùng Nguyên lý Phương pháp luận đòi hỏi luôn xét nhiều giả thuyết cạnh tranh (như hiện tượng trẻ biết đọc sớm, tr. 163).",
                "Trang 164–167 trình bày cao trào kiến trúc của toàn sách (Hình 9.1): đi qua từng bước trong 7 bước của Phương pháp Khoa học, tác giả chỉ rõ tư duy Sáng tạo, Phản biện, Phân tích, Logic, Hệ thống, Chiến lược và Xác suất lần lượt tham gia ở bước nào—trước khi trao lại quyền tự chủ cho người đọc qua câu chuyện Con chim trong tay ở trang 171.",
            ],
            "sub_methods": [
                {
                    "name": "1. Chủ nghĩa Thực nghiệm, Khả năng Bác bỏ (Popper) & Tính Tái lập",
                    "pages": "tr. 162–163",
                    "desc": "Tiêu chuẩn phân ranh giới rạch ròi giữa tri thức khoa học đáng tin cậy với niềm tin mù quáng, mê tín hay ngụy khoa học.",
                    "steps": "Hỏi ngay ‘Bằng chứng thực tế nào nếu xảy ra sẽ chứng minh khẳng định này sai?’ (Falsifiability) → Đòi dữ liệu quan sát/thí nghiệm → Kiểm tra tính tái lập độc lập & các giả thuyết thay thế.",
                    "book_example": "Khẳng định ‘kiếp trước tái sinh’ (tr. 163) hay ‘mệt mỏi do ma ám’ (tr. 167) không thể bác bỏ bằng thực nghiệm; hiện tượng trẻ biết đọc sớm cần đặt nhiều giả thuyết (di truyền, môi trường sách gia đình, phương pháp dạy) để kiểm tra (tr. 163).",
                },
                {
                    "name": "2. Chu trình Phương pháp Khoa học 7 Bước & Sự Hội tụ của 8 Phương pháp",
                    "pages": "tr. 164–166",
                    "desc": "Hình 9.1 kết nối toàn bộ 8 phương pháp ở các chương trước thành một vòng lặp kiểm chứng và tự hiệu chỉnh liên tục.",
                    "steps": "(1) Quan sát chủ đích → (2) Đặt câu hỏi [Sáng tạo + Phản biện] → (3) Hình thành giả thuyết [Sáng tạo + Logic] → (4) Thiết kế & chạy thí nghiệm kiểm soát [Chiến lược + Hệ thống + Logic] → (5) Phân tích dữ liệu [Phân tích + Xác suất + Logic + Hệ thống] → (6) Kết luận / Sửa giả thuyết nếu bị bác bỏ → (7) Chia sẻ để cộng đồng phản biện [Phản biện].",
                    "book_example": "Trang 164–166 chỉ rõ vai trò cụ thể của từng phương pháp tư duy ở từng mắt xích của Hình 9.1.",
                },
                {
                    "name": "3. Thực nghiệm Có Kiểm soát Trong Đời sống Hàng ngày",
                    "pages": "tr. 166–167",
                    "desc": "Ứng dụng ngay quy trình khoa học vào công việc, sức khỏe và học tập cá nhân mà không cần thiết bị phòng thí nghiệm phức tạp.",
                    "steps": "Quan sát triệu chứng bất thường → Đặt giả thuyết cụ thể kiểm tra được → Thay đổi TỪNG yếu tố trong khi giữ cố định các yếu tố nhiễu khác → Đo lường kết quả → Điều chỉnh tiếp.",
                    "book_example": "Ví dụ thực tế trang 166–167 tìm nguyên nhân chứng mệt mỏi khi làm việc dù ăn ngủ bình thường, kèm 4 lỗi phổ biến cần tránh khi làm thực nghiệm.",
                },
                {
                    "name": "4. Lời kết Toàn sách: Cậu Học Trò, Cô Giáo & Con Chim Trong Tay Bạn",
                    "pages": "tr. 171",
                    "desc": "Phá vỡ cái bẫy nhị nguyên ‘Sống hay Chết’ bằng tư duy thấu suốt và nhắn gửi thông điệp thực hành cuối sách.",
                    "steps": "Nhận diện khung câu hỏi gài bẫy → Nhìn thẳng vào chủ thể nắm quyền quyết định → Biến kiến thức trong sách thành hành động rèn luyện mỗi ngày.",
                    "book_example": "Cậu học trò giấu con chim sống sau lưng đố cô giáo sống hay chết; bằng tư duy, cô trả lời: ‘Em muốn nó sống thì nó sống, em muốn nó chết thì nó chết—nó nằm trong tay em!’ (tr. 171).",
                },
            ],
        },
    },
}
