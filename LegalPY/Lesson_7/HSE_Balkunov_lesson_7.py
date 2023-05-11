"""
Задание
Реализуйте класс CourtCase.

При вызове метода конструктора экземпляра (__init__) должны создаваться следующие атрибуты экземпляра:
●	case_number (строка с номером дела — обязательный параметр) передаётся в качестве аргумента при создании экземпляра
●	case_participants (список по умолчанию пустой)
●	listening_datetimes (список по умолчанию пустой)
●	is_finished (значение по умолчанию False)
●	verdict (строка по умолчанию пустая)

У экземпляра должны быть следующие методы:
●	set_a_listening_datetime — добавляет в список listening_datetimes судебное заседание (структуру можете придумать сами)
●	add_participant — добавляет участника в список case_participants (можно просто ИНН)
●	remove_participant — убирает участника из списка case_participants
●	make_a_decision — вынести решение по делу, добавить verdict и сменить атрибут is_finished на True
"""

class CourtCase:
    manufacturer = 'Piter'

    def __init__(self,case_number, case_participants=[],
                 listening_datetimes=[], is_finished=False, verdict=''):
        self.case_number = case_number
        self.case_participants = case_participants
        self.listening_datetimes = listening_datetimes
        self.is_finished = is_finished
        self.verdict = verdict

    def set_a_listening_datetime(self,court_datetime):
        self.listening_datetimes.append(court_datetime)

    def add_participant(self, INN):
        self.case_participants.append(INN)

    def remove_participant(self,INN):
        if INN in self.case_participants:
            self.case_participants.remove(INN)
        else:
            print ('Данный участник отсутствует')

    def make_a_decision(self,verdict):
        self.verdict = verdict
        self.is_finished = True

AVP_case = CourtCase('A56-34590/2022')
AVP_case.set_a_listening_datetime({'date':'12.03.2022', 'time': '12:50', 'topic': 'переход в основное заседание'})
AVP_case.add_participant('4851237821')
AVP_case.remove_participant('1234567890')
AVP_case.make_a_decision('Исковое заявление удовлетворить. Взыскать долг 1 млн рублей')

print(AVP_case.verdict, AVP_case.case_participants, AVP_case.listening_datetimes)

