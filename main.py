from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your own API key
API_KEY = "1c08d3ff0dbaf19ae519a946bddee985
"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city_name = request.form.get("city")
        if city_name:
            try:
                # API request
                params = {
                    "q": city_name,
                    "appid": API_KEY,
                    "units": "metric"
                }
                response = requests.get(BASE_URL, params=params)
                if response.status_code == 200:
                    weather_data = response.json()
                else:
                    error = f"City '{city_name}' not found."
            except Exception as e:
                error = f"An error occurred: {e}"
        else:
            error = "Please enter a city name."

    return render_template("index.html", weather_data=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
