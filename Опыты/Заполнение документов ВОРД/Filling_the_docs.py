from docx import Document
from docx import styles
from docx import shared
from docx.enum.style import WD_STYLE_TYPE
import re
class ResponsiblePerson:
    def __init__(self, doc_name):
        self.document = Document(doc_name)
        self.add_new_style()

    def add_new_style(self):
        obj_styles = self.document.styles
        obj_charstyle = obj_styles.add_style('MainStyle', WD_STYLE_TYPE.CHARACTER)
        obj_font = obj_charstyle.font
        obj_font.size = shared.Pt(11)
        obj_font.name = 'Cambria'

    def fill_organisation_name(self, organisation):
        self.document.paragraphs[0].clear()
        self.document.paragraphs[0].add_run(organisation).bold = True

    def fill_ogrn_inn_kpp(self, ogrn, inn, kpp):
        # записываем текст параграфа в переменную
        par_text = self.document.paragraphs[3].text

        # убираем текст параграфа из документа, чтобы переписать его с изменениями
        self.document.paragraphs[3].clear()

        # меняем старый текст (par_text), который собираемся записать в документ
        par_text = re.sub('ОГРН_+', f'ОГРН {ogrn}', par_text)
        par_text = re.sub('ИНН _+', f'ИНН {inn}', par_text)
        par_text = re.sub('КПП _+', f'КПП {kpp}', par_text)

        # записываем изменённый текст обратно в документ
        self.document.paragraphs[3].add_run(par_text).bold = True

    def fill_city_and_date(self, city, day, month, year):
        # записываем текст параграфа в переменную
        par_text = self.document.paragraphs[8].text

        # убираем текст параграфа из документа, чтобы переписать его с изменениями
        self.document.paragraphs[8].clear()

        # меняем старый текст (par_text), который собираемся записать в документ
        par_text = re.sub('^_+', city, par_text)
        par_text = re.sub('     _____\\.', f' {day}.', par_text)
        par_text = re.sub('\\._____\\.', f' {month} ', par_text)
        par_text = re.sub(' _+$', f' {year} года', par_text)
        # записываем изменённый текст обратно в документ
        self.document.paragraphs[8].add_run(par_text).bold = True

    def fill_company_full_name(self, company_full_name):
        # записываем текст параграфа в переменную
        par_text = self.document.paragraphs[10].text
        print(par_text)

        # убираем текст параграфа из документа, чтобы переписать его с изменениями
        self.document.paragraphs[10].clear()

        # меняем старый текст (par_text), который собираемся записать в документ
        par_text = re.sub(' _+',' '+company_full_name, par_text)

           # записываем изменённый текст обратно в документ
        self.document.paragraphs[10].add_run(par_text)



    def __str__(self):
        result = ''
        for par in self.document.paragraphs:
            result += '\n' + par.text
        return result

doc_name = 'Document_templates/1. Приказ о назначении ответственного за обраотку ПДн, должностные обязанности.docx'

responsible_person = ResponsiblePerson(doc_name)
responsible_person.fill_organisation_name('Наша Организация!')
responsible_person.fill_ogrn_inn_kpp(123456, 3245678, 345678)
responsible_person.fill_city_and_date('Москва', 12, 'июня', 2020)
responsible_person.fill_company_full_name('Oбщество с ограниченной ответственностью "Всегда первые"')

# print(responsible_person)
responsible_person.document.save('Output_docs/demo.docx')