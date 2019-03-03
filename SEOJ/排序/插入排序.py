def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def print_a(arr):
    for i in range(len(arr)-1):
        print(arr[i],end=' ')
    print(arr[len(arr)-1])


def insert_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                swap(arr, j-1, j)
            else:
                break

    print_a(arr)


if __name__ == '__main__':
    while True:
        try:
            arr = input().split()
            arr = [int(i) for i in arr]
            length = arr[0]
            arr = arr[1:length+1]
            insert_sort(arr)
        except EOFError:
            break