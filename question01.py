def full_name(first_name, last_name):
    return first_name+' '+last_name


def string_alternative(full_name):
    return full_name[0: len(full_name): 2]


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(string_alternative(full_name(first_name, last_name)))


if __name__ == '__main__':
    main()
