# -*- coding:utf-8 -*-
from typing import List, Dict

class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = '#'

    def insertWord(self, word: str, node: Dict):
        for ch in word:
            node = node.setdefault(ch, {})
        node[self.end_of_word] = word

    # def findWords(self, word: str, node: Dict):
    #     for ch in word:
    #         if ch not in node:
    #             return False
    #         node = node[ch]
    #     return self.end_of_word in node

    # def findPrefix(self, prefix: str, node: Dict):
    #     for ch in prefix:
    #         if ch not in node:
    #             return False
    #         node = node[ch]
    #     return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def inner(board: List[List[str]], node: Dict, i: int, j: int, result: List[str]):
            if '#' in node:
                result.append(node['#'])
                del node['#']
            m = len(board)
            n = len(board[0])
            if not (0 <= i < m and 0 <= j < n and board[i][j] != '.' and board[i][j] in node):
                return
            tmp = board[i][j]
            board[i][j] = '.'
            inner(board, node[tmp], i - 1, j, result)
            inner(board, node[tmp], i + 1, j, result)
            inner(board, node[tmp], i, j - 1, result)
            inner(board, node[tmp], i, j + 1, result)
            board[i][j] = tmp

        trie = Trie()
        for word in words:
            trie.insertWord(word, trie.root)
        result = []
        m = len(board)
        n = len(board[0])
        print(trie.root)
        for i in range(m):
            for j in range(n):
                inner(board, trie.root, i, j, result)
        return result

