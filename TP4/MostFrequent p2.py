L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

def plus_freq(list):
  # Permet de compter la fréquence de chaque nombre
  frequencies = []
  for i in range(len(list)):
    frequency = list.count(list[i])
    frequencies.append(frequency)
  
  # Trouver l'index du nombre le plus fréquent
  max_frequency_index = frequencies.index(max(frequencies))
  
  # Return le nombre le plus fréquent et sa fréquence d'apparition
  return list[max_frequency_index], frequencies[max_frequency_index]

# Test avec une liste d'exmple

plus_freq_nombre, frequency = plus_freq(L1)
print(f"Le nombre le plus fréquent dans la liste est le :{plus_freq_nombre} ({frequency}x).")