# Weather Notifier

A simple Python script that fetches the current weather for a given city and displays a Windows toast notification.

## Requirements
- Windows OS
- Python 3.x
- An API key from OpenWeatherMap

## Installation
1. Install the required libraries:
   ```sh
   pip install win10toast requests
   ```
   If you encounter issues, try:
   ```sh
   pip install win10toast-persist requests
   ```
   or
   ```sh
   pip install pywin32
   pip install win10toast-persist requests
   ```

## Steps to Use
1. Replace `API_KEY` in the script with a valid API key from OpenWeatherMap.
2. Run the script:
   ```sh
   python script.py
   ```
3. Enter the city name when prompted.
4. A toast notification will display the weather information.

## Getting an API Key from OpenWeatherMap
1. Sign up at OpenWeatherMap: [OpenWeatherMap Sign Up](https://openweathermap.org/current)
2. Create a free account and verify your email.
3. Go to your API keys section: [API Keys](https://home.openweathermap.org/api_keys)
4. Use the default key or create a new one.

## References
- [OpenWeatherMap API Documentation](https://openweathermap.org/current)
- [Win10Toast Library](https://pypi.org/project/win10toast/)

## License
This project is licensed under the MIT License.

## About
This script is designed to fetch and display weather updates as a Windows notification using the OpenWeatherMap API.

