# Task 1
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(5)) # 120




# Task 2
def divisors(n):
    d = [x for x in range(1, n + 1) if n % x == 0]
    return d


def is_prime(n):
    if len(divisors(n)) == 2:
        return True
    else:
        return False


print(is_prime(5)) # True




# Task 3
# которая принимает список целых чисел и возвращает новый список, содержащий только нечетные числа.
# Для решения задачи используйте функцию filter и lambda-функцию.


f = lambda x: True if x % 2 != 0 else False


def filter_odd(numbers):
    answer = list(filter(f, numbers))
    return answer


print(filter_odd([1, 2, 3, 4, 5, 5])) # [1, 3, 5, 5]




# Task 4
# Для решения задачи используйте функцию map и lambda-функцию

f = lambda x: x ** 2


def map_square(numbers):
    return list(map(f, numbers))


print(map_square([1, 2, 3, 4, 5])) # [1, 4, 9, 16, 25]




# Task 5
# Напишите функцию reduce_sum, которая принимает список чисел и возвращает сумму этих чисел.
# Для решения задачи используйте функцию reduce из модуля functools и lambda-функцию.
from functools import reduce

g = lambda x, y: x + y


def reduce_sum(numbers):
    answer = reduce(g, numbers)
    return answer


print(reduce_sum([1, 2, 3, 4, 5, 6, 7])) # 28




# Task 6

f = lambda x, y: x ** y


def partial_apply(func, x, y=2):
    return func(x, y)


print(partial_apply(f, 11)) # 121




# Task 7

def compose(func1, func2):
    def h(x):
        return f(g(x))


f = lambda x: x ** 2
g = lambda x: x + 1

fg = compose(f, g)

print(fg(2)) # 121



# Task 8

def create_function_with_arguments(func, arguments):
    new_func = func(arguments)
    return new_func


f = lambda x: x * 2

print(create_function_with_arguments(f, [1, 2, 3, 4])) # [1, 2, 3, 4, 1, 2, 3, 4]




# Task 9

def compose_functions(functions):
    def composed_function(x, L = functions):
        if len(L) == 1:
            return L[0](x)
        else:
            return L[0](composed_function(x, L[1:]))

    return composed_function


f1 = lambda x: x ** 2
f2 = lambda x: x ** 3
f3 = lambda x: x + 1

comp = compose_functions([f1, f2, f3])
print(comp(2)) # 729
