# Task 1
import math
import random

# 1
a = [1, 2, 3, 4, 5]
import statistics
print(statistics.mean(a))

# 2
from statistics import *
print(mean(a))

# 3
from statistics import mean
print(mean(a))

# 4
from statistics import mean as mn
print(mn(a))

# 5
import statistics as st
print(st.mean(a))




# Task 2
# 1
# help() # help> modules или help("modules")

# 2
import sys
for _ in sys.modules:
    print(_)

# 3
print(dir()) # ['NormalDist', 'StatisticsError', '__ann... - лист из модулей

# 4
# pip list
# $ pip freeze




# Task 3
from sys import setrecursionlimit
setrecursionlimit(2000)
def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n - 1, sum + n)


print(recursive_function(1000, 0))





# Task 4
# import re
from re import findall # - тогда без re
text = 'ул. Кутузовская, дом № 13, корпус 3, квартира 98'
print(findall('\d+', text))





# Task 5
from random import randint as rnd
from random import choice as chc
array = [rnd(1, 100) for x in range(10)]
print(array)
print(chc(array))




# Task 6
from math import sqrt

def find_answer(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return f'Корни мнимые'
    elif D == 0:
        x = (-b) / 2*a
        return f'Квадратное уравнение имеет один корень: {x}'
    else:
        x1 = (-b + sqrt(D)) / 2 * a
        x2 = (-b - sqrt(D)) / 2 * a
        return f'Квадратное уравнение имеет два корня: {x1} и {x2}'

print(find_answer(4, 5, -1))





# Task 7
from datetime import datetime
print(datetime.now().time()) # 19:55:52.381250




# Task 8
from datetime import date, timedelta

d1 = date.fromisoformat('2023-06-09')
d2 = date(2023, 5, 31)
if (d1 > d2):
    delta = d1 - d2
    print(delta.days)
    delta2 = timedelta(days=30)
    print((d1 + delta2).weekday()+1)

# 9 7
# Это означает, что через 30 дней мы "перепрыгнем" через 4 полные недели и еще на 2 дня вперед.
#
# Пятница + 2 дня = Воскресенье
# через 30 дней после 9 июня 2023 года, то есть 9 июля 2023 года, будет воскресенье.

# Первое число 9 - это количество дней между 31 мая и 9 июня 2023 года.
# Второе число 7 соответствует воскресенью (7-й день недели).





# Task 9
sys.path.append('C:\\Users\\User\\Desktop\\work\\python education\\ППШ\\MyModules')
from MyModules import py_version
print(py_version.get_python_version())





# Task 10
from MyModules.calculator import *

def calc(a,b):
    print('Доступны операции: сложение, вычитание, умножение, деление')
    info = input('Какую операцию вы хотите совершить?\n')
    if info == 'сложение':
        return add(a, b)
    if info == 'вычитание':
        return subtract(a, b)
    if info == 'умножение':
        return multiply(a, b)
    if info == 'деление':
        return divide(a, b)

print(calc(5.8, 6))



# Task 11
from MyModules.imp_modules import imp_modules
modules_to_import = ['math', 'random']
imp_modules(modules_to_import)
print(math.factorial(random.randint(1,10)))




# Task 12
from MyModules import geometry
print(geometry.circle())
print(geometry.triangle())
print(geometry.square())