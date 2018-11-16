def merge(A):
    B=[]
    A.sort(key=lambda x:x[0])
    B.append(A[0])

    for i in range(1,len(A)):
        if A[i][0] > B[-1][1]:
            B.append([ A[i][0],A[i][1] ])

        elif B[-1][1] < A[i][1]:
            B[-1][1]=A[i][1]
    print(B)
merge( [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ])
