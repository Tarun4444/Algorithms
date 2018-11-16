def reverseWords(s):
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
        # print(len(l[0]))
        print ' '.join(str(x) for x in l)

reverseWords("fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq")