// Create map and set initial view to Helsinki
const map = L.map('map').setView([60.168992, 24.932366], 13);  // Default view: Kamppi, Helsinki

// Add OpenStreetMap tiles to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Set the Karaportti (school) coordinates
const schoolCoordinates = '60.175294,24.684855'; // Karaportti 2, Espoo

// Function to get coordinates from an address using the Nominatim API
async function getCoordinates(address) {
    const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${address}`);
    const data = await response.json();
    if (data && data.length > 0) {
        return { lat: parseFloat(data[0].lat), lon: parseFloat(data[0].lon) };
    }
    return null;
}

// Function to fetch the route from Digitransit API
async function getRoute(fromLat, fromLon) {
    const query = `
        {
            plan(
                fromPlace: "User Address::${fromLat},${fromLon}",
                toPlace: "Karaportti, Espoo::${schoolCoordinates}"
            ) {
                itineraries {
                    duration,
                    legs {
                        mode,
                        startTime,
                        endTime,
                        from {
                            lat
                            lon
                            name
                        },
                        to {
                            lat
                            lon
                            name
                        },
                        legGeometry {
                            length
                            points
                        }
                    }
                }
            }
        }
    `;

    const response = await fetch('https://api.digitransit.fi/routing/v1/routers/hsl/route', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query })
    });

    const data = await response.json();
    return data.data.plan.itineraries[0];  // Returning the first itinerary
}

// Function to draw the route on the map
function drawRoute(route) {
    const latLngs = route.legs.map(leg => [leg.from.lat, leg.from.lon]);
    const routeLine = L.polyline(latLngs, { color: 'blue' }).addTo(map);
    map.fitBounds(routeLine.getBounds());
}

// Function to display route info (start and end time)
function displayRouteInfo(route) {
    const firstLeg = route.legs[0];
    const startTime = new Date(firstLeg.startTime * 1000).toLocaleString();
    const endTime = new Date(firstLeg.endTime * 1000).toLocaleString();

    const infoDiv = document.getElementById('route-info');
    infoDiv.innerHTML = `
        <h3>Route Info</h3>
        <p><strong>Start Time:</strong> ${startTime}</p>
        <p><strong>End Time:</strong> ${endTime}</p>
    `;
}

// Handle form submission
document.getElementById('address-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const address = document.getElementById('address').value;
    const userCoords = await getCoordinates(address);

    if (userCoords) {
        const route = await getRoute(userCoords.lat, userCoords.lon);
        drawRoute(route);
        displayRouteInfo(route);
    } else {
        alert('Could not find coordinates for that address.');
    }
});
