nombre = float(input("Vous chercher la table de multiplication de quel nombre?"))
print("La table de multiplication de : ", nombre)
for compte in range(1, 11):
    print(nombre, 'x', compte, '=', round(nombre * compte, 1))