import python_weather
import asyncio

async def main(location) -> None:
    weather = await client.get(str(location))

    print(weather.temperature)
    print(weather.precipitation)
    print(weather.wind speed + weather.wind_direction)