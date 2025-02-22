import numpy as np


# Task 1
# Дан двумерный массив размером N×N, заполненный случайными числами от
# 1 до 10. Ваша задача — найти максимальное значение в каждом столбце
# и сохранить результаты в одномерный массив.

# Для двумерного массива

str_arr = [[4, 2, 7], [9, 5, 1], [3, 8, 6]]
arr = np.array(str_arr)
max_elem = arr.max(axis=0)
print(max_elem)

# вообще для любого массива который подется с клавиатуры:

# str = input('введите массив, если он двумерный, используйте "[[ ]]. используйте '
#            'запятые как разделитель пожалуйста" \n')
# str = [[4, 2, 7], [9, 5, 1], [3, 8, 6]]
# if '[[' in str and ']]' in str:
#     arr = np.array(ast.literal_eval(str)) # literal_eval() превращает строку в Python-объект (список списков)
# else:
#     str = str.replace("[", "").replace("]", "")
#     arr = np.array(str.split(','), dtype=int)
# max_elem = arr.max(axis=0)
# print(max_elem) # 0 для столбца



# Task 2
# Дан двумерный массив размером  N × M, содержащий оценки студентов
# по нескольким предметам. Ваша задача — найти среднюю оценку
# каждого студента и сохранить результаты в одномерный массив.

# т е среднее арифм каждого массива (строки матрицы) в двумерном массиве

arr = [[8, 7, 9],
       [6, 8, 7],
       [9, 9, 8],
       [7, 6, 8]]

avg_grades = np.average(arr, axis=1) # по строкам
# print(avg_grades)
list_avg_grades = [int(x) if x.is_integer() else float(x) for x in avg_grades]
print(list_avg_grades)



# Task 3
# Дан двумерный массив размером N × M, содержащий данные о продажах
# товаров в разных магазинах. Ваша задача — найти общий объем продаж в
# каждом магазине и сохранить результаты в одномерный массив.

arr = [[10, 15, 20],
       [5, 25, 15],
       [30, 10, 5]]

list_of_sum = np.sum(arr, axis=1).tolist() # по строкам
print(list_of_sum)



# Task 4
# Напишите программу, которая находит наиболее часто встречающееся значение в одномерном массиве.

arr1 = np.array([1,2,3,4,1,1])
arr2 = np.array([2,2,3,4,2,2])
arr3 = np.array([3,2,3,4,1,1])

elems, el_count = np.unique(arr1, return_counts=True)
print(elems[np.argmax(el_count)]) # np.argmax(el_count) — находит индекс максимального элемента
                                  # в el_count, то есть индекс самого частого элемента.


# Task 5
# У вас есть двумерный массив, представляющий собой матрицу, в которой каждый элемент обозначает
# высоту точки на ландшафте. Напишите программу, которая находит самую низкую точку на этом
# ландшафте и определяет, сколько раз эта высота встречается в матрице.

arr = [[10, 15, 20],
       [5, 25, 15],
       [30, 10, 5]]

uniq_coord, coord_counter = np.unique(arr, return_counts=True)
print(f"Самая низкая точка на этом ландшафте: {uniq_coord[0]}, встречается {coord_counter[0]} раз(а).")



# Task 6
# Магический квадрат — это квадратная матрица, в которой сумма элементов
# каждой строки, каждого столбца и каждой из двух диагоналей одинакова.
# Напишите программу, которая проверяет, является ли двумерный массив магическим квадратом

arr2 = [[10, 10, 10],
       [10, 10, 10],
       [10, 10, 10]]

def magick_square(D2_array):
       main_diag_sum = np.sum(np.diagonal(D2_array))
       not_main_diag_sum = np.sum(np.diagonal(np.fliplr(D2_array)))  # меняет матрицу np.fliplr
       string_sums = np.sum(D2_array, axis=1)  # строка
       column_sums = np.sum(D2_array, axis=0)  # столбец
       if (
               np.all(string_sums == main_diag_sum) and
               np.all(column_sums == main_diag_sum) and
               main_diag_sum == not_main_diag_sum
       ):
              return "Magic square!"
       return "Not magic square!"

print(magick_square(arr2))
