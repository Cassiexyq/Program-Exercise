def findsubstr(arr):
    size = len(arr)
    result = []
    if size == 0:
        return result
    elif size <= 2:
        if size == 1:
            result.append(arr[0])
        elif size == 2:
            if arr[0] > arr[1]:
                result.append(arr[0])
            else:
                result.append(arr[0])
                result.append(arr[1])
    else:
        result.append(arr[0])
        for i in range(1, size):
            if arr[i] > result[-1]:
                result.append(arr[i])
            elif len(result) >= 2 and arr[i] > result[-2] and arr[-1] < result[-1]:
                result.pop()
                result.append(arr[i])
    # print(result)
    return result


def formate(arr,temp):
    result = ""
    for item in arr:
        result = result + temp[item]
    print(result)


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    # str1 = "1A2BD3G4H56JK"
    # str2 = "23EFG4I5J6K7"
    common = [i for i in str1 if i in str2]
    index_com = []
    common_index = []
    for item in common:
        index_com.append(str2.index(item))
    for i in range(len(index_com)):
        a = index_com[0:i]
        b = index_com[i:]
        # print("第"+str(i)+"次循环")
        sub_a = findsubstr(a)
        sub_b = findsubstr(b)
        if len(sub_a) > 0 and len(sub_b) > 0 and sub_a[-1] < sub_b[0]:
            sub_a.extend(sub_b)
            # print("公共子序列：{}".format(sub_a))
            if sub_a not in common_index:
                common_index.append(sub_a)
    # print("公共子序列：{}".format(common_index))
    maxLength = 0
    for item in common_index:
        maxLength = max(maxLength, len(item))
    for i in common_index:
        if len(i) == maxLength:
            formate(i, str2)
