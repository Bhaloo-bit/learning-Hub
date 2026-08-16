class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


class Doubllylinkedlist:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, value):
        temp = Node(value)
        if self.head == None :
            self.head = temp 
            return 
        t1 = self.head
        while t1.next != None:
            t1 = t1.next
        t1.next = temp
        t1.prev = t1     

    def insertAtBegn(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp 
        self.head = temp

    def insertAtMid(self, value, loc):
        t1 = self.head
        while(t1.next !=None):
            if(t1.data == loc):
                break
            else:
                t1 = t1.next
        temp = Node(value)
        temp.next = t1.next
        t1.next.prev = temp
        t1.next = temp
        temp.prev = t1

    def deletionDLL(self,value):
        t1 = self.head
        if( t1 == None):
            print("Doubly linked list is empty")
            return
        t1 = self.head
        if(t1 == value): # deletion form the begn
            self.head = t1.next
            self.head.prev = None
            return
        while(t1.next != None):# deletion at middle
            if(t1 == value):
                t1.prev.next = t1.next
                t1.next.prev = t1.prev
            else:
                t1 = t1.next

        if(t1.head == value):# deletion at the end
            t1.prev = None        
        
    def printDLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end = ' <--> ')  
            t1 = t1.next  
        print(t1.data)    

obj = Doubllylinkedlist()
obj.InsertAtEnd(10)        
obj.InsertAtEnd(20) 
obj.InsertAtEnd(30)  
obj.insertAtMid(25,20) 
obj.insertAtBegn(5) 
obj.printDLL()     