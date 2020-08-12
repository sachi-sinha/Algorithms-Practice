class Node:
    def __init__(self, element, nextNode):
        self.data = element
        self.nextNode = nextNode
        
    def setNext(self, nextNode):
        self.nextNode = nextNode
        
    def getNext(self):
        return self.nextNode
    
    def getElement(self):
        return self.data
  
class SingleLL:
    def __init__(self):
        self.head, self.curr, self.tail = None, None, None
        self.size = 0
        
    def size(self):
        return self.size()

    def isEmpty(self):
        return (self.head == None)

    def getCurr(self):
        if (self.curr == None):
            return None
        self.curr.getElement()

    def goToHead(self):
        if (self.isEmpty()):
            return False
        self.curr = self.head
        return True

    def goToTail(self):
        if (isEmpty()):
            return False
        self.curr = self.tail
        return True

    def goToNext(self):
        if self.curr == None or self.curr.getNext() == None:
            return False

        self.curr = self.curr.getNext()
        return True

    def insertNext(self, nextNode):
        if self.head == None:
            self.insertHead(nextNode)

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
            self.tail = self.curr

        self.size -= 1

    def insertHead(self, element):
        oldHead = self.head
        self.head = Node(element, oldHead)
        self.size += 1
        self.curr = self.head

        if self.tail == None:
            self.tail = self.curr
    

class HashTable:
    def __init__(self):
        self.table = [None] * 100000
        
    def calculate_hash_value(self, string):
        hash_value = ord(string[0]) * 31 + ord(string[1])
        return hash_value

    def store(self, string):
        value = self.calculate_hash_value(string)
        if self.table[value] is None:
            self.table[value] = SingleLL()
            self.table[value].insertHead(string)
        else:
            self.table[value].insertNext(string)

    def lookup(self, string):
        value = self.calculate_hash_value(string)
        if self.table[value] == None:
            return False
        self.table[value].goToHead()
        current = self.table[value].curr.data
        while(current):
            if current == string:
                return True
            current = self.table[value].curr.getNext().data
        return False
        

table = HashTable()
table.store("hi")
table.store("abc")
table.store("abd")
print(table.lookup("abd"))
