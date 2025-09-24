# 🌤️ Weather App

A sleek weather application built with **Python** and **Flask** that provides **real-time weather information** for any location.



## ✨ Features

* 🌎 **Real-time weather data** using [WeatherAPI](https://www.weatherapi.com/)
* 🎨 **Clean & responsive UI** with simple HTML/CSS
* 🔑 **Environment variable support** for secure API keys
* ⚡ Lightweight and easy to set up

📸 UI Preview
<p align="center"> <img src="https://res.cloudinary.com/dlvxjnycr/image/upload/v1758702054/Lucknow_Fahrenheit_dd4smm.png" alt="Weather App Screenshot - Fahrenheit" width="45%"/> &nbsp;&nbsp; <img src="https://res.cloudinary.com/dlvxjnycr/image/upload/v1758701988/lucknow_whether_of2ahy.png" alt="Weather App Screenshot - Weather Info" width="45%"/> </p>

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root and add your API key:

   ```env
   WEATHER_API_KEY=your_api_key_here
   ```

---

## 📦 Requirements

* Python **3.8+**
* Flask
* Weather API key (free at [weatherapi.com](https://www.weatherapi.com/))

---

## 📂 Project Structure

```
weather-app/
├── app.py              # Main Flask app
├── .env                # API key & environment variables
├── .gitignore          # Ignored files
├── static/
│   └── style.css       # Stylesheet
└── templates/
    └── index.html      # UI template
```

---

## ▶️ Usage

1. **Run the development server**

   ```bash
   python app.py
   ```
2. Open your browser and visit 👉 [http://localhost:5000](http://localhost:5000)

---

## 📝 Notes

* Add your **API key** to the `.env` file before running
* Uses Flask’s built-in development server (not for production)
* For production, deploy with **Gunicorn** or another WSGI server


