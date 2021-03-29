# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def generate(self, left: int, right: int, n: int, chars: str, result: List[str]):
        if left == n and right == n:
            result.append(chars)
        if left < n:
            self.generate(left+1, right, n, chars+'(', result)
        if right < left:
            self.generate(left, right+1, n, chars+')', result)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate(0, 0, n, '', result)
        return result