class LRUCache:

    def __init__(self, capacity: int):
        self.len = capacity
        self.cache = dict()
        self.stack = []

    def get(self, key: int) -> int:
        if key in self.stack:
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.stack:
            self.cache[key] = value
            self.stack.remove(key)
            self.stack.append(key)

        else:
            if self.len == 0:
                last_key = self.stack.pop(0)
                del self.cache[last_key]

            else:
                self.len -= 1

            self.cache[key] = value
            self.stack.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    capacity = 1
    obj = LRUCache(capacity)
    obj.put(1, 1)
    obj.put(2,2)
    print(obj.get(1))
    obj.put(3,3)
    print(obj.get(2))
    obj.put(4,4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
    obj.put(5, "five")
    print(obj.get(4))
    print(obj.get(5))



