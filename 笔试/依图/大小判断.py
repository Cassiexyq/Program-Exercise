# -*- coding: utf-8 -*-

# @Author: xyq

def check(quest, eq, sm):
    for i in range(len(eq)):
        if quest[0] in eq[i] and quest[1] in eq[i]:
            return 1
    for i in range(len(sm)):
        if sm[i][0] == quest[0] and sm[i][1] == quest[1]:
            return 0
    return 3

def create(eq):
    res = [eq[0]]
    flag = 0
    for i in range(1,len(eq)):
        for j in res:
            if eq[i][0] in j:
                j.append(eq[i][1])
                flag = 1
                break
            if eq[i][1] in j:
                j.append(eq[i][0])
                flag = 1
                break
        if flag == 0:
            res.append(eq[i])
        flag = 0
    return res

def create2(res, sm):
    new_sm = []
    for i in range(len(sm)):
        new_sm.append([sm[i][0],sm[i][1]])
        for j in range(len(res)):

            if sm[i][0] in res[j]:
                for k in res[j]:
                    new_sm.append([k, sm[i][1]])
            if sm[i][1] in res[j]:
                for k in res[j]:
                    new_sm.append([sm[i][0],k])

    return new_sm

def main():
    line = input()
    if line == ' ':
        line = input()
    n,m,k = list(map(int, line.split()))
    eq = []
    sm = []
    for _ in range(m):
        line = input()
        if line == ' ':
            line = input()
        a,b,c = list(map(int, line.split()))
        if c == 1:
            eq.append([a,b])
        if c == 0:
            sm.append([a,b])
    question = []
    for _ in range(k):
        question.append(list(map(int, input().split())))
    # eq.sort(key=lambda x: x[0]+x[1])
    res = create(eq)
    # print(res)
    new_sm = create2(res,sm)
    # print(new_sm)
    for i in question:
        print(check(i,res, new_sm))


if __name__ == '__main__':
    main()

