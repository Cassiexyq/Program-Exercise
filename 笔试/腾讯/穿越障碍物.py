# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def __init__(self):
        self.maxl = 1000
        self.dx = [-1,1,0,0]
        self.dy = [0,0,-1,1]

    def dfs(self,x,y,cur):
        if x == r and y == c:
            if cur < self.maxl:
                self.maxl = cur
            return
        for i in range(4):
            xx = x + self.dx[i]
            yy = y + self.dy[i]
            if 0 <= xx < len(res) and 0 <=  yy < len(res[0]) and res[xx][yy] and not f[xx][yy]:
                f[xx][yy] = 1
                self.dfs(xx,yy,cur+1)
                f[xx][yy] = 0


r,c,n = list(map(int, input().split()))
r,c = r + 500, c + 500
res = [[1] * 1000 for _ in range(1000)]
f = [[0]*1000 for _ in range(1000)]
for _ in range(n):
    a,b = list(map(int, input().split()))
    res[a+500][b+500] = 0
f[500][500] = 1
s = Solution()
s.dfs(500,500,0)
print(s.maxl)
