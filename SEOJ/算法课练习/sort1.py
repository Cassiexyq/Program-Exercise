def check_frecquency(arr):
    arr = sorted(arr, reverse=False)
    # print(arr)
    dict_arr = {}
    for i in arr:
        if i in dict_arr.keys():
            dict_arr[i] += 1
        else:
            dict_arr[i] = 1
    # print(dict_arr)
    dict_arr = sorted(dict_arr.items(),key=lambda d:d[1],reverse=True)
    result = []
    # print(dict_arr)
    for i in range(len(dict_arr)):
        value = dict_arr[i][0]
        num = dict_arr[i][1]
        # print(i)
        for j in range(num):
            result.append(value)
    for i in result:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    # arr = [5,5,4,6,4,3]
    # check_frecquency(arr)
    num = int(input())
    for i in range(num):
        length = int(input())
        arr = input().split(' ')
        # print(arr)
        # new_arr = [length]
        arr = arr[:length]
        for i in range(length):
            arr[i] = int(arr[i])
        check_frecquency(arr)

