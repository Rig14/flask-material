from flask import Flask
from flask import render_template
from flask import request
from openweather import weather_data

app = Flask(__name__)
app.config.from_object('config:Config')

@app.route('/')
def home():  
    return render_template('index.html')

@app.route('/weather')
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    data = weather_data(lat, lon, app.config['OPEN_WEATHER_API_KEY'])
    return render_template('weather.html', data=data)

if __name__ == '__main__':
    app.run()
