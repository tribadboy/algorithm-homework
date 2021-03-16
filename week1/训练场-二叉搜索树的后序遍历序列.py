# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def checkTree(self, nums: List[int], start: int, end: int) -> bool:
        if start >= end:
            return True

        for i in range(start, end):
            if nums[i] > nums[end]:
                break
        else:
            i += 1

        # check [start,i) [i, end)
        for j in range(i, end):
            if nums[j] < nums[end]:
                return False

        return self.checkTree(nums, start, i - 1) and self.checkTree(nums, i, end - 1)

    def verifyPostorder(self, postorder: List[int]) -> bool:
        return self.checkTree(postorder, 0, len(postorder) - 1)