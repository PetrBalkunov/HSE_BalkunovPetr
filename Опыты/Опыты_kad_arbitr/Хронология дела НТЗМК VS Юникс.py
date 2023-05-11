

from ics import Calendar
from datetime import datetime
import aspose.words as aw
import json
import re


def read_events_date(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    file_text = file.read()
    file.close()
    calendar_events = Calendar(file_text)
    return calendar_events

calendar_events = read_events_date('А40-161743-2018.ics')
#print(calendar_events.events.pop().location)

def clean_events(calendar_events):
    clean_events = []
    for event in calendar_events.events:
        if not event.location is None:
            clean_events.append(event)
            #clean_events.append(event.location)
    return clean_events

clean_events = clean_events(calendar_events)
#print (clean_events)

#Создаем регулярное выражение для поиска суда 1-ой инстанции в строках ("...АС города...")
first_court_re = re.compile('АС города')
#Создаем регулярное выражение для поиска суда апелляционной (2-й) инстанции в строках ("...арбитражный апелляционный суд."
second_court_re = re.compile('арбитражный апелляционный суд')
#Создаем регулярное выражение для поиска суда кассационной (3-й)инстанции в строках ("...АС...округа.")
third_court_re = re.compile('АС \w+ округа')
#Создаем регулярное выражение для поиска Верховного суда (4-й) инстанции в строках ("...Верховный суд РФ.")
high_court_re = re.compile('Верховный суд РФ')
def filter_courts(clean_events):
    first_court_events = []
    second_court_events = []
    third_court_events = []
    high_court_events = []
    for court in clean_events:
        if first_court_re.search(court.description):
            first_court_events.append(court)
        elif second_court_re.search(court.description):
            second_court_events.append(court)
        elif third_court_re.search(court.description):
            third_court_events.append(court)
        elif high_court_re.search(court.description):
            high_court_events.append(court)
        else:
            print(court.description)
    return first_court_events,second_court_events, third_court_events, high_court_events

first_court_events,second_court_events, third_court_events, high_court_events = filter_courts(clean_events)

print(first_court_events)
'''
def print_court_dates(clean_events):
# Можно выгрузить данные о датах судебных заседаний в вордовский файл
    doc = aw.Document()
# create a document builder object это уже специальные методы работы для ворда
    builder = aw.DocumentBuilder(doc)
    title_head = 'Хронология судебных заседаний по делу № А40-183194-2015: \n\n'
    builder.write(title_head)
    print(title_head)
    counter = 1
    for court_event in clean_events:
        event_info = f'Заседание № {counter} '
        # print (f'Заседание № {counter}')
        if first_court_re.search(court_event.description):
            event_info += 'в первой инстанции'
        elif second_court_re.search(court_event.description):
            event_info += 'в апелляционной инстанции'
        elif third_court_re.search(court_event.description):
            event_info += 'в кассационной инстанции'
        elif high_court_re.search(court_event.description):
            event_info += 'в Верховном суде'
        event_info += '\n'
        date_info_start = datetime.fromisoformat(str(court_event.begin))
        event_info += f'Дата: {date_info_start.strftime("%d-%m-%Y")}\n'
        # print (f'Дата: {date_info_start.strftime("%d-%m-%Y")}')
        date_info_finish = datetime.fromisoformat(str(court_event.end))
        event_info += f'Время: {date_info_start.strftime("%H:%M")} - {date_info_finish.strftime("%H:%M")}\n\n'
        # print (f'Время: {date_info_start.strftime("%H:%M")} - {date_info_finish.strftime("%H:%M")}')
        # print()
        print(event_info)
        counter += 1
        builder.write(event_info)
    doc.save("chronology_dela.docx")

print_court_dates(clean_events)
'''


