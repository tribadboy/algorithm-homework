# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        result = [[]]
        for num in nums:
            new_result = []
            for alist in result:
                for i in range(0, len(alist)+1):
                    new_result.append(alist[:i] + [num] + alist[i:])
            result = new_result
        return result