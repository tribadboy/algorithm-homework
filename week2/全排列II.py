# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def generate(nums: List[int], result: List[int], index, tmp: List[int]):
            if index == len(nums):
                if len(tmp) > 0:
                    result.append(tmp)
                return
            for i in range(0, len(tmp) + 1):
                new_tmp = tmp[:i] + [nums[index]] + tmp[i:]
                generate(nums, result, index + 1, new_tmp)
                if i < len(tmp) and nums[index] == tmp[i]:
                    break

        result = []
        nums.sort()
        flag_list = [False for i in range(len(nums))]
        generate(nums, result, 0, [])
        return result