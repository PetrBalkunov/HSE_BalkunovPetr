'''
Создаем словарь для каждой базы данный.
Для каждого пользователя формируется сразу 3 словаря и данные оттуда подтягиваются из 3 баз данных.
Ключом для всех 3 таблиц является ИНН компании (INN_company)
'''

dadata_data = {
    'INN_company': '123123123',
    'kpp_company': '234234234',
    'full_name_company': 'Общество с ограниченной ответственностью "Ромашка"',
    'short_name_company': 'ООО "Ромашка"',
    'OGRN_company': '567890123',
    'address_company': '456783б, г. Санкт-Петербург, ул. Морская, дом 12, оф. 34',
    'CEO': 'генеральный директор',
    'CEO_name': 'Иванов Иван Иванович',
    'est_date_company': '25-06-2002'
}

form_data = {
    'INN_company': '123123123',
    'server_address': '456783б, г. Санкт-Петербург, ул. Морская, дом 12, оф. 34',
    'internet_name_company': 'www.romashka.ru',
    'public_email_company': 'romashka@yandex.ru',
    'PD_person': 'Сидор Никонорович Федоров',
    'sign_date': '20-06-2023'
}
