# -*-coding:utf-8 -*-
from typing import List

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1] * n
        p2 = 0
        p3 = 0
        p5 = 0
        current_num = 1
        while current_num != n:
            p2n = nums[p2] * 2
            p3n = nums[p3] * 3
            p5n = nums[p5] * 5
            min_num = min(p2n, p3n, p5n)
            if min_num == p2n:
                p2 += 1
            if min_num == p3n:
                p3 += 1
            if min_num == p5n:
                p5 += 1
            nums[current_num] = min_num
            current_num += 1
        
        return nums[n-1]