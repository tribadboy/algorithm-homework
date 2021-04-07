# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        length = max(arr1) + 1
        cnt_array = [0] * length
        result = []
        for i in arr1:
            cnt_array[i] += 1
        for i in arr2:
            result += [i] * cnt_array[i]
            cnt_array[i] = 0
        for i in range(length):
            if cnt_array[i] > 0:
                result += [i] * cnt_array[i]
        return result
