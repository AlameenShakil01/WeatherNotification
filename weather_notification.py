import requests
from win10toast import ToastNotifier

def get_weather(city):
    # Replace with your OpenWeatherMap API key
    API_KEY = "3cecca025842449d7a3472c1a3148289"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        # Fetch weather data
        response = requests.get(URL)
        data = response.json()
        
        # Check if the request was successful
        if data["cod"] == 200:
            weather = data["weather"][0]["description"].title()
            temp = data["main"]["temp"]
            return f"{city} Weather: {weather}, {temp}°C"
        else:
            return f"Error: {data.get('message', 'City not found!')}"
    except Exception as e:
        return f"Error: {str(e)}"

def notify_weather():
    # Initialize the toast notifier
    toaster = ToastNotifier()
    
    # Ask the user for a city name
    city = input("Enter city: ")
    
    # Get weather information for the entered city
    weather_info = get_weather(city)
    
    # Display the notification
    toaster.show_toast("Weather Update", weather_info, duration=10)

if __name__ == "__main__":
    notify_weather()