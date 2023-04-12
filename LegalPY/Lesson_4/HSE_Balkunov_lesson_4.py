'''
Задание

Напишите функцию для валидации ИНН (идентификационного номера налогоплательщика), которая принимает в качестве аргумента строку, содержащую ИНН или просто набор цифр, похожий на ИНН.

Функция возвращает True в случае, если ИНН прошёл проверку, и False, если проверка не пройдена.

Для удобства лучше разбить код на несколько взаимосвязанных функций.

ТЗ составлено с использованием материалов Kholenkov.ru.

ИНН организации состоит из 10 цифр:
●	1-4-я цифры:
○	для российской организации — код налогового органа, который присвоил ИНН;
○	для иностранной организации — индекс, определяемый Федеральной налоговой службой;
●	5-9-я цифры:
○	для российской организации — порядковый номер записи о лице в территориальном разделе Единого государственного реестра налогоплательщиков налогового органа, который присвоил ИНН;
○	для иностранной организации — код иностранной организации (КИО) согласно Справочнику «Коды иностранных организаций»;
●	10-я цифра — контрольное число.

ИНН физического лица (индивидуального предпринимателя) состоит из 12 цифр:
●	1-4-я цифры — код налогового органа, который присвоил ИНН;
●	5-10-я цифры — порядковый номер записи о лице в территориальном разделе Единого государственного реестра налогоплательщиков налогового органа, который присвоил ИНН;
●	11-12-я цифры — контрольное число.

Алгоритм проверки ИНН организации (10 знаков)

1.	Вычисляется контрольная сумма со следующими весовыми коэффициентами: (2, 4, 10, 3, 5, 9, 4, 6, 8, 0), т. е. необходимо вычислить сумму произведений цифр ИНН (с 1-й по 9-ю) на следующие коэффициенты — [2, 4, 10, 3, 5, 9, 4, 6, 8]:

2 * inn[0] + 4 * inn[1] + .... +  8 * inn[9]

2.	Вычисляется контрольное число как остаток от деления контрольной суммы на 11 (оператор деления по модулю %).
3.	Если контрольное число больше 9, то контрольное число вычисляется как остаток от деления контрольного числа на 10

4.	Контрольное число проверяется с десятым знаком ИНН. В случае их равенства ИНН считается правильным.

Алгоритм проверки ИНН физического лица и ИП (12 знаков)

1.	Необходимо вычислить сумму произведений цифр ИНН (с 1-й по 10-ю) на следующие коэффициенты — [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]:

7 * inn[0] + 2 * inn[1] + .... +  8 * inn[9]

2.	Вычисляется первое контрольное число как остаток от деления контрольной суммы на 11. Если контрольное число больше 9, то контрольное число вычисляется как остаток от деления контрольного числа на 10

3.	Необходимо вычислить сумму произведений цифр ИНН (с 1-й по 11-ю) на следующие коэффициенты — [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]:

3 * inn[0] + 7 * inn[1] + .... +  8 * inn[10]

4.	Вычисляется второе контрольное число как остаток от деления контрольной суммы на 11. Если контрольное число больше 9, то контрольное число вычисляется как остаток от деления контрольного числа на 10

5.	Первое контрольное число проверяется с одиннадцатым знаком ИНН, а второе контрольное число проверяется с двенадцатым знаком ИНН. В случае их равенства ИНН считается правильным.
'''

# На 1 шаге мы создаем функцию для проверки двух следующийх функций (для ИНН физ лица и для ИНН юр лица)
def check_validity (inn_input):
    try:
        if len(inn_input) == 10:
            return check_org_inn(inn_input)
        elif len(inn_input) == 12:
            return check_ind_inn(inn_input)
        else:
            print('Введен некорректный ИНН. Проверьте количество цифр')
            return False
    except ValueError:
        print('ИНН состоит только из цифр. Попробуйте снова')


# Шаг 4. Поскольку один и тот же алгорить вычислений будет использоваться несколько раз,
# то леге вывести это отдельной функцией, где осуществляются расчеты. А не копипастить один и тот же кусок кода
def calculate_control_number(inn_input, coef_list):
    control_sum = 0
    for pair in zip(inn_input, coef_list):
        inn_digit = int(pair[0])
        prod = inn_digit * pair[1]
        control_sum += prod
    control_number = control_sum % 11
    control_number = control_number % 10
    return control_number


#Шаг2. Создаем функцию для проверки данных для ИНН юридического лица
def check_org_inn(inn_input):
    coef_list = [2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
    control_number = calculate_control_number(inn_input, coef_list)
    if control_number == int(inn_input[9]):
        print('Все ок. Введен корректный ИНН юридического лица')
        return True
    else:
        print('Введен некорректный ИНН')
        return False

# Шаг 3. Создаем функцию для проверки данных для ИНН физического лица.
# И тут мы замечаем, что используем один и тот алгоритм расчетов и идет копи-паст кода из предыдущей функции
def check_ind_inn(inn_input):
    coef_list_ind_1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    control_number = calculate_control_number(inn_input, coef_list_ind_1)
    if control_number != int(inn_input[10]):
        print('Введен некорректный ИНН')
        return False
    coef_list_ind_2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    control_number = calculate_control_number(inn_input, coef_list_ind_2)
    if control_number == int(inn_input[11]):
        print('Все ок. Введен корректный ИНН физического лица')
        return True
    else:
        print('Введен некорректный ИНН')
        return False


if __name__ == "__main__":
    inn_input = input('Введите ИНН ')
    check_validity(inn_input)

