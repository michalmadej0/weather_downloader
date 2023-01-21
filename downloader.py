import schedule
import time
import requests
import csv
from datetime import datetime

def download_weather():
    print('Ruszam')
    api_key = 'a3c8518113db5c7bc4513414babcb42c'
    lang = 'pl'
    units = 'metric'
    city = 'Warszawa'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}' \
              f'&lang={lang}'

    response = requests.get(url).json()
    temp = response['main']['temp']
    description = response['weather'][0]['description']
    pressure = response['main']['pressure']
    currently_date = str(datetime.now().replace(microsecond=0))
    data = {'city':city,'temp':temp, 'description':description, 'pressure':pressure, 'date': currently_date}

    with open('weather_file.csv', 'a', newline='') as file:
        fieldnames = ['key', 'value']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for key, value in data.items():
            writer.writerow({'key': key, 'value':value})


schedule.every(3).seconds.do(download_weather)

while True:
    schedule.run_pending()
    time.sleep(1)

