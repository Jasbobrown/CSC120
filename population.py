def main():
    x = input("file: ")
    x = x.lstrip().rstrip()
    file = open(x)
    states, population, multiWord = [], 0, 0
    for line in file.readlines():
        if not line or not line.strip() or line.lstrip()[0] == '#':
            continue

        for i in range(1, len(line) - 1):
            if line[i] == ' ' and line[i-1].isalpha() and line[i+1].isalpha():
                multiWord += 1 

        if multiWord:
            state = " ".join(line.split(' ')[:multiWord + 1])
            pop = line.split()[-1]
            states.append(state)
            population += int(pop)
            print(f"State/Territory: {state}")
            print(f"Population: {int(pop)}")
            print()
            multiWord = 0

        else:
            state = line.split()[0]
            pop = line.split()[1]
            states.append(state)
            population += int(pop)
            print(f"State/Territory: {state}")
            print(f"Population: {int(pop)}")
            print()
            
    print(f"# of States/Territories: {len(states)}")
    print(f"Total Population: {population}")

main()