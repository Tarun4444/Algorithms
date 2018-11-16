import sys

def reach(source,step,dest):
    if abs(source) > dest:
        return sys.maxsize
    if source == dest:
        return step
    pos = reach(source+step+1,step+1,dest)
    neg = reach(source-step-1,step-1,dest)
    
    return min(pos,neg)
    
    #return min(reach(source+step+1,step+1,dest),reach(source-step-1,step-1,dest))

t=int(input())
while t:
    d=int(input())
    print(reach(0,0,d))
    t-=1
    
