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

# 改进，如果没有发生内部交换说明已经有序，则直接退出
def bubble2(arr):
    for i in range(len(arr)-1):
        flag = 1
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 0
        if flag == 1:
            break
# 记录上次交换的最后的一个位置
def bubble3(arr):
    k = 0
    pos = 0
    for i in range(len(arr)-1):
        flag = 1
        for j in range(k):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                flag = 0
                pos = j
        k = pos
        if flag == 1:
            return

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