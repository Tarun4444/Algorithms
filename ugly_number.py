
def ugly(n):

    u=[0]*n
    u[0]=1
    i=i1=i2=i3=0

    m1=2
    m2=3
    m3=5

    for l in range(1,n):
        u[l]=min(m1,m2,m3)
        if u[l]==m1:
            i1+=1
            m1=u[i1]*2

        if u[l]==m2:
            i2+=1
            m2=u[i2]*3

        if u[l]==m3:
            i3+=1
            m3=u[i3]*5

    return u[-1]

print(ugly(150))
