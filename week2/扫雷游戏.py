# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def check(board: List[List[str]], x, y):
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x+i < len(board) and 0 <= y+j < len(board[0]) and board[x+i][y+j] == 'M':
                        count += 1
            return count

        def generate(board: List[List[str]], x, y, click_flag) -> List[List[str]]:
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] not in ['M', 'E']:
                return
            if board[x][y] == 'M' and click_flag:
                board[x][y] = 'X'
            elif board[x][y] == 'E':
                count = check(board, x, y)
                if count == 0:
                    board[x][y] = 'B'
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            generate(board, x+i, y+j, False)
                else:
                    board[x][y] = str(count)

        generate(board, click[0], click[1], True)
        return board