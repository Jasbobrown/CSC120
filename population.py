def main():
    x = input("file: ")
    x = x.lstrip().rstrip()
    file = open(x)
    states, population = [], 0
    for line in file.readlines():
        if not line or not line.strip() or line.lstrip()[0] == '#':
            continue
        if len(line.split(' ', 1)) > 1:
            state = line.split(' ', 1)[0] + ' ' + line.split(' ', 1)[1].split()[0]
            pop = line.split(' ', 1)[1].split()[1]
            states.append(state)
            population += int(pop)
            print(f"State/Territory: {state}")
            print(f"Population: {int(pop)}")
            print()
        else:
            state = line.split()[0]
            pop = line.split()[1]
            states.append(state)
            pops += int(pop)
            print(f"State/Territory: {state}")
            print(f"Population: {int(pop)}")
            print()
    print(f"# of States/Territories: {len(states)}")
    print(f"Total Population: {population}")

main()