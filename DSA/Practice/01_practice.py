class Node :
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

class Singllylinkedlist :
    def __init__(self, head = None):
        self.head = head

    def InsertAtEnd (self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next !=None):
                t1 = t1.next
                t1.next = temp
        else :
            self.head = temp

    def InsertAtbegin (self,value):
        temp = Node(value)
        temp.next = self.head 
        self.head = temp


    def printLL (self):
        t1 = self.head 
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)
obj = Singllylinkedlist()
obj.InsertAtEnd(10)            
obj.InsertAtEnd(20)            
obj.InsertAtEnd(30)            
obj.printLL()