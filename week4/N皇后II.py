# -*- coding:utf-8 -*-
from typing import Set

class Solution:
    def totalNQueens(self, n: int) -> int:

        col_set = set()
        add_set = set()
        sub_set = set()

        def dfs(i: int, col_set: Set[int], add_set: Set[int], sub_set: Set[int]):
            if i == n:
                return 1
            count = 0
            for j in range(n):
                if j not in col_set and (i + j) not in add_set and (i - j) not in sub_set:
                    col_set.add(j)
                    add_set.add(i + j)
                    sub_set.add(i - j)
                    count += dfs(i + 1, col_set, add_set, sub_set)
                    col_set.remove(j)
                    add_set.remove(i + j)
                    sub_set.remove(i - j)
            return count

        return dfs(0, col_set, add_set, sub_set)
