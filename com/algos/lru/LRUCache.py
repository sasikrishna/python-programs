
'''

'''


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.end = None

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.delete(node)
            self.set_head(node)
            return node.value

        return -1

    def set(self, key, value):

        if key in self.map:
            node = self.map[key]
            node.value = value
            self.delete(node)
            self.set_head(node)
        else:
            node = Node(key, value)
            if len(self.map) >= self.capacity:
                del self.map[self.end.key]
                self.delete(self.end)
                self.set_head(node)
            else:
                self.set_head(node)
            self.map[key] = node

    def set_head(self, node):
        node.next = self.head

        if self.head is not None:
            self.head.prev = node

        self.head = node

        if self.end is None:
            self.end = self.head

    def delete(self, node):

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.end = node.prev


class Node:

    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value


if __name__ == '__main__':
    cache = LRUCache(5)
    cache.set("key1", 1)
    cache.set("key2", 2)
    cache.set("key3", 3)
    cache.set("key4", 4)
    cache.set("key5", 5)
    cache.set("key6", 6)

    print('Key6 value is ', cache.get('key6'))
    print('Key3 value is ', cache.get('key3'))
    print('Key 1 is evicted' if cache.get('key1') == -1 else cache.get('key1'))

    cache.set("key7", 7)
    print('Key 2 is evicted' if cache.get('key2') == -1 else cache.get('key2'))
