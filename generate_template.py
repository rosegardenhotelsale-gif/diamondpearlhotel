with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

head_str = content.split('</header>')[0] + '</header>'
head_str = head_str.replace('href="./css/', 'href="../css/').replace('href="css/', 'href="../css/')
head_str = head_str.replace('src="./img/', 'src="../img/').replace('src="img/', 'src="../img/')
head_str = head_str.replace('href="./"', 'href="../index.html"').replace('href="./index.html"', 'href="../index.html"')
head_str = head_str.replace('href="index.html"', 'href="../index.html"')
head_str = head_str.replace('href="#', 'href="../index.html#')
head_str = head_str.replace('</head>', '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.css"/>\n</head>')
head_str = head_str.replace('<div class="hero-wrapper" id="home">', '<div class="inner-page-wrapper">')

footer_str = '</div>\n<!-- Footer Section -->' + content.split('<!-- Footer Section -->')[1]
footer_str = footer_str.replace('src="./img/', 'src="../img/').replace('src="./js/', 'src="../js/').replace('src="js/', 'src="../js/')
footer_str = footer_str.replace('</body>', '    <script src="../js/prices.js"></script>\n    <script src="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.umd.js"></script>\n    <script>\n        Fancybox.bind(\'[data-fancybox="gallery"]\', {\n            backdropClick: "close",\n            on: {\n                reveal: (fancybox, slide) => {\n                    const image = slide.$el.querySelector(".f-image");\n                    if (image) {\n                        image.style.cursor = "pointer";\n                        image.addEventListener("click", () => {\n                            fancybox.close();\n                        });\n                    }\n                }\n            }\n        });\n    </script>\n</body>')

body_content = """
    <!-- Hero Banner -->
    <section class="room-detail-hero">
        <div class="container">
            <h1 class="room-detail-title">ROOM_NAME_PLACEHOLDER</h1>
            <div class="room-detail-breadcrumb">
                <a href="../index.html">HOME</a> <span style="margin: 0 10px; color: var(--primary-color);">/</span>
                <a href="../index.html#rooms">ROOMS</a> <span style="margin: 0 10px; color: var(--primary-color);">/</span>
                <span style="color: #fff;">ROOM_NAME_PLACEHOLDER</span>
            </div>
        </div>
    </section>

    <!-- Room Detail Section -->
    <section class="room-gallery-section">
        <div class="container">
            <div class="row">
                
                <!-- Main Content (Gallery) -->
                <div class="col-lg-8">
                    <!-- Main Image -->
                    <a data-fancybox="gallery" href="../img/rooms/ROOM_FOLDER/ROOM_IMG_1">
                        <img src="../img/rooms/ROOM_FOLDER/ROOM_IMG_1" alt="ROOM_NAME_PLACEHOLDER" class="gallery-main-img">
                    </a>
                    
                    <!-- Gallery Grid -->
                    <div class="gallery-grid">
                        <div class="gallery-item">
                            <a data-fancybox="gallery" href="../img/rooms/ROOM_FOLDER/ROOM_IMG_2">
                                <img src="../img/rooms/ROOM_FOLDER/ROOM_IMG_2" alt="Gallery 1">
                            </a>
                        </div>
                        <div class="gallery-item">
                            <a data-fancybox="gallery" href="../img/rooms/ROOM_FOLDER/ROOM_IMG_3">
                                <img src="../img/rooms/ROOM_FOLDER/ROOM_IMG_3" alt="Gallery 2">
                            </a>
                        </div>
                        <div class="gallery-item">
                            <a data-fancybox="gallery" href="../img/rooms/ROOM_FOLDER/ROOM_IMG_4">
                                <img src="../img/rooms/ROOM_FOLDER/ROOM_IMG_4" alt="Gallery 3">
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Sidebar (Booking Card) -->
                <div class="col-lg-4">
                    <div class="booking-card">
                        <h3 class="booking-card-title">Room Details</h3>
                        <p class="booking-desc">ROOM_DESC_PLACEHOLDER</p>
                        
                        <ul class="booking-features-list">
                            <li><i class="fa-regular fa-user"></i> ROOM_GUEST_PLACEHOLDER Guests</li>
                            <li><i class="fa-solid fa-bed"></i> ROOM_BED_PLACEHOLDER Bed</li>
                            <li><i class="fa-solid fa-bath"></i> 1 Bathroom</li>
                            <li><i class="fa-solid fa-wifi"></i> Free High-Speed Wi-Fi</li>
                            <li><i class="fa-solid fa-tv"></i> Flat-screen TV</li>
                            <li><i class="fa-solid fa-mug-hot"></i> Coffee / Tea Maker</li>
                            <li><i class="fa-solid fa-snowflake"></i> Air Conditioning</li>
                        </ul>

                        <div class="booking-price-wrap">
                            <span class="booking-price-label">Starting from</span>
                            <div class="booking-price-value" data-room="ROOM_ID_PLACEHOLDER">$120 <span>/ Night</span></div>
                        </div>

                        <a href="../index.html#contacts" class="outline-gold-btn booking-btn">BOOK NOW</a>
                    </div>
                </div>
                
            </div>
        </div>
    </section>

    <!-- Similar Rooms Section -->
    <section class="similar-rooms-section" style="padding: 40px 0 80px; background-color: var(--bg-color);">
        <div class="container">
            <h2 style="font-family: var(--font-heading); color: var(--primary-color); text-align: center; margin-bottom: 40px; font-size: 2.5rem;">Similar Rooms</h2>
            <div class="row" id="similar-rooms-container">
                SIMILAR_ROOMS_PLACEHOLDER
            </div>
        </div>
    </section>
"""

with open('suite/template.html', 'w', encoding='utf-8') as f:
    f.write(head_str + '\n' + body_content + '\n' + footer_str)
