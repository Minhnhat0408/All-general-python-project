# HE PHUONG TRINH
x = input("So he phuong trinh : ")


def matrix(number):
    matrix = []
    for i in range(1, int(number) + 1):
        row = input(f'Nhap he so cua dong {i}: ')
        roww = row.split()
        matrix.append(roww)
        #matrix.sort(reverse=True)
    return matrix


def algorithm(matrix):
    i = 0
    i1 = 0
    while i1 < int(x) - 1:
        # print(matrix)
        if float(matrix[i1][i1]) == 0:
            tg = matrix[i1 + 1]
            matrix[i1 + 1] = matrix[i1]
            matrix[i1] = tg
        s1 = float(matrix[i + 1][i1]) / float(matrix[i1][i1])
        for j in range(0, int(x) + 1):
            matrix[i + 1][j] = float(matrix[i + 1][j]) - float(matrix[i1][j]) * s1
        if i == int(x) - 2:
            i1 += 1
            i = i1
        else:
            i += 1
    return matrix


def result(laddermatrix, sohe):
    i = sohe - 1
    nghiem = []
    while i >= 0:
        a = float(laddermatrix[i][-1]) / float(laddermatrix[i][-2])
        for z in reversed(laddermatrix):
            if len(z) > 2:
                z[-1] = float(z[-1]) - a * float(z[-2])
                z.pop(-2)
        nghiem.append(round(a, 2))
        i -= 1
    [print(f"Gia tri cua x{a+1} : {b}") for a,b in enumerate(nghiem[::-1])]
    return 0



#result(algorithm(matrix(x)),int(x))
name  = "minh"
print("hello , ",name)

