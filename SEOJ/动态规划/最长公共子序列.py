def LCS(arr1, arr2):
    result = [[0 for i in range(len(arr2)+1)] for j in range(len(arr1) + 1)]
    dp = [[None for i in range(len(arr2)+1)] for j in range(len(arr1) + 1)]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                result[i+1][j+1] = result[i][j] + 1
                dp[i+1][j+1] = 'ok'
            elif result[i+1][j] > result[i][j+1]:
                result[i+1][j+1] = result[i+1][j]
                dp[i+1][j+1] = 'left'
            else:
                result[i+1][j+1] = result[i][j+1]
                dp[i+1][j+1] = 'up'
    # return result, dp
    # for i in result:
    #     print(i)
    # for j in dp:
    #     print(j)
    return dp


def printlcs(dp, arr, i,j):
    if i == 0 or j == 0:
        return
    if dp[i][j] == 'ok':
        printlcs(dp, arr, i-1, j-1)
        print(arr[i-1],end='')
    elif dp[i][j] == 'left':
        printlcs(dp, arr, i,j-1)
    else:
        printlcs(dp, arr,i-1,j)


if __name__ == '__main__':
    arr1 = '1A2BD3G4H56JK'
    arr2 = '23EFG4I5J6K7'
    dp = LCS(arr1,arr2)
    printlcs(dp, arr1, len(arr1), len(arr2))