# Task 1
class Employee:
    def __init__(self, name, employee_id, position, mail):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.mail = mail

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Mail: {self.mail}")

    def generate_email(self):
        email = f"{self.name.lower().replace(' ', '.')}.{self.employee_id}@company.com"
        return email

    def send_email(self, recipient, subject, message):
        print(f"Sending email to {recipient}:\nSubject: {subject}\nMessage: {message}")


# Какому принципу противорчит данный код?

# Ответ:
# Данный код противрочит принципу единственной ответственности
# (Single responsibility principle)






# Task 2
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'FAV':
            return self.price * 0.2


# Вдруг, вы решаете добавить скидку 40% для VIP клиентов. Каким образом вы это сделаете?

class Vip_Discount(Discount):
    def __init__(self, customer, price):
        super().__init__(customer, price)

    def give_discount(self):
        super().give_discount()
        if self.customer == 'VIP':
            return self.price * 0.4


vip1 = Vip_Discount('VIP', 7500)
print(vip1.give_discount())  # 3000.0





# Task 3
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2


def calculate_total_area(shapes):
    return sum(shape.area() for shape in shapes)


rectangle = Rectangle(4, 5)
square = Square(3)
print(calculate_total_area([rectangle, square]))  # 29






# Task 4
from abc import ABC, abstractmethod


class Bird:
    @abstractmethod
    def walk(self):
        print('Животное идет')

    @abstractmethod
    def fly(self):
        print('Животное летит')

    @abstractmethod
    def swim(self):
        print('Животное плывет')


class Crow(Bird):
    def walk(self):
        print('Ворона идет')

    def fly(self):
        print('Ворона летает')

    def swim(self):
        raise NotImplementedError('Ворона не умеет плавать')


class Penguin(Bird):
    def walk(self):
        print('Пингвин идет')

    def swim(self):
        print('Пингвин плывет')

    def fly(self):
        raise NotImplementedError('Пингвин не умеет летать')


p1 = Penguin()
p1.walk()
# p1.fly()


# 2 вариант
from abc import ABC, abstractmethod


class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Crow(Walkable, Flyable):
    def walk(self):
        pass

    def fly(self):
        pass


class Penguin(Walkable, Swimmable):
    def walk(self):
        pass

    def swim(self):
        pass






# Task 5
from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Lamp(Device):
    def turn_on(self):
        print(f'Lamp turned on')

    def turn_off(self):
        print(f'Lamp turned off')


class MotionSensor(Device):
    def turn_on(self):
        print(f'Motion sensor turned on')

    def turn_off(self):
        print(f'Motion sensor turned off')


class Thermostat(Device):
    def turn_on(self):
        print(f'Thermostat turned on')

    def turn_off(self):
        print(f'Thermostat turned off')


class SmartHome(Device):
    def __init__(self, devices):
        self.devices = devices

    def turn_on(self):
        for device in self.devices:
            device.turn_on()

    def turn_off(self):
        for device in self.devices:
            device.turn_off()


# Создаем экземпляры устройств
lamp = Lamp()
motion_sensor = MotionSensor()
thermostat = Thermostat()

# Создаем экземпляр умного дома и передаем ему список устройств
smart_home = SmartHome([lamp, motion_sensor, thermostat])

# print(smart_home.List_of_devices)

# Включаем все устройства
smart_home.turn_on()
# Вывод:
# Lamp turned on
# Motion sensor turned on
# Thermostat turned on

# Выключаем все устройства
smart_home.turn_off()
# Lamp turned off
# Motion sensor turned off
# Thermostat turned off






# Task 6

class Transfer(ABC):
    @abstractmethod
    def transfer(self, destination_account, amount):
        pass


class Transferable(Transfer):
    def __init__(self, source_account, destination_account):
        self.source_account = source_account
        self.destination_account = destination_account
    def transfer(self, destination_account, amount):
        self.source_account.transfer(self.destination_account, amount)


class Account(Transferable):
    '''банковский счет'''
    def __init__(self, account_number, balance):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError('Недостаточно средств на счету')

    def get_balance(self):
        return self.balance

    def transfer(self, destination_account, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            destination_account.deposit(amount)
        else:
            raise ValueError('Недостаточно средств на счету отправителя')

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return (self.interest_rate/100) * self.balance

    def get_interest_rate(self):
        return self.interest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance, fee_percentage):
        super().__init__(account_number, balance)
        self.fee_percentage = fee_percentage

    def deduct_fees(self):
        fee = self.balance * (self.fee_percentage/100)
        if self.balance >= fee:
            self.balance -= fee
        else:
            raise ValueError('Недостаточно средств')

    def get_fee_percentage(self):
        return self.fee_percentage

class Bank:
    def __init__(self):
        self.List_of_Accounts = []
    def add_account(self, account):
        if account not in self.List_of_Accounts:
            if isinstance(account, Account):
                self.List_of_Accounts.append(account)
        else:
            raise ValueError
    def remove_account(self, number):
        for account in self.List_of_Accounts:
            if account.account_number == number:
                self.List_of_Accounts.remove(account[number])
        else:
            print(f'Элемента с id [{number}] в банке нет')

    def transfer_funds(self, source_account_number, destination_account_number, amount):
        for account in self.List_of_Accounts:
            if account.account_number == source_account_number:
                account.withdraw(amount)
        for account in self.List_of_Accounts:
            if account.account_number == destination_account_number:
                account.deposit(amount)



# 2 вариант:

#     def find_account(self, account_number):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account
#         return None

# def transfer_funds(self, source_account_number, destination_account_number, amount):
#         source_account = self.find_account(source_account_number)
#         destination_account = self.find_account(destination_account_number)
#
#         if source_account and destination_account:
#             transfer_service = TransferService(source_account, destination_account)
#             transfer_service.transfer(amount)
#         else:
#             raise ValueError("Source or destination account not found")


# Создаем экземпляры счетов
savings_account = SavingsAccount(account_number="SAV-001", balance=1000, interest_rate=5)
checking_account = CheckingAccount(account_number="CHK-001", balance=500, fee_percentage=2)

# Создаем экземпляр банка и добавляем счета
bank = Bank()
bank.add_account(savings_account)
bank.add_account(checking_account)

# Выводим балансы счетов
print("Savings Account Balance:", savings_account.get_balance())
print("Checking Account Balance:", checking_account.get_balance())
# Savings Account Balance: 1000
# Checking Account Balance: 500

# Переводим деньги со счета-источника на счет-назначение
bank.transfer_funds(source_account_number="SAV-001", destination_account_number="CHK-001", amount=500)

# Выводим обновленные балансы счетов
print("Savings Account Balance:", savings_account.get_balance())
print("Checking Account Balance:", checking_account.get_balance())
# Savings Account Balance: 500
# Checking Account Balance: 1000