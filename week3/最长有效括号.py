# -*- coding:utf-8 -*-

class Solution:

    # 方法1: stack
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif len(stack) > 1:
                left_match = stack.pop()
                left_unmatch = stack[-1]
                max_len = max(max_len, i - left_unmatch)
            else:
                stack[0] = i
        return max_len

    # # 方法2: dp
    def longestValidParentheses2(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        max_len = 0
        for i in range(1, len(s)):
            if s[i] == '(':
                continue
            elif s[i - 1] == '(':
                dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = 2 + dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
            max_len = max(max_len, dp[i])
        return max_len
