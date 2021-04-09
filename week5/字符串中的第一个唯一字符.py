# -*- coding:utf-8 -*-

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_map = {}
        for index in range(len(s)):
            ch = s[index]
            if ch in ch_map:
                ch_map[ch] = float('inf')
            else:
                ch_map[ch] = index
        min_value = float('inf')
        for v in ch_map.values():
            min_value = min(min_value, v)
        return -1 if min_value == float('inf') else min_value