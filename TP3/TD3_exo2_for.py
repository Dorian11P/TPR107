import time

i = 0
print("Nombre jusqu'à 0:")
x = int(input())
y = x
for i in range(0, y+1) :
    time.sleep(1)
    print(x)
    x = x - 1


