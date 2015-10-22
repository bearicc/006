var map = new L.Map('map', {
    scrollWheelZoom: true,
    touchZoom: true,
    doubleClickZoom: true,
    zoomControl: true,
    dragging: true
});

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var center = new L.LatLng(41.902025,-87.633368);
map.setView(center, 17);

var marker = L.marker(center).addTo(map);
marker.bindPopup("<b>This is BEAR!</b><br>I am here!").openPopup();
