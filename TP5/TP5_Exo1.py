noms = []

for i in range(2):
    nom = input("Entrez le nom de la personne : ")
    prenom = input("Entrez le prénom de la personne : ")
    noms.append((nom.upper(), prenom.capitalize()))

noms.sort()

for nom, prenom in noms:
    print(f"{prenom} {nom}")