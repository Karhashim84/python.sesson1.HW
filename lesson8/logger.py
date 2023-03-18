from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"Какой вариант записи вы предпочитаете?\n\n"
                    f"1 вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 вариант:\n\n"
                    f"{surname} {name}, {phone}, {address}\n\n"
                    f"Выберете вариант: "))

    while var != 1 and var != 2:
        print('Некорректно выбран пункт!')
        var = int(input("Введите корректный вариант записи: "))

    if var == 1:
        with open('lesson8/data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n')
    else:
        with open('lesson8/data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name} {surname}, {phone}, {address}\n')


def print_data():
    print('Первый вариант:\n')
    with open('lesson8/data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('Второй вариант:\n')
    with open('lesson8/data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


  
def put_data():
    print('Какой файл с данными вы хотите изменить?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Неверный пункт!')
        number_file = int(input('Выберете файл: '))

    if number_file == 1:
        print("Какой контакт хотите изменить?")
        number_journal = int(input('Введите номер контакта: '))
        number_journal -= 1
        
        print(f'Контакт изменен\n{data_first[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                     data_first[number_journal + 1:]
        with open('lesson8/data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения сохранены!')
    else:
        print("Какой контакт хотите изменить?")
        number_journal = int(input('Введите номер контакта: '))
        number_journal -= 1
        
        print(f'Контакт изменен\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address}\n'] + \
                      data_second[number_journal + 1:]
        with open('lesson8/data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Контакт изменен!')


def delete_data():
    print('Какой контакт хотите удалить?')
    data_first, data_second = print_data()
    number_file = int(input('Выберете файл: '))

    while number_file != 1 and number_file != 2:
        print('Неверный номер файла!')
        number_file = int(input('Выберете номер файла: '))

    if number_file == 1:
        print("Какой контакт хотите удалить?")
        number_journal = int(input('Выберете номер контакта: '))
        
        print(f'Контакт удален\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('lesson8/data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Контакт удален!')
    else:
        print("Какой контакт хотите удалить?")
        number_journal = int(input('Введите номер контакта: '))
        
        print(f'Контакт удален\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('lesson8/data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Контакт удален!')