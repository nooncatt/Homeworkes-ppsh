import matplotlib.pyplot as plt
import numpy as np

# Task 1

days_of_week = np.arange(1,8)
temperatures = np.array([25, 28, 30, 27, 22, 24, 26])

plt.figure(figsize=(5,5))
plt.plot(days_of_week, temperatures, marker='o')
plt.xticks(ticks=np.arange(1,8), labels=['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'], rotation=15)
plt.xlabel('Дни недели')
plt.ylabel('Температура, C')
plt.grid()

plt.show()




# Task 2

music_genres = 'Рок', 'Поп', 'Хип-Хоп', 'Электронная', 'Классическая'
votes = [30, 20, 15, 10, 25]

fig, ax = plt.subplots()
ax.pie(votes, labels=music_genres, autopct='%1.1f%%')
plt.title('Предпочтения музыкальных жанров')
plt.show()



# Task 3

matches = ('Матч 1', 'Матч 2', 'Матч 3', 'Матч 4', 'Матч 5')
well_done = [2, 3, 1, 4, 2]
not_well = [1, 2, 0, 3, 1]

x = np.arange(len(matches))
width = 0.35

fig, ax = plt.subplots()

rects1 = ax.bar(x - width/2, well_done, width, label='забито', color='pink')
rects2 = ax.bar(x + width/2, not_well, width, label='пропущено', color='black')

ax.set_xticks(x)
ax.set_xticklabels(matches)

ax.legend()
plt.grid()

plt.show()



# Task 4

fruits = ('Яблоки', 'Груши', 'Бананы', 'Апельсины', 'Персики')
sales = [100, 85, 70, 60, 45]

x = np.arange(len(fruits))

fig, ax = plt.subplots(figsize=(7.5,4))
ax.barh(fruits, sales)
plt.xlabel('Количество продаж')
plt.ylabel('Фрукты')
plt.title('Продажи фруктов')

plt.grid()
plt.show()




# Task 5

x = np.random.uniform(0,50,size=50)
y = 3 * x # a = 150/50

plt.plot(x, y)
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('Нарисуй линию')

plt.show()



# Task 6

# np.linspace позволяет генерировать равномерно распределенные значения на отрезке чтобы он был не корявым

# Интервал 1
x1 = np.sort(np.linspace(10,20, 100))
y1 = 2*x1 # функция y = 2x

# Интервал 2
x2 = np.sort(np.linspace(20,30, 100))
y2 = -3 * x2 + 100

# Интервал 1
x3 = np.sort(np.linspace(10,20, 100))
y3 = -3 * x3 + 70

# Интервал 2
x4 = np.sort(np.linspace(20,30, 100))
y4 = 2 * x4 - 30

# Построение графиков
x_full_blue = np.concatenate((x1, x2[1:]))
y_full_blue = np.concatenate((y1, y2[1:]))

x_full_orange = np.concatenate((x3, x4[1:]))
y_full_orange = np.concatenate((y3, y4[1:]))

plt.plot(x_full_blue, y_full_blue, label='Синяя линия')
plt.plot(x_full_orange, y_full_orange, label='Оранжевая линия')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Кусочно-заданная функция')
plt.legend()

plt.show()




# Task 7

x = np.arange(5)

site_a = np.array([50, 60, 70, 80, 90])
site_b = np.array([40, 55, 75, 85, 95])

fig, axes = plt.subplots(1,2, figsize=(9, 4))

ax1 = axes[0]
ax2 = axes[1]

# Настройки 1 графика
ax1.set_title('Посещения сайта A')
ax1.set_xlabel('День')
ax1.set_ylabel('Количество посещений')

# Настройки 2 графика
ax2.set_title('Посещения сайта B')
ax2.set_xlabel('День')
ax2.set_ylabel('Количество посещений')

ax1.plot(x, site_a)
ax2.plot(x, site_b)

plt.subplots_adjust(wspace=0.4)
plt.show()




# Task 8

x = np.arange(6)
popularity = [22, 18, 9, 8, 7, 6]

plt.figure(figsize=(7,5))

plt.title('Популярность языков программирования')
plt.xlabel('Языки программирования')
plt.ylabel('Популярность')

plt.xticks(ticks=np.arange(6) , labels=['Java', 'Python', 'Php', 'JavaScript', 'C#', 'C++'])
plt.bar(x, popularity, color=['red', 'black', 'pink', 'blue', 'yellow', 'lightblue'])

# Включаем сетку для вспомогательных делений
plt.minorticks_on()
plt.grid(True, which='minor', color='gray', linestyle=':', linewidth=0.5)

# Включаем сетку для основных делений
plt.grid(which='major', linestyle='-', linewidth='0.5', color='r')

plt.show()




# Task 9

x = np.arange(10)
y = np.array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])

plt.figure(figsize=(7,5))
plt.bar(x,y, hatch=['|', '\\', '/', '+', '-', '.', '*', 'x', 'o', 'O'], color='white', edgecolor='black')

plt.show()




# Task 10

x = np.random.uniform(-2, 2, 60)
y = np.random.uniform(-3, 3, 60)

plt.scatter(x, y, color='deeppink')
plt.xticks(ticks=np.arange(-2,3))
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
