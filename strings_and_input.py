def something():
    x = input("input string: ")
    print(len(x))
    print(x[1])
    print(x[:9])
    print(x[:-5])
    print(x.upper())
    if x[0].lower() in 'qwerty':
        print("QWERTY")
    elif x[0] in 'uiop':
        print("UIOP")
    elif x[0].isalpha():
        print("LETTER")
    elif x[0].isdigit():
        print("DIGIT")
    else:
        print("OTHER")
        
    y, z = input(), input()
    print(int(y) * int(z))
