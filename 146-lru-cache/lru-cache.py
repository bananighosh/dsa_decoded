class LRUCache:

    # Intuition:
    # If this value is not present in the queue then push this value in front of the queue and
    # remove the last value if the queue is full
    # If the value is already present then remove it from the queue and 
    # push it in the front of the queue

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

        # self.head = LinkedNode()
        # self.tail = LinkedNode()

        # self.head.next = self.tail
        # self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)