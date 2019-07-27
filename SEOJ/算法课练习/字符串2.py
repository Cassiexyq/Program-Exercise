def solution(arr_str, search):
    locate = []
    for i in range(len(arr_str)):
        if arr_str[i] == search[0]:
            locate.append(i)
    # print(locate)
    ant = []
    for j in locate:
        temp = j
        if temp + len(search) > len(arr_str):
            continue
        ant.append(str(j))
        for t in range(len(search)):
            if arr_str[temp] == search[t]:
                temp = temp + 1
            else:
                ant.pop(-1)
                break
    print(' '.join(ant))


if __name__ == "__main__":
    # arr_str = "THIS IS A TEST TEXT"
    # search = "TEST"
    # solution(arr_str,search)
    xun = int(input())
    for i in range(xun):
        arr_str, search = input().split(',')
        solution(arr_str,search)