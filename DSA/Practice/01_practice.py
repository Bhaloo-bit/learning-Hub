class Node :
    def __init__(self, data, next=None):
        self.head = data 
        self.next = next

class Singlylinkedlist :
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertionAtbegn(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp 

    def insertAtmid(self, value, loc):
        temp = Node(value)
        t1 = self.head

        while(t1.next != None):
            if(t1.head == loc):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next    

    def deleteLL(self,value):
        t1 = self.head
        prev = t1
        if(t1.head == value):
            self.head = t1.next
        while(t1.next !=None):
            if(t1.head == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if(t1.head == value):
            prev.next = None


                
    def printll(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.head)
            t1 = t1.next        
        print(t1.head)         
            

Obj = Singlylinkedlist()
Obj.insertAtEnd(10)
Obj.insertAtEnd(20)
Obj.insertAtEnd(30)
Obj.insertionAtbegn(5)
Obj.insertAtmid(25,20)

Obj.insertAtEnd(40)
Obj.insertAtEnd(50)
Obj.deleteLL(30)
Obj.printll()
