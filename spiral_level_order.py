class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Tree:
    def createNode(self, data):
        return Node(data)
    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right
    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i
def height(root):
    if root is None:
        return 0
    
    l = height(root.left)
    r = height(root.right)
    return l+1 if l > r else r+1  
    
def printGivenLevel(root, level, itr):
    if root is None:
        return
    elif level is 1:
        print (root.data, end=" ")
    else:
        if (itr):
            printGivenLevel(root.left, level-1, itr)
            printGivenLevel(root.right, level-1, itr)
        else:
            printGivenLevel(root.left, level-1, itr)
            printGivenLevel(root.right, level-1, itr)
            
def printSpiralLevelOrder(root):
    # Code here
    h = height(root)
    itr = False
    for i in range(1,h+1):
        printGivenLevel(root, i, itr)
        itr = not itr

# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n ==0:
            print()
            continue
        tree = Tree()
        lis=[]
        root = None
        root = tree.insert(root, int(arr[0]), 'L')
        lis.append(root)
        k=0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k+=3
        printSpiralLevelOrder(root)
        print()
