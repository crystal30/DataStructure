from AVLTree import AVLTree

class AVLMap():
    def __init__(self):
        self.avl = AVLTree

    def getSize(self):
        return self.avl.getSize()

    def isEmpty(self):
        return self.avl.isEmpty()

    def add(self,key,val):
        self.avl.add(key,val)

    def remove(self,key):
        return self.avl.remove(key)

    def set(self, key, newVal):
        self.avl.set(key, newVal)

    def contains(self,key):
        return self.avl.contains(key)

    def get(self,key):
        return self.avl.get(key)
