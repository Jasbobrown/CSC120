while True:
    x = input()
    if 'quit' in x:
        break
    print(len(x) - len(x.lstrip()))