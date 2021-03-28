# -*- coding:utf-8 -*-

class Solution:
    def climbStairs(self, n: int) -> int:
        def inner(a1: int, b1: int, a2: int, b2: int, n: int):
            """ 2*2 矩阵n次方 """
            if n == 1:
                return a1, b1, a2, b2
            if n % 2 == 0:
                a1_, b1_, a2_, b2_ = inner(a1, b1, a2, b2, n >> 1)
                return a1_ * a1_ + b1_ * a2_, a1_ * b1_ + b1_ * b2_, a2_ * a1_ + b2_ * a2_, a2_ * b1_ + b2_ * b2_
            else:
                a1_, b1_, a2_, b2_ = inner(a1, b1, a2, b2, n >> 1)
                a1_, b1_, a2_, b2_ = a1_ * a1_ + b1_ * a2_, a1_ * b1_ + b1_ * b2_, a2_ * a1_ + b2_ * a2_, a2_ * b1_ + b2_ * b2_
                return a1_ * a1 + b1_ * a2, a1_ * b1 + b1_ * b2, a2_ * a1 + b2_ * a2, a2_ * b1 + b2_ * b2

        a1, b1, a2, b2 = inner(1, 1, 1, 0, n)
        return a2 + b2