def print_a(arr):
    for i in range(len(arr)-1):
        print(arr[i],end=' ')
    print(arr[len(arr)-1])


def count_sort(arr):
    arr_max = max(arr)
    arr_min = min(arr)
    temp = [0]*(arr_max-arr_min+1)
    for i in range(len(arr)):
        temp[arr[i]-arr_min] += 1
    a = 0
    for i in range(len(temp)):
        for j in range(temp[i]):
            arr[a] = i + arr_min
            a += 1
    print_a(arr)


if __name__ == '__main__':
    # while True:
    #     try:
    #         arr = input().split()
    #         arr = [int(i) for i in arr]
    #         length = arr[0]
    #         arr = arr[1:length+1]
    #         count_sort(arr)
    #     except EOFError:
    #         break
    arr = [24,3,56,34,3,78,12,49,84,51,9,100]
    count_sort(arr)