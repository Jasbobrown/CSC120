def main():
    x = input("File to scan:")
    x = x.lstrip().rstrip()
    file = open(x)
    D, L = {}, []
    for line in file.readlines():
        if not line or not line.strip() or line.lstrip()[0] == '#':
            continue
        if line.split()[0] in D:
            D[line.split()[0]] += int(line.split()[1])
        else:
            D[line.split()[0]] = int(line.split()[1])
    
    print("STEP 1: THE ORIGINAL DICTIONARY")
    for k in sorted(D.keys()):
        print(f"Key: {k} Value: {D[k]}")

    print("STEP 2: A LIST OF VALUE->KEY TUPLES")
    for k in sorted(D.keys()):
        L.append((D[k], k))
    print(L)
    
    print("STEP 3: AFTER SORTING")
    print(sorted(L))

    print("STEP 4: THE ACTUAL OUTPUT")
    for i in sorted(L):
        print(f"{i[1]} {i[0]}")

main()