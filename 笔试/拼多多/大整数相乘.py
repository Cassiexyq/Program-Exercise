# -*- coding: utf-8 -*-

# @Author: xyq



def solution(s1, s2):
    l1 = list(reversed(list(map(lambda x: int(x), s1))))
    l2 = list(reversed(list(map(lambda x: int(x), s2))))
    # print(l1)
    # print(l2)
    c = [0]*(len(l1)+len(l2))
    for i in range(len(l1)):
        for j in range(len(l2)):
            c[i+j] += l1[i] * l2[j]
            if c[i+j] >= 10:
                c[i+j+1] += int(c[i+j]/10)
                c[i+j] %= 10
    res = []
    # print(c)
    flag = 0
    for i in range(len(c)-1,-1,-1):
        if flag == 0 and c[i] == 0:
            continue
        else:
            res.append(str(c[i]))
            flag = 1
    if res:
        return "".join(res)
    else:
        return 0


if __name__ == '__main__':
    s1,s2 = input().split()
    res = solution(s1,s2)
    print(res)