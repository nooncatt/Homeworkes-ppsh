# Task 1
from random import *

class CRM:
    def __init__(self):
        self.__abiturients = {}

    def add(self, abiturient):
        # получение СНИЛСа
        number = abiturient.get_number()
        if self.__is_number(number):
            if number not in self.__abiturients.keys():

        # добавление абитуриента в словарь,
        # где информация хранится под СНИЛСами
                self.__abiturients[number] = abiturient
            else:
                raise ValueError('Такой абитуриент уже есть в словаре')
        else:
            raise ValueError('Number is not correct')
    def get_status(self, number):
        return self.__abiturients[number].get_status(number)
    @staticmethod
    def __is_number(number):
        return (len(number) == 14 and number[:3].isdigit() and number[3]=='-' and number[4:7].isdigit() and number[7]=='-'
        and number[8:11].isdigit() and number[11]==' ' and number[12:].isdigit())


class Abiturient:
    def __init__(self, name, surname, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age

        # СНИЛС
        self.__number = number

        # Russian National Exam (ЕГЭ), баллы
        self.__RNE = self.__fetch_RNE()

        # есть ли БВИ
        self.__bvi = bvi

    # функция получения результатов ЕГЭ
    def __fetch_RNE(self):
        return tuple(randint(0, 100) for _ in range(3))

    # функция ответа на вопрос, проходит ли абитуриент
    def __check(self):
        if all(score >= 95 for score in self.__RNE):
            return "Да"
        elif self.__bvi:
            return "Да"
        elif random() > 0.95:
            return "Да"
        else:
            return "Нет"
    def get_number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = self.__check_fio(name)
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = self.__check_fio(surname)
        return self.__surname
    @property
    def patronymic(self):
        return self.__patronymic
    @patronymic.setter
    def patronymic(self, patronymic):
        self.__patronymic = self.__check_fio(patronymic)
        return self.__patronymic
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = self.__check_age(age)
        return self.__age

    @property
    def RNE(self):
        return self.__RNE
    @RNE.setter
    def RNE(self, Tuple):
        self.__RNE = self.__check_RNE(Tuple)
        return self.__RNE
    @property
    def bvi(self):
        return self.__bvi
    @bvi.setter
    def bvi(self, bvi):
        if bvi == 'False' or bvi == 'True':
            self.__bvi = bvi
            return self.__bvi
        else:
            raise ValueError('Bvi result is not correct: True or False')
    def get_status(self, number):
        return self.__check()
    @staticmethod
    def __check_fio(fio_item):
        if fio_item.isalpha() :
            fio_item = fio_item.capitalize()
            return fio_item
        else:
            raise ValueError('Fio is not correct')
    @staticmethod
    def __check_age(age):
        if isinstance(age, int):
            if age >=18 and age <=100:
                return age
        else:
            raise ValueError('Age is not correct')
    @staticmethod
    def __check_RNE(RNE_tuple):
        answer = []
        if len(RNE_tuple) == 3:
            for ball in RNE_tuple:
                if isinstance(ball, int) and 0<=ball<=100:
                    answer.append(ball)
            return tuple(answer)




module = CRM()

# добавление АР-а в список абитуриентов
module.add(Abiturient("Александр", "Вотяков", "Романович", 18, "111-222-333 00", True))

# добавление РА в список абитуриентов
module.add(Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00"))

# проверка, проходят ли абитуриенты
print(module.get_status("111-222-333 00"))
print(module.get_status("333-222-111 00"))

# Старая ф-я проверки прохождения абитуриента
# def __check(self):
#     if self.__bvi:
#         return "Да"
#     if random() > 0.95:
#         return "Да"
#     return "Нет"






# Task 2
import random
class Emerald:
    __all_statuses = ["не учтён", "учтён", "отправлен под спуд"]
    def __init__(self):
        # статус изумруда:
        # 0 - не учтён
        # 1 - учтён
        # 2 - отправлен под спуд
        self.__status = 0

        # цена изумруда
        self.__price = 0
    def account(self):
        if self.__status == 0:
            self.__status = 1
            self.__price = random.randint(1, 122)*100
        else:
            raise ValueError

    def store(self):
        if self.__status == 1:
            self.__status = 2
        else:
            raise ValueError
    @property
    def status(self):
        return Emerald.__all_statuses[self.__status]
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, new_rate):
        if new_rate > 0 and isinstance(new_rate, int):
            self.__price = new_rate
            return self.__price
        else:
            raise ValueError
    def __str__(self):
        return 'Изумруд'

em1 = Emerald()
em1.account()
print(em1)
print(em1.price)
em1.store()
print(em1.status)

class Shell:
    __all_statuses = ["не учтена", "учтена",
                  "отправлена в монетолитейное отделение",
                  "переплавлена в монету"]
    def __init__(self):
        # статус скорлупки:
        # 0 - не учтена
        # 1 - учтена
        # 2 - отправлена в монетолитейное отделение
        # 3 - переплавлена в монету
        self.__status = 0

        # цена скорлупки
        self.__price = 0

    def account(self):
        if self.__status == 0:
            self.__status = 1
            self.__price = random.randint(1, 17) * 100
        else:
            raise ValueError
    def process(self):
        if self.__status == 1:
            self.__status = 2
        else:
            raise ValueError
    def smelt(self):
        if self.__status == 2:
            self.__status = 3
            for _ in range(self.__price // 10):
                serial_number = random.randint(1, 1000000)
                archive.add(Entry(Coin(serial_number, '2023', 10)))
            for _ in range(self.__price % 10):
                serial_number = random.randint(1, 1000000)
                archive.add(Entry(Coin(serial_number, '2023', 1)))
        else:
            raise ValueError

    @property
    def status(self):
        return Shell.__all_statuses[self.__status]

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_rate):
        if new_rate > 0 and isinstance(new_rate, int):
            self.__price = new_rate
            return self.__price
        else:
            raise ValueError
    def __str__(self):
        return 'Скорлупка золотая'


sh1 = Shell()
print(sh1)
print(sh1.status)
sh1.account()
print(sh1.price)
sh1.process()
# print(sh1.status)
# print(sh1.price)

class Coin:
    def __init__(self, serial_number, year, value):
        # серийный номер монеты
        self.__serial_number = serial_number

        # год выпуска монеты
        self.__year = year

        # номинал монеты
        self.__value = value
    @property
    def serial_number(self):
        return self.__serial_number
    @property
    def year(self):
        return self.__year
    @property
    def value(self):
        return self.__value
    def __str__(self):
        return 'Монета'


class Entry:
    def __init__(self, item, date="01.01.1970", info="", secret=False):
        # идентификационный номер, создаётся автоматически
        self.__ID = self.__get_next_ID()

        # указатель на объект
        self.__item = item

        # дата создания записи
        self.__date = date

        # дополнительная информация об объекте
        self.__info = info

        # информация засекречена?
        self.__secret = secret

    def __get_next_ID(self):
        # можно создать свою функцию вместо этой
        return hash(self)
    @property
    def ID(self):
        return self.__ID
    @property
    def item(self):
        return self.__item
    @property
    def date(self):
        return self.__date
    @property
    def info(self):
        return self.__info
    @info.setter
    def info(self, new_info):
        self.__info = new_info
        return self.__info
    @property
    def secret(self):
        return self.__secret
    @secret.setter
    def secret(self, is_secret):
        if isinstance(is_secret, bool):
            self.__secret = is_secret
        else:
            raise ConnectionError

s = Entry(Emerald, '01.12.2023','Very big and green')


class Archive:
    def __init__(self):
        # список учтённых объектов
        self.__storage = []

    def info(self):
        for item in range(len(self.__storage)):
            print(self.get(item))
    def item(self, index):
        return self.__storage[index].item
    def add(self, entry):
        if isinstance(entry, Entry):
            self.__storage.append(entry)
        else:
            raise ValueError('Not Entry')
    def get(self, index):
        try:
            entry = self.__storage[index]
            if entry == None or entry.secret:
                return None
            else:
                item = entry.item
                result = f'[Запись №{entry.ID}] [Дата создания записи в архиве:{entry.date}] '
                if not entry.info == '':
                    result += f'[Доп. информация: {entry.info}] '
                if str(item) == 'Монета':
                    result += f'[{item}] [Cерийный номер:{item.serial_number}] [Год выпуска:{item.year}] [Номинал:{item.value} руб]'
                    # Обращаемся к item, а не entry, т к мы вызываем класс - Coin и есть item. Т к хотим взять метод класса Coin
                if str(item) == 'Изумруд' or str(item) == 'Скорлупка золотая':
                    result += f'[{item}] Статус :{item.status} Цена :{item.price}'
                return result
        except IndexError:
            return f'Index out of range'

    def edit(self, index, new_info):
        self.__storage[index].info = new_info
    def classify(self, index):
        try:
            entry = self.__storage[index]
            entry.secret = True
        except IndexError:
            return f'Index out of range'
    def declassify(self, index):
        try:
            entry = self.__storage[index]
            entry.secret = False
        except IndexError:
            return f'Index out of range'
    def delete(self, index):
        self.__storage[index] = None
        return self.__storage[index]

archive = Archive()
# a.add(Entry(Coin(1, 2024, 5), '17.08.2024'))
# a.add(Entry(Emerald(), '01.01.2023', 'VBV'))
# a.add(Entry(Shell()))
#
# print(a.edit(1, 'New'))
# a.delete(1)
# print(a.get(1))

for emerald in range(10):
    emerald = Emerald()
    emerald.account()
    archive.add(Entry(emerald))
archive.info()
for shell in range(20):
    shell = Shell()
    shell.account()
    archive.add(Entry(shell))
archive.info()

for i in range(10):
    archive.item(i).store()

for i in range(10,30):
    archive.item(i).process()

archive.info()

for i in range(10,30):
    archive.item(i).smelt()

archive.info()

for i in range(10):
    archive.classify(i)

archive.info()
for i in range(10,30):
    archive.delete(i)

for i in range(5):
    archive.declassify(i)

for i in range(5):
    archive.edit(i, 'New information')

archive.info()

i = 30
try:
    while i<100:
        print(archive.get(i))
        i += 1
except IndexError:
    pass

