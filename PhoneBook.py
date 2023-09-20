# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def enter_first_name():
    return input("Введите имя абонента: ").title()


def enter_second_name():
    return input("Введите фамилию абонента: ").title()


def enter_family_name():
    return input("Введите отчество абонента: ").title()


def enter_phone_number():
    return input("Введите номер телефона: ")


def enter_address_number():
    return input("Введите адрес абонента: ").title()


def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')


def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def search_line():
    print('Выбертите вариант поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1
    searched = input('Введите поисковые данные: ').title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(item, end="\n\n")
        # file.seek(0)
        # print(file.readlines())


def delete_data():
    print('Выбертите вариант удаления:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес\n'
          '6. Удалить контакт целиком')

    index = int(input('Введите вариант: ')) - 1
    searched = input('Введите поисковые данные: ').title()

    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')

    new_data = []

    for item in data:
        if index == 5 and searched in item:
            continue  # Skip this contact (do not add to new_data list)
        # else:
        #     new_data.append(item)

        contact_info = item.replace('\n', ' ').split()

        if len(contact_info) >= index + 1:  # Check if the selected field exists in the contact info
            field_to_delete = contact_info[index]
            if searched == field_to_delete and index != 5:
                contact_info[index] = 'deleted'
                # new_data.append('\n'.join(contact_info))
                new_data.append(f'{contact_info[0]} {contact_info[1]} {contact_info[2]}\n{contact_info[3]}\n{contact_info[4]}\n')
            else:
                new_data.append(item)
        else:
            new_data.append(item)

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_data))


def change_data():

    print('Выберите вариант, где нужно внести изменения:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес\n')

    index = int(input('Введите вариант: ')) - 1
    searched = input('Введите данные, которые необходимо изменить: ').title()
    replacement = input('Введите новые данные: ').title()

    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')

    new_data = []
    my_check = False

    for item in data:
        contact_info = item.replace('\n', ' ').split()
        if len(contact_info) >= index + 1:  # Check if the selected field exists in the contact info
            if contact_info[index] == searched:
                my_check = True
                contact_info[index] = replacement
                new_data.append(
                    f'{contact_info[0]} {contact_info[1]} {contact_info[2]}\n{contact_info[3]}\n{contact_info[4]}\n')
            else:
                new_data.append(item)
        else:
            new_data.append(item)

    if not my_check:
        print('Совпадений не найдено. Введите корректные данные для поиска замены.')

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_data))


def interface():
    cmd = 0
    while cmd != '6':
        print("Выберите действие: \n"
              "1. Добавить контакт\n"
              "2. Вывести все контакты\n"
              "3. Поиск контакта\n"
              "4. Удаление контакта\n"
              "5. Изменить контакт\n"
              "6. Выход\n")
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод')
            cmd = input("Введите действие: ")
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
                break
            case '3':
                search_line()
            case '4':
                delete_data()
            case '5':
                change_data()
            case '6':
                print('Всего доброго! ')


interface()
