# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = -1
        for i in range(len(nums)):
            if nums[i] == 0 and zero_pos == -1:
                zero_pos = i
            if nums[i] != 0 and zero_pos != -1:
                nums[zero_pos], nums[i] = nums[i], nums[zero_pos]
                zero_pos += 1
