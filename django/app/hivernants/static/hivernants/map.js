const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
const markers = JSON.parse(document.getElementById('markers-data').textContent);
let feature = L.geoJSON(markers).bindPopup(function (layer) {
    var content = "<img src='/media/" + layer.feature.properties.picture + "'  class=\"picture_small\"/>";
    content = content + "<h1>" + layer.feature.properties.names + "</h1>";
    content = content + "<p>" + layer.feature.properties.fulladdress.replace(/(?:\r\n|\r|\n)/g, '<br />') + "</p>";
    return content;
}).addTo(map);
map.fitBounds(feature.getBounds(), { padding: [100, 100] });
