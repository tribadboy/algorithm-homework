# -*- coding:utf-8 -*-

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result |= ((n >> i) & 1) << (31-i)
        return result