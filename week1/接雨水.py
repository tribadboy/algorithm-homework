# -*-coding: utf-8 -*-
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        i = 0
        j = 0
        while i < len(height) and j < len(height):
            j = i + 1
            while j < len(height):
                if height[j] >= height[i]:
                    volume += sum([height[i] - height[k] for k in range(i + 1, j)])
                    i = j
                    break
                j += 1

        i = len(height) - 1
        j = len(height) - 1
        while i >= 0 and j >= 0:
            j = i - 1
            while j >= 0:
                if height[j] > height[i]:
                    volume += sum([height[i] - height[k] for k in range(i - 1, j, -1)])
                    i = j
                    break
                j -= 1

        return volume