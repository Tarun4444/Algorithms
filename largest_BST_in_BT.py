class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class Info:
    def __init__(self,isBST,size,minn,maxx):
        self.size = size
        slef.min  = minn
        self.max  = maxx
        self.isBST =  isBST
