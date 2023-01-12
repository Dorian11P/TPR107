print("Saisir le nombre de minutes : ")
minutes = int(input())
reste = minutes % 1440 
nbjours = (minutes - reste) /1440
nbheures = (reste -(reste % 60))/60
reste = reste % 60
nbminutes = reste
print("Nb de minutes",int(nbjours),"jours",int(nbheures),"heures", nbminutes,"minutes")
