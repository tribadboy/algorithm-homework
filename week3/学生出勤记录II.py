# -*- coding:utf-8 -*-

class Solution:
    def checkRecord(self, n: int) -> int:
        p = 2
        q = 3
        dp = [[[0 for _ in range(q)] for _ in range(p)] for _ in range(n)]
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        dp[0][0][2] = 0
        dp[0][1][0] = 1
        dp[0][1][1] = 0
        dp[0][1][2] = 0
        mod = 10 ** 9 + 7
        for i in range(1, n):
            dp[i][0][0] = sum(dp[ i -1][0]) % mod
            dp[i][0][1] = dp[ i -1][0][0]
            dp[i][0][2] = dp[ i -1][0][1]
            dp[i][1][0] = (sum(dp[ i -1][1]) + dp[i][0][0]) % mod
            dp[i][1][1] = dp[ i -1][1][0]
            dp[i][1][2] = dp[ i -1][1][1]
        return sum([sum(dp[ n -1][0]), sum(dp[ n -1][1])]) % mod

