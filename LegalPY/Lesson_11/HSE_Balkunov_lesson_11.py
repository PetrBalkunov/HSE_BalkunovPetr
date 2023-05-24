'''
Задание
Напишите класс SirotinskyAPI для взаимодействия с API, размещённым по адресу https://api.sirotinsky.com/.

Класс должен содержать в себе функционал для работы со всеми методами, указанными в документации к API, которые размещены по адресу https://api.sirotinsky.com/docs.

Метод инициализации экземпляра класса должен принимать в качестве аргументов логин и пароль для получения токена авторизации и сразу производить вызов приватного метода для получения токена в целях его сохранения как аргумента экземпляра.

Метод получения токена должен быть приватным и не доступен для вызова вне класса.

Методы для получения данных из ЕФРСБ должны быть публичными

Данные для доступа:
●	Логин: HSE_student
●	Пароль: 123123123
'''

import requests

class SirotinskyAPI:

    def __init__(self, login, password):
        self.__get_token(login, password)

    def __get_token (self, login, password):
        r = requests.post('https://api.sirotinsky.com/token', data={'username': login, 'password': password})
        data = r.json()
        self.private_token = data['access_token']


    def get_efrsb_data(self):
        end_point = input('Выберите раздел: 1. manager; 2. trader; 3. person; 4. organisation;\n')
        data_types = {1: 'manager', 2: 'trader', 3: 'person', 4: 'organisation'}
        inn = input('Введите ИНН: ')
        r = requests.get(f'https://api.sirotinsky.com/{self.private_token}/efrsb/{data_types[int(end_point)]}/{inn}')
        if r.status_code == 200:
            print('Статус запроса: успешно!')
            if r.text != 'null':
                print(r.text)
            else:
                print('Данные не найдены')
        else:
            print('Статус запроса: ошибка!')


efrsb_sirot = SirotinskyAPI('HSE_student', '123123123')
efrsb_info = efrsb_sirot.get_efrsb_data()





