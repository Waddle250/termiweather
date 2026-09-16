#!/bin/python
import python_weather
import asyncio
import sys

async def getWeather(location) -> None:
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(str(location))

        print("Temperature: " + weather.temperature)
        print("Precipitation: " + weather.precipitation)
        print("Wind Speed and Direction: " + weather.wind speed + weather.wind_direction)
        print("Humidity: " + weather.humidity)

if __name__ == '__main__':
    location = sys.argv[1]
    asyncio.run(getWeather(location))
