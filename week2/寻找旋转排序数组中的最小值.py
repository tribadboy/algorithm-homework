# -*- coding:uft-8
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)

            if nums[left] <= nums[right]:
                return nums[left]
            elif mid == left:
                return nums[right]
            elif nums[left] < nums[mid]:
                left = mid
            else:
                right = mid