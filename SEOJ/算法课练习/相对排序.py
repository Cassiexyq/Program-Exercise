def checksort(arr1,arr2):
    dict_arr = {}
    for i in arr1:
        if i in dict_arr.keys():
            dict_arr[i] += 1
        else:
            dict_arr[i] = 1
    new_sort = []
    # print(dict_arr)
    for i in arr2:
        if i in dict_arr.keys():
            num = dict_arr[i]
            for j in range(num):
                new_sort.append(i)
            del dict_arr[i]
    # print(new_sort)
    dict_arr = sorted(dict_arr.items(),key=lambda d:d[0],reverse=False)
    for i in range(len(dict_arr)):
        num = dict_arr[i][1]
        for j in range(num):
            new_sort.append(dict_arr[i][0])
    for i in new_sort:
        print(i, end=' ')
    print()


def getarr(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr


if __name__ == '__main__':
    # arr1 = [2,1,2,5,5,1,9,3,6,8,8]
    # arr2 = [2,1,8,3]
    # checksort(arr1, arr2)
    num = int(input())
    for i in range(num):
        _length = input().split(' ')
        len1 = int(_length[0])
        len2 = int(_length[1])
        arr1 = input().split(' ')
        arr2 = input().split(' ')
        arr1 = getarr(arr1[:len1])
        arr2 = getarr(arr2[:len2])
        checksort(arr1,arr2)