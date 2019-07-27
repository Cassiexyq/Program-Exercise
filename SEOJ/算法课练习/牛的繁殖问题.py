def main(n):
    i = 3
    a = 1
    b = 1
    c = 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        while i < n:
            a = a + c
            c = b
            b = a
            i += 1
        return a + b + c


if __name__ =="__main__":
    xun = int(input())
    for i in range(xun):
        n = int(input())
        print(main(n))
