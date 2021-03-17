# -*- coding:utf-8 -*-
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generate(self, s_pre: int, e_pre: int, s_in: int, e_in: int, preorder: List[int],
                 inorder: List[int]) -> TreeNode:
        root_val = preorder[s_pre]
        mid = inorder.index(root_val)
        left_cnt = mid - s_in
        right_cnt = e_in - mid
        left_node, right_node = None, None
        if left_cnt > 0:
            left_node = self.generate(s_pre + 1, s_pre + left_cnt, s_in, mid - 1, preorder, inorder)
        if right_cnt > 0:
            right_node = self.generate(s_pre + left_cnt + 1, s_pre + left_cnt + right_cnt, mid + 1, e_in, preorder,
                                       inorder)
        return TreeNode(val=root_val, left=left_node, right=right_node)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.generate(0, len(preorder) - 1, 0, len(inorder) - 1, preorder, inorder)