"""
49 38 65 97 76 13 index= 2
错误： 49 38 65 13 76 97
正确： 49 13 65 38 76 97
"""
def shell_sort(arr, distance): # 错误的排序
    for gap in distance:
        for j in range( len(arr)):

            if j + gap > len(arr)-1:
                break

            if arr[j] > arr[j+gap]:
                arr[j], arr[j+gap] = arr[j+gap],arr[j]
                # temp = arr[j]
                # arr[j] = arr[j+i]
                # arr[j+i] = temp
    # print_a(arr)
    arr = list(map(lambda x:str(x), arr))
    print(" ".join(arr))

def ShellSort(arr,index):  # 正确的排序
    n = len(arr)
    for gap in index:
        for i in range(gap,n):
            for j in range(i,gap-1,-gap):
                if arr[j] < arr[j-gap]:
                    arr[j],arr[j-gap] = arr[j-gap],arr[j]
                else:
                    break
    arr = list(map(lambda x: str(x), arr))
    print(" ".join(arr))
    # return arr


if __name__ == '__main__':
    # arr = [49,38,65,97,76,13,27,49,55,4]
    xun = int(input())
    for i in range(xun):
        arr = list(map(int, input().split(' ')))
        distance = list(map(int, input().split(' ')))
        shell_sort(arr,distance)