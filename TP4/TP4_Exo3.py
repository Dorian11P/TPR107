# Déclaration des variables
nMax = 3
v1 = []
v2 = []

# Demande de la taille des vecteurs
while True:
    n = int(input("Entrez la taille des vecteurs (entre 1 et 3) : "))
    if 1 <= n <= nMax:
        break

# Demande des composantes des vecteurs
for i in range(n):
    v1.append(int(input("Entrez la composante v1[{}] : ".format(i))))
    v2.append(int(input("Entrez la composante v2[{}] : ".format(i))))

# Calcul du produit scalaire
scalar_product = 0
for i in range(n):
    scalar_product += v1[i] * v2[i]

# Affichage du résultat
print("Le produit scalaire de v1 et v2 est : {}".format(scalar_product))