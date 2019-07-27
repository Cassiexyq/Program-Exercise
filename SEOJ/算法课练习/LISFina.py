from collections import deque
import copy


def idS(arr):
    queue = deque()
    result = deque()
    queue.append({"i": 0, "list": [arr[0]]})
    queue.append({"i": 0, "list": []})
    while queue:
        t = queue.popleft()
        i = t['i']
        l = copy.copy(t['list'])
        i += 1
        if i <= len(arr):
            if i == len(arr):
                j = 1
                while j < len(l):
                    if l[j] <= l[j-1]:
                        break
                    j += 1
                flag = True
                while j < len(l):
                    if l[j] >= l[j - 1]:
                        flag = False
                        break
                    j += 1
                if flag:
                    while result and len(result[-1]) < len(l):
                        result.pop()

                    if result:
                        if len(result[-1]) == len(l):
                            result.append(l)
                    else:
                        result.append(l)
            else:
                if result:
                    if len(result[0]) > len(l) + len(arr) - i:
                        continue
                queue.append({"i": i, "list": l})
                c = copy.copy(l)
                c.append(arr[i])
                queue.append({"i": i, "list": c})
    return result


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    # arr = [1, 2, 4, 7, 11, 10, 9, 3, 5, 8, 6]
    # a = [2,5,7, 4,12,45,8,4,10,2]
    # arr = [2, 11, 3, 6, 5, 12]
    s = idS(arr)
    while s:
        print(" ".join(str(item) for item in s[-1]))
        s.pop()