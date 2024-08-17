# Task 1
def infiltrate():
    # здесь Пётр позже напишет код
    pass


class SignedMessage:
    def __new__(cls, *args, **kwargs):
        infiltrate()
        return object.__new__(cls)

    def __init__(self, message=str(), signature='Noname'):
        self.message = message
        self.signature = signature

    def __str__(self):
        return f'{self.message} {self.signature}'

    def __add__(self, other):
        if isinstance(other, SignedMessage):
            return f'{self.message} {other}'
        return f'{self.message} {other} {self.signature}'


SIGNATURE = '-~=$([{PETR}])$=~-'
print(SignedMessage("Hello ", SIGNATURE))
print(SignedMessage("world!", SIGNATURE))

print(SignedMessage("Hello ", SIGNATURE) + SignedMessage("world!", SIGNATURE))
# Hello  world! -~=$([{PETR}])$=~-
print(SignedMessage("Hello ", SIGNATURE) + "world!")  # Hello  world! -~=$([{PETR}])$=~- !





# Task 2

import math


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector3(-self.x, -self.y)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return math.sqrt(sum(list(map(lambda x: x ** 2, self.coords))))

    def __len__(self):
        return math.sqrt(sum(list(map(lambda x: x ** 2, self.coords))))

    def __str__(self):
        return f'{self.coords}'

    def __eq__(self, other):
        if self.coords == other.coords:
            return True
        return False

    def __ne__(self, other):
        if self.coords != other.coords:
            return True
        return False

    def __mul__(self, other):
        a = []
        for i in range(2):
            a.append(self.coords[i] * other.coords[i])
        return tuple(a)


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.coords = (self.x, self.y, self.z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __abs__(self):
        return math.sqrt(sum(list(map(lambda x: x ** 2, self.coords))))

    def __len__(self):
        return math.sqrt(sum(list(map(lambda x: x ** 2, self.coords))))

    def __str__(self):
        return f'{self.coords}'

    def __eq__(self, other):
        if self.coords == other.coords:
            return True
        return False

    def __ne__(self, other):
        if self.coords != other.coords:
            return True
        return False

    def __mul__(self, other):
        a = []
        for i in range(3):
            a.append(self.coords[i] * other.coords[i])
        return tuple(a)



print((Vector3(1, 2, 3) + Vector3(3, 4, 5)).coords)
# (4, 6, 8)
print((-Vector3(1, 0, -1)).coords)
# (-1, 0, 1)
print((Vector3(7, 7, 7) - Vector3(3, 2, 1)).coords)
# (4, 5, 6)
print(abs(Vector3(3, 4, 0)))  # 5.0
# print(len(Vector3(3, 4, 0)))
print(str(Vector3(0, 5, 2)))
# (0, 5, 2)
print((Vector3(0, 5, 2) == Vector3(7, 7, 7)))
# False
print((Vector3(0, 5, 2) == Vector3(0, 5, 2)))
# True
print((Vector3(0, 5, 2) != Vector3(7, 7, 7)))
# True
print((Vector3(0, 5, 2) * Vector3(7, 7, 7)))
# (0, 35, 14)




# Task 3
from random import randint

RARITY = [0, 1, 2, 3]
class Item:
    def __init__(self, ID, price, rarity, color):
        self.ID = ID
        self.price = price
        self.rarity = rarity
        self.color = color
        self.all_parametrs = [self.ID, self.price, self.rarity, self.color]
    def __lt__(self, other):
        if self.ID < other.ID:
            return True
        if self.ID > other.ID:
            return False
        if self.price < other.price:
            return True
        if self.price > other.price:
            return False
        if self.rarity > other.rarity:
            return True
        if self.rarity < other.rarity:
            return False
        if self.color > other.color:
            return True
        if self.color < other.color:
            return False
        return False
    def __le__(self, other):
        return not self > other
    def __gt__(self, other):
        return not self < other or self == other
    def __ge__(self, other):
        return not self < other
    def __ne__(self, other):
        return not self == other
    def __eq__(self, other):
        return (self.ID == other.ID and self.price == other.price and
                self.rarity == other.rarity and self.color == other.color)
    def __str__(self):
        return f"[{self.ID}] {self.price}$ {RARITY[self.rarity]} #{self.color}"


new_item = Item(128, 500, 1, "FF0000")

def generate_item():
    return Item(randint(0, 12),
                randint(0, 1) * 100,
                randint(0, 3),
                hex(randint(0, 16) * 1000000)[2:].zfill(6).upper())

#
# item =[]
# for i in range(100):
#     items = generate_item().all_parametrs
#     item.append(items)
# item.sort()
# print(*item, sep ='\n')

items = [generate_item() for i in range(256)]
items.sort()
print(*items, sep="\n")