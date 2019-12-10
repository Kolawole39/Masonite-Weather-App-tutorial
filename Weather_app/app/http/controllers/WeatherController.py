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
        cities_weather = []

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

        return view.render('weather',{'cities':cities})
    
    def store(self, request: Request, view:View):
        City.create(
            name = request.input('name')
        )

        return view.render('weather')
