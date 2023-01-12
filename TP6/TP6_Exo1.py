l1= [0] * 3
print(l1, type(l1), id(l1))

print(l1, type(l1[0]), id(l1[0]))
print(l1, type(l1[1]), id(l1[1]))
print(l1, type(l1[2]), id(l1[2]))
#c'est 3x le même ID
l1[1] += 1
print("après incrémentation")
print(l1, type(l1), id(l1))

print(l1, type(l1[0]), id(l1[0]))
print(l1, type(l1[1]), id(l1[1]))
print(l1, type(l1[2]), id(l1[2]))
#la liste ne change pas d'ID
#il y a que la valeur incrémentée à changé
