"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    #Weather App
    Get('/weather', 'WeatherController@show'),
    Post('/weather/add','WeatherController@store'),
]
