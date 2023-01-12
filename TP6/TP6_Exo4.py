import numpy

## Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr' valeurs comprises entre 'vmin' et 'vmax'
def generer(nbr, vmin, vmax):
    lst = numpy.random.choice(range(vmin, vmax), size=nbr, replace=True)
    return lst

print(generer(5, 0, 5))
## Fonction combienInferieur(table, vseuil) pour compter le nombre devaleurs d'un tableau 'table' inférieures à la valeur 'vseuil'
def combienInferieur(tab, vseuil):
    totalnb = 0
    for i in tab:
        if tab[i]  < vseuil :
            totalnb += 1
    return totalnb

choix = input("Utiliser une seed aléatoire? o/n")

if  choix == 'o' :
    print("Utilisation d'une seed aléatoire pour le tirage")
    numpy.random.seed(seed=None)
elif choix == 'n' :
    seed = input("Entrer la seed :")
    print("La seed sélectionnée est :", seed)
    numpy.random.seed(seed=graine)




tab = generer(int(input("nombre de valeurs")), int(input("vmin")), int(input("vmax")))

tab.sort()
print(tab)
total = combienInferieur(tab, 25)
print(f"Il y en a {total} inférieurs à 25")