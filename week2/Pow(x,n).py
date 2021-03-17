# -*- coding:utf-8 -*-

class Solution:
    def compute(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        half_n = int(n / 2)
        half_value = self.compute(x, half_n)
        if n % 2 == 1:
            return half_value * half_value * x
        else:
            return half_value * half_value

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.compute(x, -n)
        else:
            return self.compute(x, n)