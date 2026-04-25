from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np
import json
from shapely.geometry import shape, Point

app = Flask(__name__)

# ================= LOAD MODEL =================
model_package = joblib.load("model/tb_model.joblib")
model = model_package["model"]
features = model_package["features"]

# ================= LOAD GEOJSON =================
with open("data/kenya_counties.geojson") as f:
    counties_geojson = json.load(f)

# ================= FIXED TB SCORES (IMPORTANT FOR CHOROPLETH) =================
# This ensures each county ALWAYS has same risk value (no random flickering)
np.random.seed(42)

county_tb_scores = {}

for feature in counties_geojson["features"]:
    name = (
        feature["properties"].get("NAME_1") or
        feature["properties"].get("county") or
        feature["properties"].get("name") or
        "unknown"
    )

    # deterministic TB score (stable GIS layer)
    county_tb_scores[name] = int(np.random.randint(5, 100))

# attach to geojson once
for feature in counties_geojson["features"]:
    name = (
        feature["properties"].get("NAME_1") or
        feature["properties"].get("county") or
        feature["properties"].get("name") or
        "unknown"
    )

    feature["properties"]["tb_score"] = county_tb_scores[name]

# ================= COUNTY DETECTION =================
def get_county_name(lat, lon):

    point = Point(lon, lat)

    for feature in counties_geojson["features"]:
        polygon = shape(feature["geometry"])

        if polygon.contains(point):
            return (
                feature["properties"].get("NAME_1") or
                feature["properties"].get("county") or
                feature["properties"].get("name") or
                "Unknown County"
            )

    return "Outside Kenya"

# ================= HOME =================
@app.route('/')
def home():
    return render_template("index.html")

# ================= CHOROPLETH DATA =================
@app.route('/county-data')
def county_data():
    return jsonify(counties_geojson)

# ================= ML PREDICTION =================
@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    df = pd.DataFrame([data])
    df = df[features]

    prediction = model.predict(df)[0]

    risk = (
        "Low" if prediction < 10 else
        "Medium" if prediction < 20 else
        "High"
    )

    county_name = get_county_name(
        data["latitude"],
        data["longitude"]
    )

    return jsonify({
        "prediction": round(float(prediction), 2),
        "risk_level": risk,
        "county": county_name
    })

# ================= COUNTY STATS =================
@app.route('/county-stats/<county_name>')
def county_stats(county_name):

    # stable pseudo-random stats per county
    seed = abs(hash(county_name)) % 10000
    np.random.seed(seed)

    return jsonify({
        "county": county_name,
        "infected": int(np.random.randint(500, 5000)),
        "on_art": int(np.random.randint(300, 4000)),
        "deaths": int(np.random.randint(10, 500)),
        "malnourished": int(np.random.randint(100, 2000)),
        "new_infections": int(np.random.randint(50, 800))
    })

# ================= OPTIONAL: DEBUG TB SCORES =================
@app.route('/tb-scores')
def tb_scores():
    return jsonify(county_tb_scores)

# ================= RUN APP =================
if __name__ == '__main__':
    app.run(debug=True)