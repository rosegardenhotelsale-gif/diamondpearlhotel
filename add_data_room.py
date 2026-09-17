import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

rooms = [
    ('studioking', 'Studio King'),
    ('deluxeking', 'Deluxe King'),
    ('deluxetwincityview', 'Deluxe Twin City View'),
    ('deluxeriverview', 'Deluxe Twin River View'),
    ('executivesuite', 'Executive Suite')
]

for rid, name in rooms:
    # Use re.DOTALL to match across lines
    pattern = r'(<h3 class="room-title">' + name + r'</h3>.*?)(<div class="room-price">)'
    replacement = r'\g<1><div class="room-price" data-room="' + rid + r'">'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if '<script src="js/prices.js"></script>' not in content:
    content = content.replace('</body>', '    <script src="js/prices.js"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
