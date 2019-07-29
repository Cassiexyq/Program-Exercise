# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not len(grid): return 0
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.dfs(grid, i, j)
                    num += 1
        return num

    def dfs(self,grid,i,j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j]:
            return
        grid[i][j] = False
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        return
s = Solution()
res = s.numIslands([[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]])
print(res)