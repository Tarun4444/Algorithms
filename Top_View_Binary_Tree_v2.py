 #Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, root):
        if root is None:
            return
    
        node=queue(root,0)
        q=[]
        s=set()
        
        while len(q) > 0:
            
            node=queue(q.pop(0))
            
            node.hd not in s:
                s.add(node.hd)
                print(node.data)
        
            if node.left is not None:
                q.append([node.left,node.hd-1])
            if node.right is not None:
                q.append([node.right,node.hd+1])
                
class queue :
    def __init__(self,node_list):
        self.node=node_list[0]
        self.hd=node_list[1]
    
