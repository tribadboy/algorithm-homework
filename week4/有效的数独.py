# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row_set_list = [set() for _ in range(n)]
        col_set_list = [set() for _ in range(n)]
        blk_set_list = [set() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    row_set = row_set_list[i]
                    col_set = col_set_list[j]
                    blk_set = blk_set_list[(i // 3) * 3 + j // 3]
                    if board[i][j] in row_set | col_set | blk_set:
                        return False
                    else:
                        row_set.add(board[i][j])
                        col_set.add(board[i][j])
                        blk_set.add(board[i][j])
        return True