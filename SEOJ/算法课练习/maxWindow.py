def getinput():
    a = input()
    w = input()
    a = a.split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
    return a,int(w)


def getMaxWindow(arr, w):
    if arr == None or w < 1 or len(arr) < w:
        return
    res = []
    deque = []
    for i in range(len(arr)):
        while deque and arr[deque[-1]] <= arr[i]:
            deque.pop()
        deque.append(i)
        if deque[0] <= i-w:
            deque.pop(0)
        if i-w+1 >= 0:
            res.append(arr[deque[0]])
    return res


if __name__ == '__main__':
    a, w = getinput()
    res = getMaxWindow(a,w)
    if res == None:
        print(0)
    else:
        print(sum(res))



