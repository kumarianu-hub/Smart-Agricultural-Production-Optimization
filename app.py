from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Crop recommendation logic
def recommend_crop(soil, season):
    crops = {
        ("Loamy", "Summer"): "Maize",
        ("Loamy", "Winter"): "Wheat",
        ("Clay", "Summer"): "Rice",
        ("Clay", "Winter"): "Barley",
        ("Sandy", "Summer"): "Groundnut",
        ("Sandy", "Winter"): "Millets"
    }
    return crops.get((soil, season), "Vegetables")

# Yield prediction
def predict_yield(area):
    try:
        return round(float(area) * 2.5, 2)
    except:
        return 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        farmer = request.form['farmer']
        soil = request.form['soil']
        season = request.form['season']
        area = request.form['area']

        crop = recommend_crop(soil, season)
        yield_value = predict_yield(area)

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS records(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            farmer TEXT,
            soil TEXT,
            season TEXT,
            area REAL,
            crop TEXT,
            yield REAL
        )
        """)

        cur.execute("""
        INSERT INTO records
        (farmer, soil, season, area, crop, yield)
        VALUES (?,?,?,?,?,?)
        """, (farmer, soil, season, area, crop, yield_value))

        conn.commit()
        conn.close()

        return render_template(
            "result.html",
            farmer=farmer,
            crop=crop,
            yield_value=yield_value
        )

    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)