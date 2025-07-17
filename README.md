# 🌤️ Weather App

A sleek, black-themed weather application that fetches real-time weather data using the OpenWeatherMap API. The app allows users to search for weather by **city, state, and country**, or interactively select a location on a **Leaflet.js-powered map**.  

The backend is built with Flask, with a modular Python structure for maintainability, and Bootstrap provides a responsive UI design.  

---

## 📸 Screenshots

### 🏠 Homepage
![Homepage](examples/Example_1.png)

---

### ⚠️ Error Handling
![Error Handling](examples/Example_2.png)

---

### 📍 Map Interaction
![Map Interaction](examples/Example_3.png)

---

### 🌦️ Weather Results (London)
![Weather Results London](examples/Example_4.png)

---

### 🌦️ Weather Results (Atlanta)
![Weather Results Atlanta](examples/Example_5.png)

---

## 🛠 Project Structure

```
Weather-App-project/
│
├── src/ # Python source code
│ ├── app.py # Flask app entry point
│ └── weather.py # API integration and logic
│
├── templates/ # HTML templates (Jinja2)
│ └── index.html
│
├── examples/ # Screenshots for README
│ ├── Example_1.png
│ ├── Example_2.png
│ ├── Example_3.png
│ ├── Example_4.png
│ └── Example_5.png
│
├── .env # Environment variables (API_KEY)
├── .gitignore # Files/folders to exclude from Git
├── requirements.txt # Python dependencies
└── README.md # Project overview (this file)
```

---

## 🚀 Features
- 🌎 Search weather by **city, state, and country**  
- 📍 Interactive map for selecting coordinates  
- 🌑 **Sleek black aesthetic** with responsive design  
- ⚡ Real-time data powered by **OpenWeatherMap API**  
- 🧱 Modular codebase (Flask backend, Jinja2 templates, Leaflet.js map)  

---

## 📄 Notes
This project was built as part of a personal portfolio to demonstrate API integration, backend design, and UI theming.
