'''
Задание
1.	Сгенерируйте с использованием функции range (случайный шаг от 3 до 5) массив, содержащий отсортированные числа от 10 до 250 млн.

Можно использовать функцию randomint из модуля random для ещё большей рандомизации значений, но для целей работы алгоритма бинарного поиска проследите, чтобы значения в массиве были отсортированы.

2.	Сгенерируйте с помощью list comprehensions и функции randomint (встроенный модуль random) 10 случайных чисел.

3.	Напишите функцию для алгоритма линейного поиска.

4.	Напишите функцию для алгоритма бинарного поиска.

5.	Проверьте наличие ранее сгенерированных случайных чисел в массиве с помощью алгоритмов линейного и бинарного поиска, замерьте время
'''
import random
import time

spisok = list(range(10,250000000,4))
#print(spisok[:7:2])

search_numbers = [random.randint(0, 20000000) for i in range(10)]
#print(search_numbers)

#создаем линейный поиск
def linear_search(spisok,number):
    for i,element_spiska in enumerate(spisok):
        if number == element_spiska:
            return i
    return -1
'''
total_time = 0
for number in search_numbers:
    time_1 = time.time()
    index_in_spisok = linear_search(spisok,number)
    time_2 = time.time()
    element_time = time_2 - time_1
    total_time += element_time
    if index_in_spisok != -1:
        print(f'Элемент найден. Индекс элемента в списке: {index_in_spisok}')
    else:
        print ('Заданное число в списке не найдено')
    print(f'Время поиска элемента в списке составило {element_time}')

print(f'Общее время поиска составило: {round(total_time,3)} секунд')
'''
def binary_search(spisok,number):
    start = 0
    end = len(spisok) - 1
    middle_index = (start + end) // 2
    while True:
        if number > spisok[middle_index]:
            start = middle_index
        elif number < spisok[middle_index]:
            end = middle_index
        else: #если первые два ифа не сработали, то элс, где число равно
            return middle_index
        middle_index = (start + end) // 2
        if end == start + 1:
            return -1


total_time = 0
for number in search_numbers:
    time_1 = time.time()
    index_in_spisok = binary_search(spisok,number)
    time_2 = time.time()
    element_time = time_2 - time_1
    total_time += element_time
    if index_in_spisok != -1:
        print(f'Элемент найден. Индекс элемента в списке: {index_in_spisok}')
    else:
        print ('Заданное число в списке не найдено')
    print(f'Время поиска элемента в списке составило {element_time}')

print(f'Общее время поиска составило: {round(total_time,3)} секунд')

