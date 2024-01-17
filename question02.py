import os

def main():
    dict = {}
    with open('input.txt', 'r') as fp:
        for each_line in fp.readlines():
            for word in each_line.strip().split(' '):
                dict.setdefault(word, 0)
                dict[word] = dict[word]+1

    os.remove('output.txt')

    for k, v in dict.items():
        print(f'{k} : {v}')

    for k, v in dict.items():
        with open('output.txt', 'a') as fp:
            fp.write(f'{k}: {v}\n')


if __name__ == '__main__':
    main()