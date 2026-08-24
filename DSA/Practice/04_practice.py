# stack -  liner data structure && crud opertation
# len , insertion, peek func to see  last entered element, pull

'''class Stack :
    def __init__(self):
        self.list = []

    def length (self):
        L = len(self.list)
        print(L)

    def push(self,value):
        self.list.insert(0,value)
        

    def peek(self):
        length = len(self.list)
        if (length == 0):
            raise Exception("Stack is Empty")
        else :
            last_inserted_Elemnet = self.list[0] 
            print(last_inserted_Elemnet)   

    def pull(self):
        length = len(self.list)
        if (length == 0):
            raise Exception("Stack is Empty")
        else:
            print(self.list.pop(0))

    def printStack(self):
        print(self.list)      

obj = Stack()
obj.push(10)            
obj.push(20)            
obj.push(30)     
obj.peek()     

obj.pull()
obj.pull()
obj.pull()
obj.pull()

obj.printStack()

# Queue linear data struture &&  crud operations
#len, insertion, deletion, print

class Queue:
    def __init__(self):
        self.item = []

    def size(self):
        L = self.item
        if (len(L) == 0):
            raise Exception("Queue is Empty")

    def insert(self,value):
        insert = self.item
        insert.append(value)

    def deletion(self):
        Que = self.item
        if (len(Que) ==0):
            raise Exception("Queue is empty")
        Que.pop(0)    

    
    def printt(self):
        print(self.item)  

        

obj = Queue()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.deletion()
obj.deletion()
obj.deletion()
obj.deletion()

obj.printt()


         '''

## D-Queue linear data struture allow insertion & deletion at its both end

class DQueue:
    def __init__(self):
        self.item = []

    def lenght(self):
        D_que = self.item
        print("D_que",len(D_que))

    def insertAtEnd(self, value):
        D_que = self.item
        D_que.append(value)
    def insertAtBegn(self,value):
        D_que = self.item
        D_que.insert(0,value)


    def deleteAtfron(self):
        D_que = self.item
        L = len(D_que)
        if (L == 0):
            raise Exception("Dqueue is Empyt")
        D_que.pop(0)
    def deletionAtEnd(self):
        D_que = self.item
        l = len(D_que) 
        if(l == 0):
            raise Exception("Dqueue is Empty")
        D_que.pop()       

    def printdq(self):
        print(self.item)     

obj = DQueue()
obj.insertAtEnd(10)        
obj.insertAtEnd(20)        
obj.insertAtEnd(30)
obj.insertAtBegn(5)
obj.deletionAtEnd()
obj.deleteAtfron()


obj.printdq()        