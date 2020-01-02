"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    #Get('/', 'WelcomeController@show').name('welcome'),

    #Weather App
    Get('/', 'WeatherController@show'),
    Post('/add','WeatherController@store'),
    Get('/@id/delete','WeatherController@delete')
]
