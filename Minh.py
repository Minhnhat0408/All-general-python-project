person1 = [["9:00", "10:30"], ["12:00", "13:00"], ["15:00", "18:00"]]
person2 = [["10:00", "11:30"], ["12:30", "14:30"], ["15:00", "15:30"],
           ['16:00', '17:00'], ['17:30', '19:00'], ['20:00', '21:00'], ['23:00', '24:00']]
import math


def FreeTime(sch1, sch2):
    list_nottime = []
    p1 = 0
    p2 = 0
    listok = []
    run = True
    while run:
        if Gettime(sch1[p1][0], sch2[p2][0]) == 1:
            list_nottime.append(sch1[p1])
            p1 += 1
        elif Gettime(sch1[p1][0], sch2[p2][0]) == 2:
            list_nottime.append(sch2[p2])
            p2 += 1
        else:
            if Gettime(sch1[p1][1], sch2[p2][1]) == 1:
                list_nottime.append(sch1[p1])
                p1 += 1
            else:
                list_nottime.append(sch2[p2])
                p2 += 1
        if p1 == len(sch1):
            list_nottime.extend(sch2)
            for i in list_nottime:
                if i not in listok:
                    listok.append(i)
            run = False
        elif p2 == len(sch2) :
            list_nottime.extend(sch1)
            listok = []
            for i in list_nottime:
                if i not in listok:
                    listok.append(i)
            run = False
    print(f"Overall schedule after sorting in order : {listok}")
    i = 0
    while i < len(listok) - 1:
        end1 = listok[i][1]
        start2 = listok[i + 1][0]
        if Gettime(end1, start2) == 2:
            end2 = listok[i + 1][1]
            if Gettime(end2, end1) == 1:
                listok.pop(i + 1)
                i -= 1
            else:
                listok[i][1] = end2
                listok.pop(i + 1)
                i -= 1
        i += 1
    print(f"List of their both busy time :{listok}")
    dif(listok)


def Gettime(time1,time2):
    hour1, minutes1 = time1.split(":")
    hour2, minutes2 = time2.split(":")
    int_time1 = int(hour1) * 60 + int(minutes1)
    int_time2 = int(hour2) * 60 + int(minutes2)

    if int_time1 > int_time2:
        return 2
    elif int_time1 < int_time2:
        return 1
    else:
        return 0


def comparetimes(time1, time2):
    hour1, minutes1 = time1.split(":")
    hour2, minutes2 = time2.split(":")
    int_time1 = int(hour1) * 60 + int(minutes1)
    int_time2 = int(hour2) * 60 + int(minutes2)
    if math.fabs(int_time1 - int_time2) >= 30:
        return 0


def dif(list_sch):
    output = []
    i = 0
    while i < len(list_sch) - 1:
        end1 = list_sch[i][1]
        start2 = list_sch[i + 1][0]
        if comparetimes(end1, start2) == 0:
            output.append([end1, start2])

        i += 1
    print(f"Their available time: {output}")


FreeTime(person1, person2)
