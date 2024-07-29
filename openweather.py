import requests

def weather_data(lat: int, lon: int, api_key: str) -> dict:
    """
    Retrieves weather data from the OpenWeatherMap API based on latitude and longitude coordinates.

    Args:
        lat (int): The latitude coordinate.
        lon (int): The longitude coordinate.
        api_key (str): The API key for accessing the OpenWeatherMap API.

    Returns:
        dict: A dictionary containing the weather data.

    """
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    return response.json()