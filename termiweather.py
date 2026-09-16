#!/bin/python
import python_weather
import asyncio
import sys

async def getWeather(location) -> None:
    weather = await client.get(str(location))

    print("Temperature: " + weather.temperature)
    print("Precipitation: " + weather.precipitation)
    print("Wind Speed and Direction: " + weather.wind speed + weather.wind_direction)
    print("Humidity: " + weather.humidity)

getWeather(sys.argv[0])
