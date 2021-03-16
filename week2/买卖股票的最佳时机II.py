# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        pos = 0
        while pos < len(prices)-1:
            if prices[pos+1] > prices[pos]:
                profit += prices[pos+1] - prices[pos]
            pos += 1
        return profit