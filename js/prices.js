// Centralized Room Prices
// You can change the prices here and they will update everywhere on the website automatically.
const roomPrices = {
    "studioking": "$58",
    "deluxeking": "$58",
    "deluxetwincityview": "$58",
    "deluxeriverview": "$68",
    "executivesuite": "$118"
};

// Function to update prices on the page
function updateRoomPrices() {
    // Update elements like: <div class="room-price" data-room="studioking">$120 / Night</div>
    const priceElements = document.querySelectorAll('.room-price[data-room]');
    priceElements.forEach(el => {
        const roomId = el.getAttribute('data-room');
        if (roomPrices[roomId]) {
            el.innerHTML = `${roomPrices[roomId]} <span>/ Night</span>`;
        }
    });

    // Update elements in the booking card: <div class="booking-price-value" data-room="studioking">$120 <span>/ Night</span></div>
    const bookingPriceElements = document.querySelectorAll('.booking-price-value[data-room]');
    bookingPriceElements.forEach(el => {
        const roomId = el.getAttribute('data-room');
        if (roomPrices[roomId]) {
            el.innerHTML = `${roomPrices[roomId]} <span style="font-size: 16px; color: rgba(255,255,255,0.6); font-weight: 400;">/ Night</span>`;
        }
    });
}

// Run the function when the document is loaded
document.addEventListener('DOMContentLoaded', updateRoomPrices);
