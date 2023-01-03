date_exemple = input("Entrer une année ")
def est_date_valide(chaine_date):
  # Vérifier si la date est au bon format
  if len(chaine_date) != 8:
    print("Format de date non valide. Veuillez entrer la date au format 'jjmmaaaa'.")
    return False
  
 
  
  # Extraire le jour, le mois et l'année de la chaîne de date
  jour = int(chaine_date[:2])
  mois = int(chaine_date[2:4])
  annee = int(chaine_date[4:])
  
  # Vérifier si l'année est une année bissextile
  if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    annee_bissextile = True
  else:
    annee_bissextile = False
  
  # Vérifier si le mois est valide
  if mois < 1 or mois > 12:
    print("Mois non valide. Veuillez entrer un mois entre 1 et 12.")
    return False
  
  # Vérifier si le jour est valide pour le mois donné
  if mois == 2:
    # Février
    if annee_bissextile:
      # Année bissextile
      if jour < 1 or jour > 29:
        print("Jour non valide pour le mois de février dans une année bissextile. Veuillez entrer un jour entre 1 et 29.")
        return False
    else:
      # Année commune
      if jour < 1 or jour > 28:
        print("Jour non valide pour le mois de février dans une année commune. Veuillez entrer un jour entre 1 et 28.")
        return False
  elif mois in (4, 6, 9, 11):
    # Avril, juin, septembre, novembre
    if jour < 1 or jour > 30:
      print(f"Jour non valide pour le mois de {mois}. Veuillez entrer un jour entre 1 et 30.")
      return False
  else:
    # Janvier, mars, mai, juillet, août, octobre, décembre
    if jour < 1 or jour > 31:
      print(f"Jour non valide pour le mois de {mois}. Veuillez entrer un jour entre 1 et 31.")
      return False
  
  # Si tous les tests passent, la date est valide
  return True

# Tester la fonction avec une date d'exemple

if est_date_valide(date_exemple):
  print("La date est valide.")
else:
  print("La date n'est pas valide.")