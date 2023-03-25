# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print ("what a hell") # burn after reading



# Шифр Цезаря Учебный проект
SYMBOLS = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ". lower()
mode = 0
result = ''
key = 7
while True:
    print ("Вы хотите за(ш)ифровать или (р)асшифровать сообщение?")
    response = input ('| '). lower()
    print ("Введите ключ")
    key = int (input ('| '))

    if response.startswith('ш'):
        mode =0
        break;
    elif response.startswith ('р'):
        mode = 1
        break;
        print ("Введите ш или р")

        print ("ВВедите сообщение:")
        message =input ('| '). lower()

        for synbol in message:
            if symbol in SYMBOLS:
                num = SYMBOLS.find (symbol)

                if mode == 0:
                    num = num + key
                elif mode == 1:
                    num = num - key

                    if num >= len (SYNBOLS):
                        num = num - len (SYMBOLS)

                        result += SYMBOLS (num)

                        print(result)
