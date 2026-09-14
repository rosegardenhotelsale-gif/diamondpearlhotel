import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the 4 room cards
cards = re.findall(r'(<div class="room-card">.*?<div class="room-footer".*?</div>\s*</div>\s*</div>)', html, re.DOTALL)

if len(cards) == 4:
    mobile_carousel = f'''
            <!-- Mobile Carousel Wrapper spanning 3 columns -->
            <div id="roomsCarouselMobile" class="carousel slide d-block d-md-none" data-bs-ride="carousel"
                style="grid-column: span 3; height: 100%; position: relative; overflow: hidden; border-radius: 12px;">
                <div class="carousel-inner" style="height: 100%; overflow: visible;">
                    <!-- Slide 1 -->
                    <div class="carousel-item active" style="height: 100%;">
                        <div class="rooms-carousel-track" style="display: grid; grid-template-columns: 1fr; height: 100%;">
                            {cards[0]}
                        </div>
                    </div>
                    <!-- Slide 2 -->
                    <div class="carousel-item" style="height: 100%;">
                        <div class="rooms-carousel-track" style="display: grid; grid-template-columns: 1fr; height: 100%;">
                            {cards[1]}
                        </div>
                    </div>
                    <!-- Slide 3 -->
                    <div class="carousel-item" style="height: 100%;">
                        <div class="rooms-carousel-track" style="display: grid; grid-template-columns: 1fr; height: 100%;">
                            {cards[2]}
                        </div>
                    </div>
                    <!-- Slide 4 -->
                    <div class="carousel-item" style="height: 100%;">
                        <div class="rooms-carousel-track" style="display: grid; grid-template-columns: 1fr; height: 100%;">
                            {cards[3]}
                        </div>
                    </div>
                </div>
                <!-- Global Nav Arrows -->
                <div class="room-nav-arrows"
                    style="position: absolute; bottom: 30px; right: 30px; display: flex; gap: 15px; z-index: 10;">
                    <a class="nav-arrow-small prev" href="#roomsCarouselMobile" role="button" data-bs-slide="prev"
                        style="text-decoration: none; color: inherit;">
                        <i class="fa-solid fa-caret-left"></i>
                    </a>
                    <a class="nav-arrow-small next" href="#roomsCarouselMobile" role="button" data-bs-slide="next"
                        style="text-decoration: none; color: inherit;">
                        <i class="fa-solid fa-caret-right"></i>
                    </a>
                </div>
            </div>
    '''
    
    html = html.replace('id="roomsCarousel" class="carousel slide"', 'id="roomsCarouselDesktop" class="carousel slide d-none d-md-block"')
    html = html.replace('href="#roomsCarousel"', 'href="#roomsCarouselDesktop"')
    html = html.replace('data-bs-target="#roomsCarousel"', 'data-bs-target="#roomsCarouselDesktop"')
    
    # insert mobile_carousel after roomsCarouselDesktop
    html = html.replace('<!-- Services Section -->', mobile_carousel + '\n\n    <!-- Services Section -->')
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success! Created mobile carousel.")
else:
    print(f"Error: Found {len(cards)} cards instead of 4")
