# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        k_wave_list = [None, -1, 0, 1]
        current_pos = 1
        k = 1
        k_wave_index = 0
        stack = [(current_pos, k, k_wave_index)]
        stones_set = set(stones)
        false_tuple_set = set()
        while stack[-1][0] != stones[-1]:
            current_pos, k, k_wave_index = stack[-1]
            if k_wave_index == len(k_wave_list) - 1:
                stack.pop()
                false_tuple_set.add((current_pos, k))
            else:
                k_wave_index += 1
                next_flag = False
                while k_wave_index < len(k_wave_list):
                    distance = k + k_wave_list[k_wave_index]
                    if distance > 0 and (current_pos + distance) in stones_set and (current_pos + distance, distance) not in false_tuple_set:
                        next_flag = True
                        stack[-1] = current_pos, k, k_wave_index
                        stack.append((current_pos + distance, distance, 0))
                        break
                    k_wave_index += 1
                if not next_flag:
                    stack.pop()
                    false_tuple_set.add((current_pos, k))
            if not stack:
                return False
        return True
