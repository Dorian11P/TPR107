# déclaration de la fonction ajouter_elt(liste, elt):

print("avant traitement")
lst1=[0, 1, 2]

print(lst1, type(lst1), id(lst1))
print(lst1, type(lst1[0]), id(lst1[0]))
print(lst1, type(lst1[1]), id(lst1[1]))
print(lst1, type(lst1[2]), id(lst1[2]))

def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst
print("après traitement")
print(ajouter_elt(lst1, 3))
lst = ajouter_elt(lst1, 3)
print("lst1")
print(lst1, type(lst1), id(lst1))
print(lst1, type(lst1[0]), id(lst1[0]))
print(lst1, type(lst1[1]), id(lst1[1]))
print(lst, type(lst[2]), id(lst1[2]))
print("lst")
print(lst, type(lst), id(lst))
print(lst, type(lst[0]), id(lst[0]))
print(lst, type(lst[1]), id(lst[1]))
print(lst, type(lst[2]), id(lst[2]))

#on peut constater que l'ID est strictement identique dans les deux cas, comme si la deuxième liste était juste un surnom pour la première liste

