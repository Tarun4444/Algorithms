
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

def level_order(root):
    queue=[]
    if root is None:
        return
    
    queue.append(root)
    
    while len(queue) > 0:
        node=queue.pop(0)
        print(node.data)
        
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)        

level_order(root)