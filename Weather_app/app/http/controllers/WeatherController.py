"""A WeatherController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class WeatherController(Controller):
    """WeatherController Controller Class."""

    def __init__(self, request: Request):
        """WeatherController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        pass
