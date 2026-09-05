class Node :
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
    if(root == None):
        return Node(value)
    if(root.data == value):
        return root
    if(root.data > value):
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)  
    return root 
     
def search(root, value):
    if(root == None):
        print("Element not found")
    if(root.data == value):
        print("Element found")
    if(root.data > value):
        search(root.left, value)
    else:
        search(root.right, value)  
    
def delete(root, value):
    if (root == None):
        return root 
    if(root.data > value):
        root.left = delete(root.left, value)
    if(root.data < value):
       root.right =  delete(root.right, value)

    else :
        if(root.left == None):
            return root.right
        elif(root.right == None):
            return root.left
        else :
            succ = get_succesor(root)
            root.data = succ.data
            root.right = delete(root.right, succ.data)
    return root

def get_succesor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root

def InOrder(root):
    if (root != None):
        InOrder(root.left)
        print(root.data , end = " ")
        InOrder(root.right)

# root = Node(20)
# root.left = Node(15)
# root.right = Node(30)

# root.left.left = Node(12)
# root.left.right= Node(18)
# InOrder(root)

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)

InOrder(root)

delete(root, 12)
print('\n')
InOrder(root)
