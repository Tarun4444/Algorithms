{
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)
		
def LCA(root, a, b):
    # Code here
    if root is None:
        return root
    if root.data==a or root.data==b
        return root
    if max(a,b) < root.data:
        return LCA(root.left,a,b)
    elif min(a,b) > root.data:
        return LCA(root.right,a,b)
    else:
        return root
		
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
        a,b = list(map(int, input().strip().split()))
        res = LCA(root, a, b)
        print(res.data)
# Contributed by: Harshit Sidhwa
}