def main():
    lst1 = [int(val) for val in input("Enter Height in Inches: ").split(' ')]
    lst_cm = [val * 2.54 for val in lst1]
    print("Height in Centimeters: ")
    print(lst_cm)


if __name__ == '__main__':
    main()
