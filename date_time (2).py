def date_time(a):
    count = [0]*10
    for i in range(len(a)):
        count[a[i]]+=1

    #Month
    m=""
    if count[1] > 0:
        m+='1'
        count[1]-=1
        for i in range(2,-1,-1):
            if count[i] > 0:
                m+=str(i)
                count[i]-=1
                break
    elif count[0] > 0 :
        m+='0'
        count[0]-=1
        for i in range(9,-1,-1):
            if count[i] > 0:
                m+=str(i)
                count[i]-=1
                break
    else :
        print(0)
        return
    
    #Date
    d=""
    if count[3] > 0 :
        d+='3'
        count[3]-=1
        if count[1] > 0:
            d+='1'
            count[1]-=1
        if count[0] > 0:
            d+='0'
            count[0]-=1
            
    elif count[2] > 0:
        d+='2'
        count[2]-=1
        for i in range(9,-1,-1):
            if count[i] > 0:
                d+=str(i)
                count[i]-=1
                break

    elif count[1] > 0:
        d+='1'
        count[1]-=1
        for i in range(9,-1,-1):
            if count[i] > 0:
                d+=str(i)
                count[i]-=1
                break
        
    elif count[0] > 0:
        d+='0'
        count[0]-=1
        for i in range(9,-1,-1):
            if count[i] > 0:
                d+=str(i)
                count[i]-=1
                break
        
    else :
        print(0)
        return
    
    date=m+"/"+d

    #print(date)

    ##Hour
    h=""
    if count[2] > 0 :
        h+='2'
        count[2]-=1
        for i in range(3,-1,-1):
            if count[i] > 0:
                h+=str(i)
                count[i]-=1
                break
    elif count[1] > 0 :
        h+='1'
        count[1]-=1
        for i in range(9,-1,-1):
            if count[i] > 0:
                h+=str(i)
                count[i]-=1
                break
    elif count[0] > 0 :
        h+='0'
        count[0]-=1
        for i in range(9,-1,-1):
            if count[i] > 0:
                h+=str(i)
                count[i]-=1
                break
    else :
        print(0)
        return

    ##Minute
    t=""
    flag=0
    for i in range(5,-1,-1):
         if count[i] > 0:
                t+=str(i)
                flag=1
                count[i]-=1
                break
    if flag==0:
        print(0)
        return

    flag=0
    for i in range(9,-1,-1):
        if count[i] > 0:
            t+=str(i)
            count[i]-=1
            flag=1
            break
    if flag==0:
        print(0)
        return
    
    time=h+":"+t  
    print(date+" "+time)
    
a=[0,0,1,2,2,2,3,5,9,9,9,9]
date_time(a)
        
