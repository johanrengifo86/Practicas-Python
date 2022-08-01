class Clase():
    # En la logica de python primero se invoca la <new>
    def __new__(cls): # Personalizar la creacion de instancias de clases
        print('new')
        return super().__new__(cls)  # sin esta linea no se ejecutara el <init>

    def __init__(self):   # Tareas de inicializacion cuando la instancia de una clase es creada
        print('init')

c = Clase()