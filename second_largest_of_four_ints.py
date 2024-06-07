L = [int(input()), int(input()), int(input()), int(input())]
max, sec = L[0], L[0]
for i in L:
    if i > max:
        max = i
for i in L:
    if i > sec and i < max:
        sec = i
print(sec)