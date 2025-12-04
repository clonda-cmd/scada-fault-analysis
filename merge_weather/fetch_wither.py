import pandas as pd
import requests
import os

# Путь к вашей папке
folder = ('data/weather/')
filename = os.path.join(folder, "weather.csv")

# URL API
url = "https://api.open-meteo.com/v1/forecast?latitude=47.18078639647388&longitude=39.647388&hourly=temperature_2m&timezone=Europe%2FMoscow&start_date=2025-11-11&end_date=2025-11-25"

# Создаем папку если её нет
if not os.path.exists(folder):
    os.makedirs(folder)

# Получаем и сохраняем данные
response = requests.get(url)
data = response.json()

weather_df = pd.DataFrame({
    'datetime': pd.to_datetime(data['hourly']['time']),
    'temperature': data['hourly']['temperature_2m']
})

weather_df.to_csv(filename, index=False)
print(f"✅ Сохранено {len(weather_df)} строк в {filename}")
