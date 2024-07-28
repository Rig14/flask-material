from flask import Flask
from flask import render_template
from openweather import weather_data

app = Flask(__name__)
app.config.from_object('config:Config')

@app.route('/')
def hello_world():  # put application's code here
    data = weather_data(40.7128, -74.0060, app.config['OPEN_WEATHER_API_KEY'])
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
