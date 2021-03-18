# -*- coding:utf-8 -*-
from typing import List
import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def getNextList(word, word_map):
            result = []
            for i in range(len(word)):
                for j in range(26):
                    new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]
                    if word[i] != chr(ord('a') + j) and word_map.get(new_word, '') == False:
                        result.append(new_word)
            return result

        def bfs(result_list, root_map, beginWord, word, current_result):
            if word == beginWord:
                result_list.append(current_result)
                return
            for root in root_map[word]:
                bfs(result_list, root_map, beginWord, root, [root] + current_result)

        word_map = {i: False for i in wordList if i != beginWord}
        if endWord not in word_map:
            return []
        root_map = {i: set() for i in wordList}
        deque = collections.deque()
        deque.append(beginWord)
        flag = False
        while deque and not flag:
            new_deque = collections.deque()
            while deque:
                word = deque.popleft()
                next_list = getNextList(word, endWord, word_map)
                for next_word in next_list:
                    root_map[next_word].add(word)
                new_deque.extend(next_list)

            for next_word in new_deque:
                word_map[next_word] = True
                if next_word == endWord:
                    flag = True
            deque = new_deque

        result_list = []
        bfs(result_list, root_map, beginWord, endWord, [endWord])

        return result_list
