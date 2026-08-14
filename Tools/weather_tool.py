from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get the current weather for the given city"""

    weather_data={
        'Kathmandu': 'Sunny, 30°C',
        'Dharan': 'Cloudy, 18C',
        'London': 'Rainy, 15C'
    }

    return weather_data.get(city, 'Weather not available for this city')


result = get_weather.invoke({
    'city': 'Kathmandu'
})

print(result)