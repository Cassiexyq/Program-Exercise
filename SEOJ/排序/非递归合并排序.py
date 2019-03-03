def print_a(arr):
    for i in range(len(arr)-1):
        print(arr[i],end=' ')
    print(arr[len(arr)-1])


def merge(arr, low,mid,height):
    left = arr[low:mid]
    right = arr[mid:height]
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    arr[low:height] = result


def merge_sort(arr):
    i = 1
    while i < len(arr):
        low = 0
        while low < len(arr):
            mid = low + i
            height = min(low + 2*i, len(arr))
            if mid < height:
                merge(arr, low, mid, height)
            low += 2*i
        i *= 2
    print_a(arr)


if __name__ == '__main__':
    while True:
        try:
            arr = input().split()
            arr = [int(i) for i in arr]
            length = arr[0]
            arr = arr[1:length+1]
            merge_sort(arr)
        except EOFError:
            break
    # arr = [24,3,56,34,3,78,12,49,84,51,9,100]
    # merge_sort(arr)