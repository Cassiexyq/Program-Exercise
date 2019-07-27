# def hanoi(n,a,b,c):
#     if n == 1:
#         # print("%d, %s,%s" %(n, a, b))
#         # print("%d, %s,%s" % (n, b, c))
#         return 2
#     else:
#         num1 = hanoi(n-1, a, b,c)
#         # print("%d, %s,%s" %(n, a, b))
#         num2 =hanoi(n-1, c, b,a)
#         # print("%d, %s,%s"%(n, b,c))
#         num3 =hanoi(n-1, a,b,c)
#         result = num1+num2+num3+2
#         return result


def hanoi(n):
    if n == 1:
        return 2
    else:
        return hanoi(n-1)*3+2


if __name__ == '__main__':
    while True:
        try:
            a = input()
            # result = hanoi(int(a),'A','B','C')
            result = hanoi(int(a))
            print(result)
        except EOFError:
            break