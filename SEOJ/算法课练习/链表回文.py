def getHuiwen(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    while True:
        try:
            arr = input().split()
            length = int(arr[0])
            arr = arr[1:length+1]
            if getHuiwen(arr) == True:
                print('true')
            else: print('false')
        except EOFError:
            break