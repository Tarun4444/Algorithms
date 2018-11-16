from collections import OrderedDict
class Node:
    def __init__(self,data,count):
        self.data=data
        self.count=count
        self.left=None
        self.right=None

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,data):
        self.data=data
    def getNodeValue(self):
        return self.data

class Tree:        
    def insert(self,data):pass
            
    def delete(self):pass
    
    def inOrder(self,node):
        if node == None:
            return
        self.inOrder(node.left)
        print(node.data,node.count)
        self.inOrder(node.right)
        
    def preOrder(self,node):
        if node == None:
            return
        print(node.data,node.count)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self,node):
        if node == None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data)
        
    def TopViewLevelOrderTraversal(self,root):
        if root is None:
            return
        q=[]
        s=set()

        node=queue([root,0])
        q.append(node)

        while len(q) > 0:
            
            n=q.pop(0)
            hd=n.hd
            node=n.node
            
            if hd not in s:
                s.add(hd)
                print(node.data)
        
            if node.left is not None:
                q.append(queue([node.left,hd-1]))
            if node.right is not None:
                q.append(queue([node.right,hd+1]))
                
    def getLeftChildDistance(self,root):
        count=root.count
        count-=1
        return count
    
    def getRightChildDistance(self,root):
        count=root.count
        count+=1
        return count


    def verticalOrderTraversal(self, root):
        if root is None:
            return
        
        q=[]
        d={}
        
        node=queue([root,0])
        q.append(node)

        while len(q) > 0:
            
            n=q.pop(0)
            hd=n.hd
            node=n.node

            try:
                d[hd].append(node.data)
            except KeyError:
                d[hd] = [node.data]

            #b = OrderedDict(sorted(d.items()))
            
            if node.left is not None:
                q.append(queue([node.left,hd-1]))
            if node.right is not None:
                q.append(queue([node.right,hd+1]))

        sd = sorted(d.items())

        #print(sd)

        vertical=[]
        for key,value in sd:
            vertical.append(value)
            
        print(vertical)
        
##        for ll in vertical:
##            for l in ll:
##                print (l,end=" ")

class queue :
    def __init__(self,node_list):
        self.node=node_list[0]
        self.hd=node_list[1]

    
x=Node(1,0)
y=Tree()
c=y.getLeftChildDistance(x)
x.left=Node(2,c)
c=y.getRightChildDistance(x)
x.right=Node(3,c)
c=y.getRightChildDistance(x.left)
x.left.right=Node(4,c)
c=y.getRightChildDistance(x.left.right)
x.left.right.right=Node(5,c)
c=y.getRightChildDistance(x.left.right.right)
x.left.right.right.right=Node(6,c)

root = x

#y.inOrder(root)
#y.preOrder(root)
#y.postOrder(root)

#y.TopViewLevelOrderTraversal(x)                   
y.verticalOrderTraversal(x)
