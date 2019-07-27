# def solution(str_arr):
#     size = len(str_arr)
#     longest = 1
#     for i in range(2,size+1):
#         for x in range(size - i + 1):
#             t = x
#             temp = []
#             for j in range(i):
#                 temp.append(int(str_arr[t]))
#                 t = t+1
#             if check_Sum(temp) == True and len(temp) > longest:
#                 longest = len(temp)
#     print(longest)
#
#
# def check_Sum(arr):
#     size = len(arr)
#     if size == 1:
#         return True
#     inter = int(size / 2)
#     if size % 2 == 0:
#         left = sum(arr[:inter])
#     else:
#         left = sum(arr[:inter+1])
#
#     right = sum(arr[inter:size])
#     if left == right:
#         return True
#     else:
#         return False

def solution(s):
    flag = True
    for i in range(len(s), -1, -1):
        if i % 2 == 0 and flag:
            for j in range(0, len(s) - i + 1):
                sum1 = 0
                sum2 = 0
                for m in range(j, j + int(i / 2)):
                    sum1 += s[m]
                for n in range(j + int(i / 2), j + i):
                    sum2 += s[n]
                if sum1 == sum2:
                    print(i)
                    flag = False
                    break


if __name__ == '__main__':
    # arr = [4,3,4,7]
    xun = int(input())
    for i in range(xun):
        str_arr = list(map(int,input()))
        solution(str_arr)
