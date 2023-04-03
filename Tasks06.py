# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_el = int(input("Введите первый элемент: "))
diff = int(input("Разность: "))
arr_size = int(input("Количество элементов: "))

arr_new = []
for i in range(arr_size):
    first_el + i * diff
    arr_new.append(first_el + i * diff)
print(arr_new)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
input_arr = [random.randint(1, 30) for _ in range(10)]
print(input_arr)
start = int(input("Начало диапазона: "))
finish = int(input("Конец диапазона: "))
index_arr = []

for i in range(len(input_arr)):
    if input_arr[i] >= start and input_arr[i] <= finish:
        index_arr.append(i)
print(index_arr)