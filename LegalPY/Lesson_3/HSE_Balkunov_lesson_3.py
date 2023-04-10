
"""
Задание

1.	Создайте ряд функций для проведения математических вычислений:

●	функция вычисления факториала числа (произведение натуральных чисел от 1 до n). Принимает в качестве аргумента число, возвращает его факториал;

●	поиск наибольшего числа из трёх. Принимает в качестве аргумента кортеж из трёх чисел, возвращает наибольшее из них;

●	расчёт площади прямоугольного треугольника. Принимает в качестве аргумента размер двух катетов треугольника. Возвращает площадь треугольника.
"""
import random
from lesson_2_data import repondents, courts

''' 
def factorial(n):
    answer = 1
    for mnogitel in range (1, n + 1, 1):
        answer = answer * mnogitel
    return answer
    
    
n = int(input())
print(factorial(n))
'''

''' 
def maximum (i):
    x = i[0]
    y = i[1]
    z = i[2]
    if x > y:
        y = x
    if y > z:
        z = y
    return z
    
    
i = (random.randint(1,100), random.randint(1,100), random.randint(1,100))
print(i)
print(maximum(i))
'''
'''
def ploschad (catet_1, catet_2):
    s = (catet_1 * catet_2) / 2
    return s

catet_1, catet_2 = map(int,input(f'Введите значение катетов, обе цифры через пробел: ').split())
print(ploschad(catet_1, catet_2))
'''



def shapka (case_number, defendant):
    #Здесь мы находили нужный суд по коду суда из словаря ответчиков,
    # т.к. у каждого ответчика есть номер дела, в котором содержится
    # код суда

    court_code = case_number.split("-")[0]
    current_court = -1
    for court in courts:
        if court["court_code"] == court_code:
            current_court = court
            break
    if current_court == -1:
        return 'Отсутствуют данные о суде'
    #Теперь нам нужно откорректировать имя суда с учетом падежа и обрезанных данных
    court_name_before = current_court['court_name'].split()
    for i in range(len(court_name_before)):
        if 'арбитраж' in court_name_before[i].lower():
            court_name_before[i] = 'арбитражный'
        if 'суд' in court_name_before[i]:
            court_name_before[i] = 'суд'
    court_name_final = ''
    for word in court_name_before:
        court_name_final = court_name_final + word + ' '
    final_text = f'В {court_name_final} \nАдрес: {current_court["court_address"]}\n\n\
Истец: Пупкин Василий Геннадьевич\nИНН 1236182357 ОГРНИП 218431927812733\n\
Адрес: 123534, г. Москва, ул. Водников, 13\n\n\
Ответчик: {defendant["short_name"]}\n\
ИНН {defendant["inn"]} ОГРН {defendant["ogrn"]}\n\
Адрес: {defendant["address"]}\n\n\
Номер дела {case_number}\n\n'
    return final_text


def all_defendant(defendants):
    for defendant in defendants:
        try:
            print(shapka(defendant['case_number'], defendant))
        except:
            print ("Отсутствуют данные о номере дела по ответчику\n\n")


all_defendant(repondents)


