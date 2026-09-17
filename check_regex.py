import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<section class="rooms-section" id="rooms">.*?</section>\s*(?=<!-- Testimonial Section -->)'
match = re.search(pattern, content, flags=re.DOTALL)
print('Match found?', bool(match))
if not match:
    pattern2 = r'<section class="rooms-section" id="rooms">.*?</section>'
    match2 = re.search(pattern2, content, flags=re.DOTALL)
    print('Match2 found?', bool(match2))
