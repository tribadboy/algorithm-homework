# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def union(x1: int, y1: int, x2: int, y2: int, board: List[List[str]]):
            [x1_, y1_] = find(x1, y1, board)
            [x2_, y2_] = find(x2, y2, board)
            board[x1_][y1_] = [x2_, y2_]

        def find(x: int, y: int, board: List[List[str]]):
            root_x, root_y = x, y
            while board[root_x][root_y] != [root_x, root_y]:
                [root_x, root_y] = board[root_x][root_y]
            while board[x][y] != [root_x, root_y]:
                tmp_x, tmp_y = x, y
                [x, y] = board[x][y]
                board[tmp_x][tmp_y] = [root_x, root_y]
            return root_x, root_y

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = [i, j]
        edge_x = -1
        edge_y = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'X':
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        if edge_x == -1 and edge_y == -1:
                            edge_x = i
                            edge_y = j
                        else:
                            union(i, j, edge_x, edge_y, board)
                    if i + 1 < m and board[i + 1][j] != 'X':
                        union(i, j, i + 1, j, board)
                    if j + 1 < n and board[i][j + 1] != 'X':
                        union(i, j, i, j + 1, board)
        result = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if edge_x != -1 and edge_y != -1 and find(edge_x, edge_y, board) == find(i, j, board):
                    result.append([i, j, 'O'])
                else:
                    result.append([i, j, 'X'])
        for [i, j, ch] in result:
            board[i][j] = ch

