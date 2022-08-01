class Err(Exception):
    def __init__(self, valor):
        print('Fue el error por: ',valor)

try:
    raise Err(4)
except Err:
    print('error escrito:')
        