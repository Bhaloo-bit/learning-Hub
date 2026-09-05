class stack:
    def __init__(self):
        self.list = []

    def length(self):
        return len(self.list)
    
    def push(self,value):
        self.list.insert(0,value)

    def peek(self):
        L= self.list
        if len(L) == 0:
            print("Stack is empty")
            raise Exception("Stack is Empty")
        else:
            return self.list[0]    
        
    # def push(self,value):
    #     self.list.append(value)

    def pull(self):
        if len(self.list) == 0:
            raise Exception("Stack is Empty")
        else:
           return self.list.pop()

Stack = stack()
Stack.push(10)
Stack.push(20)
Stack.push(30)
Stack.push(40)
# print(Stack.peek())
print(Stack.pull())


