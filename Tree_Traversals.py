class Node:

    def __init__(self,data):
        self.val=val
        self.left=None
        self.right=None

def inOrder(root):
    current = root
    s=[]
    done = 0
    while not done:
        if current is not None:
            s.append(current)
            current=current.left
        else:
            if(len(s) > 0):
                current = s.pop()
                print current.data
                current=current.right
            else:
                done = 1

def preOrder(root):
	current=root
	s=[]
	B=[]

	if current is None:
	    return

	s.append(current)

	while len(s)>0 :
	    current = s.pop()
	    B.append(current.val)

	    if current.right is not None:
		s.append(current.right)
	    if current.left is not None:
		s.append(current.left)

	return B
        

def postOrderIterative(root): 
	if root is None:
		return

	s1=[]
	s2=[]
	B=[]

	s1.append(root)
		
	while s1:
		current = s1.pop()
		s2.append(current)

		if current.left is not None:
			s1.append(current.left)
		if current.right is not None:
			s1.append(current.right)

	while s2:
		print(s2.pop().data)
		




