
# Node Class

class Node:
    def __init__(self):
        self.element = None
        self.nextNode = None

    def __init__(self, element, nextNode):
        self.element = element
        self.nextNode = nextNode

    def getElement(self):
        return self.element

    def setElement(self, element):
        self.element = element

    def getNext(self):
        return self.nextNode

    def setNext(self, nextNode):
        self.nextNode = nextNode

# Singly Linked List

class SingleLL:

    def __init__(self):
        self.size = 0
        self.head, self.tail, self.curr = None, None , None

    def size(self):
        return self.size()

    def isEmpty(self):
        return (self.head == None)

    def getCurr(self):
        self.curr.getElement()

    def goToHead(self):
        if (isEmpty()):
            return false
        self.curr = self.head
        return true

    def goToTail(self):
        if (isEmpty()):
            return false
        self.curr = self.tail
        return true

    def goToNext(self):
        if self.curr == None or self.curr.getElement() == None:
            return false

        self.curr = self.curr.getNext()
        return true

    def insertNext(self, nextNode):
        if self.head == None:
            insertHead(nextNode)

        newNode = Node(nextNode, self.curr.getNext())
        self.curr.setNext(newNode)

        self.size += 1

        if self.tail == self.curr:
            self.tail = newNode

        self.curr = newNode

    def deleteNext(self):
        if self.curr == None or self.curr.getNext() == None:
            return None

        self.curr.setNext(curr.getNext().getNext())

        if self.curr.getNext() == None:
            self.tail = curr

        self.size -= 1

    def insertHead(self, element):
        oldHead = self.head
        self.head = Node(element, oldHead)
        self.size += 1
        self.curr = self.head

        if self.tail == None:
            self.tail = self.curr

    def deleteHead(self):
        if self.head == None:
            return

        self.head = self.head.getNext()

        self.size -= 1

        self.curr = self.head

        if self.size == 1 :
            self.tail = self.curr


