from tkinter import *

# Constucción de la raíz
raiz = Tk()
# Título para la ventana creada
raiz.title('Ventana de prueba')
# Método para controlar la dimensión de la ventana 
#raiz.resizable(1,1)
# Método para cambiar icono de la ventana
raiz.iconbitmap('goku.ico')
# Cambio del tamaño por defecto
#raiz.geometry('650x350')

# Metodo config
raiz.config(bg='blue') # Color de Fondo en la raiz
raiz.config(bd=45)     # Tamaño de borde en la raiz
raiz.config(relief='groove') # Tipo de borde en la raiz
raiz.config(cursor='hand2') # Tipo de cursor de la raiz

# Creación de Frame y empaquetación en la raiz
miFrame = Frame()
#miFrame.pack(side='left', anchor='n')

# rellenado
#miFrame.pack(fill='x')
# En el eje y
#miFrame.pack(fill='y', expand='True') # Para expandir el frame en todo el tamaño de la raiz
# se utiliza <fill = 'both'>
miFrame.pack()

# Cambiar caracteristicas del frame
miFrame.config(bg='red')
miFrame.config(width='650', height='350')

# Caracteristas del borde
miFrame.config(bd=35)
miFrame.config(relief='groove') # Bordes --> 'sunken', 

# Cambiar cursor del raton 
miFrame.config(cursor='pirate')





# Método que se encarga de que la ventana se encuentre en ejecución
raiz.mainloop()