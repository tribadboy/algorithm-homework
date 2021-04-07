# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(array: List[int], left: int, right: int) -> int:
            if left >= right:
                return 0
            mid = left + ((right - left) >> 1)
            count = 0
            count += mergeSort(array, left, mid)
            count += mergeSort(array, mid+1, right)
            p, q = left, mid+1
            while p <= mid and q <= right:
                if array[p]/2.0 > array[q]:
                    count += mid - p + 1
                    q += 1
                else:
                    p += 1
            i, j = left, mid+1
            tmp = []
            while i <= mid and j <= right:
                if array[i] <= array[j]:
                    tmp.append(array[i])
                    i += 1
                else:
                    tmp.append(array[j])
                    j += 1
            while i <= mid:
                tmp.append(array[i])
                i += 1
            while j <= right:
                tmp.append(array[j])
                j += 1
            for k in range(len(tmp)):
                array[left+k] = tmp[k]
            return count

        return mergeSort(nums, 0, len(nums)-1)