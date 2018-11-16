def date_time(a):

    if len(a) < 12 :
        print(0)
        return
    
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

    if m == "00":
        print(0)
        return

    date_count = count
    
    #Date
    d=""
    if count[3] > 0 :
        d+='3'
        count[3]-=1
        if count[1] > 0:
            d+='1'
            count[1]-=1
        elif count[0] > 0:
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
    
    if d == "00":
        print(0)
        return
   
    dd = int(d)
    mm = int(m)

    if mm == 2 :
        if dd >= 28 :
            count=date_count
            d=""
            if count[2] > 0:
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
            
    elif int(mm)%2 == 1 :
        if dd == 31:
            d='30'
            
    date=m+"/"+d

    

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
    
def main():
    a=input()
    a=a.split(',')
    a=list(map(int,a))
    date_time(a)

main()        
