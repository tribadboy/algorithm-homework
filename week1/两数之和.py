# -*-coding:utf-8 -*-
from typing import List
import collections

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = collections.defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[target-nums[i]] = i
            else:
                return [num_dict[nums[i]], i]