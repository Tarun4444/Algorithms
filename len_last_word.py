def lengthOfLastWord(self, s):
        i=0
        l=[]
        j=len(s)
        ss=''
        
        if j==0:
            return 0
        else:
            while i<j :
                if s[i]==' ':
                    l.insert(0,ss)
                    ss=''
                else:
                    ss+=s[i]
                i+=1
            
            l.insert(0,ss)

            for i in range(len(l)):
                if len(l[i])>0:
                    return len(l[i])
            else:
                return 0