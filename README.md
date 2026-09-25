# weather-data-dashboard

A Python-based weather dashboard that retrieves real-time weather data and a 7-day forecast for any city using the Open-Meteo API.

The project uses Pandas to organize the forecast data and Matplotlib to visualize temperature and rainfall trends.

## Features

- Search for any city by name
- Retrieve the city's latitude and longitude
- Display current:
  - Temperature
  - Humidity
  - Wind speed
- Display a 7-day weather forecast
- Store forecast data in a Pandas DataFrame
- Export forecast data to a CSV file
- Generate a 7-day temperature chart
- Generate a 7-day rainfall chart

## Technologies

- Python
- Requests
- Pandas
- Matplotlib
- Open-Meteo API

## Project Structure

```text
weather-data-dashboard/
│
├── weather_dashboard.py
├── weather_forecast.csv
├── temperature_forecast.png
├── rainfall_forecast.png
├── README.md
└── .gitignore
