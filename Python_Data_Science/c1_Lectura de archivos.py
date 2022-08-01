# Descarga de Datos
'''
import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)
'''
# Lectura de archivos de texto

# Read the Example1.txt
example1 = "Example1.txt"
file1 = open(example1, "r")
#print(file1.name) #--> Imprime la ruta del archivo
#file.mode #--> Modo en el que se encuentra el archivo 'r' or ''w'

# Read the file
'''
fileContent = file1.read()
print(fileContent)
file1.close() # Cierra el archivo despues de finalizar
'''
# Usar la sentencia 'with' es una mejor prática para abrir archivos
# ya que cierra automáticamente el archivo

# Open file using with 
'''
with open(example1, "r") as file1:
    fileContent = file1.read()
    #print(fileContent)
'''
# Leer cierta cantidad de caracteres 
'''
with open(example1, "r") as file1:
    print(file1.read(4)) 
    print(file1.read(4))
    print(file1.read(7))
'''
# Leer una linea del archivo a la vez utilizando el método <readline()>
'''
with open(example1, "r") as file1:
    print('Firts Line: ' + file1.readline())
'''
# Iterar a través de las líneas
''' 
with open(example1, "r") as file1:
    i = 0
    for line in file1:
        print("Iteration ", str(i), ": ", line)
        i = i + 1
'''
# Leer todas las líneas y guardarlas como un lista
with open(example1, "r") as file1:
    fileaslist = file1.readlines()
print(fileaslist[0])






