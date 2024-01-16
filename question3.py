def main():
    while True:
        score = int(input('Enter the input score: '))

        if 90 <= score <= 100:
            print("A")
        elif 80 <= score <= 89:
            print("B")
        elif 70 <= score <= 79:
            print("C")
        elif 60 <= score <= 69:
            print("D")
        elif 0 <= score <= 59:
            print("F")
        else:
            print("Input Valid Score!!")


if _name_ == '_main_':
    main()