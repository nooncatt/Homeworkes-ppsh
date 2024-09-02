# Task 1

# pip show pip
# pip --help
# pip list
# pip install numpy
# pip show numpy
# pip list
# pip uninstall numpy
# pip list




# Task 2
# import os
#
# directory_name = 'folder' # Название нового каталога
# os.mkdir(directory_name) # Создание каталога
#
# python -m venv venv1
#
# cd venv1\Scripts
# .\activate.ps1
#
# pip install --upgrade pip # Обновим менеджер пакетов pip
# pip install pillow
# pip list
# # Сохраним версии и одновременно сгенерируем файл
# pip freeze > requirements.txt
# deactivate
#
# cd ..
# cd ..
# rm -r venv1
#
# py -3.12 -m venv venv2
#
# cd venv2\Scripts
# .\activate.ps1
#
# python.exe -m pip install --upgrade pip
# pip install -r requirements.txt
# pip list




# Task 3

# pip install Pillow pyscreenshot
from time import sleep

from pyscreenshot import grab
# help('pyscreenshot')
# help(grab)
import pyscreenshot as ImageGrab

# print(dir(ImageGrab))
# for _ in range(5):
#     im = grab()
#     im.save("scr" + str(_) + ".png")
#     sleep(5)




# Task 4
# pip install fuzzywuzzy
# pip install fuzzywuzzy[speedup]

from fuzzywuzzy import fuzz
# help('fuzzywuzzy')
# dir(fuzz)
# help(fuzz.ratio)

# Данный метод возвращает индекс схожести двух строк.
print(fuzz.ratio("Я разобрался с виртуальным окружением", "Это оказалось совсем не трудно"))
# 42
print(fuzz.ratio("Я разобрался с виртуальным окружением!", "Я разобрался с виртуальным окружением!"))
# 100
print(fuzz.ratio("Я разобрался с виртуальным окружением?", "Я разобрался с виртуальным окружением!"))
# 97




# Task 5
# pip install psutil
# pip install pyttsx3

# help('psutil')
# help('pyttsx3')
from psutil import sensors_battery
from pyttsx3 import init

# dir(sensors_battery)
# help(sensors_battery)
# help(init().say)
# print(dir(init().say))
# print(dir(init().runAndWait))
# help(init().runAndWait)

battery = sensors_battery()

if battery.percent < 20:
    engine = init()
    engine.say(f'Заряд батареи {battery.percent} %. '
               f'В срочном порядке зарядите её')
    engine.runAndWait()




# Task 6
# pip install win11toast

from win11toast import toast
from datetime import datetime
# help(toast)
# print(dir(toast))

def validate_time(alarm_time):
    if len(alarm_time) != 5:
        return 'Неверный формат'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Неверный формат часов'
        elif int(alarm_time[3:5]) > 59:
            return 'Неверный формат минут'
        else:
            return True

while True:
    alarm_time = input("Укажите время будильника в формате 'HH:MM' \nВремя будильника: ")
    validate = validate_time(alarm_time)
    if validate:
        name = input('Введите название: ')
        print(f'Будильник установлен на время {alarm_time}')
        break
    else:
        print(validate)

alarm_HH = int(alarm_time[0:2])
alarm_MM = int(alarm_time[3:5])

while True:
    now = datetime.now()
    current_hour = now.hour
    current_min = now.minute
    if alarm_HH == current_hour:
        if alarm_MM == current_min:
            import os
            toast('Будильник', name, button='Выключить', audio="audio='C:\Windows\Media\Alarm01.wav")





# Task 7
# pip install python-dotenv

# import os
# dir_name = 'project 1' # Название нового каталога
# os.mkdir(dir_name) # Создание каталога

# help('dotenv')
# print(dir(dotenv))

import os
from dotenv import load_dotenv

load_dotenv("C:\\Users\\User\\Desktop\\work\\python education\\ППШ\\project1\\.env.txt")

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
API_KEY = os.getenv("API_KEY")

print(USERNAME, PASSWORD, API_KEY)

# pip freeze > requirements.txt
# Теперь файл requirements.txt можно использовать для установки
# всех требуемых модулей, используя команду pip install -r requirements.txt