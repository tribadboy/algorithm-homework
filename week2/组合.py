# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def generate(start: int, n: int, k: int, result: List[List[int]], tmp: List[int]):
            if k == 0 and len(tmp) > 0:
                result.append(tmp)
                return
            if start == n:
                return
            start += 1
            generate(start, n, k - 1, result, tmp + [start])
            generate(start, n, k, result, tmp)

        result = []
        generate(0, n, k, result, [])
        return result
