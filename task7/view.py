def input_number():
    while(True):
        try:
            number = int(input('Введите число: '))
            return number
        except:
            print('Введено некорректное значение: ')

def input_operation():
    operation = input('Введите операцию("+" ,"-", "/" ,"*" , " = "): ')
    while (True):
        if operation == '+':
            return operation
        elif operation == '-':
            return operation
        elif operation == '*':
            return operation
        elif operation == '/':
            return operation
        elif operation == '=':
            return operation
        else:
            print('Введён некорректный знак')
            operation = input('Введите операцию("+" ,"-", "/" ,"*", "="): ')

def print_result(smth):
    print(smth)

def expression():
    temp = input('Введите число или выражение: ')
    return temp

 
