import view

phone_book = []

def get_phone_book() -> list:
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list) -> list:
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)

def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно удалить контакт {phone_book[id - 1][0]}? (да/нет)')
    if confirm.lower() == 'да':
        del_contact = phone_book.pop(id - 1)
        print()
        print('Контакт удалён')
        print()
    elif confirm.lower() == 'нет':
        pass
    else:
        print('Введено некорректное значение')

def replase_contact():
    global phone_book
    name_or_id = view.input_replase_contact()
    try:
        name_or_id == int(name_or_id)
        new_id = int(name_or_id)
        if new_id < 0 or new_id > len(phone_book) + 1:
            print('Такого контакта не существует')
        else:
            phone_book[new_id - 1] = view.input_new_contact()
    except:
        name = name_or_id
        for id, contact in enumerate(phone_book,1):
            if contact[0] == name:
                phone_book[id - 1] = view.input_new_contact()
                break
        else:
            print('Такого контакта не существует')

def search_contact():
    global phone_book
    name_or_id = view.input_contact()
    try:
        name_or_id == int(name_or_id)
        new_id = int(name_or_id)
        if new_id < 0 or new_id > len(phone_book) + 1:
            print('Такого контакта не существует')
        else:
            print('Контакт, который вы искали')
            print(*phone_book[new_id - 1])
    except:
        name = name_or_id
        for id, contact in enumerate(phone_book,1):
            if contact[0] == name:
                print('Контакт, который вы искали')
                print(*phone_book[id - 1])
                break
        else:
            print('Такого контакта не существует')




