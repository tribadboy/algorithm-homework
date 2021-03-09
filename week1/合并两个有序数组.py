# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        current = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 or j >= 0:
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[current] = nums1[i]
                current -= 1
                i -= 1
            else:
                nums1[current] = nums2[j]
                current -= 1
                j -= 1
