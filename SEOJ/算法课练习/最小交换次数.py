def getHUAN(arr):
    ans = 0
    vis = []
    m = []
    for i in range(max(arr)+1):
        m.append(0)
    for i in range(len(arr)+1):
        vis.append(0)
    for i in range(1,len(arr)+1,1):
        m[arr[i-1]] = i
    # print(vis)
    # print(m)
    arr = sorted(arr,reverse=False)
    for i in range(1,len(arr)+1,1):
        if vis[i] == 0:
            ans = ans+1
        j = i
        while vis[j] == 0:
            vis[j] = 1
            j = m[arr[j-1]]
    print(len(arr)-ans)


def getarr(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr


if __name__ == '__main__':
    # arr = [4,3,2,1]
    for i in range(int(input())):
        length = int(input())
        arr = getarr(input().split(' ')[:length])
        getHUAN(arr)