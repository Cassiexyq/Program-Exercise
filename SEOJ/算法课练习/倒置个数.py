def getnum(arr):
    res = 0
    for i in range(len(arr)):
        x = arr[i]
        j = i-1
        while j >= 0 and arr[j] > x:
            res+=1
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = x
    print(res)


def getarr(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr


if __name__ == '__main__':
    for i in range(int(input())):
        length = int(input())
        arr = input().split(' ')
        arr = getarr(arr[:length])
        getnum(arr)
    # arr = [8,3,2,9,7,1,5,4]

