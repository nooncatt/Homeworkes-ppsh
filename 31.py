# Task 0
import howdoi
print(dir(howdoi))
print(howdoi.__version__)
# howdoi create list in python



# Task 1
import requests
def ask():
    res = requests.get(input('Введите адрес страницы в кавычках\n'))
    if res.status_code == 200:
        print('Успешно')
        print("Код состояния HTTP-ответа:", res.status_code)
    else:
        print('Что-то не так')

# ask() # http://sky.pro/media

# Успешно
# Код состояния HTTP-ответа: 200




# Task 2
from PIL import Image
# Pillow — это ответвление библиотеки PIL.
# Поэтому вам все равно придется использовать PIL при импорте в ваш код.

img = Image.open("strawberry.jpg")
resized_image = img.resize((800, 600))
resized_image.save("resized_image.jpg")

# img.show()
img.close()




# img1 = Image.open("image-pillow.png")
# img1.show()




# Task 3
from pytube import YouTube
def download_video(url):
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    try:
        video.download()
        print("Видео успешно загружено")
    except:
        print("Произошла ошибка.")

# download_video('https://www.youtube.com/watch?v=5DEdR5lqnDE') # https://www.youtube.com/watch?v=5DEdR5lqnDE
# https://www.youtube.com/watch?v=OUcgazZDoDQ




# Task 4
from colorama import init
init()

from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.BLACK + 'черный текст')
print(Back.YELLOW + 'на желтом фоне')
print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
print('обычный текст')

print(Fore.CYAN + 'сам текст покрашен в какой-то цвет' + Style.RESET_ALL)
print(Back.MAGENTA + 'сам текст + его фон покрашен в какой-то цвет' + Style.RESET_ALL)
print('снова текст, но без какого-либо окрашивания')
print(Fore.BLACK + Back.GREEN + 'сам текст с покрашенным фоном в какой-то цвет'+ Style.RESET_ALL)




# Task 5
from emoji import demojize

text = 'Buy 📈📈📈 the programming after 👀 school 👏📚🏫 course! 😂'
print(demojize(text))




# Task 6

import pyperclip
import time

# def transform_text(text):
#     text = ' '.join(text.split())
#     text = text.replace('ё', 'е').lower()
#     return text
#
# while True:
#     original_text = pyperclip.paste()
#     new_text = transform_text(original_text)
#     pyperclip.copy(new_text)
#     time.sleep(1)



# 2 ВАРИАНТ

# from pyperclip import copy, paste
# from time import sleep
#
# while True:
#     text = paste()
#     text = " ".join(text.split()).replace("ё", "е").lower()
#     copy(text)
    # sleep(1)




# Task 7
print('\n')
import wikipedia
# распечатать резюме того, что такое компьютерная программа
print(wikipedia.summary("Computer program"))

