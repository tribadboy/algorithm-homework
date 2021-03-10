# -*- coding:utf-8 -*-
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [(root, False)]
        result = []
        while len(stack) != 0:
            node, flag = stack.pop()
            if len(node.children) == 0:
                result.append(node.val)
                continue
            if not flag:
                stack.append((node, True))
                stack.extend([(ch, False) for ch in node.children[::-1]])
            else:
                result.append(node.val)

        return result