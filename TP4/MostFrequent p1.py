L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

def plus_freq(list):
  # Compte le nombre d'occurence
  frequencies = []
  for number in list:
    frequency = 0
    for i in range(len(list)):
      if list[i] == number:
        frequency += 1
    frequencies.append(frequency)
  
  # Trouve l'index du nombre le plus présent
  max_frequency_index = frequencies.index(max(frequencies))
  
  #Retourne le nombre le plus présent ainsi que le nombre de fois qu'il apparait
  return list[max_frequency_index], frequencies[max_frequency_index]

# Test de la méthode plus_freq

nombre_plus_freq, frequency = plus_freq(L1)
print(f"Le nombre le plus fréquent est : {nombre_plus_freq} ({frequency}x).")