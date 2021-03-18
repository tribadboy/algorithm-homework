# -*- coding:utf-8 -*-
from typing import List, Dict
import collections


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def getNextWordList(word: str, word_map: Dict[str, bool]):
            result = []
            for i in range(0, len(word)):
                for j in range(26):
                    new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]
                    if word[i] != chr(ord('a') + j) and word_map.get(new_word, '') == False:
                        result.append(new_word)
                        word_map[new_word] = True
            return result

        word_map = {i: False for i in wordList}
        deque = collections.deque()
        deque.append(beginWord)
        distance = 1
        while deque:
            distance += 1
            new_deque = collections.deque()
            while deque:
                word = deque.popleft()
                next_list = getNextWordList(word, word_map)
                for next_word in next_list:
                    if next_word == endWord:
                        return distance
                new_deque.extend(next_list)
            deque = new_deque

        return 0
