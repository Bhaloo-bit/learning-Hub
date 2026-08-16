class Node:
    def __init__(self, value):
        self.value = value
        self.data = None        
        self.prev = None
        self.next = None

class Doublylinkedlist:
    def __int__(self,value):
        self.head = value

    def insertAtEnd(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        t1 = self.head
        while(t1.next != None):
            t1 = t1.next
        t1.next = temp
        t1.prev = t1

    def insertAtbegn(self, value):
        temp = Node(value)
        t1 = self.head
        if(t1 == None):
            t1 = temp
            return
            
