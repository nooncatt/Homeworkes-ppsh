# Task 1
# Ответ: 3, 1, 2 (или 231 если смотреть от текстов)


# Task 2
# Используя парадигму функционального программирования
def sum_even_numbers(numbers):
    List_of_even_numbers = [x for x in numbers if x % 2 == 0]
    return sum(List_of_even_numbers)


numbers = [14, 93, 19, 38, 18, 51, 77]
print(sum_even_numbers(numbers))


# Task 3
# Используя парадигму императивного программирования

def sum_even_numbers(numbers):
    s = 0
    for numb in numbers:
        if numb % 2 == 0:
            s += numb
    return s


numbers = [60, 84, 9, 49, 7, 85, 38]
print(sum_even_numbers(numbers))
