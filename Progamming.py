number = int(input('Nhap 1 so tu nhien :'))


def Base(row):
    i = 1
    pascal_book = []
    while i <= number:
        if i == 1:
            pascal_book.append([1])
        else:
            pascal_book.append([1, 1])
        i += 1

    return pascal_book


def Logic(list):
    i = 2
    while i < len(list):
        for x in range(0, len(list[i - 1]) - 1):
            T = list[i - 1][x] + list[i - 1][x + 1]
            list[i].insert(x + 1, T)
        i += 1
    return list


def Output(list):
    for i in range(0, len(list)):
        x = f"{list[i]}"
        Q = True
        while len(x) < len(f"{list[-1]}"):
            if Q:
                x = x + ' '
                Q = False
            else:
                x = ' ' + x
                Q = True
        print(x)


Output(Logic(Base(number)))
print(Logic(Base(number)))

