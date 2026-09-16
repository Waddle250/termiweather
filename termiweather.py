import python_weather
import asyncio
import sys

async def getWeather(location) -> None:
    weather = await client.get(str(location))

    print(weather.temperature)
    print(weather.precipitation)
    print(weather.wind speed + weather.wind_direction)

getWeather(sys.argv[0])
