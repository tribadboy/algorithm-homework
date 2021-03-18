# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        start = 0
        end = start + nums[start]
        distance = end
        count = 1
        while end < len(nums) - 1:
            distance = max(distance, start + nums[start])
            if start == end:
                end = distance
                count += 1
            start += 1

        return count
