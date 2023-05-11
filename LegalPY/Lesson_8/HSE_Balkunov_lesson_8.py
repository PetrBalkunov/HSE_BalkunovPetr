




class CupofCoffe:

    manufacturer = 'Balkunov&Co'

    def __init__(self, coffee_sort='Арабика', country='ЮАР'):
        self.choose_coffee_sort(coffee_sort)
        self.country = country
        self.grind = None
        self.style = None
        self.additions = []

    def choose_coffee_sort(self, coffee_sort):
        coffee_sort_manual = input(f'Выберите сорт кофе цифрой: 1. Арабика; 2. Робуста; 3. Пропустить\n')
        if coffee_sort_manual == '1':
            self.coffee_sort = 'Арабика'
        elif coffee_sort_manual == '2':
            self.coffee_sort = 'Робуста'
        else:
            self.coffee_sort = coffee_sort

    def grind_coffee(self):
        grind = input('Выберите вид помола цифрой: 1. крупный помол; 2. средний помол; 3. мелкий помол\n')
        grind_types = {1: 'крупный помол', 2:'средний помол', 3:'мелкий помол'}
        self.grind = grind_types[int(grind)]



    def make_cup_of_coffee(self):
        coffee_style = input('Выберите стиль приготовления: 1. эспрессо; 2. американо; 3. каппучино; 4. латте\n')
        coffee_types = {1: 'эспрессо', 2: 'американо', 3: 'каппучино', 4: 'латте'}
        self.style = coffee_types[int(coffee_style)]
        coffee_adds = input('Выберите добавки к кофе (можно несколько сразу): 1. карамель; 2. шоколадная крошка; 3. сливки; 4. доп сахар\n')
        addition_types = {1:'карамель', 2: 'шоколадная крошка', 3:'сливки', 4: 'доп сахар'}
        for addition in coffee_adds:
            self.additions.append(addition_types[int(addition)])

    def confirm_order(self):
        print(f'Вы выбрали: {self.coffee_sort}, {self.grind}, {self.style} c добавками {"; ".join(self.additions)}.\n'
              f' Приятного кофепития Вам желает {self.manufacturer}')

# создаём новый объект
cup_of_coffee = CupofCoffe(coffee_sort='robusta')
cup_of_coffee.grind_coffee()
cup_of_coffee.make_cup_of_coffee()
cup_of_coffee.confirm_order()


