import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the 5 rooms
rooms = [
    {
        "id": "studioking",
        "name": "Studio King",
        "desc": "Enjoy a comfortable stay in our 25 sqm Comfortable King Room, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    },
    {
        "id": "deluxeking",
        "name": "Deluxe King",
        "desc": "Enjoy a comfortable stay in our 35 sqm Deluxe King Room, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    },
    {
        "id": "deluxetwincityview",
        "name": "Deluxe Twin City View",
        "desc": "Enjoy a comfortable stay in our 35 sqm City View with twin bed, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    },
    {
        "id": "deluxeriverview",
        "name": "Deluxe Twin River View",
        "desc": "Enjoy a comfortable stay in our 35 sqm River View with twin bed, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    },
    {
        "id": "executivesuite",
        "name": "Executive Suite",
        "desc": "Enjoy a comfortable stay in our luxurious Executive Suite, ideal for up to 2 adults and 1 child. The room features a king-size bed, air conditioning, high-speed Wi-Fi, TV with TV Box, mini bar, tea and coffee facilities, hairdryer, bathrobe, slippers, safety box, and complimentary bathroom amenities. Baby cot is available upon request.",
        "guest": "2",
        "bed": "1"
    }
]

# Build the Swiper HTML
swiper_html = """    <section class="rooms-section" id="rooms">
        <div class="container">
            <h2 class="section-title">SUITE & ROOMS</h2>
            
            <!-- Swiper Carousel -->
            <div class="swiper roomsSwiper" style="padding-bottom: 50px;">
                <div class="swiper-wrapper">
"""

for room in rooms:
    swiper_html += f"""                    <div class="swiper-slide" style="height: auto;">
                        <div class="room-card" style="height: 100%;">
                            <img src="./img/rooms/{room['id']}/thumbnail.jpg" alt="{room['name']}" class="room-bg">
                            <button class="favorite-btn"><i class="fa-regular fa-heart"></i></button>
                            <div class="room-info">
                                <a href="./suite/{room['id']}.html" style="text-decoration: none; color: inherit;"><h3 class="room-title">{room['name']}</h3></a>
                                <p class="room-desc">{room['desc']}</p>
                                <div class="room-footer">
                                    <div class="room-features">
                                        <span><i class="fa-regular fa-user"></i> {room['guest']} Guest</span>
                                        <span><i class="fa-solid fa-bed"></i> {room['bed']} Bed</span>
                                        <span><i class="fa-solid fa-bath"></i> 1 Bath</span>
                                    </div>
                                    <div class="room-price" data-room="{room['id']}">$120 / Night</div>
                                </div>
                            </div>
                        </div>
                    </div>
"""

swiper_html += """                </div>
                <!-- Swiper Pagination and Navigation -->
                <div class="swiper-pagination"></div>
                <div class="swiper-button-prev">
                    <div class="nav-arrow-diamond prev"><div class="diamond-inner"></div></div>
                </div>
                <div class="swiper-button-next">
                    <div class="nav-arrow-diamond next"><div class="diamond-inner"></div></div>
                </div>
            </div>
        </div>
    </section>"""

# Replace in content using regex
pattern = r'<section class="rooms-section" id="rooms">.*?</section>\s*(?=<!-- Testimonial Section -->)'
content = re.sub(pattern, swiper_html, content, flags=re.DOTALL)

# Add Swiper CSS in head if not exists
if 'swiper-bundle.min.css' not in content:
    content = content.replace('</head>', '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />\n</head>')

# Add Swiper JS and init script before closing body
swiper_js = """    <!-- Swiper JS -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
    <script>
        var swiper = new Swiper(".roomsSwiper", {
            slidesPerView: 1,
            spaceBetween: 30,
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                },
                1024: {
                    slidesPerView: 3,
                }
            }
        });
    </script>
"""

if 'swiper-bundle.min.js' not in content:
    content = content.replace('</body>', swiper_js + '</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
