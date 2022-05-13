function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}


getLocation();
mapboxgl.accessToken = 'pk.eyJ1IjoiYWRyaWFud2lpIiwiYSI6ImNreWE2aGtyMzAyZ2kydW9kbDYycHgwYm4ifQ.n4ZtY21Yl6wFvgxzmzy4-Q';

function showPosition(position) {
    const map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/light-v10',
        center: [position.coords.longitude, position.coords.latitude],
        zoom: 12
    });

    const geojson = {
        type: 'FeatureCollection',
        features: [{
            type: 'Feature',
            geometry: {
                type: 'Point',
                coordinates: [19.886462889603695, 50.0211787264026]
            }
        }]
    };

    for (const feature of geojson.features) {
        const el = document.createElement('div');
        el.className = 'marker';

        new mapboxgl.Marker(el).setLngLat(feature.geometry.coordinates).addTo(map);
    }
}