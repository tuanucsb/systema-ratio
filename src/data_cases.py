# -*- coding: utf-8 -*-
"""36 Real-World Case Studies across all 9 Chapters of Đào Minh Châu’s Học Tư Duy, explicitly stating Methods Used and Concrete Results."""

CASE_CATEGORIES = [('all', 'All 36 Cases', 'Tất cả 36 Hồ sơ'),
 ('ai-tech', 'AI, Tech & Product', 'AI, Công nghệ & Sản phẩm'),
 ('business', 'Business & Finance', 'Kinh doanh & Tài chính'),
 ('medicine', 'Medicine & Science', 'Y học & Khoa học'),
 ('aerospace', 'Aviation & Engineering', 'Hàng không & Kỹ thuật'),
 ('policy', 'History, Law & Policy', 'Lịch sử, Luật & Chính sách')]

CASES_VAULT = [{'id': 'cs-af447',
  'ch': 'ch1',
  'cat': 'aerospace',
  'year': '2009',
  'domain_en': 'Aviation · Cockpit Startle',
  'domain_vi': 'Hàng không · Phản xạ Hoảng loạn',
  'title_en': 'Air France Flight 447: When System 1 Grabbed the Controls at 35,000 Feet',
  'title_vi': 'Chuyến bay Air France 447: Khi Hệ thống 1 Giật Cần Lái Ở Độ Cao 10.000m',
  'story_en': 'Ice crystals briefly blocked the Airbus A330’s speed sensors over the Atlantic, disconnecting autopilot. Startled in '
              'darkness, the junior pilot’s System 1 pulled the stick nose-up continuously—stalling a mechanically healthy jet because no '
              'one paused to run a conscious diagnostic frame.',
  'story_vi': 'Tinh thể băng làm nghẽn cảm biến tốc độ vài chục giây khiến chế độ lái tự động ngắt giữa đêm tối Đại Tây Dương. Trong cơn '
              'giật mình, Hệ thống 1 khiến cơ phó kéo ngược cần lái liên tục làm máy bay thất tốc rơi tự do dù động cơ hoàn toàn bình '
              'thường.',
  'lesson_en': 'High-stress automation handoffs trigger System 1 tunnel vision unless crews pause to state Information, Assumptions, and '
               'Implications aloud.',
  'lesson_vi': 'Khi máy móc trả quyền đột ngột, con người cực dễ rơi vào hoảng loạn bản năng nếu không có quy trình gọi tên Thông tin & '
               'Giả định tường minh.',
  'url': 'https://en.wikipedia.org/wiki/Air_France_Flight_447',
  'src_label': 'BEA Report & Dossier',
  'lab': 'labs:octagon',
  'methods_en': 'Overview of Thinking (Ch. 1 · System 1 Startle Override & Paul–Elder 8-Element Conscious Frame: Information + '
                'Assumptions)',
  'methods_vi': 'Khái quát về Tư duy (Chương 1 · Kiếm soát phản xạ Hệ thống 1 & Khung 8 thành tố Paul–Elder: Thông tin + Giả định)',
  'result_en': 'Tragic loss of all 228 lives; BEA’s 2012 final report overhauled global airline stall-recovery training and cockpit '
               'callout protocols.',
  'result_vi': 'Máy bay rơi khiến 228 người thiệt mạng; báo cáo BEA năm 2012 buộc ngành hàng không toàn cầu cải tổ quy trình huấn luyện '
               'thoát thất tốc và đọc to thông số buồng lái.'},
 {'id': 'cs-jcpenney',
  'ch': 'ch1',
  'cat': 'business',
  'year': '2012',
  'domain_en': 'Retail Strategy · Anchoring',
  'domain_vi': 'Bán lẻ · Thiên kiến Mỏ neo',
  'title_en': 'J.C. Penney’s $4.3B ‘Fair & Square’ Crash: Shoppers Missed the Fake Discounts',
  'title_vi': 'Cú Sập 4,3 Tỷ USD Của J.C. Penney: Khách Hàng Nghiện ‘Giá Gốc Ảo’',
  'story_en': 'New CEO Ron Johnson eliminated fake ‘Was $60, Now $24!’ coupons and offered honest everyday low prices. Revenue plunged '
              '$4.3 billion in 12 months—just like Chapter 1’s Three-Shop Shirt parable, System 1 craves the emotional thrill of beating a '
              'high anchor more than objective price.',
  'story_vi': 'CEO mới xóa bỏ chiêu trò “giá gốc 60 đô giảm còn 24 đô” để niêm yết giá thật minh bạch. Doanh thu lập tức bốc hơi 4,3 tỷ '
              'USD chỉ sau 1 năm—chứng minh y hệt câu chuyện chiếc áo 900 ngàn ở trang 15: Hệ thống 1 mua cảm giác “được hời so với mỏ '
              'neo” chứ không mua giá trị thực.',
  'lesson_en': 'Never underestimate Anchoring Bias (#2, p. 15) in pricing, salary talks, or M&A negotiations.',
  'lesson_vi': 'Đừng bao giờ coi thường sức mạnh của Mỏ neo đầu tiên (Thiên kiến #2, tr. 15) trong định giá và đàm phán.',
  'url': 'https://en.wikipedia.org/wiki/Ron_Johnson_(businessman)#J._C._Penney',
  'src_label': 'Retail Case Study',
  'lab': 'traps',
  'methods_en': 'Overview of Thinking (Ch. 1 · Anchoring Bias Audit #2, p. 15 & System 1 Reference-Point Framing)',
  'methods_vi': 'Khái quát về Tư duy (Chương 1 · Nhận diện Thiên kiến Mỏ neo #2, tr. 15 & Hiệu ứng Đóng khung)',
  'result_en': 'Annual revenue plunged $4.3 billion (−25%) and shares fell over 50% in 12 months; the board ousted CEO Ron Johnson and '
               'restored reference price anchors.',
  'result_vi': 'Doanh thu bốc hơi 4,3 tỷ USD (−25%), cổ phiếu mất hơn 50% giá trị sau 12 tháng; HĐQT sa thải CEO và phải khôi phục lại '
               'bảng giá mỏ neo.'},
 {'id': 'cs-avianca-ai',
  'ch': 'ch1',
  'cat': 'ai-tech',
  'year': '2023',
  'domain_en': 'AI Era · Fluency Heuristic',
  'domain_vi': 'Kỷ nguyên AI · Bẫy Trôi chảy',
  'title_en': 'Mata v. Avianca: Veteran Lawyers Sanctioned After ChatGPT Invented Six Fake Lawsuits',
  'title_vi': 'Vụ Kiện Mata v. Avianca: Luật Sư Kỳ Cựu Bị Phạt Vì Tin 6 Án Lệ Bịa Đặt Của AI',
  'story_en': 'Filing a federal brief in New York, attorneys pasted eloquent judicial quotes generated by ChatGPT. Every single case was a '
              'hallucination. Lazy System 2 mistook grammatical fluency for truth—the exact cognitive atrophy Đào Minh Châu warns against '
              'in the Preface (p. 5).',
  'story_vi': 'Nộp hồ sơ lên tòa án liên bang Mỹ, nhóm luật sư đưa vào 6 án lệ cực kỳ hùng hồn do ChatGPT viết. Cả 6 vụ đều không hề tồn '
              'tại! Hệ thống 2 lười biếng đã đánh đồng “văn phong trôi chảy” với “sự thật”—đúng lời cảnh báo ở Lời nói đầu (tr. 5).',
  'lesson_en': "Question Substitution ('Does it sound authoritative?' vs. 'Does it exist in primary records?') is the #1 AI-era trap.",
  'lesson_vi': 'Thay thế câu hỏi (“Nghe có vẻ uyên bác không?” thay cho “Có hồ sơ gốc không?”) là cái bẫy nguy hiểm nhất thời AI.',
  'url': 'https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.',
  'src_label': 'Court Case Dossier',
  'lab': 'labs:octagon',
  'methods_en': 'Overview of Thinking (Ch. 1 · Question Substitution Audit, p. 14) + Critical Thinking (Ch. 3 · Primary Source '
                'Verification, p. 56)',
  'methods_vi': 'Khái quát về Tư duy (Chương 1 · Chống mẹo Thay thế câu hỏi, tr. 14) + Tư duy Phản biện (Chương 3 · Kiểm chứng nguồn gốc '
                'bằng chứng, tr. 56)',
  'result_en': 'Federal judge sanctioned the lawyers $5,000, dismissed the fabricated filing, and triggered mandatory AI '
               'citation-verification standing orders across courts worldwide.',
  'result_vi': 'Thẩm phán liên bang phạt tiền nhóm luật sư, bác bỏ hồ sơ kiện và châm ngòi cho quy định bắt buộc kiểm tra nguồn trích dẫn '
               'AI tại tòa án khắp thế giới.'},
 {'id': 'cs-knight-cap',
  'ch': 'ch1',
  'cat': 'business',
  'year': '2012',
  'domain_en': 'FinTech · Unchecked Routine',
  'domain_vi': 'Tài chính Số · Lỗi Chủ quan',
  'title_en': 'Knight Capital’s 45-Minute $440 Million Nightmare',
  'title_vi': '45 Phút Đốt Cháy 440 Triệu USD Của Knight Capital',
  'story_en': 'Deploying trading code to 8 servers, an engineer forgot to update the 8th server, awakening dormant test code (‘Power Peg’) '
              'that bought high and sold low 4 million times in 45 minutes—wiping out a Wall Street giant in one morning.',
  'story_vi': 'Khi cập nhật phần mềm lên 8 máy chủ, kỹ sư bỏ sót máy thứ 8 làm kích hoạt đoạn mã thử nghiệm cũ tự động mua đắt bán rẻ 4 '
              'triệu giao dịch trong 45 phút, xóa sổ định chế Phố Wall chỉ trong một buổi sáng.',
  'lesson_en': 'Routine habits fail under complexity; conscious checklists turn implicit assumptions into verified gates.',
  'lesson_vi': 'Thói quen tự động luôn sụp đổ trước hệ thống phức tạp nếu thiếu cổng kiểm chứng có ý thức.',
  'url': 'https://en.wikipedia.org/wiki/Knight_Capital_Group#2012_stock_trading_disruption',
  'src_label': 'Incident Analysis',
  'lab': 'atlas:t-paul-elder-8',
  'methods_en': 'Overview of Thinking (Ch. 1 · Conscious System 2 Verification Gate vs. Unchecked System 1 Routine, pp. 18–21)',
  'methods_vi': 'Khái quát về Tư duy (Chương 1 · Cổng kiểm soát có ý thức của Hệ thống 2 thay cho thói quen tự động, tr. 18–21)',
  'result_en': 'Lost $440 million in 45 minutes (4 million erroneous trades), wiping out 75% of market value and forcing Knight Capital '
               'into an emergency buyout.',
  'result_vi': 'Lỗ ròng 440 triệu USD chỉ sau 45 phút với 4 triệu lệnh sai, bốc hơi 75% vốn hóa và buộc công ty phải bán mình khẩn cấp.'},
 {'id': 'cs-wald-srg',
  'ch': 'ch2',
  'cat': 'aerospace',
  'year': '1943',
  'domain_en': 'Military Math · Inversion',
  'domain_vi': 'Toán Quân sự · Tư duy Đảo ngược',
  'title_en': 'Abraham Wald & Columbia’s Statistical Research Group: Armoring the Missing Holes',
  'title_vi': 'Abraham Wald & Nhóm Nghiên Cứu Thống Kê Thế Chiến II: Bọc Thép Vùng Không Trúng Đạn',
  'story_en': 'Featured on page 31 of the book: US Navy officers mapped bullet holes on returning bombers and wanted armor over the '
              'most-hit wing sections. Wald inverted the frame—realizing survivors showed where planes could take hits and live, whereas '
              'clean engines marked fatal hits sitting on the ocean floor.',
  'story_vi': 'Câu chuyện tâm điểm trang 31: Quân đội Mỹ đếm lỗ đạn trên máy bay trở về và định bọc thép phần cánh bị bắn nhiều nhất. Wald '
              'lật ngược bài toán: chỗ chi chít đạn mà vẫn bay về được là chỗ an toàn; động cơ lành lặn mới là tử huyệt khiến máy bay rơi '
              'mất xác!',
  'lesson_en': "Always ask: 'What invisible graveyard did my dataset filter out before reaching my eyes?'",
  'lesson_vi': 'Luôn tự hỏi: “Phần dữ liệu tử vong câm lặng nào đã bị sàng lọc mất trước khi đến mắt ta?”',
  'url': 'https://en.wikipedia.org/wiki/Survivorship_bias#Military',
  'src_label': 'Survivorship Dossier',
  'lab': 'labs:wald',
  'methods_en': 'Creative Thinking (Ch. 2 · Inversion Thinking & Problem Redefinition, pp. 30–31) + Probabilistic Thinking (Ch. 8 · '
                'Survivorship Bias Audit)',
  'methods_vi': 'Tư duy Sáng tạo (Chương 2 · Tư duy Đảo ngược & Định nghĩa lại vấn đề, tr. 30–31) + Tư duy Xác suất (Chương 8 · Khử thiên '
                'kiến sống sót)',
  'result_en': 'Allied aircraft combat survival rose markedly from World War II through Vietnam/Korea while adding minimal armor weight; '
               'founded modern operations research.',
  'result_vi': 'Tỷ lệ máy bay sống sót trở về tăng vọt từ Thế chiến II sang các cuộc chiến sau đó với khối lượng giáp tăng tối thiểu; khai '
               'sinh ngành vận trù học hiện đại.'},
 {'id': 'cs-marshall-nobel',
  'ch': 'ch2',
  'cat': 'medicine',
  'year': '1984 / 2005',
  'domain_en': 'Nobel Medicine · Dogma Smash',
  'domain_vi': 'Giải Nobel Y học · Đập Vỡ Định kiến',
  'title_en': 'Barry Marshall & Robin Warren: Drinking H. pylori to Cure Millions of Ulcers',
  'title_vi': 'Barry Marshall & Robin Warren: Tự Uống Vi Khuẩn HP Lật Đổ Giáo Điều Y Khoa',
  'story_en': 'Highlighted on page 29: medical textbooks insisted stomach acid was sterile, consigning ulcer patients to lifelong antacids '
              'or surgery. By reframing ulcers as an infectious disease and drinking the bacterial broth himself, Marshall proved a $20 '
              'antibiotic course cures ulcers permanently.',
  'story_vi': 'Được tác giả nhấn mạnh ở trang 29: sách giáo khoa y học từng mặc định axit dạ dày vô trùng tuyệt đối. Nhờ định nghĩa lại '
              'loét dạ dày là bệnh nhiễm khuẩn và tự uống vi khuẩn làm thí nghiệm, Marshall giúp hàng trăm triệu bệnh nhân khỏi bệnh chỉ '
              'bằng một đợt kháng sinh.',
  'lesson_en': "When an entire field is stuck for 50 years, inspect the 'obvious truth' nobody dares question.",
  'lesson_vi': 'Khi cả một ngành bế tắc suốt 50 năm, thủ phạm luôn nằm ở “chân lý hiển nhiên” không ai dám nghi ngờ.',
  'url': 'https://www.nobelprize.org/prizes/medicine/2005/press-release/',
  'src_label': 'NobelPrize.org Official',
  'lab': 'reader:ch2',
  'methods_en': 'Creative Thinking (Ch. 2 · Challenging Entrenched Assumptions & Problem Redefinition, pp. 25, 29–30) + Scientific '
                'Thinking (Ch. 9 · Controlled Self-Experiment)',
  'methods_vi': 'Tư duy Sáng tạo (Chương 2 · Thách thức giả định cố hữu & Định nghĩa lại vấn đề, tr. 25, 29–30) + Tư duy Khoa học (Chương '
                '9 · Thực nghiệm kiểm chứng)',
  'result_en': 'Transformed peptic ulcers from a chronic surgical condition into an illness cured >90% by a 2-week antibiotic course; '
               'awarded the 2005 Nobel Prize in Medicine.',
  'result_vi': 'Biến bệnh viêm loét dạ dày từ căn bệnh mạn tính phải phẫu thuật thành bệnh chữa khỏi trên 90% bằng 2 tuần kháng sinh; nhận '
               'Giải Nobel Y học 2005.'},
 {'id': 'cs-nintendo-wii',
  'ch': 'ch2',
  'cat': 'ai-tech',
  'year': '1989 / 2006',
  'domain_en': 'Product Design · Reframing',
  'domain_vi': 'Thiết kế Sản phẩm · Đặt lại Vấn đề',
  'title_en': 'Nintendo’s ‘Lateral Thinking with Withered Technology’ (Game Boy & Wii)',
  'title_vi': 'Triết lý ‘Tư Duy Ngang Trên Công Nghệ Cũ’ Của Nintendo (Game Boy & Wii)',
  'story_en': 'While Sony and Microsoft burned billions racing for photorealistic GPUs, Nintendo engineer Gunpei Yokoi and Satoru Iwata '
              'redefined the question from ‘How do we render more polygons?’ to ‘How do grandparents and kids play together in 10 '
              'seconds?’—outselling rivals with cheap, mature sensors.',
  'story_vi': 'Khi Sony và Microsoft đốt hàng tỷ USD đua cấu hình đồ họa, Nintendo định nghĩa lại hoàn toàn câu hỏi từ “Làm sao nét hơn?” '
              'sang “Làm sao cả ông bà lẫn cháu nhỏ cầm lên chơi vui ngay sau 10 giây?”—thắng áp đảo nhờ linh kiện rẻ bền và góc nhìn sáng '
              'tạo.',
  'lesson_en': 'Problem Redefinition (pp. 27–30) beats brute-force spending in hyper-competitive markets.',
  'lesson_vi': 'Định nghĩa lại vấn đề (tr. 27–30) tạo ra đại dương xanh vượt lên trên cuộc đua đốt tiền.',
  'url': 'https://en.wikipedia.org/wiki/Gunpei_Yokoi#Lateral_Thinking_with_Withered_Technology',
  'src_label': 'Design Philosophy',
  'lab': 'atlas:t-redefine',
  'methods_en': 'Creative Thinking (Ch. 2 · Problem Redefinition, SCAMPER Adapt/Put-to-Other-Use & ‘What If’ Reframing, pp. 27–30, 40–45)',
  'methods_vi': 'Tư duy Sáng tạo (Chương 2 · Định nghĩa lại vấn đề, SCAMPER & Đặt câu hỏi ‘Sẽ ra sao nếu’, tr. 27–30, 40–45)',
  'result_en': 'Game Boy sold 118.7 million units and Nintendo Wii sold 101.6 million units—outselling Sony PS3 and Xbox 360 while earning '
               'higher hardware profit per console.',
  'result_vi': 'Game Boy bán 118,7 triệu máy và Nintendo Wii bán 101,6 triệu máy—vượt mặt cả PS3 lẫn Xbox 360 với biên lợi nhuận phần cứng '
               'vượt trội.'},
 {'id': 'cs-premortem',
  'ch': 'ch2',
  'cat': 'business',
  'year': '2007',
  'domain_en': 'Decision Science · Pre-Mortem',
  'domain_vi': 'Quản trị Dự án · Giải phẫu Trước Thất bại',
  'title_en': 'Gary Klein’s ‘Pre-Mortem’ Method: Boosting Hazard Detection by 30%',
  'title_vi': 'Kỹ thuật ‘Khám Nghiệm Tử Thi Trước Khi Chết’ (Pre-Mortem) Của Gary Klein',
  'story_en': 'Before launching a major initiative, polite teams suppress doubts (Groupthink). Psychologist Gary Klein inverted kickoff '
              "meetings: 'Imagine we are 12 months in the future and this project has failed spectacularly. Write down the exact history "
              "of why it died.'",
  'story_vi': 'Trước ngày ra mắt dự án, các thành viên thường ngại nói điều xui (tư duy bầy đàn). Nhà tâm lý học Gary Klein đảo ngược cuộc '
              'họp: “Hãy tưởng tượng 1 năm nữa dự án này đã thất bại thảm hại. Mỗi người hãy viết lại nguyên nhân vì sao nó chết!”',
  'lesson_en': 'Prospective hindsight turns Inversion Thinking (pp. 30–33) into socially safe candor.',
  'lesson_vi': 'Đảo ngược thời gian giúp cả đội nói thẳng những rủi ro chết người mà bình thường không ai dám mở lời.',
  'url': 'https://hbr.org/2007/09/performing-a-project-premortem',
  'src_label': 'Harvard Business Review',
  'lab': 'atlas:t-inversion',
  'methods_en': 'Creative Thinking (Ch. 2 · Inversion Thinking & De Bono’s Black-Hat Risk Lens, pp. 30–33, 43)',
  'methods_vi': 'Tư duy Sáng tạo (Chương 2 · Tư duy Đảo ngược kết hợp Chiếc mũ Đen nhận diện rủi ro, tr. 30–33, 43)',
  'result_en': 'Empirical studies (Mitchell, Russo & Pennington) proved prospective hindsight increases accurate identification of future '
               'failure causes by 30%; adopted across Fortune 500 & NASA.',
  'result_vi': 'Nghiên cứu thực nghiệm chứng minh kỹ thuật này giúp tăng 30% khả năng phát hiện sớm nguyên nhân thất bại; trở thành chuẩn '
               'mực quản trị dự án toàn cầu.'},
 {'id': 'cs-theranos',
  'ch': 'ch3',
  'cat': 'business',
  'year': '2015',
  'domain_en': 'BioTech Fraud · Authority Halo',
  'domain_vi': 'Đại án Công nghệ Sinh học · Hào quang Uy quyền',
  'title_en': 'Theranos ($9B Collapse): When Famous Statesmen Forgot Browne–Keeley Question #6',
  'title_vi': 'Đại Án Theranos (9 Tỷ USD): Khi Dàn Chính Khách Quên Mất Câu Hỏi Số 6 Của Browne–Keeley',
  'story_en': 'Theranos claimed one finger-prick drop could run 200 lab tests. Dazzled by turtleneck charisma and former cabinet '
              'secretaries on the board, investors wired $700M without demanding peer-reviewed validation—until reporter John Carreyrou '
              'checked the raw lab evidence.',
  'story_vi': 'Theranos tuyên bố chỉ 1 giọt máu đầu ngón tay xét nghiệm được 200 chỉ số. Bị lóa mắt bởi hào quang truyền thông và hội đồng '
              'quản trị toàn cựu bộ trưởng, giới đầu tư rót 700 triệu USD mà quên hỏi câu cơ bản nhất ở Chương 3: “Bằng chứng kiểm định '
              'độc lập nằm ở đâu?”',
  'lesson_en': 'Prestige and storytelling are zero substitute for verifiable empirical evidence (Ch. 3, p. 56).',
  'lesson_vi': 'Uy tín cá nhân và lời kể truyền cảm hứng không bao giờ thay thế được bằng chứng thực nghiệm độc lập.',
  'url': 'https://en.wikipedia.org/wiki/Theranos',
  'src_label': 'Full Case History',
  'lab': 'atlas:t-browne-keeley',
  'methods_en': 'Critical Thinking (Ch. 3 · Browne–Keeley Evidence Quality Audit & Authority-Halo Skepticism, pp. 56–57) + Scientific '
                'Thinking (Ch. 9 · Peer Replication)',
  'methods_vi': 'Tư duy Phản biện (Chương 3 · Thẩm định độ tin cậy bằng chứng & Kháng hào quang uy quyền, tr. 56–57) + Tư duy Khoa học '
                '(Chương 9 · Tái lập độc lập)',
  'result_en': 'Investigative verification exposed fake blood-test devices, voided millions of flawed patient lab results, dissolved the '
               '$9B company, and led to federal fraud convictions.',
  'result_vi': 'Phanh phui máy xét nghiệm giả, hủy hàng triệu kết quả xét nghiệm sai lệch, xóa sổ công ty 9 tỷ USD và đưa ban lãnh đạo ra '
               'tòa án hình sự.'},
 {'id': 'cs-berkeley-simpson',
  'ch': 'ch3',
  'cat': 'policy',
  'year': '1973',
  'domain_en': 'Data Science · Simpson’s Paradox',
  'domain_vi': 'Khoa học Dữ liệu · Nghịch lý Simpson',
  'title_en': 'UC Berkeley’s 1973 Admissions Shock: When Overall Averages Lie Backward',
  'title_vi': 'Nghịch Lý Tuyển Sinh ĐH California Berkeley (1973): Khi Số Trung Bình Chung Đảo Ngược Sự Thật',
  'story_en': 'Aggregate data showed 44% of male applicants admitted vs. only 35% of women—triggering fears of bias. Yet when '
              'statisticians audited each department separately, women actually had HIGHER admission rates in most departments! Women had '
              'simply applied to 6%-acceptance humanities PhDs while men applied to 60%-acceptance engineering.',
  'story_vi': 'Số liệu tổng toàn trường cho thấy 44% nam trúng tuyển so với chỉ 35% nữ. Nhưng khi bóc tách từng khoa riêng biệt, tỷ lệ đỗ '
              'của nữ lại CAO HƠN nam ở hầu hết các khoa! Lý do: nữ nộp đơn dồn vào những khoa cực khó (tỷ lệ chọi 6%), còn nam nộp vào '
              'khoa dễ đỗ (60%).',
  'lesson_en': 'Pooled averages can reverse reality when a hidden confounding variable lurks underneath (pp. 57–58).',
  'lesson_vi': 'Số trung bình gộp luôn có thể nói ngược sự thật nếu che khuất biến số phân tầng bên dưới (tr. 57–58).',
  'url': 'https://en.wikipedia.org/wiki/Simpson%27s_paradox#UC_Berkeley_gender_bias',
  'src_label': 'Science Paper & Wiki',
  'lab': 'traps',
  'methods_en': 'Critical Thinking (Ch. 3 · Auditing Deceptive Averages & Confounding Variables, pp. 57–58) + Analytical Thinking (Ch. 4 · '
                'Stratified Decomposition)',
  'methods_vi': 'Tư duy Phản biện (Chương 3 · Vạch trần thống kê trung bình gộp & biến gây nhiễu, tr. 57–58) + Tư duy Phân tích (Chương 4 '
                '· Phân rã theo khoa)',
  'result_en': 'Proved zero admissions discrimination against women (4 of 6 largest departments favored female applicants) and redirected '
               'reform toward STEM pipeline outreach.',
  'result_vi': 'Chứng minh các hội đồng chấm tuyển không hề thiên vị nam giới, giúp nhà trường chuyển đúng trọng tâm sang khuyến khích nữ '
               'sinh nộp đơn vào các ngành kỹ thuật.'},
 {'id': 'cs-literary-digest',
  'ch': 'ch3',
  'cat': 'policy',
  'year': '1936',
  'domain_en': 'Polling · Selection Bias',
  'domain_vi': 'Thống kê Dư luận · Lệch Mẫu',
  'title_en': '2.4 Million Ballots & Dead Wrong: The 1936 Literary Digest Fiasco',
  'title_vi': 'Khảo Sát 2,4 Triệu Phiếu Vẫn Sai Bét: Thảm Họa Dự Báo Bầu Cử Mỹ 1936',
  'story_en': 'The Literary Digest mailed 10 million ballots and tallied 2.4 million replies predicting Alf Landon would crush FDR. '
              'Meanwhile young George Gallup polled just 50,000 representative voters and nailed FDR’s landslide—because the Digest '
              'sampled car owners and telephone subscribers during the Great Depression!',
  'story_vi': 'Tạp chí Literary Digest thu về tới 2,4 triệu phiếu khảo sát và tuyên bố Landon thắng đậm. Ngược lại, chàng trai trẻ George '
              'Gallup chỉ hỏi 50.000 cử tri đại diện và đoán trúng chiến thắng vang dội của Roosevelt—bởi danh sách 2,4 triệu người kia '
              'lấy từ sổ đăng ký ô tô và điện thoại (tầng lớp giàu thời Đại suy thoái)!',
  'lesson_en': 'A biased sample of 2,400,000 is far less accurate than an unbiased sample of 1,000.',
  'lesson_vi': 'Mẫu dữ liệu khổng lồ nhưng chọn lệch đối tượng luôn sai thảm hại hơn mẫu nhỏ mà khách quan.',
  'url': 'https://en.wikipedia.org/wiki/The_Literary_Digest#Presidential_poll',
  'src_label': 'Polling Case Study',
  'lab': 'traps',
  'methods_en': 'Critical Thinking (Ch. 3 · Sampling-Bias Audit & Evidence Representativeness, pp. 56–58) + Logical Thinking (Ch. 5 · '
                'Inductive Sample Rules, p. 94)',
  'methods_vi': 'Tư duy Phản biện (Chương 3 · Kiểm định tính đại diện của mẫu thống kê, tr. 56–58) + Tư duy Logic (Chương 5 · Quy tắc mẫu '
                'quy nạp, tr. 94)',
  'result_en': 'FDR won 60.8% of the popular vote and 46 of 48 states (crushing the Digest’s 57%-Landon prediction); Literary Digest '
               'folded within 18 months while Gallup pioneered scientific polling.',
  'result_vi': 'Roosevelt thắng áp đảo 46/48 bang (ngược hoàn toàn dự báo của tờ báo); Literary Digest phá sản sau 18 tháng, còn Gallup '
               'khai sinh ngành điều tra dư luận khoa học.'},
 {'id': 'cs-subprime-cdo',
  'ch': 'ch3',
  'cat': 'business',
  'year': '2008',
  'domain_en': 'Global Finance · Hidden Premise',
  'domain_vi': 'Tài chính Toàn cầu · Tiền đề Ngầm',
  'title_en': 'The 2008 Subprime AAA Illusion: One Unexamined Assumption Shook the World',
  'title_vi': 'Ảo Vọng Xếp Hạng AAA Năm 2008: Một Giả Định Ngầm Làm Rúng Động Thế Giới',
  'story_en': 'Wall Street bundled risky mortgages into ‘AAA risk-free’ bonds using complex Gaussian copula math. Inside the equations sat '
              'one unspoken assumption (#3 in Browne–Keeley): that housing prices in Florida, Nevada, and California would never fall at '
              'the same time.',
  'story_vi': 'Phố Wall đóng gói các khoản vay dưới chuẩn thành trái phiếu hạng AAA tuyệt đối an toàn nhờ mô hình toán học tinh vi. Nhưng '
              'toàn bộ lâu đài ấy dựng trên một giả định ngầm chưa từng kiểm chứng: giá nhà trên toàn nước Mỹ không bao giờ sụt giảm cùng '
              'một lúc!',
  'lesson_en': 'Fancy math built on a false premise guarantees precision-engineered disaster.',
  'lesson_vi': 'Mô hình toán học càng phức tạp mà đặt trên giả định gốc sai lầm thì hậu quả sụp đổ càng khôn lường.',
  'url': 'https://en.wikipedia.org/wiki/2008_financial_crisis',
  'src_label': 'Crisis Dossier',
  'lab': 'labs:octagon',
  'methods_en': 'Critical Thinking (Ch. 3 · Browne–Keeley Question #3: Exposing Unstated Assumptions, p. 54) + Probabilistic Thinking (Ch. '
                '8 · Tail Correlation Audit)',
  'methods_vi': 'Tư duy Phản biện (Chương 3 · Câu hỏi Browne–Keeley số 3: Bóc trần giả định ngầm, tr. 54) + Tư duy Xác suất (Chương 8 · '
                'Rủi ro đuôi tương quan)',
  'result_en': 'Triggered the 2008 Global Financial Crisis (> $2 trillion in bank write-downs), while the few investors who audited the '
               'hidden nationwide-housing assumption earned historic returns.',
  'result_vi': 'Châm ngòi Khủng hoảng Tài chính Toàn cầu 2008 gây thiệt hại hơn 2.000 tỷ USD, trong khi nhóm ít nhà đầu tư soi ra giả định '
               'ngầm này bảo toàn và nhân bội tài sản.'},
 {'id': 'cs-challenger-oring',
  'ch': 'ch4',
  'cat': 'aerospace',
  'year': '1986',
  'domain_en': 'Spaceflight · Root-Cause Data',
  'domain_vi': 'Vũ trụ · Phân tích Dữ liệu Gốc',
  'title_en': 'Challenger O-Rings & Richard Feynman’s Glass of Ice Water',
  'title_vi': 'Thảm Họa Tàu Con Thoi Challenger & Cốc Nước Đá Của Richard Feynman',
  'story_en': 'The night before launch at 29°F (−2°C), engineers warned rubber O-rings stiffen in freezing cold, yet charts showing only '
              'past damaged flights obscured the clean-flight comparison. On live TV, physicist Richard Feynman dunked an O-ring clamp '
              'into ice water—cutting straight to the physical root cause.',
  'story_vi': 'Đêm trước giờ phóng ở nhiệt độ −2°C, biểu đồ trình bày rời rạc chỉ vẽ các chuyến bay có vết cháy khiến ban lãnh đạo bỏ lỡ '
              'mối liên hệ nhiệt độ lạnh khi đặt cạnh các chuyến bay lành lặn. Nhà vật lý Richard Feynman nhúng thẳng vòng cao su vào cốc '
              'nước đá ngay tại phiên điều trần để phơi bày bản chất vật lý.',
  'lesson_en': 'Analytical clarity compares ALL cases (successes + failures) across the true causal variable.',
  'lesson_vi': 'Phân tích chuẩn xác buộc phải đặt cả ca thành công lẫn thất bại lên cùng một trục biến số.',
  'url': 'https://en.wikipedia.org/wiki/Space_Shuttle_Challenger_disaster#Rogers_Commission',
  'src_label': 'Rogers Commission',
  'lab': 'atlas:t-fishbone',
  'methods_en': 'Analytical Thinking (Ch. 4 · Root-Cause Decomposition & Full-Dataset Comparative Analysis, pp. 69–75, 82) + Scientific '
                'Thinking (Ch. 9 · Direct Physical Test)',
  'methods_vi': 'Tư duy Phân tích (Chương 4 · Mổ xẻ nguyên nhân gốc & Phân tích so sánh toàn bộ dữ liệu, tr. 69–75, 82) + Tư duy Khoa học '
                '(Chương 9 · Thực nghiệm trực tiếp)',
  'result_en': 'Pinpointed cold-stiffened rubber O-rings and management communication silos, Grounded the fleet 32 months to redesign '
               'booster joints, and reformed NASA engineering governance.',
  'result_vi': 'Xác định chính xác thủ phạm vòng đệm cao su mất đàn hồi ở nhiệt độ âm, buộc thiết kế lại tên lửa đẩy và cải tổ toàn diện '
               'quy trình an toàn của NASA.'},
 {'id': 'cs-gawande-checklist',
  'ch': 'ch4',
  'cat': 'medicine',
  'year': '2009',
  'domain_en': 'Surgery · Structural Decomposition',
  'domain_vi': 'Phẫu thuật · Chuẩn hóa Phân tích',
  'title_en': 'The 90-Second WHO Surgical Checklist That Cut Hospital Deaths by 47%',
  'title_vi': 'Bảng Kiểm Phẫu Thuật 90 Giây Của WHO Giảm 47% Tử Vong Tại 8 Quốc Gia',
  'story_en': 'Surgeon Atul Gawande borrowed aviation’s analytical checklists to create a 19-item pause across 8 global hospitals. '
              'Inpatient surgical mortality plunged from 1.5% to 0.8%—saving more lives than any billion-dollar drug.',
  'story_vi': 'Bác sĩ Atul Gawande đưa tư duy phân rã quy trình từ buồng lái máy bay vào phòng mổ qua bảng kiểm 19 mục chỉ mất 90 giây. Tỷ '
              'lệ tử vong hậu phẫu giảm gần một nửa (47%) trên toàn cầu mà không tốn thêm thiết bị đắt tiền nào.',
  'lesson_en': 'Structured decomposition frees expert working memory from preventable slips under pressure.',
  'lesson_vi': 'Công cụ phân tích giúp giải phóng bộ nhớ chuyên gia khỏi những sai sót sơ đẳng dưới áp lực cao.',
  'url': 'https://www.nejm.org/doi/full/10.1056/NEJMsa0810119',
  'src_label': 'New England J. Med',
  'lab': 'atlas:t-eisenhower',
  'methods_en': 'Analytical Thinking (Ch. 4 · Systematic Process Decomposition & Critical-Gate Prioritization, pp. 69–70, 80)',
  'methods_vi': 'Tư duy Phân tích (Chương 4 · Phân rã quy trình có hệ thống & Quản trị điểm chốt trọng yếu, tr. 69–70, 80)',
  'result_en': 'Across 7,688 patients in 8 global cities, major surgical complications fell 36% (from 11.0% to 7.0%) and inpatient deaths '
               'plunged 47% (from 1.5% to 0.8%).',
  'result_vi': 'Thử nghiệm trên 7.688 ca mổ tại 8 quốc gia giúp giảm 36% biến chứng hậu phẫu nghiêm trọng và giảm tới 47% tỷ lệ tử vong '
               'tại viện.'},
 {'id': 'cs-toyota-andon',
  'ch': 'ch4',
  'cat': 'business',
  'year': '1950s–Present',
  'domain_en': 'Lean Manufacturing · 5 Whys',
  'domain_vi': 'Sản xuất Tinh gọn · 5 Tại sao',
  'title_en': 'Toyota’s Andon Cord & Taiichi Ohno’s Five-Whys Floor Discipline',
  'title_vi': 'Sợi Dây Dừng Chuyền Andon & Kỷ Luật 5 Câu Hỏi Tại Sao Của Toyota',
  'story_en': 'In mass factories, workers were punished for stopping the conveyor belt, hiding defects until cars reached dealers. Toyota '
              'gave every worker an overhead Andon cord to halt the line immediately and run a 5-Whys root-cause drill on the spot (Ch. 4, '
              'p. 76).',
  'story_vi': 'Ở các nhà máy cũ, công nhân sợ bị phạt nên giấu lỗi cho xe chạy tiếp. Toyota trao quyền cho mọi người thợ giật dây Andon '
              'dừng chuyền ngay khi thấy bất thường để cùng truy 5 câu hỏi Tại sao tìm tận gốc rễ (tr. 76).',
  'lesson_en': 'Surface small anomalies early; fixing root causes at the source is 100x cheaper than downstream recalls.',
  'lesson_vi': 'Phát hiện và trị tận gốc ngay tại nguồn rẻ hơn gấp trăm lần so với thu hồi hàng triệu sản phẩm lỗi.',
  'url': 'https://global.toyota/en/company/vision-and-philosophy/production-system/',
  'src_label': 'Toyota Global TPS',
  'lab': 'atlas:t-five-whys',
  'methods_en': 'Analytical Thinking (Ch. 4 · Taiichi Ohno’s 5 Whys & 6M Fishbone Root-Cause Analysis, pp. 74–79) + Systems Thinking (Ch. '
                '6 · No-Blame Learning Loop, p. 115)',
  'methods_vi': 'Tư duy Phân tích (Chương 4 · 5 Câu hỏi Tại sao & Biểu đồ Xương cá 6M, tr. 74–79) + Tư duy Hệ thống (Chương 6 · Vòng lặp '
                'học hỏi không giấu lỗi, tr. 115)',
  'result_en': 'Cut defect rates and assembly rework to the lowest in global automotive history, propelling Toyota past legacy mass '
               'producers to become the world’s #1 automaker.',
  'result_vi': 'Đưa tỷ lệ lỗi xuất xưởng xuống mức thấp nhất lịch sử ngành ô tô, đưa Toyota vượt qua các hãng sản xuất đại trà cũ để giữ '
               'ngôi đầu thế giới.'},
 {'id': 'cs-netflix-swot',
  'ch': 'ch4',
  'cat': 'ai-tech',
  'year': '2007–2013',
  'domain_en': 'Tech Strategy · SWOT Pivot',
  'domain_vi': 'Chiến lược Số · Tự Chuyển mình',
  'title_en': 'Netflix’s Self-Cannibalization: Killing Its Own DVD Cash Cow Before Broadband Did',
  'title_vi': 'Netflix Tự Đập Nồi Cơm Đĩa DVD Khi Đang Ở Đỉnh Cao Lợi Nhuận',
  'story_en': 'In 2007, DVD-by-mail generated nearly 100% of Netflix’s profit, while Blockbuster stumbled. Mapping external broadband '
              'Opportunity/Threat against internal recommendation Strengths, Reed Hastings poured cash into streaming—surviving the death '
              'of physical media.',
  'story_vi': 'Năm 2007, cho thuê đĩa DVD qua bưu điện vẫn mang lại gần 100% lợi nhuận cho Netflix. Nhưng nhìn thẳng vào biến chuyển băng '
              'thông Internet trên ma trận SWOT, Netflix chủ động dồn lực sang phát trực tuyến trước khi đĩa vật lý biến mất.',
  'lesson_en': 'Honest SWOT analysis prepares you to disrupt your own business before outsiders do.',
  'lesson_vi': 'Phân tích SWOT trung thực giúp ta tự làm mới chính mình trước khi bị thời cuộc đào thải.',
  'url': 'https://en.wikipedia.org/wiki/Netflix#Transition_to_streaming_services_(2007%E2%80%932012)',
  'src_label': 'Company History',
  'lab': 'atlas:t-swot',
  'methods_en': 'Analytical Thinking (Ch. 4 · SWOT Internal/External Matrix, pp. 71–73) + Creative Thinking (Ch. 2 · ‘What If’ Business '
                'Model Reframing, p. 45)',
  'methods_vi': 'Tư duy Phân tích (Chương 4 · Phân tích ma trận SWOT, tr. 71–73) + Tư duy Sáng tạo (Chương 2 · Câu hỏi ‘Sẽ ra sao nếu’, '
                'tr. 45)',
  'result_en': 'Grew from 7 million DVD-mail members in 2007 to >280 million global streaming subscribers while rival Blockbuster (which '
               'clung to store late fees) went bankrupt in 2010.',
  'result_vi': 'Tăng trưởng từ 7 triệu thuê bao DVD năm 2007 lên hơn 280 triệu thuê bao trực tuyến toàn cầu, trong khi đối thủ Blockbuster '
               'phá sản năm 2010.'},
 {'id': 'cs-john-snow',
  'ch': 'ch5',
  'cat': 'medicine',
  'year': '1854',
  'domain_en': 'Epidemiology · Causal Proof',
  'domain_vi': 'Dịch tễ học · Kiểm chứng Nhân quả',
  'title_en': 'Dr. John Snow’s Soho Ghost Map & The Broad Street Pump Handle',
  'title_vi': 'Bản Đồ Dịch Tả Luân Đôn 1854 Của John Snow & Chiếc Tay Bơm Phố Broad',
  'story_en': 'Victorian elites blamed cholera on ‘foul miasma air.’ Physician John Snow plotted every death house-by-house—and noticed '
              'brewery workers next to the Broad Street water pump never died because they drank beer instead of pump water, while a widow '
              'miles away who had Broad Street water delivered died! Removing the pump handle halted the outbreak.',
  'story_vi': 'Giới y học đương thời tin bệnh tả lây qua “khí độc bốc mùi”. Bác sĩ John Snow chấm từng ca tử vong lên bản đồ và phát hiện: '
              'công nhân xưởng bia sát giếng nước phố Broad không ai mắc bệnh (vì họ chỉ uống bia!), trong khi một bà lão ở xa đặt chở '
              'nước giếng này về uống lại tử vong! Tháo tay bơm nước lập tức dập tắt ổ dịch.',
  'lesson_en': 'Crucial outliers (brewery workers & distant widow) clinch causal logic where correlations stay blurry (Ch. 5, p. 95).',
  'lesson_vi': 'Những trường hợp đối chứng sắc bén chính là chìa khóa khóa chặt mắt xích nhân quả thực sự (tr. 95).',
  'url': 'https://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak',
  'src_label': 'Epidemiology Classic',
  'lab': 'atlas:t-causal-logic',
  'methods_en': 'Logical Thinking (Ch. 5 · 5-Criterion Causal Inference & Crucial Outlier Elimination, pp. 95–96) + Analytical Spatial '
                'Mapping',
  'methods_vi': 'Tư duy Logic (Chương 5 · Suy luận nhân quả 5 tiêu chuẩn & Đối chứng ngoại lệ, tr. 95–96) + Phân tích dữ liệu không gian',
  'result_en': 'Removing the Broad Street pump handle ended the Soho cholera surge immediately, refuted miasma dogma, and spurred modern '
               'urban clean-water & sewage engineering.',
  'result_vi': 'Tháo tay bơm giếng phố Broad dập tắt ngay ổ dịch tả, bác bỏ thuyết ‘khí độc’ và đặt nền móng cho hệ thống cấp thoát nước '
               'đô thị hiện đại.'},
 {'id': 'cs-semmelweis',
  'ch': 'ch5',
  'cat': 'medicine',
  'year': '1847',
  'domain_en': 'Medical Logic · Method of Difference',
  'domain_vi': 'Logic Y học · Phép Đối chứng',
  'title_en': 'Ignaz Semmelweis & The Two Maternity Clinics of Vienna',
  'title_vi': 'Bác Sĩ Semmelweis & Bí Ẩn Tử Vong Chênh Lệch Gấp 5 Lần Giữa Hai Khoa Sản',
  'story_en': 'Vienna General Hospital had two side-by-side maternity wards: Clinic 1 (doctors) had a 10%+ maternal death rate; Clinic 2 '
              '(midwives) had 2%. Semmelweis eliminated diet, ventilation, and crowding—isolating one difference: doctors walked straight '
              'from autopsies to deliveries without washing hands in chlorinated lime.',
  'story_vi': 'Bệnh viện Viên có hai khoa sản sát vách nhau: Khoa 1 (bác sĩ đỡ) sản phụ tử vong hơn 10%, Khoa 2 (nữ hộ sinh đỡ) chỉ 2%. '
              'Dùng phép loại trừ logic từng giả thuyết, Semmelweis tìm ra điểm khác biệt duy nhất: các bác sĩ vừa mổ tử thi xong đã sang '
              'đỡ đẻ mà chưa rửa tay sát khuẩn!',
  'lesson_en': 'Systematic elimination of rival hypotheses isolates hidden mechanisms even before germ theory existed.',
  'lesson_vi': 'Loại trừ có hệ thống giúp tìm ra quy luật cứu người ngay cả khi nhân loại chưa nhìn thấy vi trùng.',
  'url': 'https://en.wikipedia.org/wiki/Ignaz_Semmelweis',
  'src_label': 'Historical Dossier',
  'lab': 'atlas:t-deduction',
  'methods_en': 'Logical Thinking (Ch. 5 · Deductive Falsification of Rival Premises & Mill’s Method of Difference, pp. 91–96)',
  'methods_vi': 'Tư duy Logic (Chương 5 · Loại trừ diễn dịch các tiền đề sai & Phép đối chứng tìm khác biệt duy nhất, tr. 91–96)',
  'result_en': 'Mandatory chlorinated-lime handwashing slashed Clinic 1 maternal mortality by 90%—from 18.3% in April 1847 down to under '
               '2% within two months.',
  'result_vi': 'Quy định rửa tay bằng nước vôi clo kéo tỷ lệ tử vong sản phụ tại Khoa 1 giảm 90%—từ đỉnh 18,3% xuống dưới 2% chỉ sau hai '
               'tháng.'},
 {'id': 'cs-sally-clark',
  'ch': 'ch5',
  'cat': 'policy',
  'year': '1999',
  'domain_en': 'Forensic Law · Conditional Fallacy',
  'domain_vi': 'Tư pháp · Ngụy biện Xác suất',
  'title_en': 'The Sally Clark Wrongful Conviction: How ‘1 in 73 Million’ Violated Logic',
  'title_vi': 'Án Oan Sally Clark: Khi Con Số ‘1 Phần 73 Triệu’ Vi Phạm Logic Độc Lập',
  'story_en': 'After two infants died of SIDS in one family, an expert witness squared 1/8,543 × 1/8,543 = 1 in 73 million and the jury '
              'convicted mother Sally Clark. The Royal Statistical Society intervened: squaring assumes shared genes and environment have '
              'ZERO link between siblings, AND confuses P(Evidence | Innocent) with P(Innocent | Evidence)!',
  'story_vi': 'Khi hai trẻ sơ sinh trong một gia đình đột tử, nhân chứng tòa án lấy 1/8.543 × 1/8.543 = 1/73 triệu khiến người mẹ bị kết '
              'án oan. Hội Thống kê Hoàng gia Anh phải lên tiếng: phép nhân ấy sai cơ bản vì hai anh em ruột có chung yếu tố di truyền, '
              'đồng thời tòa đã đánh tráo xác suất có điều kiện!',
  'lesson_en': 'Logical & statistical literacy in courtrooms literally separates justice from tragedy.',
  'lesson_vi': 'Sai một bước ngữ pháp logic và điều kiện xác suất có thể hủy hoại cả một đời người.',
  'url': 'https://en.wikipedia.org/wiki/Sally_Clark',
  'src_label': 'Royal Stat Society Case',
  'lab': 'labs:bayes',
  'methods_en': 'Logical Thinking (Ch. 5 · Auditing False Premise of Independence & Conditional Fallacy, pp. 91–92) + Probabilistic '
                'Thinking (Ch. 8 · Bayes’ Theorem & Appendix, p. 159)',
  'methods_vi': 'Tư duy Logic (Chương 5 · Vạch trần tiền đề độc lập giả tạo, tr. 91–92) + Tư duy Xác suất (Chương 8 · Định lý Bayes & Công '
                'thức xác suất có điều kiện, tr. 159)',
  'result_en': 'Court of Appeal overturned Sally Clark’s wrongful conviction in 2003, reviewed hundreds of criminal cases, and reformed '
               'forensic statistical standards across UK courts.',
  'result_vi': 'Tòa Phúc thẩm Anh hủy bản án oan năm 2003, rà soát lại hàng trăm vụ án tương tự và siết chặt quy chuẩn thống kê pháp y tại '
               'tòa án.'},
 {'id': 'cs-bradford-hill',
  'ch': 'ch5',
  'cat': 'medicine',
  'year': '1965',
  'domain_en': 'Public Health · Causal Criteria',
  'domain_vi': 'Y tế Công cộng · Tiêu chuẩn Nhân quả',
  'title_en': 'Defeating Tobacco Doubt: Austin Bradford Hill’s 9 Criteria for Causation',
  'title_vi': 'Vạch Trần Ngành Thuốc Lá: Bộ Tiêu Chuẩn Chứng Minh Nhân Quả Của Bradford Hill',
  'story_en': "For decades, cigarette lobbyists argued: 'You can’t lock humans in cages to force smoking, so lung cancer is merely "
              "correlation, not causation!' Epidemiologist Sir Austin Bradford Hill codified dose-response gradient, temporality, "
              'biological plausibility, and consistency—mirroring Chapter 5’s 5-criterion causal check (p. 95).',
  'story_vi': 'Suốt nhiều thập kỷ, các hãng thuốc lá cãi: “Không thể nhốt người ép hút thuốc làm thí nghiệm, nên ung thư phổi chỉ là tương '
              'quan ngẫu nhiên thôi!” Nhà dịch tễ học Bradford Hill thiết lập khung kiểm chứng nhân quả (thời gian trước–sau, liều '
              'lượng–đáp ứng, cơ chế sinh học)—chính là nền tảng mục kiểm chứng nhân quả trang 95.',
  'lesson_en': 'Rigorous multi-criterion causal logic defeats weaponized skepticism.',
  'lesson_vi': 'Hệ tiêu chuẩn nhân quả chặt chẽ giúp khoa học đánh bại mọi ngụy biện đánh bùn sang ao.',
  'url': 'https://en.wikipedia.org/wiki/Bradford_Hill_criteria',
  'src_label': 'Causal Framework',
  'lab': 'atlas:t-causal-logic',
  'methods_en': 'Logical Thinking (Ch. 5 · Multi-Criterion Causal Reasoning: Correlation, Temporality, Mechanism & Confounder Control, pp. '
                '95–96)',
  'methods_vi': 'Tư duy Logic (Chương 5 · Kiểm chứng nhân quả đa tiêu chuẩn: Tương quan, Thời gian, Cơ chế & Loại trừ nhiễu, tr. 95–96)',
  'result_en': 'Clinched the scientific and legal proof that smoking causes lung cancer—triggering global health warnings, public smoking '
               'bans, and millions of prevented deaths.',
  'result_vi': 'Khóa chặt bằng chứng khoa học và pháp lý rằng thuốc lá gây ung thư phổi, dẫn tới luật cảnh báo sức khỏe toàn cầu và cứu '
               'sống hàng triệu người.'},
 {'id': 'cs-hanoi-rats',
  'ch': 'ch6',
  'cat': 'policy',
  'year': '1902',
  'domain_en': 'Hanoi History · Perverse Incentive',
  'domain_vi': 'Lịch sử Hà Nội 1902 · Phản tác dụng Hệ thống',
  'title_en': 'The 1902 Great Hanoi Rat Massacre: Paying Per Tail Bred More Rats!',
  'title_vi': 'Vụ Săn Chuột Hà Nội Năm 1902: Trả Tiền Theo Đuôi Khiến Người Dân… Nuôi Thêm Chuột!',
  'story_en': 'To eradicate sewer rats in colonial Hanoi, authorities offered 1 cent per severed rat tail (proof of kill without carrying '
              'carcasses). Soon inspectors spotted thousands of healthy TAILLESS rats running through Hanoi—hunters were docking tails to '
              'keep breeding stock alive, plus smuggling rat farms in from the countryside!',
  'story_vi': 'Để diệt chuột cống tại Hà Nội năm 1902, chính quyền thuộc địa treo thưởng 1 xu cho mỗi chiếc đuôi chuột nộp về. Chỉ ít lâu '
              'sau, khắp phố phường xuất hiện vô số con chuột khỏe mạnh… cụt đuôi chạy nhởn nhơ—vì người bắt cắt đuôi rồi thả chuột bố mẹ '
              'ra cho đẻ tiếp, thậm chí lập trại nuôi chuột ở ngoại thành!',
  'lesson_en': 'Senge’s Law #1 & #2 in vivid Vietnamese history: linear incentives spawn reinforcing counter-loops.',
  'lesson_vi': 'Minh chứng sống động ngay tại Hà Nội cho Định luật Senge #1 & #2: giải pháp tuyến tính đẻ ra vòng lặp ngược chiều.',
  'url': 'https://en.wikipedia.org/wiki/Great_Hanoi_Rat_Massacre',
  'src_label': '1902 Hanoi Dossier',
  'lab': 'labs:systems',
  'methods_en': 'Systems Thinking (Ch. 6 · Senge’s Laws #1–#2 & Reinforcing Perverse-Incentive CLD Audit, pp. 107–117)',
  'methods_vi': 'Tư duy Hệ thống (Chương 6 · Định luật Senge #1–#2 & Sơ đồ vòng phản hồi tăng cường ngược chiều, tr. 107–117)',
  'result_en': 'Rat population and plague hazard grew worse as hunters bred rats for tails; colonial officials had to scrap the bounty '
               'completely—coining the global ‘Cobra/Rat Effect’ lesson.',
  'result_vi': 'Số lượng chuột không giảm mà còn tăng vọt vì dân cắt đuôi nuôi chuột đẻ tiếp; chính quyền buộc phải hủy bỏ chương trình '
               'treo thưởng.'},
 {'id': 'cs-yellowstone-wolves',
  'ch': 'ch6',
  'cat': 'medicine',
  'year': '1995',
  'domain_en': 'Ecology · Trophic Cascade',
  'domain_vi': 'Sinh thái học · Thác dinh dưỡng',
  'title_en': 'How 41 Reintroduced Wolves Changed the Rivers of Yellowstone',
  'title_vi': '41 Cá Thể Sói Xám Tái Thả Đã Cứu Cả Những Dòng Sông Ở Yellowstone Như Thế Nào?',
  'story_en': 'After wolves were eradicated in 1926, Yellowstone elk multiplied and chewed young willow and aspen shoots to dust, eroding '
              'riverbanks (just like Chapter 6’s p. 114 savanna story!). Returning 41 wolves in 1995 restored movement balance—trees grew '
              '5x taller, beavers returned, and river channels stabilized.',
  'story_vi': 'Sau khi sói bị tiêu diệt năm 1926, đàn hươu nai sinh sôi ăn trụi cây non ven suối làm sạt lở bờ sông (y hệt ví dụ đồng cỏ '
              'trang 114!). Khi 41 cá thể sói được đưa trở lại năm 1995, vòng cân bằng tự nhiên hồi sinh kéo theo rừng liễu, hải ly và '
              'dòng chảy ổn định trở lại.',
  'lesson_en': 'Emergence (p. 114): a system’s stability arises from relationships between parts, never parts alone.',
  'lesson_vi': 'Tính hợp trội (tr. 114): sức sống hệ thống nằm ở mối liên kết giữa các mắt xích chứ không nằm ở từng loài riêng lẻ.',
  'url': 'https://www.nps.gov/yell/learn/nature/wolf-restoration.htm',
  'src_label': 'US National Park Service',
  'lab': 'labs:systems',
  'methods_en': 'Systems Thinking (Ch. 6 · Predator–Prey Balancing Loop B [Fig. 6.1, p. 112], Emergence & Holistic Boundaries, pp. '
                '104–112)',
  'methods_vi': 'Tư duy Hệ thống (Chương 6 · Vòng phản hồi cân bằng thú ăn thịt – con mồi [Hình 6.1, tr. 112] & Tính trồi hệ sinh thái, '
                'tr. 104–112)',
  'result_en': 'Overgrazed willow and aspen groves rebounded up to 5× in height, beaver colonies multiplied from 1 to 9+, songbirds '
               'returned, and eroding riverbanks stabilized.',
  'result_vi': 'Rừng cây non ven suối cao gấp 5 lần, quần thể hải ly tăng từ 1 lên 9 đàn, chim chóc quay lại và bờ sông Yellowstone ổn '
               'định trở lại.'},
 {'id': 'cs-svb-run',
  'ch': 'ch6',
  'cat': 'business',
  'year': '2023',
  'domain_en': 'Banking · Exponential R-Loop',
  'domain_vi': 'Ngân hàng · Vòng tăng cường R1',
  'title_en': 'Silicon Valley Bank’s 36-Hour Implosion: A Smartphone-Speed Reinforcing Loop',
  'title_vi': '36 Giờ Sụp Đổ Của Ngân Hàng Thung Lũng Silicon (SVB): Vòng Xoáy Hoảng Loạn Thời Công Nghệ',
  'story_en': 'Textbook illustration of Chapter 6’s p. 123 bank-run graph: duration losses forced SVB to sell bonds -> Slack & group-chat '
              'panic spread among VCs -> $42 billion in mobile wire withdrawals hit in a single day, collapsing the 16th-largest US bank '
              'before weekend.',
  'story_vi': 'Minh họa thời đại số cho đồ thị rút tiền ngân hàng ở trang 123: tin lỗ trái phiếu lan qua các nhóm chat nhà đầu tư -> kích '
              'hoạt vòng lặp tăng cường tự kỷ ám thị -> 42 tỷ USD bị rút qua điện thoại chỉ trong 1 ngày làm sụp đổ ngân hàng lớn thứ 16 '
              'nước Mỹ.',
  'lesson_en': 'When digital speed removes friction from a Reinforcing panic loop (R), circuit-breaker Balancing loops must act in hours, '
               'not weeks.',
  'lesson_vi': 'Khi công nghệ xóa bỏ độ trễ của vòng hoảng loạn R, van cân bằng B phải can thiệp tính bằng giờ.',
  'url': 'https://en.wikipedia.org/wiki/Collapse_of_Silicon_Valley_Bank',
  'src_label': 'SVB Collapse Analysis',
  'lab': 'labs:systems',
  'methods_en': 'Systems Thinking (Ch. 6 · Unchecked Reinforcing Panic Loop R & Fig. 6.10 Runaway Bank-Collapse BOT Curve, p. 123)',
  'methods_vi': 'Tư duy Hệ thống (Chương 6 · Vòng phản hồi tăng cường R mất kiểm soát & Đồ thị sụp đổ ngân hàng Hình 6.10, tr. 123)',
  'result_en': '$42 billion exited in 24 hours (a $100B+ two-day queue), collapsing a $209B bank in 36 hours and forcing emergency federal '
               'systemic-risk deposit guarantees.',
  'result_vi': '42 tỷ USD bị rút sạch trong 24 giờ, đánh sập ngân hàng quy mô 209 tỷ USD chỉ sau 36 tiếng và buộc cơ quan liên bang phải '
               'kích hoạt bảo lãnh khẩn cấp.'},
 {'id': 'cs-boeing-mcas',
  'ch': 'ch6',
  'cat': 'aerospace',
  'year': '2018–2019',
  'domain_en': 'Aerospace · Symptom Patching',
  'domain_vi': 'Hàng không · Vá Chữa Triệu chứng',
  'title_en': 'Boeing 737 MAX & MCAS: Patching Hardware Physics With a Single-Sensor Software Band-Aid',
  'title_vi': 'Boeing 737 MAX & Hệ Thống MCAS: Dùng Bản Vá Phần Mềm Che Đậy Vấn Đề Khí Động Học',
  'story_en': 'Rushing to match Airbus without designing a new airframe, larger engines shifted pitch aerodynamics. Instead of structural '
              'redesign, software (MCAS) pushed the nose down based on ONE angle-of-attack sensor, while schedule pressure muted internal '
              'engineering warnings (p. 123 error-hiding loop).',
  'story_vi': 'Vì áp lực tiến độ cạnh tranh không muốn thiết kế lại khung thân khi lắp động cơ to hơn, hãng dùng phần mềm MCAS tự chúc mũi '
              'máy bay chỉ dựa vào MỘT cảm biến duy nhất—đúng kiểu “chữa triệu chứng” (Hình 6.7, tr. 118) cộng với văn hóa ngại báo tin '
              'xấu.',
  'lesson_en': 'Symptomatic shortcuts in safety-critical systems compound hidden catastrophic debt.',
  'lesson_vi': 'Dùng bản vá triệu chứng để né chi phí cấu trúc luôn tích tụ món nợ thảm họa về sau.',
  'url': 'https://en.wikipedia.org/wiki/Boeing_737_MAX_groundings',
  'src_label': 'Engineering Report',
  'lab': 'atlas:t-senge-laws',
  'methods_en': 'Systems Thinking (Ch. 6 · Fig. 6.7 Symptom-Patching Trap, p. 118 + Figs. 6.3–6.4 Error-Suppression Loop, p. 115)',
  'methods_vi': 'Tư duy Hệ thống (Chương 6 · Bẫy chữa triệu chứng Hình 6.7, tr. 118 & Vòng lặp giấu lỗi Hình 6.3–6.4, tr. 115)',
  'result_en': 'Two fatal crashes (346 lives lost), a 20-month worldwide fleet grounding, >$20 billion in direct fines and losses, and '
               'mandatory dual-sensor architecture redesign.',
  'result_vi': 'Hai thảm họa cướp đi 346 sinh mạng, toàn bộ đội bay bị cấm bay 20 tháng trên toàn cầu, thiệt hại trực tiếp hơn 20 tỷ USD '
               'và phải thiết kế lại hệ thống kép.'},
 {'id': 'cs-shell-scenarios',
  'ch': 'ch7',
  'cat': 'business',
  'year': '1973',
  'domain_en': 'Energy Strategy · Scenario Worlds',
  'domain_vi': 'Chiến lược Năng lượng · Đa kịch bản',
  'title_en': 'Pierre Wack & Royal Dutch Shell: Rehearsing the 1973 Oil Shock Years Before It Hit',
  'title_vi': 'Pierre Wack & Tập Đoàn Shell: Diễn Tập Khủng Hoảng Dầu Mỏ 1973 Trước Khi Cả Thế Giới Trở Tay',
  'story_en': 'While rivals extrapolated smooth 6%/year oil demand forever, Shell planner Pierre Wack built two vivid Scenario '
              'Worlds—including an OPEC supply-shock world. When prices quadrupled overnight in October 1973, Shell’s leaders adapted '
              'immediately, vaulting from the weakest Seven Sister to the industry’s top tier.',
  'story_vi': 'Khi mọi đối thủ đều vẽ đường thẳng dự báo giá dầu êm ả mãi mãi, chiến lược gia Pierre Wack của Shell xây dựng sẵn kịch bản '
              'cú sốc nguồn cung Trung Đông. Khi khủng hoảng 1973 nổ ra làm giá dầu tăng gấp 4, Shell phản ứng tức thì và vươn từ nhóm '
              'cuối lên dẫn đầu thế giới.',
  'lesson_en': 'Scenario Planning (pp. 133–135) is not fortune-telling; it pre-wires institutional reflexes before the storm.',
  'lesson_vi': 'Hoạch định kịch bản (tr. 133–135) không phải bói toán tương lai mà là luyện sẵn phản xạ sống còn trước biến cố.',
  'url': 'https://hbr.org/1985/09/scenarios-uncharted-waters-ahead',
  'src_label': 'HBR Classic by Pierre Wack',
  'lab': 'atlas:t-scenarios',
  'methods_en': 'Strategic Thinking (Ch. 7 · PESTLE Macro Scan & 6-Step Scenario Strategy Construction, pp. 131–135)',
  'methods_vi': 'Tư duy Chiến lược (Chương 7 · Quét vĩ mô PESTLE & Quy trình 6 bước xây dựng chiến lược theo Kịch bản, tr. 131–135)',
  'result_en': 'Shell pivoted refining and shipping months ahead of paralyzed competitors during the 1973 OPEC embargo, vaulting from #7 '
               'to the top 2 most profitable oil majors on Earth.',
  'result_vi': 'Shell xoay chuyển chuỗi lọc dầu và vận tải đi trước mọi đối thủ trong cú sốc dầu mỏ 1973, vươn từ vị trí yếu nhất trong '
               '‘Bảy Chị Em’ lên top 2 tập đoàn dầu khí dẫn đầu thế giới.'},
 {'id': 'cs-axelrod-tft',
  'ch': 'ch7',
  'cat': 'ai-tech',
  'year': '1980',
  'domain_en': 'Game Theory · Repeated Play',
  'domain_vi': 'Lý thuyết Trò chơi · Chiến lược Lặp',
  'title_en': 'Axelrod’s Computer Tournament: Why a 4-Line ‘Tit-for-Tat’ Code Beat Every Sneaky Rival',
  'title_vi': 'Giải Đấu Máy Tính Của Axelrod: Vì Sao 4 Dòng Lệnh ‘Có Đi Có Lại’ Đánh Bại Mọi Thuật Toán Ranh Mãnh?',
  'story_en': 'Political scientist Robert Axelrod invited top game theorists to submit programs for a 200-round Prisoner’s Dilemma '
              'tournament. Complex, deceptive predators all lost to Anatol Rapoport’s simplest 4-line code, Tit-for-Tat: 1) Start '
              'cooperative, 2) Mirror if betrayed, 3) Forgive immediately when they cooperate again, 4) Be predictable.',
  'story_vi': 'Giáo sư Robert Axelrod mở giải đấu Tiến thoái lưỡng nan của tù nhân lặp lại 200 vòng giữa các chuyên gia hàng đầu. Mọi '
              'thuật toán gian xảo hiểm hóc đều thua đoạn mã ngắn nhất chỉ 4 dòng của Anatol Rapoport (Tit-for-Tat): Khởi đầu tử tế -> Bị '
              'phản thì đáp trả đúng mức -> Biết tha thứ ngay -> Minh bạch rõ ràng.',
  'lesson_en': 'In long-horizon life and business, clarity + reciprocity + swift forgiveness outcompetes cynicism (pp. 136–137).',
  'lesson_vi': 'Trong cuộc chơi dài hạn của cuộc đời, tử tế đi kèm nguyên tắc rõ ràng luôn thắng sự khôn lỏi chộp giật.',
  'url': 'https://en.wikipedia.org/wiki/The_Evolution_of_Cooperation',
  'src_label': 'Evolution of Cooperation',
  'lab': 'labs:games',
  'methods_en': 'Strategic Thinking (Ch. 7 · Repeated Prisoner’s Dilemma Game Theory, pp. 136–137)',
  'methods_vi': 'Tư duy Chiến lược (Chương 7 · Lý thuyết trò chơi: Tiến thoái lưỡng nan của tù nhân lặp lại nhiều vòng, tr. 136–137)',
  'result_en': 'Rapoport’s 4-line Tit-for-Tat won both global computer tournaments with the highest cumulative score, reshaping '
               'evolutionary biology, diplomacy, and contract design.',
  'result_vi': 'Thuật toán 4 dòng ‘Có đi có lại’ vô địch cả hai kỳ giải đấu máy tính quốc tế, trở thành nguyên lý kinh điển trong ngoại '
               'giao, kinh tế học và đàm phán dài hạn.'},
 {'id': 'cs-cuban-missiles',
  'ch': 'ch7',
  'cat': 'policy',
  'year': '1962',
  'domain_en': 'Geopolitics · Chicken Game',
  'domain_vi': 'Địa chính trị · Hóa giải Trò chơi Gà',
  'title_en': 'Thirteen Days in October 1962: Escaping Nuclear ‘Chicken’ Without Humiliation',
  'title_vi': '13 Ngày Tháng Mười Năm 1962: Hóa Giải ‘Trò Chơi Gà’ Hạt Nhân Mà Không Đẩy Đối Phương Vào Chân Tường',
  'story_en': 'Hawks urged JFK to bomb Cuban missile sites immediately. Recognizing Chapter 7’s Chicken Game (p. 137)—where cornering a '
              'proud adversary causes mutual annihilation—Kennedy chose a naval ‘quarantine’ (giving Khrushchev time to think) plus a '
              'quiet Jupiter-missile trade in Turkey so both sides stepped back alive.',
  'story_vi': 'Phe diều hâu giục Tổng thống Kennedy không kích ngay lập tức. Nhận rõ thế Trò chơi Gà (tr. 137)—nếu dồn đối thủ mất sạch '
              'thể diện cả hai sẽ cùng hủy diệt—Kennedy chọn vòng phong tỏa mềm trên biển để kéo giãn thời gian suy nghĩ, kèm thỏa thuận '
              'rút tên lửa ở Thổ Nhĩ Kỳ mở lối thoát danh dự cho cả hai bên.',
  'lesson_en': 'Master strategists build golden bridges for rivals to de-escalate rather than forcing catastrophic collisions.',
  'lesson_vi': 'Nhà chiến lược bậc thầy luôn mở lối thoát danh dự cho đối phương thay vì ép nhau lao xuống vực.',
  'url': 'https://en.wikipedia.org/wiki/Cuban_Missile_Crisis',
  'src_label': 'Historical Archive',
  'lab': 'labs:games',
  'methods_en': 'Strategic Thinking (Ch. 7 · Chicken Game De-Escalation, p. 137) + Creative Thinking (Ch. 2 · Reframing Beyond Binary '
                'Strike/Surrender)',
  'methods_vi': 'Tư duy Chiến lược (Chương 7 · Hóa giải Trò chơi Gà, tr. 137) + Tư duy Sáng tạo (Chương 2 · Vượt khung nhị nguyên Không '
                'kích / Đầu hàng)',
  'result_en': 'Averted global thermonuclear war, removed Soviet nuclear missiles from Cuba peacefully, and established the direct '
               'Moscow–Washington hotline & 1963 Test Ban Treaty.',
  'result_vi': 'Ngăn chặn chiến tranh hạt nhân hủy diệt nhân loại, tháo dỡ hòa bình tên lửa tại Cuba và khai sinh đường dây nóng '
               'Washington–Moskva cùng Hiệp ước cấm thử hạt nhân 1963.'},
 {'id': 'cs-fcc-auction',
  'ch': 'ch7',
  'cat': 'business',
  'year': '1994 / Nobel 2020',
  'domain_en': 'Mechanism Design · Incentives',
  'domain_vi': 'Thiết kế Luật chơi · Nobel Kinh tế',
  'title_en': 'The $61B Nobel Spectrum Auction: Engineering Fair Rules Like the Cake-Cutting Game',
  'title_vi': 'Đấu Giá Tần Số Viễn Thông 61 Tỷ USD (Giải Nobel 2020): Nghệ Thuật Thiết Kế Luật Chơi Tự Giác',
  'story_en': 'Previously, governments gave away telecom airwaves via slow lotteries or beauty contests. Economists Paul Milgrom and '
              'Robert Wilson generalized Chapter 7’s Cake-Cutting insight into Simultaneous Multiple-Round Auctions—raising tens of '
              'billions for the public while matching spectrum to the builders who valued it most.',
  'story_vi': 'Thay vì cấp phát xin–cho hay bốc thăm may rủi, hai nhà kinh tế Paul Milgrom và Robert Wilson mở rộng tinh thần Trò chơi '
              'Chia bánh (tr. 138) thành cơ chế đấu giá đồng thời nhiều vòng—thu về hàng chục tỷ USD cho ngân sách công một cách minh '
              'bạch.',
  'lesson_en': 'Smart rules align private self-interest with public fairness automatically.',
  'lesson_vi': 'Luật chơi thông minh biến động lực cá nhân thành kết quả công bằng cho toàn xã hội.',
  'url': 'https://www.nobelprize.org/prizes/economic-sciences/2020/popular-information/',
  'src_label': 'NobelPrize.org Economics',
  'lab': 'labs:games',
  'methods_en': 'Strategic Thinking (Ch. 7 · Incentive-Compatible Mechanism Design & Fair Cake-Cutting Principle, p. 138)',
  'methods_vi': 'Tư duy Chiến lược (Chương 7 · Thiết kế luật chơi tương thích động lực & Nguyên lý Chia bánh công bằng, tr. 138)',
  'result_en': 'Generated >$60B for the US Treasury in its first two decades (and >$200B globally), sped up mobile wireless rollout, and '
               'won the 2020 Nobel Prize in Economics.',
  'result_vi': 'Thu về hơn 60 tỷ USD cho ngân sách Mỹ (và hơn 200 tỷ USD trên toàn cầu), phân bổ tối ưu phổ tần di động và mang về Giải '
               'Nobel Kinh tế năm 2020.'},
 {'id': 'cs-scorpion-bayes',
  'ch': 'ch8',
  'cat': 'aerospace',
  'year': '1968 & 2011',
  'domain_en': 'Ocean Search · Bayesian Maps',
  'domain_vi': 'Tìm kiếm Đại dương · Bản đồ Bayes',
  'title_en': 'Finding Lost Sub USS Scorpion & Flight 447 Wreckage at 13,000 Feet With Bayes’ Theorem',
  'title_vi': 'Tìm Thấy Tàu Ngầm Hạt Nhân Mất Tích Dưới Đáy Biển Sâu Nhờ Định Lý Bayes',
  'story_en': 'When nuclear sub USS Scorpion vanished in the Atlantic, searchers scoured for months in vain. Mathematician John Craven '
              'polled diverse experts to build a Bayesian prior grid over the seabed, updating every cell’s posterior probability each '
              'time a sonar pass came back empty—finding the hull within 220 yards! The exact method later found Air France 447’s black '
              'boxes in 1 week after 2 years of failure.',
  'story_vi': 'Khi tàu ngầm USS Scorpion mất tích giữa đại dương mênh mông, toán gia John Craven chia đáy biển thành lưới ô vuông xác suất '
              'tiền nghiệm P(A), rồi dùng Định lý Bayes cập nhật lại bản đồ mỗi khi tàu quét sonar không thấy gì—nhờ đó tìm ra xác tàu '
              'cách tâm dự đoán chỉ 200 mét! Chính phương pháp này năm 2011 đã tìm thấy hộp đen Air France 447 chỉ sau 1 tuần quét lại.',
  'lesson_en': "Even 'negative evidence' (looking and finding nothing) powerfully updates Bayesian posteriors!",
  'lesson_vi': 'Ngay cả việc “tìm ở ô A không thấy” cũng là bằng chứng quý giá giúp Định lý Bayes dồn xác suất sang ô đúng!',
  'url': 'https://en.wikipedia.org/wiki/Bayesian_search_theory',
  'src_label': 'Bayesian Search Theory',
  'lab': 'labs:bayes',
  'methods_en': 'Probabilistic Thinking (Ch. 8 · Subjective Prior Distribution + Sequential Bayesian Updating, pp. 146, 153–156)',
  'methods_vi': 'Tư duy Xác suất (Chương 8 · Phân bổ xác suất tiền nghiệm + Cập nhật Suy luận Bayes liên hoàn, tr. 146, 153–156)',
  'result_en': 'Located USS Scorpion 10,000 ft deep within 220 yards of the Bayesian peak, and in 2011 found Air France 447’s flight '
               'recorders in just 1 week of undersea search.',
  'result_vi': 'Tìm thấy xác tàu ngầm USS Scorpion ở độ sâu hơn 3.000m cách điểm dự đoán chỉ 200m, và năm 2011 tìm ra hộp đen Air France '
               '447 chỉ sau đúng 1 tuần quét lại.'},
 {'id': 'cs-bletchley-enigma',
  'ch': 'ch8',
  'cat': 'ai-tech',
  'year': '1941',
  'domain_en': 'Cryptography · Alan Turing',
  'domain_vi': 'Mật mã học · Alan Turing & Bayes',
  'title_en': 'Alan Turing’s ‘Banburismus’ at Bletchley Park: Cracking Enigma With Daily Bayes Odds',
  'title_vi': 'Alan Turing Tại Bletchley Park: Giải Mã Enigma Đức Quốc Xã Bằng Điểm Xác Suất Bayes',
  'story_en': 'With too many Enigma rotor settings to brute-force on early electromechanical Bombes, Alan Turing invented the ‘ban’ '
              '(log-odds Bayesian weight of evidence) to score paper punch-strips each morning—pruning millions of impossible wheel '
              'combinations and saving Allied convoys.',
  'story_vi': 'Vì số lượng tổ hợp bánh răng máy mật mã Enigma quá khổng lồ so với máy cơ điện thời đó, Alan Turing phát minh đơn vị điểm '
              'chứng cứ Bayes để cập nhật xác suất từng cặp bánh răng mỗi sáng—rút ngắn hàng triệu phép thử và cứu sống hàng ngàn tàu tiếp '
              'vận.',
  'lesson_en': 'Sequential Bayesian updating turns faint statistical clues into decisive action.',
  'lesson_vi': 'Cập nhật Bayes liên hoàn biến những manh mối mờ nhạt thành lợi thế quyết định.',
  'url': 'https://en.wikipedia.org/wiki/Banburismus',
  'src_label': 'Bletchley Park Dossier',
  'lab': 'labs:bayes',
  'methods_en': 'Probabilistic Thinking (Ch. 8 · Bayesian Log-Odds Updating & Conditional Probability Multiplication, pp. 153–159)',
  'methods_vi': 'Tư duy Xác suất (Chương 8 · Cập nhật điểm chứng cứ Bayes & Xác suất có điều kiện, tr. 153–159)',
  'result_en': 'Slashed Bombe rotor-search combinations enough to read German naval Enigma traffic daily—estimated by historians to have '
               'shortened WWII in Europe by ~2 years.',
  'result_vi': 'Cắt giảm hàng triệu tổ hợp thử máy cơ điện giúp giải mã điện tín hải quân Đức mỗi ngày—được giới sử học ước tính rút ngắn '
               'Thế chiến II tại châu Âu khoảng 2 năm.'},
 {'id': 'cs-ltcm-swan',
  'ch': 'ch8',
  'cat': 'business',
  'year': '1998',
  'domain_en': 'Hedge Funds · Black Swan Tail',
  'domain_vi': 'Quỹ Đầu cơ · Rủi ro Thiên nga Đen',
  'title_en': 'Long-Term Capital Management: How 30x Leverage Turned High EV Into a $4.6B Bailout',
  'title_vi': 'Cú Sập Quỹ LTCM Của Hai Chủ Nhân Giải Nobel: Khi Kỳ Vọng Dương Gặp Thiên Nga Đen',
  'story_en': 'Led by Nobel-winning economists, LTCM earned 40%/year arbitrage returns with ‘near-zero’ model risk—leveraged 30-to-1. Then '
              'Russia defaulted on ruble bonds in August 1998 (a tail event their bell curve called once-in-a-universe), wiping out $4.6B '
              'in weeks. Directly proves Chapter 8’s p. 149 Black Swan warning!',
  'story_vi': 'Được điều hành bởi các kinh tế gia đoạt giải Nobel, quỹ LTCM lãi đều 40%/năm nhưng dùng đòn bẩy nợ gấp 30 lần vốn vì tin '
              'biến cố lớn “không thể xảy ra”. Khi Nga vỡ nợ trái phiếu tháng 8/1998, quỹ bốc hơi 4,6 tỷ USD chỉ trong vài tuần—chứng minh '
              'đanh thép cảnh báo trang 149 về Thiên nga đen!',
  'lesson_en': 'Positive Expected Value means nothing if a 1% tail event multiplies you by zero.',
  'lesson_vi': 'Giá trị kỳ vọng EV cao mấy cũng vô nghĩa nếu để một kịch bản xác suất 1% xóa sạch cuộc chơi.',
  'url': 'https://en.wikipedia.org/wiki/Long-Term_Capital_Management',
  'src_label': 'LTCM Case Study',
  'lab': 'labs:bayes',
  'methods_en': 'Probabilistic Thinking (Ch. 8 · Expected Value Caveat & Black-Swan Tail-Ruin Protection, p. 149)',
  'methods_vi': 'Tư duy Xác suất (Chương 8 · Cảnh báo giới hạn của EV & Phòng vệ rủi ro đuôi Thiên nga đen, tr. 149)',
  'result_en': 'Violation of p. 149’s ruin rule wiped out $4.6 billion in 4 months and required an emergency $3.625B Federal '
               'Reserve-brokered rescue by 14 Wall Street banks.',
  'result_vi': 'Vi phạm nguyên tắc phòng vệ Thiên nga đen (tr. 149) khiến quỹ bốc hơi 4,6 tỷ USD trong 4 tháng, buộc Cục Dự trữ Liên bang '
               'Mỹ phải đứng ra dàn xếp gói giải cứu khẩn cấp 3,625 tỷ USD.'},
 {'id': 'cs-resulting-duke',
  'ch': 'ch8',
  'cat': 'policy',
  'year': '2015 / 2018',
  'domain_en': 'Decision Quality · Resulting',
  'domain_vi': 'Ra quyết định · Bẫy Phán xét Theo Kết quả',
  'title_en': 'Super Bowl XLIX’s 1-Yard Interception & Poker Champion Annie Duke’s ‘Resulting’ Trap',
  'title_vi': 'Pha Ném Bóng Ở Vạch 1 Yard Super Bowl & Cái Bẫy ‘Nhìn Kết Quả Phán Quyết Định’',
  'story_en': 'With 26 seconds left on the 1-yard line and one timeout, Seattle called a quick pass (stopping the clock on an incomplete '
              'to preserve 3 plays; historical interception rate ~1.5%). New England made a miraculous 1.5% interception—and commentators '
              "called it 'the dumbest call in history.' Probabilistic thinkers separate decision EV from a 1.5% bad bounce!",
  'story_vi': 'Còn 26 giây cách vạch đích 1 yard và chỉ còn 1 quyền hội ý, HLV Seattle gọi pha chuyền bóng (xác suất bị cắt bóng lịch sử '
              'chỉ ~1,5% và giúp giữ đồng hồ cho 2 lượt chạy sau). Đối thủ xuất thần bắt được đúng 1,5% ấy—và báo chí chửi là “quyết định '
              'ngu ngốc nhất lịch sử”. Tư duy xác suất không bao giờ lấy may rủi hậu nghiệm để phủ nhận tính toán đúng!',
  'lesson_en': 'A good probabilistic decision can have an unlucky outcome; a reckless gamble can get lucky once.',
  'lesson_vi': 'Quyết định đúng phương pháp vẫn có thể gặp 2% không may; đánh bạc liều mạng thắng một lần vẫn là quyết định tồi.',
  'url': "https://en.wikipedia.org/wiki/Super_Bowl_XLIX#Seattle's_final_drive",
  'src_label': 'Game & EV Breakdown',
  'lab': 'atlas:t-ev-dist',
  'methods_en': 'Probabilistic Thinking (Ch. 8 · Probability Tree Branching & Separating Ex-Ante Expected Value from Single-Trial Luck, '
                'pp. 147–153)',
  'methods_vi': 'Tư duy Xác suất (Chương 8 · Cây xác suất & Tách bạch chất lượng quyết định EV với may rủi đơn lẻ, tr. 147–153)',
  'result_en': 'Became the flagship case study in decision science (Thinking in Bets) training executives and investors to audit decision '
               'process quality rather than hindsight luck.',
  'result_vi': 'Trở thành bài học kinh điển của khoa học ra quyết định hiện đại, giúp các nhà đầu tư và lãnh đạo đánh giá quy trình bằng '
               'EV thay vì phán xét theo kết quả hậu nghiệm.'},
 {'id': 'cs-eddington-1919',
  'ch': 'ch9',
  'cat': 'medicine',
  'year': '1919',
  'domain_en': 'Astrophysics · Falsifiability',
  'domain_vi': 'Vật lý Thiên văn · Khả năng Bác bỏ',
  'title_en': 'Eddington’s 1919 Total Eclipse: Putting Einstein’s Theory on the Chopping Block',
  'title_vi': 'Nhật Thực Toàn Phần Năm 1919: Khi Einstein Đặt Thuyết Tương Đối Lên Thớt Kiểm Chứng',
  'story_en': 'Karl Popper’s favorite exemplar of true science: Einstein predicted starlight grazing the Sun bends by 1.75 arcseconds '
              '(twice Newton’s 0.87). Had Arthur Eddington’s eclipse photographs in Príncipe measured 0.87 or 0, General Relativity would '
              'have been refuted immediately.',
  'story_vi': 'Hình mẫu tiêu biểu nhất mà triết gia Karl Popper ca ngợi: Einstein tiên đoán tia sáng ngôi sao đi sát Mặt Trời sẽ lệch đúng '
              '1,75 giây cung (gấp đôi mức 0,87 của Newton). Nếu ảnh chụp nhật thực của Eddington cho con số khác, Thuyết tương đối rộng '
              'đã bị bác bỏ ngay lập tức!',
  'lesson_en': 'Real science sticks its neck out with precise, falsifiable predictions (Ch. 9, pp. 162–163).',
  'lesson_vi': 'Khoa học đích thực luôn dám đưa ra dự báo cụ thể có nguy cơ bị thực nghiệm bác bỏ (tr. 162–163).',
  'url': 'https://en.wikipedia.org/wiki/Eddington_experiment',
  'src_label': '1919 Eclipse Dossier',
  'lab': 'labs:science',
  'methods_en': 'Scientific Thinking (Ch. 9 · Popperian Falsifiability & Quantitative Empirical Prediction, pp. 162–165)',
  'methods_vi': 'Tư duy Khoa học (Chương 9 · Nguyên lý Khả năng bị bác bỏ của Popper & Thực nghiệm định lượng, tr. 162–165)',
  'result_en': 'Measured starlight deflection (1.61 ± 0.30 and 1.98 ± 0.12 arcsec) matched Einstein’s 1.75 prediction and refuted Newton’s '
               '0.87—validating General Relativity worldwide.',
  'result_vi': 'Độ lệch ánh sao đo được khớp với tiên đoán 1,75 giây cung của Einstein và bác bỏ mức 0,87 của Newton—khẳng định Thuyết '
               'tương đối rộng trên toàn thế giới.'},
 {'id': 'cs-james-lind',
  'ch': 'ch9',
  'cat': 'medicine',
  'year': '1747',
  'domain_en': 'Clinical Trials · Variable Control',
  'domain_vi': 'Thử nghiệm Lâm sàng · Cô lập Biến số',
  'title_en': 'Dr. James Lind Aboard HMS Salisbury: Six Pairs of Sailors & Two Oranges',
  'title_vi': 'Bác Sĩ James Lind Trên Tàu Hải Quân 1747: Sáu Cặp Thủy Thủ & Hai Quả Cam Trị Bệnh Scurvy',
  'story_en': 'Scurvy killed more British sailors than French cannons, while doctors peddled vinegar, seawater, and sulfuric elixir. '
              'Aboard HMS Salisbury, James Lind placed 12 sick sailors in the same cabin on the same porridge—varying ONLY the daily '
              'supplement across 6 pairs. Within 6 days, the citrus pair recovered to nurse the rest!',
  'story_vi': 'Khi bệnh Scurvy giết hại thủy thủ nhiều hơn cả đại bác mà mỗi thầy thuốc phán một kiểu, bác sĩ James Lind chọn 12 thủy thủ '
              'bệnh nặng nằm chung một khoang, ăn cùng một thực đơn—chỉ thay đổi DUY NHẤT chất bổ sung cho 6 cặp. Sau 6 ngày, cặp ăn cam '
              'chanh khỏe hẳn dậy chăm sóc các cặp còn lại!',
  'lesson_en': 'Isolating one variable while holding confounders constant is the superpower of Step 4 (pp. 166–167).',
  'lesson_vi': 'Giữ nguyên mọi điều kiện nền để cô lập một biến số duy nhất là sức mạnh cốt lõi của Bước 4 (tr. 166–167).',
  'url': 'https://www.jameslindlibrary.org/articles/james-lind-and-scurvy-1747/',
  'src_label': 'James Lind Library',
  'lab': 'labs:science',
  'methods_en': 'Scientific Thinking (Ch. 9 · Step 4 Controlled Experimentation: Isolating One Variable Across Matched Pairs, pp. 164–167)',
  'methods_vi': 'Tư duy Khoa học (Chương 9 · Bước 4 Thí nghiệm có kiểm soát: Giữ cố định biến nền, cô lập biến thử nghiệm, tr. 164–167)',
  'result_en': 'Citrus-fed sailors recovered in 6 days; once the Royal Navy mandated lemon/lime juice fleet-wide, scurvy was virtually '
               'eradicated and British naval endurance doubled.',
  'result_vi': 'Cặp thủy thủ ăn cam chanh hồi phục sau 6 ngày; khi Hải quân Anh áp dụng đại trà nước cốt chanh, bệnh Scurvy gần như biến '
               'mất trên toàn hạm đội.'},
 {'id': 'cs-ab-humility',
  'ch': 'ch9',
  'cat': 'ai-tech',
  'year': '2020',
  'domain_en': 'Product & AI · Controlled Tests',
  'domain_vi': 'Sản phẩm Số · Thử nghiệm Đối chứng',
  'title_en': 'Why 70%–80% of ‘Brilliant’ Features Fail Controlled A/B Experiments at Microsoft & Booking.com',
  'title_vi': 'Vì Sao Hơn 75% Ý Tưởng ‘Tâm Đắc Nhất’ Của Chuyên Gia Đều Thất Bại Khi Chạy Thí Nghiệm A/B?',
  'story_en': 'Published studies across Microsoft, Google, Airbnb, and Booking.com reveal a humbling law: even when smart teams love a new '
              'feature, 70%–90% fail to improve user outcomes in randomized controlled trials! Running fast, honest falsification loops '
              'prevents shipping bloat.',
  'story_vi': 'Số liệu công bố từ Microsoft, Airbnb và Booking.com cho thấy một sự thật làm tỉnh ngộ mọi cái tôi: ngay cả những tính năng '
              'đội ngũ tâm đắc nhất cũng có tới 70%–90% không hề mang lại hiệu quả thực tế khi chạy thử nghiệm đối chứng ngẫu nhiên!',
  'lesson_en': 'Intellectual Humility + Controlled Experimentation beats the Highest-Paid Person’s Opinion.',
  'lesson_vi': 'Khiêm tốn trí tuệ kết hợp thí nghiệm có kiểm soát luôn thắng cảm tính chủ quan của sếp.',
  'url': 'https://hbr.org/2017/09/the-surprising-power-of-online-experiments',
  'src_label': 'HBR Experimentation Study',
  'lab': 'labs:science',
  'methods_en': 'Scientific Thinking (Ch. 9 · Randomized Controlled Trials & Falsification Loop, pp. 164–167) + Critical Thinking (Ch. 3 · '
                'Intellectual Humility, p. 63)',
  'methods_vi': 'Tư duy Khoa học (Chương 9 · Thử nghiệm đối chứng ngẫu nhiên & Vòng lặp bác bỏ, tr. 164–167) + Tư duy Phản biện (Chương 3 '
                '· Khiêm tốn trí tuệ, tr. 63)',
  'result_en': 'Running >10,000 controlled experiments/year saved hundreds of millions in wasted engineering and boosted Bing/Booking '
               'conversion & revenue by double-digit percentages.',
  'result_vi': 'Vận hành hơn 10.000 thí nghiệm đối chứng mỗi năm giúp ngăn chặn hàng trăm triệu USD lãng phí vào tính năng vô tác dụng và '
               'tăng trưởng doanh thu hai chữ số.'},
 {'id': 'cs-cold-fusion',
  'ch': 'ch9',
  'cat': 'medicine',
  'year': '1989',
  'domain_en': 'Physics · Peer Replication',
  'domain_vi': 'Vật lý · Phản biện Đồng đẳng',
  'title_en': 'The 1989 Cold Fusion Press Conference: Why Step 7 (Peer Replication) Protects Truth',
  'title_vi': 'Họp Báo ‘Nhiệt Hạch Lạnh’ Năm 1989: Vì Sao Bước 7 (Tái Lập Độc Lập) Là Chốt Chặn Cuối Cùng?',
  'story_en': 'Bypassing peer review, electrochemists announced room-temperature nuclear fusion on global TV. Within weeks, MIT, Caltech, '
              'and Harwell labs ran rigorous control calorimeters and exposed measurement artifacts—demonstrating why science trusts '
              'reproducible protocols, never press releases.',
  'story_vi': 'Bỏ qua kiểm định đồng đẳng, hai nhà hóa học mở họp báo chấn động thế giới tuyên bố tạo ra phản ứng nhiệt hạch trong cốc '
              'thủy tinh ở nhiệt độ phòng. Chỉ vài tuần sau, các phòng thí nghiệm độc lập tại MIT và Caltech kiểm tra đối chứng và vạch ra '
              'sai số đo nhiệt—chứng minh vai trò sống còn của Bước 7 (tr. 166).',
  'lesson_en': 'A finding becomes knowledge only when independent skeptics can replicate your exact protocol.',
  'lesson_vi': 'Một phát hiện chỉ trở thành tri thức khi những người hoài nghi độc lập lặp lại được kết quả ấy.',
  'url': 'https://en.wikipedia.org/wiki/Cold_fusion',
  'src_label': 'Replication Case Study',
  'lab': 'labs:science',
  'methods_en': 'Scientific Thinking (Ch. 9 · Step 7 Peer Communication, Control Calorimetry & Independent Replication, pp. 163, 166–167)',
  'methods_vi': 'Tư duy Khoa học (Chương 9 · Bước 7 Phản biện cộng đồng khoa học & Tái lập độc lập có đối chứng, tr. 163, 166–167)',
  'result_en': 'Independent labs debunked the artifact within 60 days, preventing billions in misallocated energy subsidies and '
               'reinforcing peer replication before public claims.',
  'result_vi': 'Các phòng thí nghiệm độc lập bác bỏ sai số chỉ trong 60 ngày, ngăn chặn hàng tỷ USD ngân sách đổ vào dự án ảo và củng cố '
               'kỷ luật tái lập khoa học.'}]
