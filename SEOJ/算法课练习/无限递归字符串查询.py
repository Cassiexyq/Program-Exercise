def main(time):
    src = "12345"
    for i in range(1,time+1):
        B = src[::-1]
        for j in range(1,i+1):
            src = src + "$"
        src = src + B
    print(src)
    return src


if __name__ == "__main__":
    time = int(input())
    src = main(time)
    for i in range(time):
        locate = int(input())
        print(src[locate-1])