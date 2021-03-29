# -*- coding:utf-8 -*-
from typing import List, Set

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(pos_list: List[List[int]], count: int, row_set_list: List[Set[int]], col_set_list: List[Set[int]],
                blk_set_list: List[Set[int]]):
            if count == len(pos_list):
                return True
            i, j = pos_list[count]
            all_set = row_set_list[i] | col_set_list[j] | blk_set_list[(i // 3) * 3 + j // 3]
            for num in range(1, 10):
                if num not in all_set:
                    row_set_list[i].add(num)
                    col_set_list[j].add(num)
                    blk_set_list[(i // 3) * 3 + j // 3].add(num)
                    if dfs(pos_list, count + 1, row_set_list, col_set_list, blk_set_list):
                        board[i][j] = str(num)
                        return True
                    row_set_list[i].remove(num)
                    col_set_list[j].remove(num)
                    blk_set_list[(i // 3) * 3 + j // 3].remove(num)
            return False

        n = 9
        row_set_list = [set() for _ in range(n)]
        col_set_list = [set() for _ in range(n)]
        blk_set_list = [set() for _ in range(n)]
        pos_list = []
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row_set_list[i].add(num)
                    col_set_list[j].add(num)
                    blk_set_list[(i // 3) * 3 + j // 3].add(num)
                else:
                    pos_list.append([i, j])
        dfs(pos_list, 0, row_set_list, col_set_list, blk_set_list)


