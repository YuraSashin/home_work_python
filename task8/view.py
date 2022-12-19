import phone_book as pb

def main_menu():
    print('Выберите команду меню: ')
    print('1. Показать телефонную книгу: ')
    print('2. Загрузить телефонную  книгу')
    print('3. Сохранить телефонную книгу')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выйти из приложения\n')
    return input_menu()
    
def input_menu():
    while True:
        try:
            choise = int(input('Выберите пункт меню: '))
            if choise in range(1,8) or choise == 0:
                return choise
            else:
                print('Введено некорректное значение')
        except:
            print('Введено некорректное значение')
    
def print_phone_book():
    phone_book = pb.get_phone_book()
    print()
    if len(phone_book) < 1:
        print('Телефонная книга пуста\n')
    else:
        for id, contact in enumerate(phone_book,1):
            print(id, *contact)
    print()

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите номер телефона: ') 
    comment = input('Введите коментарий к конткату: ')
    new_contact = [name, phone,comment]
    print()
    print('Контакт сохранён')
    print()
    return new_contact

def input_remove_contact():
    print()
    print_phone_book()
    id = int(input('Введите ID  котнакта, который хотите удалить: '))
    return id

def input_replase_contact():
    print()
    print_phone_book()
    id_or_name = input('Введите имя или ID контакта, который хотите изменить: ')
    return id_or_name
  
def input_contact():
    id_or_name = input('Введите имя или ID контакта, который хотите найти: ')
    return id_or_name




