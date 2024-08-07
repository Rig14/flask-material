import reverse_geocode
from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import session, flash

from database.database import create_database
from database.user import create_user, check_user
from openweather import weather_data

app = Flask(__name__)
app.config.from_object('config:Config')
app.secret_key = 'your_secret_key'
with app.app_context():
    create_database()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather')
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    location = reverse_geocode.get((lat, lon))
    data = weather_data(lat, lon, app.config['OPEN_WEATHER_API_KEY'])
    return render_template('weather.html', data=data, location=location)


@app.route('/signup', methods=["POST"])
def signup():
    name = request.form.get('name')
    password = request.form.get('password')
    create_user(name, password)
    user_id = check_user(name, password)
    if user_id:
        session['user_id'] = user_id
        session['username'] = name
        flash("User created")
        return redirect("/")
    flash("Couldn't create user")
    return redirect("/")


@app.route('/login', methods=["POST"])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    user_id = check_user(name, password)
    if user_id:
        session['user_id'] = user_id
        session['username'] = name
        flash("Login successful")
        return redirect("/")
    flash('Invalid credentials')
    return redirect("/")


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Logged out')
    return redirect("/")


if __name__ == '__main__':
    app.run()
