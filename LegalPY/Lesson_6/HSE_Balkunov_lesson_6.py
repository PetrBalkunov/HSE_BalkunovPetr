'''
Задание

Соберите информацию о судебных заседаниях в деле № А40-183194/2015 (дело о банкротстве ООО «ТрансИнвестХолдинга»).

На сайте https://kad.arbitr.ru/ в каждом деле приложен .ics файл (стандартное расширение файлов для программ календарей), в котором присутствует информация о дате и времени судебных заседаний (вы можете открыть его, кликнув по дате заседания в карточке). Однако в них присутствует и «пустая» информация, дублирующая информацию о событиях по делу, но не относящуюся к конкретным судебным заседаниям.
Чтобы ознакомиться со структурой данных в ics файле и провести первичный анализ, достаточно открыть его в любом текстовом редакторе

Подсказка:

Блоки с информацией о событиях в календаре начинаются со строки
BEGIN:VEVENT

и заканчиваются строкой
END:VEVENT

Пример блока с отсутствующей информацией о дате и времени:

BEGIN:VEVENT
DTSTART;VALUE=DATE:00010101
DTEND;VALUE=DATE:00010102
TRANSP:TRANSPARENT
DESCRIPTION:Дело: А40-183194/2015 \n http://kad.arbitr.ru/Card/5fbea45a-9f9a-4d8e-b489-fbfa221361c3#ed\n Суд: АС города Москвы \n http://www.msk.arbitr.ru/
URL;VALUE=URI:http://kad.arbitr.ru/Card/5fbea45a-9f9a-4d8e-b489-fbfa221361c3#ed
UID:00000000-0000-0000-0000-000000000000@kad.arbitr.ru
SUMMARY:А40-183194/2015. АС города Москвы. .
END:VEVENT


Пример блока с наличием информации о дате и времени:

BEGIN:VEVENT
DTSTART;TZID=UTC+3:20200514T163000
DTEND;TZID=UTC+3:20200514T173000
LOCATION;ALTREP="http://vsrf.ru":\n 121260\, г. Москва\, ул. Поварская\, д.15\,
TRANSP:TRANSPARENT
DESCRIPTION:Дело: А40-183194/2015 \n http://kad.arbitr.ru/Card/5fbea45a-9f9a-4d8e-b489-fbfa221361c3#ed\n Суд: Верховный Суд РФ \n http://vsrf.ru
URL;VALUE=URI:http://kad.arbitr.ru/Card/5fbea45a-9f9a-4d8e-b489-fbfa221361c3#ed
UID:00000000-0000-0000-0000-000000000000@kad.arbitr.ru
SUMMARY:Заседание по делу А40-183194/2015 в Верховный Суд РФ. Судья Букина И. А.
END:VEVENT


При отсутствии в блоке с информацией фактического судебного заседания можно заметить указывающие на это участки в блоке с данными. Например, по умолчанию ставится дата 01.01.0001, отсутствуют тег с локацией и т.д.

Вам необходимо очистить данные от «мусора». Для нужно написать скрипт, который соберет информацию только о реальных судебных заседаниях в деле.

В файле должен присутствовать список всех реальных заседаний с описанием, информацией о начале и окончании судебного заседания, а также о месте его проведения.

Для решения данной задачи есть два варианта:

●	Самостоятельно распарсить файл на логические блоки и произвести сбор данных. Откройте его как обычный txt файл через встроенную функцию open().
Это опция для желающих усложнить задачу, уже имеющихся знаний хватит.

●	Воспользоваться готовой библиотекой для работы с ics файлами https://icspy.readthedocs.io/en/stable/ (рекомендуем воспользоваться этой библиотекой).
Это опция для желающих упростить задачу, но надо самостоятельно разобраться в библиотеке для работы с ics (она довольно простая).

По итогу работы скрипта данные должны быть сохранены в файлик «court_dates.json».

Пример результата:

[
{
“case_number”: “А40-183194/2015”,
“start”: “2020-10-27T17:56:00+03:00”
“end”: “2020-10-27T18:56:00+03:00”
“location”: “115225, г. Москва, ул. Большая Тульская, д. 17, Зал судебных заседаний № 8014”
“description”: “'Дело: А40-183194/2015\n http://kad.arbitr.ru/Card/5fbea45a-9f9a-4d8e-b489-fbfa221361c3#ed\nСуд: АС города Москвы\nhttp://www.msk.arbitr.ru/'”
},
{...},
{...},
…
]
'''
import fileinput

from ics import Calendar
from datetime import datetime
import aspose.words as aw
import json


def read_events_date(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    file_text = file.read()
    file.close()
    calendar_events = Calendar(file_text)
    return calendar_events

calendar_events = read_events_date('А40-183194-2015.ics')
# print(calendar_events.events.pop().location)

def filter_events(calendar_events):
    clean_events = []
    for event in calendar_events.events:
        if not event.location is None:
            clean_events.append(event)
    return clean_events

clean_events = filter_events(calendar_events)
print (clean_events[5:7])

def print_court_dates (clean_events):
        # Можно выгрузить данные о датах судебных заседаний в вордовский файл
    doc = aw.Document()
    # create a document builder object это уже специальные методы работы для ворда
    builder = aw.DocumentBuilder(doc)
    title_head = 'Хронология судебных заседаний по делу № А40-183194-2015: \n\n'
    builder.write(title_head)
    print (title_head)
    counter = 1
    for court_event in clean_events:
        event_info = f'Заседание № {counter}\n'
        #print (f'Заседание № {counter}')
        date_info_start = datetime.fromisoformat(str(court_event.begin))
        event_info += f'Дата: {date_info_start.strftime("%d-%m-%Y")}\n'
        #print (f'Дата: {date_info_start.strftime("%d-%m-%Y")}')
        date_info_finish = datetime.fromisoformat(str(court_event.end))
        event_info += f'Время: {date_info_start.strftime("%H:%M")} - {date_info_finish.strftime("%H:%M")}\n\n'
        #print (f'Время: {date_info_start.strftime("%H:%M")} - {date_info_finish.strftime("%H:%M")}')
        #print()
        print (event_info)
        counter += 1
        builder.write(event_info)
    doc.save("chronology_dela.docx")

print_court_dates(clean_events)


def transform_json(clean_events):
    file = open('court_dates.json', 'w', encoding='utf-8')
    court_dates = []
    for event in clean_events:
        court_dates.append({
            'case_number': 'А40-183194/2015',
            'start': str(event.begin),
            'end': str(event.end),
            'location': str(event.location),
            'description': str(event.description)
        })
    json.dump(court_dates,file)
    file.close()

transform_json(clean_events)



