array = [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]


def largest_range(array):
    array1 = []
    [array1.append(i) for i in array if i not in array1]
    array1.sort()
    array_sort = []
    while array1:
        cmin = min(array1)
        cmax = max(array1)
        clist = []
        for i in range(cmin,cmax+1):
            if i == array1[0]:
                clist.append(array1.pop(0))
            else:
                break
        array_sort.append(clist)
        index = max(enumerate(array_sort), key = lambda tup: len(tup[1]))
    return [index[1][0],index[1][-1]]


print(largest_range(array))

























