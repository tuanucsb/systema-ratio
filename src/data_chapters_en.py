# -*- coding: utf-8 -*-
"""English chapter, floor, and research-thread content for Systema Ratio."""

META_EN = {
    "lang": "en",
    "other_lang": "vi",
    "other_href": "vi.html",
    "other_label": "Tiếng Việt",
    "lang_badge": "EN",
    "site_title": "Systema Ratio · Based on the Book Học Tư Duy (Learning How to Think) by Đào Minh Châu",
    "brand_name": "Systema Ratio",
    "brand_sub": "Book by Đào Minh Châu",
    "skip_text": "Skip to main content",
    "nav": {
        "overview": "Overview",
        "reader": "9 Methods",
        "atlas": "Method Map",
        "labs": "7 Labs",
        "traps": "Biases",
        "plates": "24 Plates",
        "cases": "Case Studies",
    },
    "depth_label": "Educator lens",
    "depth_badge": "TEACH",
    "theme_light": "Switch to light theme",
    "theme_dark": "Switch to dark theme",
    "hero": {
        "eyebrow": "Based on the Book Học Tư Duy (Learning How to Think) · By Author Đào Minh Châu (2026)",
        "title_main": "Learning How to Think: ",
        "title_accent": "9 Methods of Conscious Reason.",
        "lede": (
            "An interactive illustrated companion to Đào Minh Châu’s book Học Tư Duy (Hà Nội, 2026, 171 pp.). "
            "Explore every thinking method, guiding principle, step-by-step tool, and original book example across Part I (Conscious Thinking), "
            "Part II (Creative, Critical, Analytical & Logical Thinking), and Part III (Systems, Strategic, Probabilistic & Scientific Thinking)—followed by 7 live simulators and 36 real-world case studies."
        ),
        "cta_primary": "Explore 29-Tool Map →",
        "cta_secondary": "Open 7 Thinking Labs",
        "cta_plates": "View 24 Vector Plates",
        "kpis": [
            {"num": "3 → 9", "lbl": "Parts & Chapters (1 Foundation · 4 Core · 4 Advanced)"},
            {"num": "29", "lbl": "Actionable cognitive tools & decision frameworks"},
            {"num": "10 + 9", "lbl": "System 1 biases (with Vietnamese proverbs) & fallacies"},
            {"num": "18", "lbl": "Vector SVG plates designed for print & interactive study"},
        ],
    },
    "ai_era": {
        "eyebrow": "Preface · Why Practice Thinking in the Age of AI?",
        "title": "AI will not make you irrelevant—unless you let it think in your place",
        "cards": [
            {
                "tag": "Popper × Buddhist Wisdom",
                "head": "Suffering as Unsolved Problems",
                "body": "If 'life is suffering' and 'all life is problem solving' (Popper, 1999), then suffering persists whenever we lack the methods to untangle the problems before us. Better thinking is a practical path toward liberation.",
            },
            {
                "tag": "Harari × Cognitive Atrophy",
                "head": "From Exploitation to Irrelevance",
                "body": "In the 20th century, workers fought against exploitation; in the 21st, Harari warns of cognitive irrelevance. Research (Loga, 2025) shows that delegating thought to AI steadily weakens independent judgment.",
            },
            {
                "tag": "Jensen Huang’s Rule",
                "head": "Turn AI into a Sparring Partner",
                "body": "'AI won’t take your job. Somebody using AI will take your job.' Commanding, auditing, and co-creating with AI requires conscious human mastery of framing, critique, logic, systems, and probability.",
            },
            {
                "tag": "Two Core Audiences",
                "head": "Young Adults (18–30) & Educators",
                "body": "Written for young people making foundational life choices and for teachers from high school to university who teach students how to think through the living substance of their subjects.",
            },
        ],
    },
    "floors_heading": "Four floors of conscious reason",
    "floors_sub": (
        "Read from the ground up. System 1 runs automatically at the base; Chapter 1 installs the conscious metacognitive gate; "
        "Part II builds four core instruments; Part III integrates them into four advanced syntheses—which feed back down into better intuition."
    ),
    "simon_loop": (
        "Herbert Simon’s Consolidation Loop (p. 22): 'Intuition is nothing more and nothing less than recognition.' "
        "Whenever Floor 2 and Floor 3 practice disciplined methods consciously, those patterns store into memory and upgrade Ground Floor intuition."
    ),
    "floors": [
        {
            "id": "floor-0",
            "num": "Ground Floor · System 1",
            "name": "Instinct, Memory & Heuristics",
            "one": "Fast, effortless, always awake—and systematically tricked by complex reality.",
            "badge": "Automatic · ~95% of daily life",
            "color": "var(--c-trap)",
            "story": (
                "Daniel Kahneman’s System 1 spots danger in a split second (leaping away from a dark coil near your foot). "
                "It relies on memory recognition and three shortcuts: Question Substitution ('Is it true?' → 'Is it familiar?'), "
                "Rapid Norms, and WYSIATI ('What You See Is All There Is'). Without supervision, mistakes are not the exception—they are our default state."
            ),
            "links": [("Inspect 10 Biases", "traps"), ("Read Chapter 1", "reader:ch1")],
        },
        {
            "id": "floor-1",
            "num": "Floor 1 · Part I (Ch. 1)",
            "name": "The Conscious Metacognitive Gate",
            "one": "Slowing down is not enough—System 2 needs an explicit 8-element architecture.",
            "badge": "Paul & Elder · 8 Elements",
            "color": "var(--c-meta)",
            "story": (
                "A crucial paradox of Chapter 1: slow thinking can still be wrong if System 2 merely rationalizes System 1’s hunches. "
                "Conscious thinking places thought inside an explicit 8-element dynamic frame—Purpose, Key Question, Point of View, Assumptions, "
                "Information, Concepts/Inference, Conclusions, and Implications—embedded in real historical and social Context."
            ),
            "links": [("Open 8-Element Lab", "labs:octagon"), ("Plate 1.2", "plates:p03")],
        },
        {
            "id": "floor-2",
            "num": "Floor 2 · Part II (Ch. 2–5)",
            "name": "The Four Core Instruments",
            "one": "Generate ideas (Creative), filter truth (Critical), dissect structure (Analytical), validate inferences (Logical).",
            "badge": "4 Methods · 18 Core Tools",
            "color": "var(--c-critical)",
            "story": (
                "No single core method suffices alone. Creative Thinking expands the space of possibilities (diverge then converge). "
                "Critical Thinking acts as the mind’s immune system. Analytical Thinking disassembles the watch to reveal root causes. "
                "Logical Thinking enforces the objective grammar connecting premises to conclusions."
            ),
            "links": [("Explore in Method Atlas", "atlas"), ("Try Wald Bomber Lab", "labs:wald")],
        },
        {
            "id": "floor-3",
            "num": "Floor 3 · Part III (Ch. 6–9)",
            "name": "The Four Advanced Syntheses",
            "one": "Navigate wholes & feedback (Systems), competing agency (Strategic), uncertainty (Probabilistic), and empirical truth (Scientific).",
            "badge": "4 Methods · 11 Advanced Tools",
            "color": "var(--c-science)",
            "story": (
                "'Advanced' does not mean esoteric—everyone needs these four lenses daily, but they rest directly on Floor 2. "
                "Systems Thinking reveals feedback loops and delays; Strategic Thinking guides action amid uncertainty and rival interests; "
                "Probabilistic Thinking replaces binary 'yes/no' with Expected Value and Bayes; Scientific Thinking unites all eight methods to test falsifiable hypotheses."
            ),
            "links": [("Run Systems & Bayes Labs", "labs:systems"), ("Scientific Engine", "labs:science")],
        },
    ],
    "threads_heading": "Six structural questions through the book",
    "threads_sub": "Click any question to see the book’s diagnosis, its visual model, and where to practice it.",
    "threads": [
        {
            "q": "Why can 'thinking slowly' still produce terrible decisions?",
            "tag": "Ch. 1 · Dual-System Paradox",
            "color": "var(--c-meta)",
            "ans": (
                "Because System 2 is both effort-averse and easily co-opted as System 1’s press secretary—inventing clever reasons for conclusions already chosen by emotion or anchoring (pp. 18–19). "
                "Speed is not the differentiator; conscious structure is. Until you audit your Assumptions, Point of View, and Information inside Paul & Elder’s 8-element octagon, slow thinking is just slow rationalization."
            ),
            "target": "labs:octagon",
            "cta": "Test on the 8-Element Octagon →",
        },
        {
            "q": "Why did engineers want to armor the wrong part of WWII bombers?",
            "tag": "Ch. 2 · Inversion & WYSIATI",
            "color": "var(--c-creative)",
            "ans": (
                "Returning bombers were covered in bullet holes along the wings and fuselage, while engines and cockpits were clean (pp. 30–31). "
                "System 1 ('What You See Is All There Is') said: armor the red dots. Mathematician Abraham Wald inverted the question: where are the missing planes? "
                "Hits to the engines and cockpit brought planes down—so the unmarked zones on survivors were the fatal vulnerabilities."
            ),
            "target": "labs:wald",
            "cta": "Click the WWII Bomber Simulator →",
        },
        {
            "q": "Why does 'fixing' a problem today often make it worse six months later?",
            "tag": "Ch. 6 · Senge’s Laws & Delayed Loops",
            "color": "var(--c-systems)",
            "ans": (
                "Linear thinking treats symptoms (painkillers for a fever, an iPad to quiet a crying toddler, punishing employees who report errors). "
                "In Systems Thinking (pp. 107–118), symptomatic fixes create a fast Balancing loop (B) that masks the problem while a delayed Reinforcing loop (R, marked '//') quietly compounds the underlying disease or fear."
            ),
            "target": "labs:systems",
            "cta": "Simulate R/B Loops & Delays →",
        },
        {
            "q": "Why does a 99%-accurate medical test mean only a 33% chance you are sick?",
            "tag": "Ch. 8 · Base-Rate Neglect & Bayes",
            "color": "var(--c-prob)",
            "ans": (
                "When a disease affects 1 in 100 people (base rate P(b) = 0.01) and a test has 99% sensitivity but a 2% false-positive rate (pp. 154–155), "
                "testing 10,000 people yields ~99 true positives alongside ~198 false positives from the 9,900 healthy people! "
                "Out of 297 positive results, only 99 are genuinely ill (33.3%)—yet your risk still jumped 33× above the baseline."
            ),
            "target": "labs:bayes",
            "cta": "Explore the 100-Person Bayes Grid →",
        },
        {
            "q": "When two rational people each pick their 'best' move, why do both lose?",
            "tag": "Ch. 7 · Prisoner’s Dilemma & Chicken",
            "color": "var(--c-strategic)",
            "ans": (
                "In the Prisoner’s Dilemma (pp. 136–137)—like factories dumping waste or rivals in a ruinous ad war—individual self-protection pushes both sides to defect (3 years in prison each) rather than cooperate (2 years each). "
                "Escaping requires binding agreements, verified trust, and penalties for betrayal—changing the rules of the game rather than playing harder."
            ),
            "target": "labs:games",
            "cta": "Play the 5 Game Theory Matrices →",
        },
        {
            "q": "Why must scientists try to disprove their own favorite hypothesis?",
            "tag": "Ch. 9 · Popperian Falsifiability",
            "color": "var(--c-science)",
            "ans": (
                "Confirmation bias makes finding supporting anecdotes effortless—even astrology or superstitions can collect 'hits'. "
                "Carl Sagan and Karl Popper show that a claim is scientific only if it is falsifiable (pp. 162–167). "
                "Designing controlled experiments aimed at breaking your hypothesis is the crucible where all eight thinking methods unite."
            ),
            "target": "labs:science",
            "cta": "Open the Scientific Convergence Loop →",
        },
    ],
    "epilogue": {
        "eyebrow": "Epilogue · Page 171",
        "title": "The Bird in Your Hand",
        "story": (
            "A mischievous, clever schoolboy hid a live bird inside his cupped hands and challenged his teacher: "
            "'Tell me, teacher—when I open my hands, will the bird be alive or dead?' "
            "If she said 'dead,' he would open his palms and let it fly; if she said 'alive,' he would quietly crush it. "
            "The teacher smiled and answered: 'If you want it to live, it will live. If you want it to die, it will die.' "
            "Astonished, the boy asked how she read his mind. 'Through thinking!' she replied."
        ),
        "moral": (
            "Everything in this book is like the bird resting in that boy’s hands. The book decides nothing in your place. "
            "Whether these methods come alive or remain dead ink lies entirely in your hands—in your daily practice."
        ),
    },
}

