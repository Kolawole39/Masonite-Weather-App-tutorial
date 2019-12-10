"""A WeatherController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.City import City
import requests

class WeatherController(Controller):
    """WeatherController Controller Class."""

    def __init__(self, request: Request):
        """WeatherController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        cities = City.all()

        API_KEY = '83c2a4b1cd7f54c707c77b0aa0ad102d'

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}' 

        weather_data = []    
        for city in cities:
            city_weather = requests.get(url.format(city.name,API_KEY)).json()
        #request data in json and then convert it in python data
            weather = {
                    'city' : city.name,
                    'temperature' : city_weather['main']['temp'],
                    'description' : city_weather['weather'][0]['description'],
                    'icon' : city_weather['weather'][0]['icon']
                }

            weather_data.append(weather)
        return view.render('weather', {'weather_data':weather_data })
    
    def store(self, request: Request):
        #Before saving city in our database, we must ask our API if the city exitsts
        API_KEY = '83c2a4b1cd7f54c707c77b0aa0ad102d'

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}' 

        city = request.input('name')

        city_weather = requests.get(url.format(city,API_KEY)).json()

        if city_weather['cod'] == '404':
            return city_weather['message']
        else:
            City.create(
            name = request.input("name")
            )

        return 'City Added!'
