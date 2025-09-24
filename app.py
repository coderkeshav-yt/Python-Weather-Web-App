# app.py

from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# --- Flask App Initialization ---
app = Flask(__name__)

# --- Helper Functions ---
def get_weather_data(city_name: str, units: str = "metric") -> dict | None:
    # Immediately check if the API_KEY was loaded from the .env file
    if not API_KEY:
        print("❌ FATAL ERROR: API_KEY not found in .env file.")
        return {"cod": 401, "message": "API Key is missing."} # Return an error dict

    params = {"q": city_name, "appid": API_KEY, "units": units}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() # This will raise an error for 4xx or 5xx responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP Error: {http_err}")
        # Return the actual error response from the API if possible
        return http_err.response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ API Request Error: {e}")
        # Return a generic error for other network issues
        return {"cod": 500, "message": "Network error or API is unreachable."}

def process_weather_data(data: dict, units: str) -> dict:
    if not data or data.get("cod") != 200:
        error_message = data.get("message", "An unknown error occurred.")
        return {"error": error_message.title()}

    main = data.get('main', {})
    wind = data.get('wind', {})
    weather = data.get('weather', [{}])[0]
    sys_info = data.get('sys', {})

    unit_symbols = {
        "metric": {"temp": "°C", "speed": "km/h"},
        "imperial": {"temp": "°F", "speed": "mph"}
    }
    
    temp_unit = unit_symbols.get(units, {}).get("temp", "")
    speed_unit = unit_symbols.get(units, {}).get("speed", "")
    
    wind_speed = wind.get('speed', 0)
    if units == "metric":
        wind_speed *= 3.6

    return {
        'location': f"{data.get('name', 'N/A')}, {sys_info.get('country', 'N/A')}",
        'temp': f"{main.get('temp', 0):.0f}{temp_unit}",
        'feels_like': f"{main.get('feels_like', 0):.0f}{temp_unit}",
        'description': weather.get('description', 'N/A').title(),
        'icon': weather.get('icon', '01d'),
        'humidity': f"{main.get('humidity', 0)}%",
        'wind_speed': f"{wind_speed:.1f} {speed_unit}",
    }

# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city_name = ""
    # Use .get() with a default value to prevent KeyError
    selected_units = request.form.get('units', 'metric') 

    if request.method == 'POST':
        city_name = request.form.get('city', '')
        raw_data = get_weather_data(city_name, selected_units)
        weather_data = process_weather_data(raw_data, selected_units)
        
    return render_template('index.html', 
                           weather=weather_data, 
                           city_name=city_name, 
                           units=selected_units)

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True, port=5001)