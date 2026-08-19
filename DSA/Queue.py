class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
       Que = self.item
       if len(Que) == 0:
           return "Queue is Empty"

    def insert(self, value):
            Que = self.item
            Que.append(value)

    def delete(self):
          if len(self.item) == 0:
                 print("Queue is Empty")
          else:
                 print(self.item.pop(0))
    def print(self):
         print(self.item)      
                           
Q = Queue()
Q.insert(10)
Q.insert(20)
Q.insert(30)
Q.delete()
Q.delete()
Q.delete()
Q.delete()

Q.print()
