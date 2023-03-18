from logger import input_data, print_data, put_data, delete_data

def interface():
    print('Здравствуй. Какой пункт Вас интересует?\n'
          '1. Новая запись (2 формата записи)\n'
          '2. Удалить контакт\n'
          '3. Изменить контакт\n'
          '4. Показать все контакты\n')
    command = int(input("Выберете номер: "))

    while command < 1 or command > 4:
        print('Неверный пункт')
        command = int(input("Выберете корректный пункт: "))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print_data()