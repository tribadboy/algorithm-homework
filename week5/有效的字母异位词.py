# -*- coding:utf-8 -*-

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 方法1
        # if len(s) != len(t):
        #     return False
        # c = collections.Counter(s)
        # for char in t:
        #     if char not in c:
        #         return False
        #     new_num = c[char] - 1
        #     if new_num == 0:
        #         c.pop(char)
        #     else:
        #         c[char] = new_num
        # return len(c) == 0

        # 方法2
        return sorted(s) == sorted(t)