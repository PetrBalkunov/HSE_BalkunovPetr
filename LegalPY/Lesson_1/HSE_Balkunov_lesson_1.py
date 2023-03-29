a= "Hello, world"
print (a)

a = 10
id(a)

a = 202908346812
print(type(a))

print('А теперь приступим к домашке...')

#number_1 = int(input('Введите число '))

#print (number_1)

#Решаем 1-ую задачку: когда пользователь вводит число, а это число нужно перевести в секунды, минуты и часы

# Устанавливаем фильтр для пользователя на ввод только целых цифр
# и не выпускаем его, пока он не введет данные в нужном формате

while True:
        try:
                get_number = int(input('Введите число '))
                if get_number > 0:
                        print('Спасибо! Вы указали число:' + str(get_number)+
                      '. Сейчас мы быстренько все расчитаем!')
                        break
                else:
                        print('Все ок, только Вы ввели отрицательное число. Попробуйте снова')
                get_number = int(input('Введите число '))

        except ValueError:
                print('Вводить можно только целые и положительные числа. Попробуйте снова')

#Теперь будем переводить введенные цифры как введенные в секундах в часы. В одном часе 3600 секунд.
hours = get_number // 3600
# Теперь посчитаем кол-во минут - сначала отнимем от введенной пользователем цифры кол-во часов,
# и поделим на 60, т.к. в 1 часе 60 минут
minutes = (get_number - hours * 3600) // 60
# Теперь посчитаем кол-во оставшихся секунд -  отнимем от введенной пользователем цифры сумму кол-ва часов,
# умноженных на 3600,+ кол-во минут умноженных на 60, т.к. нужно вернуть данные в исходное состояние.
seconds = get_number - (hours * 3600 + minutes * 60)
#Для вывода используем f строку
print(f"Введенное Вами число составляет:   {hours} часов : {minutes} минут: и {seconds} секунд")


# Решаем 2-ую задачку:
# Запросите у пользователя через консоль число n (от 1 до 9).
# Найдите сумму чисел n + nn + nnn.

# Воспользуемся готовым модулем для ввода данных из предыдущего задания
# И установим фильтр на ввод целых положительных чисел от 1 до 9

import time
time.sleep(7)
print('А теперь немного магии..')
time.sleep(4)
while True:
        try:
                select_number = int(input('Введите число от 1 до 9 '))
                if  10 > select_number >= 1:
                        print('Замечательно! Вы выбрали число:' + str(select_number)+
                      '. Сейчас будет фокус со сложением этого числа!')
                        break
                else:
                        print('Почти получилось. Попробуйте снова выбрать одно из этих чисел: 1, 2, 3, 4, 5, 6. 7, 8, 9')
                select_number = int(input('Введите число от 1 до 9 '))

        except ValueError:
                print('Почти получилось. Попробуйте снова выбрать одно из этих чисел: 1, 2, 3, 4, 5, 6. 7, 8, 9')
#Добавим немного спецэффектов, чтобы было не так скучно и предусмотрим зависание программы для вычислений
print('Следите за моими руками..')
time.sleep(5)


# А теперь само задание. Тут фишка в том, что данные от пользователя должны быть разного типа в одной формуле,
# чтобы можно было сделать вычисления как с числовым значением, так и со строковым значением этиъ данных
focus = (select_number + int(str(select_number) + str(select_number))
+ int(str(select_number) + str(select_number) + str(select_number)))

print(f'Ваше число успело несколько раз преобразиться в число, потом в строку и обратно. Получилось {focus}. Фокус-покус!')





