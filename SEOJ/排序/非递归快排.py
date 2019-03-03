def print_a(arr):
    for i in range(len(arr)-1):
        print(arr[i],end=' ')
    print(arr[len(arr)-1])


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr)-1)
    stack.append(0)
    while stack:
        left = stack.pop()
        right = stack.pop()

        if left < right:
            index = partition(arr, left, right)
            if index > left:
                stack.append(index-1)
                stack.append(left)

            if right > index:
                stack.append(right)
                stack.append(index+1)
    print_a(arr)


def partition(arr,left,right):
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot
    return left


if __name__ == '__main__':
    while True:
        try:
            arr = input().split()
            arr = [int(i) for i in arr]
            length = arr[0]
            arr = arr[1:length+1]
            quick_sort(arr)
        except EOFError:
            break
    # arr = [24,3,56,34,3,78,12,49,84,51,9,100]
    # quick_sort(arr)