var map = L.map('map').setView([-1.3, 36.8], 6);

// Base map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(map);

// Load GeoJSON
fetch('/county-data')
    .then(res => res.json())
    .then(data => {

        console.log("GeoJSON loaded:", data);

        L.geoJSON(data, {

            style: function (feature) {

                let risk = feature.properties.risk_level;

                let color = "gray";

                if (risk === "Low") color = "green";
                else if (risk === "Medium") color = "orange";
                else if (risk === "High") color = "red";

                return {
                    color: color,
                    weight: 2,
                    fillOpacity: 0.6
                };
            },

            onEachFeature: function (feature, layer) {

                layer.bindPopup(
                    "<b>Risk:</b> " + feature.properties.risk_level +
                    "<br><b>TB Score:</b> " + feature.properties.tb_risk
                );
            }

        }).addTo(map);
    })
    .catch(err => console.error("Map load error:", err));