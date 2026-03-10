# Modify the code in API_and_data.py to get the weather in your city, Find your city's coordinates at https://www.latlong.net/
# and then use the API to get the weather in your city.

import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculating dates to get 1 week of weather data
today = datetime.now()
week_ago = today - timedelta(days=6)

# Formatting dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

def get_weather(lat, long):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min")
    data = response.json()
    return data

coordinates = (9.07, 7.39)
weather_data = get_weather(9.07, 7.39)

# Data Extraction (Change this to match the structure of the API response)
daily_data = weather_data['daily']

dates_data = daily_data['time']
max_temperature = daily_data['temperature_2m_max']
min_temperature = daily_data['temperature_2m_min']

print(f"{dates_data}\n{max_temperature}\n{min_temperature}")

# ------------------------------------------------------------
# Create a DataFrame using panda
df = pd.DataFrame({
    'date': dates_data,
    'max_temp': max_temperature,
    'min_temp': min_temperature
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])
print(df['date'])

# ------------------------------------------------------------
# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Lagos Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('lagos_weather_chart.png')
plt.show()

# ------------------------------------------------------------
# Save data to CSV
# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/lagos_weather.csv', index=False)
print("Data saved to data/lagos_weather.csv")
