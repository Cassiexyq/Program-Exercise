import random


def getinput():
    a = input()
    b = input()
    a = a.split(' ')
    b = b.split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
        b[i] = int(b[i])
    a.extend(b)
    # print(a)
    return a


def getMin(a):
    sum_all = sum(a)
    best = sum_all
    for i in range(600):
        new = random.sample(a,int(len(a)/2))
        diff = abs(sum_all-2*sum(new))
        if diff < best:
            best = diff
    print(best)


if __name__ == '__main__':
    # a = [100,99,98,1,2,3,1,2,3,4,5,40]
    a = getinput()
    getMin(a)


