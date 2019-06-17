from AVLTree import AVLTree

class AVLSet():
    def __init__(self):
        self.avl = AVLTree

    def getSize(self):
        return self.avl.getSize()

    def isEmpty(self):
        return self.avl.isEmpty()

    def add(self,key):
        self.avl.add(key,None)

    def remove(self,key):
        self.avl.remove(key)

    def contains(self,key):
        return self.avl.contains(key)
