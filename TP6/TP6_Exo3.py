# déclaration de la fonction ajouter_elt(lst=[0, 1, 2], elt=3)
lst1=[0, 1, 2]
char="abcd"
def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst
#ce serait  [0, 1, 2, 3]
print(ajouter_elt())
print(id(ajouter_elt()))
print(id(lst1))

def ajouter_carac(ch="abc", elt="d"):
    ch = ch + elt
    return ch
#d) ça serait abcd
print(ajouter_carac())
print(id(ajouter_carac()))
print(id(char))
#on peut voir que python créé un nombre unique pour chaque variable différente

