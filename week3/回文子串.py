# -*- coding:utf-8 -*-

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        count = 0
        for j in range(n):
            for i in range(j, -1, -1):
                if i == j and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                if i == j - 1 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                if 0 <= i < j - 1 and dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
        return count