# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        pos = 0
        while pos <= reach and pos < len(nums):
            reach = max(reach, pos + nums[pos])
            if reach >= len(nums) - 1:
                return True
            pos += 1

        return False