class Node :
    def __init__(self,value = None):
        self.value = value
        self.data = None
        self.prev = None
        self.next = None

class DoublyLL :
    def __init__(self):
        self.head = None

    def insertAtEnd (self, value):
        temp = Node(value)
        if(self.head==None):
            self.head = temp
            return
        
        t = self.head
        while(t.next != None):
            t = t.next

        t.next = temp
        t.prev = t