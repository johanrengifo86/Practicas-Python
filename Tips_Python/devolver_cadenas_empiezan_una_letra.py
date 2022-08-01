#Tiene una lista de cadenas y desea devolver solo cadenas que comiencen
#  con una letra 'a', 
# puede usar el método startswith(). 
a = ['Lemon', 'Orange', 'Apple', 'Apricot']
list1 = [i for i in a if i.startswith('A')]
print(list1)