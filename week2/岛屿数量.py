# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def search(grid: List[List[str]], i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            search(grid, i- 1, j)
            search(grid, i + 1, j)
            search(grid, i, j - 1)
            search(grid, i, j + 1)

        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    search(grid, i, j)

        return count