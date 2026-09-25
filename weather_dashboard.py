import requests
import pandas as pd
import matplotlib.pyplot as plt


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    result = data["results"][0]

    return result["latitude"], result["longitude"]


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "forecast_days": 7
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


city = input("Enter city name: ")

latitude, longitude = get_coordinates(city)

print("\nLocation")
print("Latitude:", latitude)
print("Longitude:", longitude)

data = get_weather(latitude, longitude)

current = data["current"]

print("\nCurrent Weather")
print("Temperature:", current["temperature_2m"], "°C")
print("Humidity:", current["relative_humidity_2m"], "%")
print("Wind Speed:", current["wind_speed_10m"], "km/h")


daily = data["daily"]

weather_data = {
    "Date": daily["time"],
    "Max Temperature": daily["temperature_2m_max"],
    "Min Temperature": daily["temperature_2m_min"],
    "Rain": daily["precipitation_sum"]
}

df = pd.DataFrame(weather_data)

print("\n7-Day Forecast")
print(df)


# Save weather data to CSV

df.to_csv("weather_forecast.csv", index=False)

print("\nWeather data saved to weather_forecast.csv")


# Temperature chart

plt.figure(figsize=(10, 5))

plt.plot(
    df["Date"],
    df["Max Temperature"],
    marker="o",
    label="Max Temperature"
)

plt.plot(
    df["Date"],
    df["Min Temperature"],
    marker="o",
    label="Min Temperature"
)

plt.title(f"7-Day Temperature Forecast - {city}")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("temperature_forecast.png")

plt.show()


# Rainfall chart

plt.figure(figsize=(10, 5))

plt.bar(
    df["Date"],
    df["Rain"]
)

plt.title(f"7-Day Rainfall Forecast - {city}")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("rainfall_forecast.png")

plt.show()