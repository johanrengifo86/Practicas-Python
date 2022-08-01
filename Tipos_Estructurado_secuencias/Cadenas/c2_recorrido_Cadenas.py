
# Formas diferentes de imprimir una cadena de forma invertida
a = "mi cadena"
#for i in range(len(a)):
    #print(i, a[i])
   # print(a[len(a)-i-1])

#print('\n') No arroja ningun valor 
for i in range(len(a), -1):
    print(a[i])
#print('\n')

#for i in range(len(a)-1, -1, -1):
#    print(a[i])


