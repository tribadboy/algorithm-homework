# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt_5 = 0
        cnt_10 = 0
        for i in bills:
            if i == 5:
                cnt_5 += 1
            elif i == 10:
                if cnt_5 == 0:
                    return False
                else:
                    cnt_5 -= 1
                    cnt_10 += 1
            elif i == 20:
                if cnt_10 > 0 and cnt_5 > 0:
                    cnt_10 -= 1
                    cnt_5 -= 1
                elif cnt_5 > 2:
                    cnt_5 -= 3
                else:
                    return False
        return True