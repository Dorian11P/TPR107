d=int(input("Heure de début de location : "))
f=int(input("Heure de début de fin : "))
htarif1=0
htarif2=0
while d==f or d<0 or d>25 or f<0 or f>24 or f<d :
     if (d == f):
         print("Attention ! l’heure de fin est identique à l’heure de début.")
     elif(d>24 or d<0 or f>24 or f<0):
         print("Les heures doivent être comprises entre 0 et 24 ! ")
     elif(d>f):
         print(" Attention ! le début de la location est après la fin ... ")
     d=int(input("Donnez l’heure de début de la location (un entier) : "))
     f= int(input("Donnez l’heure de fin de la location (un entier) : "))

print("Vous avez loué votre vélo pendant...")
for i in range (d,f):
    if(i<7 or i>=17):
        htarif1+=1
    else:
        htarif2+=1
if(htarif1>0):
    print(htarif1,"heure(s) au tarif horaire de 1.0 euro(s)")
if(htarif2>0):
    print(htarif2,"heure(s) au tarif horaire de 2.0 euro(s)")
print("Le montant total à payer est de: ",htarif1+htarif2*2," euros")

