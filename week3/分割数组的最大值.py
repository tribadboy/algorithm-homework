# -*- coding:utf-8 -*-
from typing import List

class Solution:
    # dp 做法超时
    # def splitArray(self, nums: List[int], m: int) -> int:
    #     n = len(nums)
    #     row_sum = [0 for _ in range(n)]
    #     cur_sum = 0
    #     for i in range(n):
    #         cur_sum += nums[i]
    #         row_sum[i] = cur_sum
    #     dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
    #     for i in range(1, m+1):
    #         for j in range(i, n+1):
    #             if i == 1:
    #                 dp[i][j] = row_sum[j-1]
    #             else:
    #                 for k in range(1, j):
    #                     dp[i][j] = min(dp[i][j], max(dp[i-1][k], row_sum[j-1] - row_sum[k-1]))
    #     return dp[m][n]

        def splitArray(self, nums: List[int], m: int) -> int:
            def checkNums(nums: List[int], value: int, m: int):
                count = 1
                cur_sum = 0
                for num in nums:
                    if cur_sum + num > value:
                        cur_sum = 0
                        count += 1
                    cur_sum += num
                return count <= m

            left = max(nums)
            right = sum(nums)
            while left <= right:
                mid = left + (right - left) // 2
                if left == mid:
                    if checkNums(nums, left, m):
                        return left
                    else:
                        return right
                flag = checkNums(nums, mid, m)
                if flag:
                    right = mid
                else:
                    left = mid

