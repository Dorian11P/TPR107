def tri_bulle(liste):
  # Obtenir la longueur de la liste
  n = len(liste)
  
  # Effectuer le tri en bulle
  for i in range(n):
    for j in range(n - i - 1):
      if liste[j] > liste[j + 1]:
        # Échanger les valeurs
        liste[j], liste[j + 1] = liste[j + 1], liste[j]
    
    # Afficher la liste après chaque itération
    print(liste)
  return liste

# Tester la fonction avec une liste d'exemple
liste_exemple = [5, 2, 4, 8, 1, 3]
print(tri_bulle(liste_exemple))
