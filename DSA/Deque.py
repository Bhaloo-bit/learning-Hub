class Deque:
    def __init__(self):
        self.item = []

    def isEmpty(self):
       Que = self.item
       if len(Que) == 0:
           return "Queue is Empty"

    def insertAtEnd(self, value):
            Que = self.item
            Que.append(value)

    def deleteAtfront(self):
          if len(self.item) == 0:
                 print("Queue is Empty")
          else:
                 print(self.item.pop(0))
    
    def insertAtBegn(self,value):
         self.item.insert(0,value)

    def deleteAtlast (self):
        if len(self.item) == 0:
             print("Queue is Empty")
        else:
            print(self.item.pop())
         

    def print(self):
         print(self.item)       

q = Deque()
q.insertAtEnd(10)         
q.insertAtEnd(20)         
q.insertAtEnd(30)     
q.insertAtBegn(5) 
q.insertAtEnd(40)   
q.deleteAtlast()
q.deleteAtlast()
q.deleteAtfront()
q.print()