# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def getGcd(self, a: int, b: int) -> int:
        if a > b:
            return self.getGcd(b, a)
        while a:
            a, b = b % a, a
        return b

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total = len(nums)
        k = k % total
        count = self.getGcd(k, total)

        for i in range(count):
            temp = nums[i]
            pos = i
            next_pos = (pos + k) % total
            while True:
                temp, nums[next_pos] = nums[next_pos], temp
                pos = next_pos
                next_pos = (pos + k) % total
                if pos == i:
                    break

        return nums