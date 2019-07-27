'''
非连续性数组< num的情况
'''
def getZ(arr,w):
    if arr == None or len(arr) == 0:
        return 0
    res = 0
    qmin = []
    qmax = []
    arr_set = {}
    i = 0
    j = 0
    while i < len(arr):
        # if arr[i] in arr_set.keys():
        #     pass
        # else:
        #     arr_set[arr[i]] = i
        #     res += 1
        while j < len(arr):
            while qmax and arr[qmax[-1]] <= arr[j]:
                qmax.pop()
            qmax.append(j)
            while qmin and arr[qmin[-1]] >= arr[j]:
                qmin.pop()
            qmin.append(j)
            if arr[qmax[0]]-arr[qmin[0]] <= w:
                break
            j += 1
        res += i-j
        if qmax[0] == i:
            qmax.pop(0)
        if qmin[0] == i:
            qmin.pop(0)
        i += 1
    print(res)


def getinput():
    a = input()
    w = input()
    a = a.split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
    return a,int(w)


if __name__ == '__main__':
    a = [3,6,4,3,2]
    w = 2
    # a,w = getinput()
    getZ(a,w)