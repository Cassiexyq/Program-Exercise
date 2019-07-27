def main(arr1, arr2):
    ant = []
    for i in arr2:
        count = 0
        for j in arr1:
            if j%i == 0:
                count += 1
        ant.append(str(count))
    print(' '.join(ant))


if __name__ == "__main__":
    xun = int(input())
    for i in range(xun):
        xun_ = list(map(int, input().split(' ')))
        arr1 = list(map(int,input().split(' ')))
        arr1 = arr1[:xun_[0]]
        # print(arr1)
        arr2 = list(map(int,input().split(' ')))
        arr2 = arr2[:xun_[1]]
        # print(arr2)
        main(arr1,arr2)