# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1), (-1, 0), (0, -1), (1,0)]
        dir_pos = 0
        max_distance = 0
        cur_pos = (0, 0)
        ob_set = {(x, y) for x,y in obstacles}
        for cmd in commands:
            if cmd == -2:
                dir_pos = (dir_pos + 1) % len(directions)
            elif cmd == -1:
                dir_pos = (dir_pos - 1) % len(directions)
            else:
                cur_dir = directions[dir_pos]
                for i in range(cmd):
                    next_x = cur_pos[0] + cur_dir[0]
                    next_y = cur_pos[1] + cur_dir[1]
                    if (next_x, next_y) in ob_set:
                        break
                    else:
                        cur_pos = (next_x, next_y)
                        max_distance = max(next_x**2 + next_y**2, max_distance)
        return max_distance
