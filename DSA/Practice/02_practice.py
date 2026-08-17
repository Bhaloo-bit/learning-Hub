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

# obj = Doubllylinkedlist()
# obj.InsertAtEnd(10)        
# obj.InsertAtEnd(20) 
# obj.InsertAtEnd(30)  
# obj.insertAtMid(25,20) 
# obj.insertAtBegn(5) 
# obj.printDLL()     



class Node:
    def __init__(self, value):
        self.head = value
        self.prev = None
        self.next = None

class DoubllyLL:
    def __init__(self, head = None):
        self.head = head

    def insertAtEnd(self , value):
        #first create Node & check if DLL exits or not if ! then create and return 
        temp = Node(value)
        if (self.head == None):
            self.head = temp 
            return
        t = self.head 
        while (t.next != None):
           t = t.next
        t.next = temp
        t.prev = t

    def insertAtbegn(self, value):
        temp = Node(value)
        if(self.head == None): # applicable when DLL does not exits
            self.head = temp
            return
        t = self.head
        temp.next = t.prev
        self.head = temp

    def insertionAtmid(self, value, location):
        temp = Node(value)
        t1 = self.head
        while(t1.next!=None):
            if(t1 == location):
                break
            else:
                t1 = t1.next
        temp.next = t1.next
        t1.next.prev = temp
        t1.next = temp
        temp.prev = t1        

    def DeletionDLL(self, value):
        t1 = self.head
        if (t1 == None):
            print("DLL is empty")
            return

        if self.head == value: # deletion at the begn
            t1.next = self.head
            t1.next.prev = None
            return
        
        while(t1.next != None): # deletion from the middle
            if (t1.data == value):
                t1.prev.next = t1.next
                t1.next.prev = t1.prev
            else:
                t1 = t1.next   

        if(t1.head== value):
            t1.prev = None
            





    def printLL(self):
        t1 = self.head
        while t1.next != None:
            print(t1.head)
            t1 = t1.next
        print(t1.head)    

obj = DoubllyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtbegn(5)
obj.printLL()
