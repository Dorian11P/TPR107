strict10 = 0
infsup15 = 0
sup15 = 0
nb = 1
while nb < 10:


    print("Nombre à tester :")
    x = int(input())
    if x <= 20 and x >=0:

        nb = nb + 1

    else:
        while x > 20 or x <0:
            print("Retapez un nombre")
            x = int(input())




    if x < 10:
        strict10 = strict10 + 1
    if x >= 10 and x < 15:
        infsup15 = infsup15 + 1
    if x >= 15:
        sup15 = sup15 + 1

print("Les nombres trouvés contiennent:",strict10,"nombres inférieur à 10,", infsup15,"nombres compris entre 10 et 15,", sup15,"nombres supérieurs ou égaux à 15.")



