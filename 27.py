# Task 1
class HeavenlyBody:
    '''Родительский класс HeavenlyBody'''

    def __init__(self, name, age, temperature, radius):
        self.name = name
        self.age = age
        self.temperature = temperature
        self.radius = radius

    def display(self):
        print(f'Название: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Температура: {self.temperature}')
        print(f'Радиус объекта: {self.radius}')


class Planet(HeavenlyBody):
    '''Дочерний класс Planet'''

    def __init__(self, name, age, temperature, radius, orbital_speed):
        self.orbital_speed = orbital_speed
        super().__init__(name, age, temperature, radius)

    def display(self):
        super().display()
        print(f'Орбитальная скорость: {self.orbital_speed}\n')


class Star(HeavenlyBody):
    '''Дочерний класс Star'''

    def __init__(self, name, age, temperature, radius, constellation):
        super().__init__(name, age, temperature, radius)
        self.constellation = constellation

    def display(self):
        super().display()
        print(f'Созвездие: {self.constellation}\n')


planet1 = Planet('Земля', 4540, '16.92', 6371, '29.8')
star1 = Star('Полярная звезда', 60, '5500', 47, 'Малая Медведица')

print(Planet.__doc__, end='\n')
planet1.display()

print(Star.__doc__, end='\n')
star1.display()




# Task 2
import datetime


class Pastry:
    '''Кондитерская'''
    _number_of_order = 0

    def __init__(self, name, price, manufacture_date, term):
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
        self.term = term

    def display(self):
        print(f'Название: {self.name}')
        print(f'Цена: {self.price} (руб.)')
        print(f'Дата изготовления: {self.manufacture_date}')

    def valid_until(self):
        today = datetime.date.today()
        delta = datetime.timedelta(days=self.term)
        end_term = self.manufacture_date + delta
        right_time = end_term - today
        if right_time.days > 0:
            print(f'Срок годности истекает через {right_time.days} дня')
            return True
        else:
            return False


class Cake(Pastry):
    def __init__(self, name, price, manufacture_date, term, filling):
        super().__init__(name, price, manufacture_date, term)
        self.filling = filling

    def display(self):
        print(f'Начинка: {self.filling}')
        print(f'Оформлен заказ {Pastry._number_of_order} - Торт с начинкой {self.filling}\n')

    def order(self):
        Pastry.display(self)
        if self.valid_until():
            Pastry._number_of_order += 1
            return self.display()
        else:
            return f'Товар просрочен. Заказ сделать нельзя. Выберите другое изделие \n'


class BentoCake(Pastry):
    def __init__(self, name, price, manufacture_date, term, celebration):
        self.celebration = celebration
        super().__init__(name, price, manufacture_date, term)

    def display(self):
        print(f'Праздник:: {self.celebration}')
        print(f'Оформлен заказ {Pastry._number_of_order} - Бенто торт на {self.celebration}\n')

    def order(self):
        Pastry.display(self)
        if self.valid_until():
            Pastry._number_of_order += 1
            return self.display()
        else:
            print(f'Товар просрочен. Заказ сделать нельзя. Выберите другое изделие \n')


cake1 = Cake('Торт', 1300, datetime.date(2024, 8, 20), 3, 'вишня')
bento1 = BentoCake('Бенто торт', 1000, datetime.date(2024, 8, 20), 4, 'день рождения')
bento2 = BentoCake('Бенто торт', 1500, datetime.date(2024, 8, 16), 5, 'день рождения')

cake1.order()
bento1.order()
bento2.order()





# Task 3
class BankAccount:
    transactions = []

    def __init__(self, holder, balance, interest_rate):
        self.__holder = holder
        self._balance = balance
        self._interest_rate = interest_rate

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, new_holder):
        self.__holder = new_holder

    def __str__(self):
        print(f'Владелец: {self.__holder}')
        print(f'Баланс: ${"{:,}".format(self._balance)}')
        print(f'Процентная ставка: {self._interest_rate}\n')


class BankOperation(BankAccount):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)
        self.__ID = id(self)

    def deposit(self, amount):
        self._balance += amount
        ph = f'Аккаунт {self.__ID} - внесение наличных на счет: ${"{:,}".format(amount)}'
        BankAccount.transactions.append(ph)

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            ph = f'Аккаунт {self.__ID} - cнятие наличных: ${"{:,}".format(amount)}'
            BankAccount.transactions.append(ph)
        else:
            print(f'Аккаунт {self.__ID} - недостаточно средств на счете')

    def add_interest(self):
        rate = self._balance * self._interest_rate
        self._balance += rate
        ph = f'Аккаунт {self.__ID} - начислены проценты по вкладу: ${"{:,}".format(rate)}'
        BankAccount.transactions.append(ph)

    @classmethod
    def history(cls):
        for ph in cls.transactions:
            print(ph)


account = BankOperation('Warren Buffett', 113000000000, 0.08)
account.__str__()
account.deposit(4000000000)
account.withdraw(88000000000)
account.add_interest()
account.history()





# Task 4
# 1) Мы исп-ли super(), кот возвр-ся к родительскому классу.
# У принтера и сканера он общий, поэтому вызвался один раз.
# 2) Она последовательно идет по каждому init





# Task 5
class Investments:
    '''Ценные бумаги'''
    def __init__(self, ticker, price, currency, industry):
        # тикер, цена, валюта, сектор
        self.ticker = ticker
        self.price = price
        self.currency = currency
        self.industry = industry
    def display(self):
        print(f'Тикер: {self.ticker}')
        print(f'Цена: {self.price}')
        print(f'Валюта: {self.currency}')
        print(f'Сектор: {self.industry}')


def buying_securities(func):
    def insight_func(self):
        if self.echelon == 3:
            print('Это высокорискованная сделка')
        func(self)
    return insight_func


class Shares(Investments):
    def __init__(self, ticker, price, currency, industry, dividend, echelon, profit):
        super().__init__(ticker, price, currency, industry)
        # дивиденды, эшелон, годовая доходность
        self.dividend = dividend
        self.echelon = echelon
        self.profit = profit

    @buying_securities
    def buying(self):
        if self.profit >= 0.05:
            n = int(input('Введите количество лотов\n'))
            print(f'Количество: {n}')
            print(f'Совершена покупка на сумму: {self.price * n}. Поздравляю, Вы стали совладельцем компании!\n')
        else:
            print('Это высокорискованная сделка \n')



class Bonds(Investments):
    def __init__(self, ticker, price, currency, industry, coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry)
        # купоны, эшелон, номинальная стоимость
        self.coupon = coupon
        self.echelon = echelon
        self.nominal = nominal

    # @staticmethod
    # def buying_securities(func):
    #     def insight_func(self):
    #         if self.echelon == 3:
    #             print('Это высокорискованная сделка')
    #         func(self)
    #     return insight_func
    @buying_securities
    def buying(self):
        if self.price <= self.nominal:
            n = int(input('Введите количество лотов\n'))
            print(f'Количество: {n}')
            print(f'Совершена покупка на сумму: {self.price * n}. Поздравляю, Вы стали кредитором компании!\n')
        else:
            print('Это высокорискованная сделка \n')


print(' ')
i1 = Shares('GAZP', 174, 'RUB', 'Энергетика', True, 1, 6)
i1.display()
i1.buying()
i2 = Bonds('ОФЗ-26233', 688, 'RUB', 'Государственные', 6, 1, 1000)
i2.display()
i2.buying()