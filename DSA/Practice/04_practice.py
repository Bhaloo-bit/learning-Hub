# stack -  liner data structure && crud opertation
# len , insertion, peek func to see  last entered element, pull

class Stack :
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