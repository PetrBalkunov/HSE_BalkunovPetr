import datetime
import json

import requests
import openpyxl
import os
from datetime import datetime


MONTHS_DICT = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12
}
class ParserCBRF:
    """
    Loads loan rates for short-term loans for non-financial organisations.
    """

    def get_loan_rate_table(self):
        r = requests.get('https://www.cbr.ru/vfs/statistics/pdko/int_rat/loans_nonfin.xlsx')
        with open(os.path.join('pars_data', 'loan_rate_data.xlsx'), 'wb') as f:
            f.write(r.content)

    def parse_xlsx_file(self):
        wookbook = openpyxl.load_workbook(os.path.join('pars_data', 'loan_rate_data.xlsx'))
        worksheet = wookbook.active
        date_data = [cell.value for cell in worksheet['A'][5:-1]]
        rate_data = [cell.value for cell in worksheet['E'][5:-1]]
        return dict(zip(date_data, rate_data))
# нужно еще сохранить этот файл со словарем
    def start(self):
        self.get_loan_rate_table()
        pairs_dict = self.parse_xlsx_file()
        CBRF_rate_dict = {}
        for date, rate in pairs_dict.items():
            month, year = date.split()
            month_integer = MONTHS_DICT[month.lower()]
            CBRF_rate_dict[f'{month_integer}-{year}'] = str(rate)
        with open(os.path.join('pars_data', 'CBRF_rate_dict.json'), 'w') as f:
            json.dump(CBRF_rate_dict, f, indent=4)



parser = ParserCBRF()
parser.start()

class LoanRateCBRF:
    def __init__(self, file_name):
        with open(os.path.join('pars_data', file_name), 'r') as f:
            CBRF_rate_dict = json.load(f)
        self.deserialize(CBRF_rate_dict)

    def deserialize(self, CBRF_rate_dict):
        self.CBRF_rate_dict = {}
        for date, rate in CBRF_rate_dict.items():
            date = datetime.strptime(date, '%m-%Y')
            self.CBRF_rate_dict[date] = float(rate)

    def round_date(self, date):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
            date = date.replace(day=1)
            return date
        except ValueError:
            print('Неправильно указана дата')


    def loan_rate_by_date(self, date):
        date = self.round_date(date)
        if date in self.CBRF_rate_dict:
            return self.CBRF_rate_dict[date]

    def loan_rate_last(self):
        last_date = max(self.CBRF_rate_dict)
        return self.CBRF_rate_dict[last_date]

    def loan_rate_range (self, start_date, end_date):
        start_date = self.round_date(start_date)
        end_date = self.round_date(end_date)
        loan_range_list = []
        for date, rate in self.CBRF_rate_dict.items():
            if date >= start_date and date <= end_date:
                loan_range_list.append((date,rate))
        return loan_range_list

    def average_loan_rate (self, start_date, end_date):
        loan_range_list = self.loan_rate_range(start_date, end_date)
        rates_list = [pair[1] for pair in loan_range_list]
        average_rate = sum(rates_list)/len(rates_list)
        return round(average_rate, 3)



loan_rate_CBRF = LoanRateCBRF('CBRF_rate_dict.json')
print(loan_rate_CBRF.CBRF_rate_dict)
print (loan_rate_CBRF.loan_rate_by_date('202115.20'))
print (f'Текущая ставка по кредитам составляет: {loan_rate_CBRF.loan_rate_last()} % годовых')
print(loan_rate_CBRF.loan_rate_range('2019-04-12', '2023-01-31'))
print(f"Средняя ставка по кредитам за указанный период сотавила: {loan_rate_CBRF.average_loan_rate('2019-05-20', '2023-01-27')} % годовых")


