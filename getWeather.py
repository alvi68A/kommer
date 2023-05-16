import requests


def getWeatherData(latitude, longitude):


    url="https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m,pressure_msl,windspeed_10m,winddirection_10m&windspeed_unit=ms".format(longitude, latitude)

    response=requests.get(url)

    return(response.json())

