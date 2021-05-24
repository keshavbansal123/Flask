# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:04:51 2021

@author: Dell
"""

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/city')
def search_city():
    API_KEY = '019de89f27354d607a50ebf5467efa51'  # initialize your key here
    city = request.args.get('q')  # city name passed as argument

    # call API and convert response into Python dictionary
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()

    # error like unknown city name, inavalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

    # get current temperature and convert it into Celsius
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        return f'Current temperature of {city.title()} is {current_temperature_celsius} &#8451;'
    else:
        return f'Error getting temperature for {city.title()}'


@app.route('/')
def index():
    return '<h1>Welcome to weather app</h1>'


if __name__ == '__main__':
    app.run()