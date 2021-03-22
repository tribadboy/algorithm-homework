# -*- coding:utf-8 -*-
from typing import List
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = collections.Counter(tasks)
        task_list = [[i, 0] for i in task_counter.values()]
        time = 0
        while True:
            max_index = -1
            max_value = -1
            flag = False
            for index in range(len(task_list)):
                if task_list[index][0] > 0:
                    flag = True
                if task_list[index][1] == 0 and task_list[index][0] > max_value:
                    max_index = index
                    max_value = task_list[index][0]
            if not flag:
                return time
            else:
                if max_index != -1:
                    task_list[max_index][0] -= 1
                    task_list[max_index][1] = n
                for index in range(len(task_list)):
                    if index != max_index and task_list[index][1] > 0:
                        task_list[index][1] -= 1
                time += 1