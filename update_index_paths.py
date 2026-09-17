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
    # Match <img src="..." alt="name" class="room-bg">
    pattern = r'<img src="\./img/rooms/.*?" alt="' + name + r'" class="room-bg">'
    replacement = r'<img src="./img/rooms/' + rid + r'/thumbnail.jpg" alt="' + name + r'" class="room-bg">'
    content = re.sub(pattern, replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
