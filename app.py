from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model (1).pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    medinc = float(request.form["MedInc"])
    houseage = float(request.form["HouseAge"])
    averooms = float(request.form["AveRooms"])
    avebedrms = float(request.form["AveBedrms"])
    population = float(request.form["Population"])
    aveoccup = float(request.form["AveOccup"])
    latitude = float(request.form["Latitude"])
    longitude = float(request.form["Longitude"])

    data = pd.DataFrame({
        "MedInc": [medinc],
        "HouseAge": [houseage],
        "AveRooms": [averooms],
        "AveBedrms": [avebedrms],
        "Population": [population],
        "AveOccup": [aveoccup],
        "Latitude": [latitude],
        "Longitude": [longitude]
    })

    prediction = model.predict(data)[0]

    price = f"${prediction * 100000:,.2f}"

    return render_template("index.html", prediction=price)

if __name__ == "__main__":
    app.run(debug=True)