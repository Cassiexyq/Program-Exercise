# -*- coding: utf-8 -*-

# @Author: xyq


M = ["","M","MM","MMM","MMM"]
C = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
X = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
I = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
n = int(input())
res = M[n//1000] + C[n%1000//100] + X[n%100//10] + I[n%10]
print(res)

# dic = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
# arr = [1,5,10,50,100,500,1000]
# n = int(input())
# res = []
# for i in range(len(arr)-1,-1,-1):
#     if n < arr[i]:
#         continue
#     else:
#         geshu = n // arr[i]
#         for _ in range(geshu):
#             res.append(dic[arr[i]])
#         n -= geshu * arr[i]
# print("".join(res))

