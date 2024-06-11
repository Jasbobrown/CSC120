def main():
    x = input("File to scan:")
    x = x.lstrip().rstrip()
    file = open(x)
    D, L = {}, []
    for line in file.readlines():
        if not line or not line.strip() or line.lstrip()[0] == '#':
            continue
        
        print(line.split())
        if line.split()[0] in D:
            D[line.split()[0]] += int(line.split()[1])
        else:
            D[line.split()[0]] = int(line.split()[1])
        
    for k,v in D.items():
        L.append((v, k))
    
    for tup in sorted(L):
        print(tup[0], tup[1])
        