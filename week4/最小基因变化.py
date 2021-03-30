# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        begin_set = {start}
        end_set = {end}
        bank_set = set(bank)
        if end not in bank_set:
            return -1
        distance = 0
        while begin_set:
            print(begin_set, end_set)
            new_begin_set = set()
            distance += 1
            for seq in begin_set:
                for i in range(len(seq)):
                    for new_ch in ['A', 'C', 'G', 'T']:
                        if new_ch != seq[i]:
                            new_seq = seq[:i] + new_ch + seq[i+1:]
                            if new_seq in end_set:
                                return distance
                            if new_seq in bank_set:
                                new_begin_set.add(new_seq)
                                bank_set.remove(new_seq)
            begin_set = new_begin_set
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
        return -1