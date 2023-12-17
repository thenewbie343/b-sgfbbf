



import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

import requests
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"The weather in {city} is {weather_description}. Temperature: {temperature}°C"
    else:
        return f"Failed to fetch weather data. Error: {data['message']}"

def main():
    api_key ="6ec11929ca4ffe9a92b36b82b94fe009"
    city = input("Enter the city name: ")

    result = get_weather(api_key, city)
    speaker.speak(result)
    print(result)


if __name__ == "__main__":
    main()
<head>


<body>

</body>
</html>