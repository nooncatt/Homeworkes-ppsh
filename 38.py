# Task 1
from PIL import Image
import requests

def upload_from_url(url, name_of_saved_i):
    try:
        r = requests.get(url)
        from io import BytesIO
        i = Image.open(BytesIO(r.content))
        i.save(f"{name_of_saved_i}.jpg")
        # i.show()
    # отлавливание любых возможных ошибок при запросе
    except requests.exceptions.RequestException as error:
        print(f'Возникла ошибка {error}')

upload_from_url('https://www.ixbt.com/digimage/kittiphot/kr_4l.jpg', 'kit')



# Task 2

def check_the_status_code(urls):
    try:
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'Сайт доступен, статус код {response.status_code}')
            else:
                print(f'Сайт недоступен, статус код {response.status_code}')
    except requests.exceptions.RequestException as err:
            print(f"{url} недоступен! Ошибка при выполнении запроса: {err}")

urls = ['https://skillbox.ru/media/', 'https://trikota.tv/']
check_the_status_code(urls)




# Task 3
# pip install requests BeautifulSoup4 lxml

import requests
from bs4 import BeautifulSoup
import random


def anime_quote():
    url = 'https://masakaru.ru/animanga-kosplej-otaku/anime-i-manga/100-luchshih-citat-iz-anime-vseh-vremen-korotkie-i-dlinnye.html'
    try:
        response = requests.get(url)
        # преобразуем запрос в html-суп, убираем ошибки сайта с помощью lxml
        soup = BeautifulSoup(response.text, 'lxml')

        anime_text = soup.find_all("blockquote", class_="wp-block-quote is-layout-flow wp-block-quote-is-layout-flow")
        clear_anime_text = [anime.text for anime in anime_text]

        r_quote = random.choice(clear_anime_text)
        print(f'Цитата из аниме: {r_quote}')
    except requests.exceptions.RequestException as error:
        print(f'Произошла ошибка {error}')



# for i in range(len(clear_anime_text)):
#    print(f'Цитата из аниме: {clear_anime_text[i]} \n')

anime_quote()





# Task 4

def info_about_weather(town):
    try:
        api_key = '8abcc5fe570640c4a1a194803241209'
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={town}"
        r = requests.get(url)
        weather_data = r.json() # можно и всю weather_data...
        print(f'The temperature in {town} is {weather_data['current']['temp_c']} °C.\n'
              f'The weather conditions: {weather_data['current']['condition']['text'].lower()}\n')
    except requests.exceptions.RequestException as error:
        print(f'Возникла ошибка {error}')

info_about_weather('Mayami') # The weather in London is 7.3 °C
info_about_weather('Saint-Petersberg') # The weather in Saint-Petersberg is 7.3 °C
info_about_weather('Omsk') # The weather in Omsk is 16.3 °C





# Task 5
# pip install freecurrencyapi

def currency_converter(amount, base_currency, required_currency):
    api_key = 'fca_live_2Ds4aW76f7IO7Fe7ym6L337gokPCl8VuPIdUbCRZ'
    url1 = f'https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&base_currency={base_currency}&currencies={required_currency}'
    r = requests.get(url1)
    money = r.json()
    # print(money)

    url2 = f'https://api.freecurrencyapi.com/v1/currencies?apikey={api_key}'
    currency_list = requests.get(url2).json()
    # print(currency_list)
    try:
        for _ in currency_list:
            if base_currency in currency_list['data'] and required_currency in money['data']: # проверка первой валюты и второй валюты
                result = amount * money['data'][f'{required_currency}']
                print(f'Если перевести {base_currency} в {required_currency}, то получится {result}')
            else:
                print('Такого обозначения валюты нет, проверьте пожалуйста еще раз')
    except KeyError:
        print('Вы неправильно обозначили валюты. Пожалуйста, ознакомьтесь со списком')


currency_converter(150, 'USD', 'EUR') # Если перевести USD в EUR, то получится 135.373515315
currency_converter(1, 'USD', 'RUB') # Если перевести USD в RUB, то получится 90.785183797
currency_converter(1, 'USD', 'RUBB') # Вы неправильно обозначили валюты. Пожалуйста, ознакомьтесь со списком
currency_converter(1, 'USDв', 'RUB') # Такого обозначения валюты нет, проверьте пожалуйста еще раз




# Task 6
import requests
import matplotlib.pyplot as plt


def forecast(days, city):
    api_key = '8abcc5fe570640c4a1a194803241209'
    url = f'http://api.weatherapi.com/v1/ forecast.json?key={api_key}&q={city}&days={days}'
    r = requests.get(url)
    weather_data = r.json()
    return weather_data
def plot_of_forecast(days, city):
    forecast_days = forecast(days, city)['forecast']['forecastday']

    dates = [forecast_day['date'][-2:] for forecast_day in forecast_days]
    temperatures = [forecast_day['day']['avgtemp_c'] for forecast_day in forecast_days]

    plt.plot(dates, temperatures, marker='o')
    plt.xlabel('Дата')
    plt.ylabel('Температура')
    plt.title(f'Прогноз погоды на {days}')
    plt.grid(which='major', linestyle=':', linewidth='1', color='pink')

    # plt.show()

plot_of_forecast(7, 'London')




# Task 7
# создайте специальную программу для скачивания этих изображений и сохранения их в формате GIF

from PIL import Image
# pip install nasapi
# pip install pandas

from nasapy import Nasa


def get_nasa_image():
    API_KEY = 'qaWz5MhEu3bAAsDDw06DgaJpK5ARI40s9oNcs45o'
    nasa = Nasa(key=API_KEY)

    today = '2022-07-07'
    today_data = nasa.epic(date=today)

    formatted_date = today.replace('-', '/')

    count_of_images = 0
    for i, data in enumerate(today_data):
        if i >= 1:
            break
        else:
            try:
                response = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{data["image"]}.png?api_key={API_KEY}')

                with open(f'image{str(i)}.png', 'wb') as file:
                    file.write(response.content)
                count_of_images += 1

            except requests.exceptions.RequestException as error:
                print(f'Error: {error}')

    for n in range(count_of_images):
        with Image.open(f'image{n}.png') as im:
            # im.show()
            im.save(f'image_of_Earth.gif')

get_nasa_image()





# Task 8
# pip install folium
import requests
import folium

from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon


def get_the_geoposition(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    if response.status_code == 200:
        map_info = response.json()
        print(map_info)

        if map_info['lat'] and map_info['lon'] not in map_info:
            print('Неверный адрес или недостаточно информации')
        else:
            coord = [map_info['lat'], map_info['lon']]

            m = folium.Map(
                location = coord,
                control_scale=True,
            )
            folium.Marker(
                location=coord,  # coordinates for the marker (Earth Lab at CU Boulder)
                popup='Map',  # pop-up label for the marker
                icon=folium.Icon()
            ).add_to(m)
            m.save("my-point.html")
    else:
        print("При извлечении информации об IP-адресе произошла ошибка.")


get_the_geoposition('95.161.221.211')




# Task 9

import requests
import base64
import json
import time

class Text2ImageAPI():
    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        if response.status_code == 200:
            data = response.json()
            return data[0]['id']
        else:
            print(f'Error. Status code {response.status_code}')

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)


api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '829E0692FDB2664E5CA66BDB115B5AA1', 'C4811F23B89E27908503AB65A4340415')
model_id = api.get_model()
uuid = api.generate("Битва Таноса и Винни Пуха", model_id)
images = api.check_generation(uuid)



image_base64 = images[0]
image_data = base64.b64decode(image_base64)
with open("image.jpg", "wb") as file:
     file.write(image_data)



