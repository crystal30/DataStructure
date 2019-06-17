from linkedlist import LinkedList

class Set():
    def __init__(self):
        self.linkedlist = LinkedList()

    def add(self, e):
        if self.linkedlist.contains(e):
            pass
        else:
            self.linkedlist.addFirst(e)

    def contains(self,e):
        return self.linkedlist.contains(e)

    def remove(self, e):
        self.linkedlist.remove(e)

    def getSize(self):
        return self.linkedlist.getSize()

    def isEmpty(self):
        return self.linkedlist.isEmpty()

if __name__ == '__main__':
    set1 = Set()
    words = ['we','we','asd','de','asd']
    for word in words:
        set1.add(word)
    print(set1.getSize())
    print (set1.contains('asd'))
    set1.remove('asd')
    print(set1.contains('asd'))
    print(set1.isEmpty())

