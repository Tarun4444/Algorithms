def isBST(root):
    # Code here
    max = 4294967296
    min = -4294967296
    isBSTutil(root,min,max)
    
def isBSTutil(root,min,max):
    if root is None:
        return 1
    
    if root.data < min and root.data > max:
        return 0
    
    return isBSTutil(root.left,min,root.data-1) and isBSTutil(root.right,root.data+1,max)