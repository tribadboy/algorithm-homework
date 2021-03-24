# -*- coding:utf-8 -*-
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = collections.Counter(t)
        s_map = dict()
        count = 0
        min_len = float('inf')
        min_s = -1
        min_e = -1
        queue = []
        queue_s = 0
        for i in range(len(s)):
            if s[i] in t_map:
                if t_map[s[i]] > 0:
                    count += 1
                    t_map[s[i]] -= 1
                else:
                    old_index = s_map[s[i]][0][s_map[s[i]][1]]
                    s_map[s[i]][1] += 1
                    queue[old_index] = None
                index = len(queue)
                queue.append([s[i], i])
                if s[i] in s_map:
                    s_map[s[i]][0].append(index)
                else:
                    s_map[s[i]] = [[index], 0]
            if count == len(t):
                while queue[queue_s] is None:
                    queue_s += 1
                new_len = queue[-1][1] - queue[queue_s][1]
                if new_len < min_len:
                    min_len = new_len
                    min_s = queue[queue_s][1]
                    min_e = queue[-1][1]
        if min_s == -1:
            return ""
        else:
            return s[min_s:(min_e+1)]


