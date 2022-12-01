import random
nombre = random.randint(0, 100)
essais = 0


while True :
    print("Nombre :")
    x = int(input())

    if x > nombre :
        (print("Plus bas"))

    if x < nombre:
        (print("Plus haut"))


    if x == nombre :
        print("Vous avez trouver en", essais, "tentatives")
        break

    essais = essais + 1