# -*- coding:utf-8 -*-
from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for p, q in counter.items():
            bucket[q].append(p)
        result = []
        for pos in range(len(bucket)-1, 0, -1):
            if len(bucket[pos]) > 0:
                result = result + bucket[pos][:k-len(result)]
                if len(result) == k:
                    return result