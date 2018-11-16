def countDistinct(a,k):
    d={}
    dist_count=0
    for i in range(k):
        if a[i] not in d:
            d[a[i]]=1
            dist_count+=1
        else :
             d[a[i]]+=1
             
    print(dist_count)
    
    for i in range(k,len(a)):

        if d[a[i-k]] == 1:
            del(d[a[i-k]])
            dist_count-=1
        else :
            d[a[i-k]]=1

        if a[i] not in d:
            d[a[i]]=1
            dist_count+=1
        else:
            d[a[i]]+=1

        print(dist_count)

countDistinct([1, 2, 1, 3, 4, 2, 3],4)
