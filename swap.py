def main():
    x = input("Please give a string to swap:")
    x = x.lstrip().rstrip()
    if len(x) % 2 == 0:
        print(x[len(x)/2:] + x[:len(x)/2])
    print(x[(len(x)//2) + 2:] + x[(len(x)//2) + 1] + x[:len(x)//2])
main()

