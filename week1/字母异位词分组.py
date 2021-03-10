# -*- coding:utf-8 -*-
from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_set = collections.defaultdict(list)
        for chars in strs:
            key_list = [0] * 26
            for char in chars:
                key_list[ord(char) - ord('a')] += 1
            key_str = tuple(key_list)
            str_set[key_str].append(chars)
        return list(str_set.values())