# memory allocation view list 

class Graph:
    def __init__(self):
        self.addList = {}

    def add_vertex(self, vertax):
        if vertax not in self.addList:
            self.addList[vertax] = [] #[vertax-key] []- empty list

    def addEdge(self, src, dest):
        self.add_vertex(src)  # directed graph
        self.add_vertex(dest)

        self.addList[src].append(dest) # undirected graph
        self.addList[dest].append(src)

    def printGraph(self):
        for vertax in self.addList :
            print(vertax, " -> ", self.addList[vertax], end ="\n")


g = Graph()
g.addEdge(1,3)            
g.addEdge(2,3)            
g.addEdge(1,4)            
g.addEdge(4,3)            
g.addEdge(2,4)            
g.addEdge(4,5)            
g.addEdge(3,5)            

g.printGraph()