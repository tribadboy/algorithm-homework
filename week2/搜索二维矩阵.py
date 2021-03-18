# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        left = 0
        right = height * width - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid == left:
                return target == matrix[left // width][left % width] or target == matrix[right // width][right % width]
            if target <= matrix[mid // width][mid % width]:
                right = mid
            else:
                left = mid