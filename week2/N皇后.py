# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def checkValid(self, stack: List[int], n: int, line: int, current_pos: int):
        if line >= n or current_pos >= n:
            return False
        for i in range(n):
            if i != line and stack[i] == current_pos:
                return False
            if stack[i] != -1 and abs(i - line) == abs(stack[i] - current_pos):
                return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        stack = [-1] * n
        line = 0
        while 0 <= line < n:
            current_pos = stack[line] + 1
            if self.checkValid(stack, n, line, current_pos):
                if line == n - 1:
                    stack[line] = current_pos
                    result.append([''.join(['Q' if j == stack[i] else '.' for j in range(n)]) for i in range(n)])
                    stack[line] = -1
                    line -= 1
                else:
                    stack[line] = current_pos
                    line += 1
            else:
                if current_pos == n:
                    stack[line] = -1
                    line -= 1
                else:
                    stack[line] += 1
        return result