def pre(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr[i])):
            if arr[i][j] == 1 and arr[i][j-1] != 0:
                arr[i][j] = arr[i][j-1] + 1
    return arr


def calMax(prearr):
    maxsum = 0
    for i in range(len(prearr)):
        for j in range(len(prearr[i])):
            tmp = 0
            value = prearr[i][j]
            count = 0
            for up in range(i-1, -1 , -1):
                if prearr[up][j] >= value and value!=0:
                    count+=1
                else:
                    break
            for down in range(i+1, len(prearr)):
                if prearr[down][j] >= value and value!=0:
                    count+=1
                else:
                    break
            if count != 0:
                tmp = prearr[i][j]*(count+1)
            if tmp > maxsum:
                maxsum = tmp

    print(maxsum)


if __name__ == '__main__':
    a = []
    # a = [[1, 0, 1, 1],
    #     [1, 1, 1, 1],
    #     [1, 1, 1, 0]]
    while True:
        try:
            an = input().split(' ')
            for i in range(len(an)):
                an[i] = int(an[i])
            a.append(an)
        except EOFError:
            break
    a = pre(a)
    # print(a)
    calMax(a)
