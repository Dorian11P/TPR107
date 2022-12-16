print("Donnez l'heure de début de la location (un entier) : ")
deb = int(input())
print("Donnez l'heure de fin de la location (un entier) : ")
fin = int(input())
heures = 0
tarif1 = 0
tarif2 = 0
tarif3 = 0
while True:


    if deb >24 or deb < 0 or fin < 0 or fin > 24:
        print('Les heures doivent être comprises entre 0 et 24!\n')
        print('Resaisir heures:')
        print("Donnez l'heure de début de la location (un entier) : ")
        deb = int(input())
        print("Donnez l'heure de fin de la location (un entier) : ")
        fin = int(input())

    if deb == fin:
        print('Attention! L heure de fin est identique à l heure de début\n')
        print('Resaisir heures:')
        print("Donnez l'heure de début de la location (un entier) : ")
        deb = int(input())
        print("Donnez l'heure de fin de la location (un entier) : ")
        fin = int(input())

    if deb > fin:
        print('Attention! Le début de la location est après la fin\n')
        print('Resaisir heures:')
        print("Donnez l'heure de début de la location (un entier) : ")
        deb = int(input())
        print("Donnez l'heure de fin de la location (un entier) : ")
        fin = int(input())
    heures = fin - deb

    if deb >= 0 and fin <= 7:
        tarif1 = 7 - heures

    if deb >= 7 and fin <= 17:
        tarif2 = (17 - heures) * 2

    if deb >= 17 and fin <= 24:
        tarif3 = (24 - heures)

    print(tarif1 + tarif2 + tarif3)

    print("Vous avez loué votre vélo pendant")







