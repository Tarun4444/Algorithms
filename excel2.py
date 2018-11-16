##def convertToTitle(A):
##        res = ""
##        while A > 0:
##            A -= 1
##            temp = A%26
##            A //= 26
##            res += chr(ord('A')+temp)
##                    
##        return res[::-1]


#print(convertToTitle( 980089))


def convertToColumn(a):
    count = 0
    res=0
    for i in range(len(a)-1,-1,-1):
        res+=(ord(a[i])-ord('A')+1)*(26**count)
        count+=1
        print(res,count)

    return res

print(convertToColumn("AA"))

def convertToTitle(A):
    res = ""
    while A > 0:
        A-=1
        temp=A%26
        res+=chr(ord('A') + temp)
        A//=26

    return res
