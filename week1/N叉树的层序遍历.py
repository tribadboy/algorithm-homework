# -*-coding:utf-8 -*-
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result = []
        stack = [root]
        while len(stack) != 0:
            new_stack = []
            val_list = []
            for node in stack:
                val_list.append(node.val)
                if node.children is not None:
                    new_stack += node.children
            stack = new_stack
            result.append(val_list)
        return result