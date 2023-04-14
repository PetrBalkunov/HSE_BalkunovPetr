'''
Задание

1.	Найдите информацию об организациях:
a.	Получите список ИНН из файла «traders.txt»;
b.	Найдите информацию об организациях с этими ИНН в файле «traders.json»;
c.	Сохраните информацию об ИНН, ОГРН и адресе организаций из файла «traders.txt» в файл «traders.csv».

2.	Напишите регулярное выражение для поиска email-адресов в тексте.

Для этого напишите функцию, которая принимает в качестве аргумента текст в виде строки и возвращает список найденных email-адресов или пустой список, если email-адреса не найдены.

Используйте дата-сет на 1000 сообщений из Единого федерального реестра сведений о банкротстве (ЕФРСБ) для практики.

Есть дата-сеты и побольше:
●	дата-сет на 10 000 сообщений,
●	дата-сет на 100 000 сообщений,
но если компьютер слабый, ограничьтесь самым маленьким.

Текст сообщений можно найти по ключу «msg_text».

Найдите все email-адреса в дата-сете и соберите их в словарь, где ключом будет выступать ИНН опубликовавшего сообщение («publisher_inn»), а в значении будет хранится множество set() с email-адресами. Пример:

{
“77010127248512”: {“name_surname@yandex.ru”, “name_surname@mail.ru”}
“77011235421242”: {“name_surname@yandex.ru”, “name_surname@gmail.com”}
…
}

Сохраните собранные данные в файл «emails.json».

'''
# 1 Задание.

import json
import pandas
import re



file = open('traders.txt')
inn_search = file.read().split()
file.close()
print(inn_search)

file = open('traders.json')
traders_list = json.load(file)
file.close()
print(type(traders_list))
print(traders_list[0])

org_list = []
for org_info in traders_list:
    if org_info['inn'] in inn_search:
        org_list.append([org_info['short_name'], org_info['inn'], org_info['ogrn'], org_info['address']])


dataframe_org = pandas.DataFrame(org_list, columns=['Наименование', 'ИНН', 'ОГРН', 'Адрес'])
#print(dataframe_org.head(3))
dataframe_org.to_csv('traders.csv', encoding='utf-8')

'''
# Задание 2.

file = open('10000_efrsb_messages.json')
email_list = json.load(file)
file.close()
print(type(email_list))
print(email_list[0].keys())

#Создаем регулярное выражение для поиска email в строках
email_re = re.compile('\\s([\\w._$+~-]+@[a-z]+\.[a-z]+)(?:\\s|$|,|\.)')


# Создаем функцию для поиска email адресов в тексте сообщения и складываем эти данные в наш словарик
def find_emails(email_list):
    publisher_dict = {}
    text_without_emails = []
    for msg_info in email_list:
        msg_text = msg_info['msg_text']
        emails = email_re.findall(msg_text)
        if emails:
            publisher_inn = msg_info['publisher_inn']
            if publisher_inn not in publisher_dict:
                publisher_dict[publisher_inn] = set(emails)
            # Проблема заключается в том, что функция запишет в словарь только последние значения для ключа по ИНН публикатора,
            # а все остальные просто сотрет. Нужно предусмотреть это - нужны 2 опции: 1 случай - когда ИНН публикатора еще не в словаре,
            #и тогда мы создаем пару ключ-значение; 2 случай - когда ИНН публикатора есть в словаре и нам нужно просто добавлять к нему все email
            #без перезаписи пары ключ-значение
            else:
                publisher_dict[publisher_inn].update(set(emails))
        else:
            text_without_emails.append(msg_text)

    return publisher_dict, text_without_emails


publisher_info, publisher_without_emails = find_emails(email_list)
#print(publisher_info)
#print(publisher_without_emails[:5])

#json не умеет записывать  множества, поэтому наши множества теперь снова сделать списками
def write_emails_dict(publisher_info):
    for publisher_inn in publisher_info:
        publisher_info[publisher_inn] = list(publisher_info[publisher_inn])
    file = open('emails.json', 'w')
    json.dump(publisher_info, file)
    file.close()

write_emails_dict(publisher_info)
print('Количество ИНН с email адресами:', len(publisher_info))
'''