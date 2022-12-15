import model
import view
import logger

def start():
    first_num = view.expression()
    try:
        first_num == int(first_num)
        model.set_first_number(int(first_num))
        operation = view.input_operation()
        count = 0
        while operation != '=':
            first = model.get_intermediate_result()
            model.set_next_number(view.input_number())
            second = model.get_next_number()
            oper = operation
            model.check_operation(operation)
            res =  model.get_intermediate_result()
            view.print_result(model.get_intermediate_result())
            if count == 0:
                logger.logger(first_num,second,oper,res)
            else:
                logger.logger(first,second,oper,res)
            operation = view.input_operation()
            count += 1
        view.print_result(model.get_intermediate_result())
    except:
        try:
            view.print_result(model.calculate(first_num))
        except:
            print('Введено некорректное выражение')

