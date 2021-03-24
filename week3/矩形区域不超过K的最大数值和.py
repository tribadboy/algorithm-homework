# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        maxSum = float("-inf")
        m = len(matrix)
        n = len(matrix[0])
        for left in range(n):
            rowSum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    rowSum[i] += matrix[i][right]
                maxSum = max(maxSum, self.getMaxSumSubArray(rowSum, k))
                if maxSum == k:
                    return k
        return maxSum

    def getMaxSumSubArray(self, nums: List[int], k: int):
        # 找到不大于 k 的最大子序列和 O(nlogn)
        accSumList = []
        accSum = 0
        maxSum = float("-inf")
        for num in nums:
            accSum += num
            # 检查 accSum - k ，返回它的位置（左侧小于等于，右侧大于等于）
            pos = self.binarySearch(accSumList, accSum - k)
            if accSum <= k:
                maxSum = max(maxSum, accSum)
            if pos < len(accSumList):
                maxSum = max(maxSum, accSum - accSumList[pos])
            if maxSum == k:
                return k
            # 将 accSum 存入 accSumList
            pos = self.binarySearch(accSumList, accSum)
            accSumList = accSumList[:pos] + [accSum] + accSumList[pos:]
        return maxSum

    def binarySearch(self, nums: List[int], key: int):
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid == left:
                if nums[left] >= key:
                    return left
                elif nums[right] >= key:
                    return right
                else:
                    return right + 1
            if nums[mid] == key:
                return mid
            elif nums[mid] > key:
                right = mid
            else:
                left = mid
