'''for i in range(0, 5):
    for j in range(0, 3):
        print(i, j)'''

'''for i in range(0, 5):
    for j in range(i, 5):
        print(i,j)'''

'''for i in range(0, 5):
    for j in range(0, i):
        print(i,j)'''

''' 
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,2):
            print(i,j,k)'''

''' 
for i in range(0,4):
    for j in range(0,4):
        for k in (i,j):
            print(i,j,k)'''

for i in range(1,5):
    for j in range(0, 10, i):
        print(i,j)