CHAPTERS_EN = [
    {
        "id": "ch1",
        "num": 1,
        "part": "I",
        "part_name": "Part I · Foundations of Thinking",
        "title": "Overview of Thinking",
        "vi_title": "Khái quát về Tư duy",
        "pages": "pp. 10–22",
        "color": "var(--c-meta)",
        "hex": "#0aa6c9",
        "role_tag": "Metacognitive Supervisor",
        "metaphor": "The Cockpit & Autopilot Switch",
        "quotes": [
            ("Laozi", "Watch your thoughts; they become words. Watch your words; they become actions... Watch your character; it becomes your destiny."),
            ("William Shakespeare", "Thought is free."),
            ("Thomas Carlyle", "Thought is the parent of the deed."),
        ],
        "concept": (
            "Thinking is a hidden, symbolic cognitive process performed by the brain to penetrate appearances, uncover underlying regularities, "
            "and mentally rehearse words and actions before executing them in reality—grounded in evidence and reason rather than impulse or dogma."
        ),
        "principles": [
            "Dual-System Architecture (Kahneman): System 1 is fast, automatic, memory-driven intuition; System 2 is slow, effortful, methodical—and chronically lazy.",
            "Two Failure Modes: (1) System 2 stays asleep and rubber-stamps System 1’s heuristics; (2) System 2 wakes up but applies a flawed method.",
            "Slow ≠ Right: Merely 'trying to think harder' fails without an explicit structural framework to audit our own reasoning.",
            "Dynamic Contextuality: All 8 elements of conscious thought interact non-linearly inside a concrete economic, cultural, and historical Context.",
            "Simon’s Virtuous Consolidation: Disciplined System 2 practice writes accurate patterns into memory, gradually upgrading System 1’s intuition.",
        ],
        "tools": ["t-heuristics-audit", "t-paul-elder-8"],
        "traps": [
            "Question Substitution: Silently swapping 'Is this claim true?' for 'Does this claim feel familiar?'",
            "WYSIATI (What You See Is All There Is): Treating partial visible data as the entire truth and rejecting disconfirming facts.",
            "10 Default Biases: Confirmation, Anchoring, Availability, Framing, Sunk Cost, Loss Aversion, Bandwagon, Overconfidence, Affect, Dunning–Kruger.",
        ],
        "exercises": [
            "Catch a System 1 hijack today: write down one snap judgment you made and identify which heuristic or bias drove it.",
            "Map a real life crossroads (career, study, relocation) across all 8 elements of the Paul–Elder octagon, explicitly stating your hidden Assumptions.",
            "Compare how your conclusion shifts when you re-examine the same Key Question from a second stakeholder’s Point of View.",
        ],
        "synthesis": (
            "Error in unexamined thinking is not an occasional glitch—it is our biological default. Conscious thinking supplies the discipline to wake System 2, "
            "while Parts II and III supply the methods System 2 needs to reason well."
        ),
        "reading": [
            "Kahneman, D. (2011). Thinking, Fast and Slow.",
            "Paul, R. & Elder, L. (2019). The Thinker’s Guide to Fallacies.",
            "Elder, L. & Paul, R. (2005). Analytic Thinking.",
            "Dobelli, R. (2013). The Art of Thinking Clearly.",
        ],
        "educator_note": (
            "Classroom integration: Before teaching any new unit (history, physics, literature), ask students to fill a 3-minute 'Assumptions & Key Question' card "
            "so they experience subject knowledge as active inquiry rather than passive memorization."
        ),
    },
    {
        "id": "ch2",
        "num": 2,
        "part": "II",
        "part_name": "Part II · Core Thinking Methods",
        "title": "Creative Thinking",
        "vi_title": "Tư duy Sáng tạo",
        "pages": "pp. 24–48",
        "color": "var(--c-creative)",
        "hex": "#e2a300",
        "role_tag": "Idea & Reframing Engine",
        "metaphor": "Divergent Prism → Convergent Lens",
        "quotes": [
            ("Twyla Tharp", "Creativity is a habit, and the best creativity is a result of good work habits."),
            ("Albert Einstein", "Imagination is more important than knowledge."),
            ("Sylvia Plath", "The worst enemy to creativity is self-doubt."),
        ],
        "concept": (
            "Creativity is the capacity to generate ideas or solutions that satisfy two simultaneous criteria (Amabile, 1983): "
            "Novelty (distinctive, non-obvious) and Appropriateness (valuable, workable in context). It is not a mystical gift for geniuses, but a trainable habit."
        ),
        "principles": [
            "Challenge Hidden Assumptions: Ask what happens if long-standing beliefs (e.g., 'ulcers come only from stress, never bacteria in stomach acid') are dropped.",
            "Question Human-Made Rules: Rules reflect the knowledge limits of when they were written.",
            "Cross-Pollinate Unrelated Domains: Breakthroughs emerge at intersections (e.g., café + bookstore).",
            "Treat Failure as Diagnostic Data: Edison’s 10,000 non-working filaments narrowed the search space.",
            "Diverge First, Converge Second: Strictly separate judgment-free idea generation ('think wide') from critical selection ('think deep').",
        ],
        "tools": ["t-redefine", "t-inversion", "t-brainstorm", "t-mindmap", "t-scamper", "t-six-hats", "t-what-if"],
        "traps": [
            "Solution-Locked Problem Framing: NASA’s 'zero-gravity ink pen' vs. the Soviet 'what writes without gravity? → pencil' parable.",
            "Premature Critique: Mixing Black-Hat judgment into the divergent phase of Brainstorming or SCAMPER.",
            "Personal & Organizational Silos: Fear of ridicule, perfectionism, rigid hierarchy, and lack of psychological safety (why wheeled suitcases took until 1972!).",
        ],
        "exercises": [
            "Random-Word Sprint: Pick a random noun from a dictionary (e.g., 'brick') and list every use, metaphor, or variation you can generate in 3 minutes.",
            "Three-Solution Rule: For your next everyday problem, apply SCAMPER or Inversion to produce at least three genuinely distinct solutions before choosing.",
            "Post-Mortem Creativity Audit: Review a recent win or setback and trace whether problem framing expanded or narrowed your options.",
        ],
        "synthesis": (
            "In a hyper-competitive AI economy, copying existing templates guarantees obsolescence. Creative thinking rests on iteration: dare to frame anew, test, err, and refine."
        ),
        "reading": [
            "Vogel, T. (2014). Breakthrough Thinking.",
            "Tharp, T. (2003). The Creative Habit.",
            "Rod, J. (2016). The Art of Creative Thinking.",
            "Michalko, M. (2006). Thinkertoys (2nd ed.).",
        ],
        "educator_note": (
            "Classroom integration: Show Archimedes’ dynamic definition of a sphere (a 2D circle rotated around its diameter) or Kapitsa’s dog at v = 0 "
            "to demonstrate that mathematical and scientific definitions are creative viewing angles, not dead formulas."
        ),
    },
    {
        "id": "ch3",
        "num": 3,
        "part": "II",
        "part_name": "Part II · Core Thinking Methods",
        "title": "Critical Thinking",
        "vi_title": "Tư duy Phản biện",
        "pages": "pp. 49–66",
        "color": "var(--c-critical)",
        "hex": "#2b6bef",
        "role_tag": "Cognitive Immune System",
        "metaphor": "Two-Tier Verification Filter",
        "quotes": [
            ("George Bernard Shaw", "All great truths begin as blasphemies."),
            ("Voltaire", "It is better to debate a question without settling it than to settle a question without debating it."),
            ("Martin Luther King Jr.", "The function of education is to teach one to think intensively and to think critically."),
        ],
        "concept": (
            "Rooted in Sino-Vietnamese 'Phản' (return to essence) + 'Biện' (examine clearly to distinguish), Critical Thinking is NOT hostile nitpicking. "
            "It is the disciplined evaluation of arguments and of our own thinking process through evidence, clarity, and intellectual fairness."
        ),
        "principles": [
            "Constructive Skepticism: Question claims and demand commensurate evidence before accepting or rejecting.",
            "Evidence-Anchored Reasoning: Weigh claims by objective proof rather than cultural habit or personal prejudice.",
            "Metacognitive Bias Vigilance: Actively surface cultural and confirmation biases (e.g., chopsticks vs. eating by hand).",
            "Semantic Precision & Open-Mindedness: Define ambiguous terms clearly while remaining ready to revise beliefs under new evidence.",
            "Rival Explanations & Nuance: Resist binary 'with me or against me' framing and hasty overgeneralization.",
        ],
        "tools": ["t-browne-keeley", "t-paul-elder-critique"],
        "traps": [
            "Weaponizing Critique: Using questions to attack an opponent ('Why make such a ridiculous claim?') rather than to uncover truth.",
            "Closed or Leading Questions: Asking 'Why do you love our service?' instead of open diagnostic prompts.",
            "Unquestioned Authority: Aristotle’s false claim that men have more teeth than women went unchecked for 1,800 years simply because nobody counted.",
        ],
        "exercises": [
            "Ad Deconstruction: Pick a viral social-media or TV ad and run all 10 Browne–Keeley questions to expose hidden assumptions and omitted facts.",
            "Self-Audit with Paul–Elder: Take a report or essay in your field and grade it against the 8 Intellectual Standards (accuracy, depth, breadth, fairness).",
            "Fallacy Field Journal: Log two real fallacies or deceptive statistics you encounter in conversation or news today and explain their mechanism.",
        ],
        "synthesis": (
            "Critical thinking operates on two tiers: Browne–Keeley audits external arguments, while Paul–Elder audits our own mind. Without critique, thinking is not yet conscious."
        ),
        "reading": [
            "Browne, M. N. & Keeley, S. M. (2018). Asking the Right Questions.",
            "Paul, R. & Elder, L. (2014). The Miniature Guide to Critical Thinking Concepts & Tools.",
            "Moore, B. & Parker, R. (2020). Critical Thinking.",
        ],
        "educator_note": (
            "Classroom integration: Present deceptive-statistics cases from p. 57–58 (average income rising while most stagnate; '80% of summer hospital patients have dengue' ≠ '80% chance you catch dengue') in math or civics classes."
        ),
    },
    {
        "id": "ch4",
        "num": 4,
        "part": "II",
        "part_name": "Part II · Core Thinking Methods",
        "title": "Analytical Thinking",
        "vi_title": "Tư duy Phân tích",
        "pages": "pp. 68–86",
        "color": "var(--c-analytical)",
        "hex": "#0d9488",
        "role_tag": "Structural Deconstructor",
        "metaphor": "A Flashlight in Dense Fog",
        "quotes": [
            ("P.S. Baber", "Analysis is the art of creation through destruction."),
            ("Nicolas Darvas", "I believe in analysis and not forecasting."),
            ("World Economic Forum (2025)", "Analytical thinking remains the #1 core skill sought by employers—essential at 7 in 10 companies."),
        ],
        "concept": (
            "Like disassembling a mechanical watch to inspect its gears, Analytical Thinking systematically decomposes a complex problem into constituent parts, "
            "maps their relationships, and uncovers root causes—dividing complexity without losing sight of the whole."
        ),
        "principles": [
            "Structured Stepwise Decomposition: Break overwhelming problems into tractable sub-problems via clear taxonomic boundaries.",
            "Relational & Structural Focus: Examine how parts connect, spot recurring data patterns, and trace cause-and-effect chains.",
            "Empirical & Logical Rigor: Ground conclusions strictly in verified data rather than subjective impressions.",
            "Tool Chaining: Real-world analysis rarely uses one tool in isolation—Fishbone maps branches, 5 Whys drills deep, SWOT frames context, Eisenhower prioritizes action.",
        ],
        "tools": ["t-swot", "t-five-whys", "t-fishbone", "t-eisenhower", "t-comparative"],
        "traps": [
            "Stopping at Symptoms: Halting 5 Whys at step 2 ('the fuse blew') instead of reaching the missing oil-pump strainer—and failing to verify the root cause.",
            "Urgency Addiction: Letting Quadrant 3 urgent-but-trivial tasks crowd out Quadrant 2 long-term preparation until everything becomes a crisis.",
            "Analysis Paralysis: Endless decomposition without deadlines, forgetting that perfect information rarely exists.",
        ],
        "exercises": [
            "Root-Cause Drill: Pick a recurring irritation (a chronically dirty street, habitual lateness) and combine Fishbone + 5 Whys to locate a verifiable root cause.",
            "Win/Loss Dissection: Analyze one recent success or failure using SWOT to separate controllable internal factors from external conditions.",
            "Weighted Choice Matrix: Build a Comparative Analysis table with explicit criteria weights to decide between two jobs, universities, or major purchases.",
        ],
        "synthesis": (
            "A flashlight does not make the fog vanish, but it illuminates the next safe steps ahead. Daily practice turns analytical decomposition into second nature."
        ),
        "reading": [
            "Lane, R. (2020). Logic & Analytical Thinking.",
            "Whimbey, A. (1999). Analytical Reading & Reasoning.",
            "Bloom, B. S. (1969). Taxonomy of Educational Objectives.",
        ],
        "educator_note": (
            "Classroom integration: Clarify the boundary on p. 69—Analytical Thinking dissects internal parts, Critical Thinking evaluates truth/validity, and Systems Thinking models dynamic feedback over time."
        ),
    },
    {
        "id": "ch5",
        "num": 5,
        "part": "II",
        "part_name": "Part II · Core Thinking Methods",
        "title": "Logical Thinking",
        "vi_title": "Tư duy Logic",
        "pages": "pp. 87–100",
        "color": "var(--c-logical)",
        "hex": "#3346e0",
        "role_tag": "Grammar of Inference",
        "metaphor": "Load-Bearing Structural Beams",
        "quotes": [
            ("Arthur Conan Doyle", "I never guess. It is a shocking habit—destructive to the logical faculty."),
            ("Niels Bohr", "No, no, you’re not thinking; you’re just being logical."),
            ("Leonard Nimoy (Spock)", "Logic is the beginning of wisdom, not the end."),
        ],
        "concept": (
            "Logic is the grammar of reasoning—the objective rules governing whether a conclusion genuinely follows from its premises. "
            "Everyone uses logic every day; the only question is whether we apply its rules validly or fall into hidden non-sequiturs."
        ),
        "principles": [
            "Law of Identity (A ≡ A): Every term must keep the exact same meaning throughout an argument ('Vietnamese citizen' ≠ 'resident in Vietnam').",
            "Law of Non-Contradiction: Nothing can both be and not be in the same respect at the same time (body in Hanoi vs. mind in Saigon are distinct respects).",
            "Law of Excluded Middle: Between a clear proposition and its negation ('It is raining now'), one holds and no murky middle exists.",
            "Principle of Sufficient Reason: Every valid claim requires sufficient causal or evidentiary ground ('taking the exam' is insufficient reason for 'passing').",
        ],
        "tools": ["t-deduction", "t-induction", "t-causal-logic", "t-analogy"],
        "traps": [
            "Undistributed Middle in Deduction: 'All footballers run fast; Bình runs fast → Bình is a footballer' (confusing subset membership).",
            "Black Swan Blindness in Induction: Treating n observations ('all swans seen in Europe are white' prior to 1697) as 100% certainty, or generalizing from outliers like Bill Gates.",
            "Spurious Correlation & Superficial Analogy: Confusing ice-cream sales with sunglass sales, or equating a local piano teacher’s 'excellence' with Chopin winner Đặng Thái Sơn.",
        ],
        "exercises": [
            "Inference Tagging: Read an op-ed or research brief and label every major argument as Deductive, Inductive, Causal, or Analogical.",
            "Media Bug-Hunt: Spot three logical violations on social media or TV news and name the exact law or inference rule broken.",
            "Self-Debate Replay: Reconstruct a recent disagreement you had and check whether your own premises actually entailed your conclusion.",
        ],
        "synthesis": (
            "Deduction yields certainty only when universal premises are true; Induction and Analogy yield probabilities; Causal reasoning requires mechanism and confounding checks. "
            "Mastery of logic powers every other method in this book."
        ),
        "reading": [
            "McInerny, D. Q. (2004). Being Logical.",
            "Wilson, D. C. (1999). A Guide to Good Reasoning.",
            "Copi, I. M., Cohen, C., & McMahon, K. (2011). Introduction to Logic.",
        ],
        "educator_note": (
            "Classroom integration: Pair Niels Bohr’s quote ('you’re just being logical') with Spock’s ('beginning of wisdom, not the end') so students see logic as necessary scaffolding rather than a substitute for empirical discovery."
        ),
    },
    {
        "id": "ch6",
        "num": 6,
        "part": "III",
        "part_name": "Part III · Advanced Thinking Methods",
        "title": "Systems Thinking",
        "vi_title": "Tư duy Hệ thống",
        "pages": "pp. 102–126",
        "color": "var(--c-systems)",
        "hex": "#10a866",
        "role_tag": "Wholes, Emergence & Feedback",
        "metaphor": "Living Ecosystem & Cybernetic Loops",
        "quotes": [
            ("Ludwig von Bertalanffy", "A system is more than the sum of its parts; it is an entity that maintains its existence through the mutual interaction of its parts."),
            ("Donella H. Meadows", "A system is an interconnected set of elements that is coherently organized in a way that achieves something."),
            ("Peter Senge", "Systems thinking is a discipline for seeing wholes... for seeing 'patterns of change' rather than 'static snapshots'."),
        ],
        "concept": (
            "When every local decision looks rational yet the whole organization or life situation deteriorates ('seeing trees but missing the forest'), linear thinking has hit its limit. "
            "Systems Thinking examines interconnected wholes, emergent properties (like life in a body), time delays, and reinforcing/balancing feedback structures."
        ),
        "principles": [
            "Wholeness & Emergence: Dividing an elephant in half does not produce two small elephants; system capabilities emerge from interaction, not isolated parts.",
            "Boundaries & Interfaces: Every system analysis begins by drawing explicit boundaries and identifying environmental inputs/outputs.",
            "Feedback Dominance & Delays: Reinforcing loops (R) drive exponential growth or collapse; Balancing loops (B) seek equilibrium; delays (//) trigger oscillation.",
            "High-Leverage Architecture over Force: 'The harder you push, the harder the system pushes back'—durable change redesigns structure and incentives rather than blaming individuals.",
        ],
        "tools": ["t-cld", "t-bot-graph", "t-senge-laws"],
        "traps": [
            "Symptomatic Addiction: Soothing pain or organizational errors superficially while a delayed Reinforcing loop worsens the root pathology.",
            "Confusing Correlation with Causal Polarity: Omitting intermediate variables (e.g., Price → [Units Sold] → Revenue) so loop direction becomes indeterminate.",
            "Departmental Silos & Time Pressure: Optimizing sub-team metrics at the expense of the enterprise whole.",
        ],
        "exercises": [
            "Relationship Loop Map: Draw the Causal Loop Diagram between your habitual behavior and a partner’s or colleague’s reaction—and locate one leverage point.",
            "Systemic Post-Mortem: Re-examine a past organizational or personal failure through Senge’s 11 Laws to see which feedback trap was triggered.",
            "BOT Sketching: Plot a key variable in your life or business over time (S-curve, oscillation, or runaway) before proposing any intervention.",
        ],
        "synthesis": (
            "Structure drives behavior. Instead of exhausting yourself fighting symptoms or scapegoating people, alter the feedback loops—or have the courage to retire a broken structure and build a new one."
        ),
        "reading": [
            "Kim, D. H. (1999). Introduction to Systems Thinking.",
            "Senge, P. (1990). The Fifth Discipline.",
            "Meadows, D. (2008). Thinking in Systems: A Primer.",
        ],
        "educator_note": (
            "Classroom integration: Compare Ch. 6’s Blame Loop (R1/R2) vs. Learning Culture Loop (B1/B2) on pp. 114–115—one single node swap ('punishment fear' → 'learning opportunity') flips runaway error growth into self-correcting mastery."
        ),
    },
    {
        "id": "ch7",
        "num": 7,
        "part": "III",
        "part_name": "Part III · Advanced Thinking Methods",
        "title": "Strategic Thinking",
        "vi_title": "Tư duy Chiến lược",
        "pages": "pp. 127–141",
        "color": "var(--c-strategic)",
        "hex": "#ff7a00",
        "role_tag": "Long-Horizon Agency",
        "metaphor": "Grandmaster Board in Shifting Winds",
        "quotes": [
            ("Leon Trotsky", "You may not be interested in strategy, but strategy is interested in you."),
            ("Michael Porter", "Sound strategy starts with having the right goal."),
            ("Sun Tzu", "Plan for what is difficult while it is easy; do what is great while it is small."),
        ],
        "concept": (
            "If analysis dissects the problem and systems thinking reveals its structure, Strategic Thinking guides purposeful action across time amid uncertainty and competing human interests—integrating 'why' (ends), 'how' (ways), and 'with what' (means)."
        ),
        "principles": [
            "Ends Govern Tactics (Clausewitz): Tactics win individual battles; strategy orchestrates battles to fulfill the overarching purpose.",
            "Dynamic Environmental Adaptation (Yarger): Strategy is not a rigid linear checklist—it continuously interacts with a shifting political, economic, and technological landscape.",
            "Focused Priorities (≤ 3): Having ten 'top priorities' means having none; concentrate scarce resources where they create decisive asymmetry.",
            "Interactive Rationality & Reflection: Anticipate how partners and rivals respond to your moves, and build learning loops to iterate.",
        ],
        "tools": ["t-tows", "t-pestle", "t-scenarios", "t-game-theory"],
        "traps": [
            "Mistaking SWOT or PESTLE for Strategy: Environmental audits are raw inputs—strategy begins only when you commit to concrete SO/ST/WO/WT actions.",
            "Pushing Rivals into 'Chicken': Leaving an opponent with nothing to lose guarantees mutual catastrophe.",
            "Tactical Busyness & Short-Termism: Confusing daily operational firefighting with long-range positioning.",
        ],
        "exercises": [
            "Strategic Retrospective: Audit a long-term goal you missed—was the failure due to vague ends, >3 scattered priorities, or ignoring PESTLE shifts?",
            "3-Year Personal Scenario Plan: Identify the 2 biggest macro uncertainties facing your career or savings, build 4 plausible scenarios, and design a resilient move for the worst case.",
            "Game-Theory Relationship Audit: Diagnose whether a recurring negotiation at home or work resembles Prisoner’s Dilemma, Chicken, or Battle of the Sexes—and shift to cooperative reciprocity.",
        ],
        "synthesis": (
            "Strategy turns dreams into navigable pathways. A great strategy does not predict a single future—it ensures you thrive in favorable worlds and never collapse in adverse ones."
        ),
        "reading": [
            "Defence Academy of the UK (2010). Thinking Strategically.",
            "Ridgley, S. K. (2012). Strategic Thinking Skills.",
            "Dixit, A. K. & Nalebuff, B. J. (1991). Strategic Thinking.",
            "Schoemaker, P. J. H. (1995). Scenario Planning: A Tool for Strategic Thinking.",
        ],
        "educator_note": (
            "Classroom integration: Use the 'Fair Cake-Cutting' ('one cuts, the other chooses first') and 'Battle of the Sexes' games (pp. 138) to show students how mechanism design resolves everyday conflicts fairly."
        ),
    },
    {
        "id": "ch8",
        "num": 8,
        "part": "III",
        "part_name": "Part III · Advanced Thinking Methods",
        "title": "Probabilistic Thinking",
        "vi_title": "Tư duy Xác suất",
        "pages": "pp. 143–159",
        "color": "var(--c-prob)",
        "hex": "#7a4dff",
        "role_tag": "Uncertainty Quantifier",
        "metaphor": "Weighted Spectrum & Bayesian Compass",
        "quotes": [
            ("Walter Bagehot", "Life is a school of probability."),
            ("Charles William Eliot", "All business proceeds on beliefs, or judgements of probabilities, and not on certainties."),
            ("Judea Pearl", "In the real world, only people who are pretty crazy are absolutely sure about anything other than maybe death."),
        ],
        "concept": (
            "Probabilistic Thinking replaces rigid binary thinking ('Will it happen—yes or no?') with calibrated degrees of belief ('How likely is each outcome, and what is its impact?'). "
            "It is not mere math—it is the rational art of living wisely with uncertainty."
        ),
        "principles": [
            "Embrace Irreducible Uncertainty: Almost every real-world outcome lives strictly between 0 and 1.",
            "Think in Full Distributions, Not Single Point Forecasts: Map all plausible gain and loss branches so their probabilities sum to 1.",
            "Expected Value + Tail-Risk Guardrails: Weigh choices by EV = Σ XᵢPᵢ, while guarding against catastrophic low-probability 'Black Swans' (Taleb).",
            "Bayesian Belief Updating: Treat subjective probabilities as provisional priors that must be disciplined and updated whenever new evidence arrives.",
            "Judge Decisions by Process, Not Single Outcomes: Because luck exists, a sound decision can occasionally lose—and a reckless gamble can occasionally win.",
        ],
        "tools": ["t-ev-dist", "t-prob-tree", "t-bayes"],
        "traps": [
            "Inverting Conditional Probabilities: Confusing P(Disease | Positive Test) with P(Positive Test | Disease).",
            "Base-Rate Neglect: Ignoring the prior prevalence P(A)—remembering that if P(A) = 0.01, even a 99% test yields ~67% false alarms!",
            "Psychological Intolerance of Ambiguity: Craving false 100%/0% certainty because evolutionary habits favor black-and-white stories.",
        ],
        "exercises": [
            "Daily Calibration Log: Assign explicit % probabilities to everyday forecasts (rain, traffic delay, project sign-off) and update them as new clues appear.",
            "Expected-Value Tree: For your next financial or career bet, draw a 2-stage Probability Tree and compute its Expected Value.",
            "Hit-and-Run Cab Puzzle (p. 157): In a city with 60% Green cabs and 40% Red cabs, a witness (85% accurate) says a fleeing cab was Red. Compute P(Green | Witness='Red') via Bayes!",
        ],
        "synthesis": (
            "A probabilistic thinker is not omniscient—they simply refuse to be fooled by randomness, mistaking short-term luck for skill or bad luck for failure."
        ),
        "reading": [
            "Rowntree, D. (1984). Probability Without Tears.",
            "Kahneman, D. (2011). Thinking, Fast and Slow.",
            "Taleb, N. N. (2007). The Black Swan.",
        ],
        "educator_note": (
            "Classroom integration: Teach Bayes visually with a 100-square or 1,000-square grid before introducing the algebraic fraction—students grasp base rates instantly when they count the false-positive squares."
        ),
    },
    {
        "id": "ch9",
        "num": 9,
        "part": "III",
        "part_name": "Part III · Advanced Thinking Methods",
        "title": "Scientific Thinking",
        "vi_title": "Tư duy Khoa học",
        "pages": "pp. 160–170",
        "color": "var(--c-science)",
        "hex": "#ec3d8c",
        "role_tag": "Grand Empirical Synthesis",
        "metaphor": "A Candle in the Dark",
        "quotes": [
            ("Carl Sagan", "Science is a way of thinking much more than it is a body of knowledge."),
            ("P. J. O’Rourke", "To mistrust science and deny the validity of the scientific method is to resign your job as a human."),
            ("Bertrand Russell", "Whatever knowledge is attainable, must be attained by scientific methods."),
        ],
        "concept": (
            "Scientific Thinking is not reserved for laboratory coats—it is humanity’s most reliable method for investigating reality and defending personal autonomy against manipulation. "
            "It treats all knowledge as provisional models refined through observation, falsifiable hypotheses, controlled testing, and open peer critique."
        ),
        "principles": [
            "Empiricism, Skepticism & Objectivity: Anchor belief in observable, reproducible experiments rather than folklore, wishful thinking, or authority.",
            "Popperian Falsifiability: A claim is scientific only if conceivable evidence could prove it wrong ('past-life karma' cannot be tested; 'coffee raises heart rate' can).",
            "Controlled Isolation & Rival Hypotheses: Isolate variables (don’t test standing breaks AND coffee simultaneously!) and rule out competing explanations.",
            "Occam’s Razor (Parsimony): Prefer the simplest explanation that accounts for all the evidence ('blown fuse' before 'sabotage').",
            "Grand Methodological Convergence: Every step of the scientific loop recruits Creative, Critical, Analytical, Logical, Systems, Strategic, and Probabilistic thinking.",
        ],
        "tools": ["t-scientific-method", "t-falsifiability-razor"],
        "traps": [
            "Unfalsifiable Hypotheses: Framing explanations that no observation could ever refute.",
            "Confounded Experiments: Changing two variables at once (e.g., exercise breaks + extra espresso in the p. 167 work-fatigue study).",
            "Cultural & Authority Barriers (Sagan): Pseudoscience, sensationalist media that 'celebrates ignorance,' and uncritical submission to political, religious, or commercial power.",
        ],
        "exercises": [
            "Falsifiability Check: For the next three bold claims you hear today, ask: 'What concrete observation would prove this claim false?'",
            "Devil’s Advocate Protocol: Treat a belief you hold DEAR as a tentative hypothesis and list the strongest empirical evidence that would refute it.",
            "Personal N=1 Experiment: Run a 7-day controlled test on one habit (sleep, focus breaks, study method), logging daily data before drawing a conclusion.",
        ],
        "synthesis": (
            "Where scientific thinking weakens, superstition, emotional manipulation, and authoritarian conformity rush in. Practicing the scientific method in everyday life keeps human dignity and free inquiry alive."
        ),
        "reading": [
            "Sagan, C. (1997). The Demon-Haunted World: Science as a Candle in the Dark.",
            "Martin, R. M. (2002). Scientific Thinking.",
            "Sagan, C. (1977). Broca’s Brain.",
        ],
        "educator_note": (
            "Classroom integration: Use Chapter 9 as a capstone showing how science is not 'one more subject' alongside literature or economics, but the synthesis of all 8 thinking methods."
        ),
    },
]
