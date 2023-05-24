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
        #print (r.status_code)
        #print (r.text)

    def get_manager_efrsb(self):
        inn = input('Введите ИНН: ')
        r = requests.get(f'https://api.sirotinsky.com/{self.private_token}/efrsb/manager/{inn}')
        print(r.status_code)
        return r.text



efrsb_sirot = SirotinskyAPI('HSE_student', '123123123')
manager_info = efrsb_sirot.get_manager_efrsb()
print(manager_info)


