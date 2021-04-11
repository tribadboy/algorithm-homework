# -*- coding:utf-8 -*-

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        i = 0
        result = list(s)
        while i < n:
            num = min(k, n-i)
            for j in range(num >> 1):
                result[i + j], result[i + num - 1 - j] = result[i + num - 1 - j], result[i + j]
            i += 2 * k
        return ''.join(result)