
def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg
nombreEtudiants = int(input("Donnez le nombre d'étudiants"))
moyenne = 0.0;
notes = []
i = 0
nb = 0


while nb < nombreEtudiants:

    nb = nb + 1
    notes_test = int(input(F'Note etudiant {nb}: ='))
    if not (notes_test <= 20 and notes_test >=0):
        while notes_test > 20 or notes_test <0:
            print("Retapez un nombre")
            notes_test = int(input(F'Note etudiant {nb}: ='))
    notes.append(notes_test)


for i in range(nombreEtudiants) :




    i = i + 1

print("La moyenne de classe est :", cal_average(notes))
print("\n")
print('Num étudiant | note | ecart')
i = 0
for i in range(nombreEtudiants) :

    print(F'{i} | {notes[i]} | {round(cal_average(notes) - notes[i], 2)} ')
    i = i + 1