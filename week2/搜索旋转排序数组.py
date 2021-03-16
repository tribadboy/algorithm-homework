# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target:
                    return left
            if nums[right] == target:
                    return right
            mid = int(left + (right - left) / 2)
            if left == mid:
                    return -1
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                elif nums[left] < nums[mid]:
                    left = mid
                elif nums[mid] <= target <= nums[left]:
                    left = mid
                else:
                    right = mid
