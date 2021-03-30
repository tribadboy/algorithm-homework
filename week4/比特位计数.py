# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        result = [0, 1] + [0] * (num - 1)
        high = 0
        for i in range(2, num+1):
            if i & (i - 1) == 0:
                high = i
            result[i] = result[i - high] + 1
        return result