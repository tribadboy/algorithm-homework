# -*- coding:utf-8 -*-
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = [(root, False)]
        while stack:
            node, flag = stack.pop()
            if not flag:
                if not node.left and not node.right:
                    result.append(node.val)
                    continue
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
            else:
                result.append(node.val)
        return result