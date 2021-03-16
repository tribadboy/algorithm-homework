# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            # 比较 g[i] 和 s[j]
            if g[i] <= s[j]:
                count += 1
                i += 1
            j += 1
        return count