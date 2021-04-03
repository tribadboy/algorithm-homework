# -*- coding:utf-8 -*-

class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = dict()
        self.remain = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after_head(self, key: int, val: int):
        node = Node(key, val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.hash_map[key] = node

    def _delete_key(self, node: Node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.hash_map.pop(node.key)

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self._delete_key(node)
        self._insert_after_head(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            self._delete_key(node)
            self._insert_after_head(key, value)
        else:
            if self.remain == 0:
                self._delete_key(self.tail.prev)
            else:
                self.remain -= 1
            self._insert_after_head(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)