BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

print("Entrer le nombre de personnes invitées :")

nbConvives= int(input())

print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :")
print("-", fromage * nbConvives / BASE, "gr de fromage")
print("-", eau * nbConvives / BASE, "dL d'eau")
print("-", ail * nbConvives / BASE, "gousse(s) d'ail")
print("-", pain * nbConvives / BASE, "gr de pain")

