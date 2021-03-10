# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        flag = 1
        i = len(digits) - 1
        while i >= 0:
            num_new = digits[i] + flag
            if num_new > 9:
                num_new -= 10
                flag = 1
            else:
                flag = 0
            digits[i] = num_new
            i -= 1

        if flag == 1:
            digits.append(0)
            for i in range(1, len(digits)):
                digits[i] = 0
            digits[0] = 1

        return digits