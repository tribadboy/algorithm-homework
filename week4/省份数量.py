# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def union(i, j, array):
            array[find(i, array)] = find(j, array)

        def find(i, array):
            root = i
            while root != array[root]:
                root = array[root]
            while array[i] != root:
                tmp = i
                i = array[i]
                array[tmp] = root
            return root

        array = [i for i in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1 and find(i, array) != find(j, array):
                    union(i, j, array)
        return len([i for i in range(len(array)) if i == array[i]])




