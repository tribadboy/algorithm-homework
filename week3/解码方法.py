# -*- coding:utf-8 -*-

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        for i in range(1, len(dp)):
            f1, f2 = False, False
            if s[i] != '0':
                dp[i] += dp[i-1]
                f1 = True
            if s[i-1] == '1' or (s[i-1] == '2' and '0' <= s[i] <= '6'):
                dp[i] += dp[i-2] if i > 1 else 1
                f2 = True
            if not (f1 or f2):
                return 0
        return dp[-1]