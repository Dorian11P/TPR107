print("Nombre à tester :")

x = float(input())


if (-11 < x and (x < -2 or x == -2) or  (0 < x and (x < 1 or x == 1)) or ((x == 2 or 2 < x) and x < 3)) :
    print(x, "appartient à I")
else :
    print(x, "n'appartient pas à I")
