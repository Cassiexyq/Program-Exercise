def getinput():
    a = input()
    w = input()
    a = a.split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
    return a,int(w)


def getCount(arr, w):
    count = 0
    for i in range(len(arr)-1):
        new_arr = [arr[i]]
        # new_arr.append(arr[i])
        for j in range(i+1, len(arr),1):
            new_arr.append(arr[j])
            if max(new_arr)-min(new_arr)>w:
                count = count+1
    print(count)


if __name__ == '__main__':
    # a = [3, 6, 4, 3, 2]
    # w = 2
    a,w = getinput()
    getCount(a, w)