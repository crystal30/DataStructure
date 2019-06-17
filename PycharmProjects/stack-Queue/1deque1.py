class Deque:
    def __init__(self):
        self.item = []

    def empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    # 将索引为0的元素看作队首
    def addFront(self,e):
        self.item.insert(0, e)

    def removeFront(self, e):
        return self.item.pop(0)

    def addRear(self, e):
        self.item.append(e)

    def removeRear(self):
        self.item.pop()
