def getinput():
    a = input()
    qujian = input()
    w = input()
    a = a.split(' ')
    qujian = qujian.split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
    left = int(qujian[0])
    right = int(qujian[1])
    return a,int(w),left,right


def getK(arr,k,left, right):
    if left > len(arr) or right < 0 or right-left+1 < k:
        return 0
    newarr = []
    for i in range(left-1,right,1):
        newarr.append(arr[i])
    newarr = sorted(newarr,reverse=False)
    return newarr[k-1]

if __name__ == '__main__':
    arr, w, left, right = getinput()
    print(getK(arr, w, left, right))
