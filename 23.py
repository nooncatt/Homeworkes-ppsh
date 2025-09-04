# Task 1
class CoffeeMachine:
    water_level = 0
    coffee_level = 0
    milk_level = 0
    sugar_level = 0
    cups = 0

    def __init__(self, water_level, coffee_level, milk_level, sugar_level=0, cups=0):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.cups = cups

    def add_water(self, amount):
        self.water_level += amount

    def add_coffee(self, amount):
        self.coffee_level += amount

    def add_milk(self, amount):
        self.milk_level += amount

    def add_sugar(self, amount):
        self.sugar_level += amount

    def add_cups(self, number):
        self.cups += number

    def check_resources(self):
        if self.water_level >= 240 and self.coffee_level >= 16 and self.milk_level >= 180 and self.sugar_level >= 2 and self.cups >= 1:
            return True
        else:
            return False

    def make_coffee(self):
        if self.check_resources() is True:
            self.water_level -= 240
            self.coffee_level -= 16
            self.milk_level -= 180
            self.sugar_level -= 2
            self.cups -= 1
            return f'Кофе готов!'
        else:
            return f'Недостаточно ингредиентов!'


cup1 = CoffeeMachine(250, 60, 200, 2, 1)
print(cup1.make_coffee())




# Task 2
class PhotoCamera:
    def __init__(self, brand, model, resolution=(0, 0), is_on='False', memory_capacity=32, photos=0):
        self.brand = brand
        self.model = model
        self.resolution = resolution
        self.is_on = is_on
        self.memory_capacity = memory_capacity
        self.photos = photos

    def take_photo(self):
        if self.is_on == 'True':
            self.photos += 1
            return f'Сделана фотография с разрешением [{self.resolution[0]}]x[{self.resolution[1]}].'
        else:
            return f'Камера {self.brand} {self.model} выключена. Включите камеру.'

    def get_camera_info(self):
        return f'Марка: [{self.brand}], Модель: [{self.model}], Разрешение: [{self.resolution[0]}]x[{self.resolution[1]}].'

    def turn_on(self):
        self.is_on = 'True'
        return f'Фотокамера включена.'

    def turn_off(self):
        self.is_on = 'False'
        return f'Фотокамера выключена.'

    def is_camera_on(self):
        if self.is_on == 'True':
            return f'Да включена'
        elif self.is_on == 'False':
            return f'Нет, выключена'

    def store_photo(self, photo=1):
        if self.photos + photo <= self.memory_capacity:
            self.photos += photo
            return True
        else:
            return False

    def view_photos(self):
        return f'{self.photos} фотографий сохранено в памяти фотокамеры'

    def clear_memory(self):
        self.photos = 0
        return f'Теперь в памяти фотокамеры {self.photos} фотографий. Память очищена.'


cam1 = PhotoCamera('instax', 'mini 12', (1800, 640), 'False', 64, 12)
print(cam1.take_photo())
print(cam1.get_camera_info())
print(cam1.turn_on())
print(cam1.take_photo())
print(cam1.turn_off())
print(cam1.is_camera_on())
print(cam1.store_photo())
print(cam1.view_photos())
print(cam1.clear_memory())




# Task 3
class Revolver:
    def __init__(self):
        self.drum_slot = []
        self.drum_slot_len = len(self.drum_slot)
        self.drum_slot_max_len = 6
    def add_bullet(self, bullet=1):
        if self.drum_slot_len + 1 <= self.drum_slot_max_len:
            self.drum_slot_len +=1
            self.drum_slot.append(bullet)
            return True
        else:
            return False

    def add_bullets_from_list(self, list):
        if len(list) == 0:
            return False
        else:
            if len(list) + self.drum_slot_len <= self.drum_slot_max_len:
                for bullet in list:
                    self.drum_slot.append(bullet)
                    self.drum_slot_len +=1
                return True
            else:
                return f'Вы хотите добавить больше патронов, чем возможно'
    def shoot(self, bullet):
        iter_bullet = iter(self.drum_slot)
        for bull in self.drum_slot:
            if bullet == bull:
                self.drum_slot.remove(bull)
                self.drum_slot_len -=1
                try:
                    next_place = next(iter_bullet)
                except StopIteration:
                    return None
                return f'Удалиил патрон номер {bull} из револьвера и переместились на место {next_place} патрона'
            else:
                next_place = next(iter_bullet)
            if bullet not in self.drum_slot:
                return None
    def unload(self, all_items=False, bullet=None):
        if all_items == 'True':
            self.drum_slot = []
            self.drum_slot_len = 0
            return self.drum_slot
        elif all_items == 'False':
            bullet = int(input('Какой патрон удалим?'))
            try:
                self.drum_slot.remove(bullet)
                self.drum_slot_len -=1
            except ValueError:
                return None
            return f'Остались {self.drum_slot} патроны'
    def scroll(self):
        import random
        bullet = random.randint(1, self.drum_slot_len + 1)
        if bullet in self.drum_slot:
            print('Вы убиты')
        return f'Выпал {bullet} слот в барабане'
    def bullet_count(self):
        return f'Количество патронов {self.drum_slot_len}'




gun = Revolver()
print(gun.__dict__)
print(gun.add_bullet())
print(gun.add_bullets_from_list([2, 3, 4, 5, 6]))
print(gun.__dict__)
print(gun.shoot(3))
print(gun.__dict__)
print(gun.unload('False', 2))
print(gun.scroll())
print(gun.bullet_count())