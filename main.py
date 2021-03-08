from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/plots/max-temperature")
def max_temp():
    return render_template("max-temp.html", name="Max Temperature")

@app.route("/plots/humidity")
def humidity():
    return render_template("humidity.html", name="Humidity")

@app.route("/plots/cloudiness")
def cloudiness():
    return render_template("cloudiness.html", name="Cloudiness")

@app.route("/plots/wind-speed")
def wind_speed():
    return render_template("wind-speed.html", name="Wind Speed")

@app.route("/comparison")
def comparison():
    return render_template("comparison.html")

@app.route("/data")
def table():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)