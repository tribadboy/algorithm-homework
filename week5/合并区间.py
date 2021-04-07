# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def mergeSort(array: List[List[int]], left: int, right: int):
            if left >= right:
                return
            mid = left + ((right - left) >> 1)
            mergeSort(array, left, mid)
            mergeSort(array, mid+1, right)
            i = left
            j = mid + 1
            tmp = []
            while i <= mid and j <= right:
                if array[i][0] <= array[j][0]:
                    tmp.append([array[i][0], array[i][1]])
                    i += 1
                else:
                    tmp.append([array[j][0], array[j][1]])
                    j += 1
            while i <= mid:
                tmp.append([array[i][0], array[i][1]])
                i += 1
            while j <= right:
                tmp.append([array[j][0], array[j][1]])
                j += 1
            for k in range(len(tmp)):
                array[left+k] = [tmp[k][0], tmp[k][1]]

        mergeSort(intervals, 0, len(intervals)-1)   # intervals.sort(key=lambda x: x[0])
        result = []
        p = intervals[0][0]
        q = intervals[0][1]
        for i,j in intervals[1:]:
            if j <= q:
                continue
            elif i <= q:
                q = j
            else:
                result.append([p, q])
                p, q = i, j
        result.append([p, q])
        return result
