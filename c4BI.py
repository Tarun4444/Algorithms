    class Node:
    def __init__(self, d):
        self.value = d
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return Node(value)
    
    if value > node.value:
        node.right = insert(node.right, value)
        
    if value < node.value:
        node.left = insert(node.left, value)
    
    return node
    
def levelOrderTraversal(root):
    if root is None:
        return None
    
    q = []
    q.append(root)
    
    while(len(q) > 0):
        print(q[0].value)
        roo = q.pop(0) 
        if roo.left is not None:
            l.append(level + 1)
            q.append(roo.left)
        if roo.right is not None:
            l.append(level + 1)
            q.append(roo.right)
    
def getLevel(root, x, level):
    if root is None:
        return 0
    
    if root.value == x:
        return level
    
    dl = getLevel(root.left, x, level+1)
    
    if dl != 0:
        return dl
    
    dl = getLevel(root.right, x, level+1)
    
    return dl
    
def solve (A,N,i):
    # Return a list of N elements, ith element representing level of A[i]
    # Write your code here
    if not A:
        return None
    
    if len(A) == 1:
        return [1]
    
    root = Node(A[0])
    
    for e in A[1:]:
        root = insert(root, e)
    
    z = []
    for e in A:
        z.append(getLevel(root, e, 1))
    
    return z

N = int(input())
A = list(map(int, input().split()))
out_ = solve(A,N,0)

print (' '.join(map(str, out_)))