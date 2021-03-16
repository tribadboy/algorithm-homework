# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tmp = None
        cnt = 0
        for i in range(0, len(nums)):
            if tmp is None:
                tmp = nums[i]
                cnt = 1
            elif tmp == nums[i]:
                cnt += 1
            elif cnt == 1:
                tmp = None
                cnt = 0
            else:
                cnt -= 1
        return tmp