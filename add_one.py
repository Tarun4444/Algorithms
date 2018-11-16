def plusOne(a):
    for x in range(len(a)):
        x += 1
        #print (a[-x])
        if a[-x] < 9:
            a[-x]+=1
            return a
        
a=[1,9,4]
print(plusOne(a))
