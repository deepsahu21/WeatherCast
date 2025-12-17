from flask import Flask, render_template, request
import sys
import os

# Get paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Import weather module
try:
    from src.weather import main as get_weather
except ImportError as e:
    # Create a dummy function if import fails
    def get_weather(*args, **kwargs):
        raise ValueError(f"Failed to import weather module: {e}")

# Setup Flask app
template_dir = os.path.join(parent_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        try:
            state = request.form.get('stateName', '')
            country = request.form.get('countryName', '')
            city = request.form.get('cityName', '')
            if city and state and country:
                data = get_weather(city, state, country)
        except Exception as e:
            print(f"Error fetching weather: {e}")
    return render_template('index.html', data=data)


@app.route('/get_coordinates', methods=['GET', 'POST'])
def handle_coordinates():
    if request.method == 'POST':
        try:
            lat = float(request.form.get('latitude', 0))
            lon = float(request.form.get('longitude', 0))
            data = get_weather(lat=lat, lon=lon)
            return render_template('index.html', data=data)
        except Exception as e:
            print(f"Error fetching weather by coordinates: {e}")
            return render_template('index.html', data=None)

# Vercel Python runtime automatically detects the Flask app
# The 'app' variable is used as the WSGI application
