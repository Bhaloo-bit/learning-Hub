class Node:
    def __init__(self, head, next =None):
        self.head = head
        self.next = next

class SinglyLL:
    def __init__(self, head = None):
        self.head = None

    def insertAtEnd(self, value):
        temp = Node(value) 
        if(self.head !=None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtBegn(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMid(self, value, loc):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.head == loc):
                temp.next = t1.next
                t1.next = temp
            t1= t1.next

    def deleteLL(self, value) :
        t1 = self.head
        prev = t1
        if(t1.data == value): # to delete the first element
            self.head = t1.next

        while(t1.next!= None):
            if(t1.data == value):
                prev.next = t1.next # to delete element in the middle
                break


            else:
                prev = t1
                t1 = t1.next
        if (t1.head == value): # to delete the last element
            prev.next = None
    def printll(self):
        t1 = self.head
        while(t1.next !=None ):
            print(t1.head)
            t1 = t1.next        
        print(t1.head)   
obj = SinglyLL()
obj.insertAtEnd(10)        
obj.insertAtEnd(20)        
obj.insertAtEnd(30)  
obj.insertAtMid(25,20)  
obj.printll()    