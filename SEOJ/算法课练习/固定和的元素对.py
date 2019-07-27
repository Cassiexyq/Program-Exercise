def getinput():
    a = input()
    w = input()
    a = a.split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
    return a,int(w)


def getCount(arr,sum):
    arr = sorted(arr)
    # print(arr)
    count = 0
    i = 0
    j = len(arr) - i - 1
    while True:
        if i >= j or i > len(arr) or j < 0:
            break
        while (arr[i] + arr[j]) >= sum:
            if j < 0:
                break
            if (arr[i] + arr[j]) == sum:
                count = count+1
            j = j - 1
        i = i+1
    print(count)


if __name__ == '__main__':
    # a = [1,2,4,7,11,0,9,5]
    # w = 11
    a,w = getinput()
    getCount(a,w)