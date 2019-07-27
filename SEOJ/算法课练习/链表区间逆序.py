def print_a(arr):
    for i in range(len(arr)-1):
        print(arr[i],end=' ')
    print(arr[len(arr)-1])


def reverse_link(arr,k):
    step = 0
    length = len(arr)
    while step < length:
        end = step + k
        if end <= length:
            temp = arr[step:end]
            temp.reverse()
            arr[step:end] = temp
        step = step + k
    print_a(arr)


if __name__ == '__main__':
    while True:
        try:
            arr = input().split()
            # arr = [int(i) for i in arr]
            length = int(arr[0])
            size = int(arr[-1])
            arr = arr[1:length+1]
            reverse_link(arr,size)
        except EOFError:
            break


