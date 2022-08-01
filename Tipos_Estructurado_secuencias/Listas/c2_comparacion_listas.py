
def comprobacionMenorque(list1, list2):
    if(list1 < list2):
        print(True)
    else:
        print(False)

def comprobacionMayorque(list1, list2):
    if(list1 > list2):
        print(True)
    else:
        print(False)

def comprobacionMenorIgualque(list1, list2):
    if(list1 <= list2):
        print(True)
    else:
        print(False)

comprobacionMenorque([1,2], [1,2])
comprobacionMenorque([1,2,3], [1,2])
comprobacionMenorque([1,1], [1,2])
comprobacionMenorque([1,3], [1,2])

comprobacionMayorque([10,20,30], [1,2,3])
comprobacionMayorque([10,20,3], [1,2,3])
comprobacionMayorque([10,2,3], [1,2,3])
comprobacionMayorque([1,20,30], [1,2,3])

comprobacionMenorIgualque([0,2,3], [1,2,3])
comprobacionMenorque([1], [2,3])
comprobacionMenorque([1], [1,2])
comprobacionMenorque([1,2], [0])



