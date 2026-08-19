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

    def insertAtBegn (self, value):
        temp = Node(value)
        if(self.head ==None):
            self.head = temp
            return
        temp.next = self.head #when insert element is the first one in DLL
        self.head.prev = temp
        self.head = temp

    def insertAtMid (self, value,x):
        t = self.head
        
        while (t.next != None):
            if(t.value == x):
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.prev = temp
        t.next = temp
        temp.prev = t

    def deletionDLL(self,value):
        if(self.head == None):
            print("Linked list is empty")
            return
        t = self.head
        t.data = self.head
        if(t.data == value):
            self.head = t.next
            self.head.prev = None
            return
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next  
                t.next.prev = t.prev
                return
            else: 
             t = t.next
        if(t.data == value):
            t.prev = None

    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.value,end=" <--> ")
            t1 = t1.next
        print(t1.value)


Obj = DoublyLL()
Obj.insertAtEnd(10)
Obj.insertAtEnd(20)
Obj.insertAtEnd(30)
Obj.insertAtMid(35,30)
Obj.insertAtEnd(40)
Obj.deletionDLL(20)
Obj.insertAtBegn(5)
Obj.printLL()