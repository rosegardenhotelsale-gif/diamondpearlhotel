import os

with open('suite/template.html', 'r', encoding='utf-8') as f:
    template = f.read()

rooms = [
    {
        "filename": "studioking.html",
        "name": "Studio King",
        "folder": "studioking",
        "img1": "thumbnail.jpg",
        "img2": "gallery-1.jpg",
        "img3": "gallery-2.jpg",
        "img4": "gallery-3.jpg",
        "desc": "Enjoy a comfortable stay in our 25 sqm Comfortable King Room, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    },
    {
        "filename": "deluxeking.html",
        "name": "Deluxe King",
        "folder": "deluxeking",
        "img1": "thumbnail.jpg",
        "img2": "gallery-1.jpg",
        "img3": "gallery-2.jpg",
        "img4": "gallery-3.jpg",
        "desc": "Enjoy a comfortable stay in our 35 sqm Deluxe King Room, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    },
    {
        "filename": "deluxetwincityview.html",
        "name": "Deluxe Twin City View",
        "folder": "deluxetwincityview",
        "img1": "thumbnail.jpg",
        "img2": "gallery-1.jpg",
        "img3": "gallery-2.jpg",
        "img4": "gallery-3.jpg",
        "desc": "Enjoy a comfortable stay in our 35 sqm City View with twin bed, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    },
    {
        "filename": "deluxeriverview.html",
        "name": "Deluxe Twin River View",
        "folder": "deluxeriverview",
        "img1": "thumbnail.jpg",
        "img2": "gallery-1.jpg",
        "img3": "gallery-2.jpg",
        "img4": "gallery-3.jpg",
        "desc": "Enjoy a comfortable stay in our 35 sqm River View with twin bed, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    },
    {
        "filename": "executivesuite.html",
        "name": "Executive Suite",
        "folder": "executivesuite",
        "img1": "thumbnail.jpg",
        "img2": "gallery-1.jpg",
        "img3": "gallery-2.jpg",
        "img4": "gallery-3.jpg",
        "desc": "Enjoy a comfortable stay in our luxurious Executive Suite, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    }
]

import random

for room in rooms:
    content = template.replace('ROOM_NAME_PLACEHOLDER', room['name'])
    content = content.replace('ROOM_FOLDER', room['folder'])
    content = content.replace('ROOM_IMG_1', room['img1'])
    content = content.replace('ROOM_IMG_2', room['img2'])
    content = content.replace('ROOM_IMG_3', room['img3'])
    content = content.replace('ROOM_IMG_4', room['img4'])
    content = content.replace('ROOM_DESC_PLACEHOLDER', room['desc'])
    content = content.replace('ROOM_GUEST_PLACEHOLDER', room['guest'])
    content = content.replace('ROOM_BED_PLACEHOLDER', room['bed'])
    content = content.replace('ROOM_ID_PLACEHOLDER', room['filename'].replace('.html', ''))
    
    # Generate Similar Rooms
    other_rooms = [r for r in rooms if r['name'] != room['name']]
    # Select 3 distinct rooms (or just the first 3 if enough)
    similar_rooms = other_rooms[:3]
    
    similar_html = ""
    for sr in similar_rooms:
        card = f'''
        <div class="col-md-4 mb-4">
            <div class="room-card" style="height: 100%; min-height: 400px;">
                <img src="../img/rooms/{sr['folder']}/{sr['img1']}" alt="{sr['name']}" class="room-bg">
                <button class="favorite-btn"><i class="fa-regular fa-heart"></i></button>
                <div class="room-info">
                    <a href="{sr['filename']}" style="text-decoration: none; color: inherit;"><h3 class="room-title">{sr['name']}</h3></a>
                    <div class="room-footer" style="margin-top: 15px;">
                        <div class="room-features">
                            <span><i class="fa-regular fa-user"></i> {sr['guest']} Guest</span>
                            <span><i class="fa-solid fa-bed"></i> {sr['bed']} Bed</span>
                            <span><i class="fa-solid fa-bath"></i> 1 Bath</span>
                        </div>
                        <div class="room-price" data-room="{sr['filename'].replace('.html', '')}">$120 / Night</div>
                    </div>
                </div>
            </div>
        </div>
        '''
        similar_html += card
        
    content = content.replace('SIMILAR_ROOMS_PLACEHOLDER', similar_html)
    
    with open('suite/' + room['filename'], 'w', encoding='utf-8') as f:
        f.write(content)

print("Created 5 HTML files.")
