from datetime import datetime as dt
path = 'log.txt'
def logger(first,second,oper,res):
    log = f'{dt.now()} | {first} {oper} {second} = {res}\n'
    with open(path, 'a') as data:
        data.write(log)
