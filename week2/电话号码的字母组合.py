# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        result = []
        for num in digits:
            if len(result) == 0:
                result = [i for i in num_map[num]]
            else:
                new_result = []
                for i in num_map[num]:
                    new_result.extend([ch+i for ch in result])
                result = new_result
        return result