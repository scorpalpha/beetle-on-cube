import math


def tupler(lst, N):
    list_tups = []
    set = 0
    for i in range(N):
        F_val = ""

        x = lst[set]
        y = lst[set+1]
        z = lst[set+2]
        if x != 0 and x != 10:
            if y == 0:
                F_val = "F"
            elif y == 10:
                F_val = "H"
            else:
                F_val = "T"
        elif x == 0:
            F_val = "L"
        elif x == 10:
            F_val = "R"
        else:
            F_val = "I"
        tup = (x, y, z, F_val)
        list_tups.append(tup)
        set = set+3
    return list_tups


def distancer(lst, N):
    k, dist = 0, 0
    dist_list = []
    while k < N-1:
        dist = math.sqrt(
            (((lst[k+1][0])-(lst[k][0]))**2) +
            (((lst[k+1][1])-(lst[k][1]))**2) +
            (((lst[k+1][2])-(lst[k][2]))**2)

        )
        print(lst[k+1][3], lst[k][3])

        if lst[k+1][3] == lst[k][3]:
            dist = round(((math.pi/3)*dist), 2)
            print(dist)
        else:
            tup1 = face_changer(lst[k+1])
            print(tup1)
            tup2 = face_changer(lst[k])
            print(tup2)
            dist = math.sqrt(
                ((tup1[0]-tup2[0])**2) +
                ((tup1[1]-tup2[1])**2) +
                ((tup1[2]-tup2[2])**2)

            )
            print(dist)
        dist_list.append(dist)
        k = k+1
    return dist_list


def face_changer(tup1):
    if tup1[3] == "R":
        x1 = (10+(10-tup1[2]))
        new_cor_tup1 = (x1, tup1[1], 10)
    elif tup1[3] == "L":
        x1 = (-1*(10-tup1[2]))
        new_cor_tup1 = (x1, tup1[1], 10)
    elif tup1[3] == "H":
        y1 = (10+(10-tup1[2]))
        new_cor_tup1 = (tup1[0], y1, 10)
    elif tup1[3] == "F":
        y1 = -1*(10-tup1[2])
        new_cor_tup1 = (tup1[0], y1, 10)
    else:
        new_cor_tup1 = tup1

    return new_cor_tup1


lst = [1, 1, 10, 2, 1, 10, 0, 5, 9, 0, 0, 10]
N = 4
p = tupler(lst, N)
print(sum(distancer(p, N)))
