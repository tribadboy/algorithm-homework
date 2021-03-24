# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        new_nums = [1] + nums + [1]
        n = len(new_nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for delta in range(1, n):
            for i in range(0, n-delta):
                j = i + delta
                if delta == 1:
                    dp[i][j] = 0
                else:
                    max_sum = float('-inf')
                    for k in range(i+1, j):
                        max_sum = max(max_sum, dp[i][k] + dp[k][j] + new_nums[i] * new_nums[k] * new_nums[j])
                    dp[i][j] = max_sum
        return dp[0][n-1]
