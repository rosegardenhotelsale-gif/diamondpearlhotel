import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<h3 class="room-title">Studio King</h3>': '<a href="./suite/studioking.html" style="text-decoration: none; color: inherit;"><h3 class="room-title">Studio King</h3></a>',
    '<h3 class="room-title">Deluxe King</h3>': '<a href="./suite/deluxeking.html" style="text-decoration: none; color: inherit;"><h3 class="room-title">Deluxe King</h3></a>',
    '<h3 class="room-title">Deluxe Twin River View</h3>': '<a href="./suite/deluxeriverview.html" style="text-decoration: none; color: inherit;"><h3 class="room-title">Deluxe Twin River View</h3></a>',
    '<h3 class="room-title">Deluxe Twin City View</h3>': '<a href="./suite/deluxetwincityview.html" style="text-decoration: none; color: inherit;"><h3 class="room-title">Deluxe Twin City View</h3></a>',
    '<h3 class="room-title">Executive Suite</h3>': '<a href="./suite/executivesuite.html" style="text-decoration: none; color: inherit;"><h3 class="room-title">Executive Suite</h3></a>'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
