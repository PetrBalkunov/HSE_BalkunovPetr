a= "Hello, world"
print (a)

a = 10
id(a)

a = 202908346812
print(type(a))



number_1 = int(input('Введите число '))

print (number_1)

#Решаем 1-ую задачку, когда пользователь вводит число, а это число нужно перевести в секунды, минуты и часы

random_number = int(input('Введите число '))
while (not random_number.isdigit()):
    random_number = int(input('Введите число '))
    print()
    if not random_number.isdigit()
        print ('Введите, пожалуйста, любое число, а не текст')
    else:
        print('Спасибо! Сейчас мы быстренько все расчитаем:')