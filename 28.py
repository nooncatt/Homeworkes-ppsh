from abc import ABC, abstractmethod
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display(self):
        pass

class Autobiography(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в '
              f'автобиографическом жанре. Автор - {self.author}')

class Psychology(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в '
              f'жанре психологии. Автор - {self.author}')


class Fantasy(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в'
              f' жанре фэнтези. Автор - {self.author}')

book1 = Autobiography('К черту все! Берись и делай!', 'Ричард Брэнсон')
book2 = Psychology('Биология добра и зла', 'Роберт Сапольски')
book3 = Fantasy('Песнь льда и пламени', 'Джордж Реймонд Ричард Мартин')

book1.display()
book2.display()
book3.display()




# Task 2
class Bird:
  def feed(self):
      print('Feeding bread crumbs')

class Swan(Bird):
  def feed(self):
      print('Feeding the swan bread crumbs')

class Duck(Bird):
  def feed(self):
      print('Feeding the duck bread crumbs')

class Mouse:
  def feed(self):
      print('Feeding the mouse bread crumbs')

def feed(bird: Bird):
  bird.feed()

feed(Duck())
feed(Mouse())



# Task 3

class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Давайте разбираться вместе!')

class Student(Human):
    def __init__(self, name):
        super().__init__(name)

    def ask_question(self, person, question):
        print(f'{person.name}, {question}')
        person.answer_question(question)
        print()

class Teacher(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if question == 'как войти в айти?':
            print('Можешь начать осваивать программирование с ППШ')
        elif question == 'как научится программировать?':
            print('Сейчас расскажу')
        else:
            super().answer_question(question)

class Mentor(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if question == 'как повысить эффективность работы?':
            print('Важно соблюдать три правила')
        else:
            super().answer_question(question)

class CodeReviewer(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if question == 'я усовершенствовал свой код. Вы проверите?':
            print('Проверил. Замечательный вариант решения. Вы отлично справились!')
        else:
            super().answer_question(question)

class Curator(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if question == 'как додуматься до этого решения?':
            print('Сейчас опишу ход мыслей при решении задачи')
        else:
            super().answer_question(question)


student1 = Student('Ваня')
teacher = Teacher('Александр Романович')
mentor1 = Mentor('Илья')
curator1 = Curator('Владимир')
reviewer1 = CodeReviewer('Евгений')

student1.ask_question(teacher, 'как войти в айти?')
student1.ask_question(teacher, 'как научится программировать?')
student1.ask_question(mentor1, 'как повысить эффективность работы?')
student1.ask_question(curator1, 'как додуматься до этого решения?')
student1.ask_question(reviewer1, 'я усовершенствовал свой код. Вы проверите?')




# Task 4
class GeometricFigures(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass
    def __str__(self):
        return f'Геометрическая фигура'
class Triangle(GeometricFigures):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return f'Периметр равен: {self.a + self.b + self.c}\n'
    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c}.'

class Square(GeometricFigures):
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return f'Периметр равен: {self.a * 4}\n'
    def __str__(self):
        return f'Квадрат со стороной {self.a}.'


class Rectangle(GeometricFigures):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def get_perimeter(self):
        return f'Периметр равен: {self.h * 2 + self.w * 2}\n'
    def __str__(self):
        return f'Прямоугольник со сторонами {self.h}, {self.w}.'

figures = [Triangle(1, 2, 3), Triangle(4, 5, 6),
            Square(10), Square(20),
            Rectangle(6, 7), Rectangle(7, 8)]

for figure in figures:
    print(figure, figure.get_perimeter())





# Task 5
from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def vote_command(self):
        pass
    @abstractmethod
    def gesture_command(self):
        pass

class Lock(ABC):
    @abstractmethod
    def close_lock(self):
        pass
    @abstractmethod
    def open_lock(self):
        pass

class SmartAssistant(Command):
    def vote_command(self):
        print(f'Умный помощник распознал голосовую команду\n')
    def gesture_command(self):
        print(f'Умный помощник распознал жестовые команды\n')


class SmartCamera(Command, Lock):
    def close_lock(self):
        print(f'Умная камера закрыла замок входной двери\n')
    def open_lock(self):
        print(f'Умная камера открыла замок входной двери\n')
    def vote_command(self):
        print(f'Умная камера распознала голосовую команду\n')
    def gesture_command(self):
        print(f'Умная камера распознала жестовые команды\n')
class SmartLock(Lock):
    def close_lock(self):
        print(f'Умный замок закрыл входную дверь\n')
    def open_lock(self):
        print(f'Умный замок открыл входную дверь\n')


sa = SmartAssistant()
sa.vote_command()
sa.gesture_command()

sc = SmartCamera()
sc.open_lock()
sc.close_lock()
sc.vote_command()
sc.gesture_command()

sl = SmartLock()
sl.open_lock()
sl.close_lock()





# 2 вариант
from abc import ABC, abstractmethod


class Lock(ABC):
    @abstractmethod
    def close_lock(self):
        pass

    @abstractmethod
    def open_lock(self):
        pass


class Command(ABC):
    @abstractmethod
    def vote_command(self):
        pass

    @abstractmethod
    def gesture_command(self):
        pass


class SmartAssistant(Command):

    def close_lock(self):
        raise NotImplementedError('Умный помощник не может выполнить данную команду')

    def open_lock(self):
        raise NotImplementedError('Умный помощник не может выполнить данную команду')

    def vote_command(self):
        print('Умный помощник распознал голосовую команду')

    def gesture_command(self):
        print('Умный помощник распознал жестовые команды')


class SmartCamera(Lock, Command):

    def close_lock(self):
        print('Умная камера закрыла замок входной двери')

    def open_lock(self):
        print('Умная камера открыла замок входной двери')

    def vote_command(self):
        print('Умная камера распознала голосовую команду')

    def gesture_command(self):
        print('Умная камера распознала жестовые команды')


class SmartLock(Lock):

    def close_lock(self):
        print('Умный замок закрыл входную дверь')

    def open_lock(self):
        print('Умный замок открыл входную дверь')

    def vote_command(self):
        raise NotImplementedError('Умный помощник не может выполнить данную команду')

    def gesture_command(self):
        raise NotImplementedError('Умный помощник не может выполнить данную команду')