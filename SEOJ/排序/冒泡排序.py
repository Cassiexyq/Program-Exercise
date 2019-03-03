def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def print_a(arr):
    for i in range(len(arr)-1):
        print(arr[i],end=' ')
    print(arr[len(arr)-1])


def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    print_a(arr)


if __name__ == '__main__':
    while True:
        try:
            arr = input().split()
            arr = [int(i) for i in arr]
            length = arr[0]
            arr = arr[1:length+1]
            bubble(arr)
        except EOFError:
            break