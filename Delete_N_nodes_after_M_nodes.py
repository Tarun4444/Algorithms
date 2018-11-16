def skipMdeleteN(head, M, N):
    if head is None:
        return None
    count=0
    l=head
    while l :
        while count < M and l:
            print(l.data,end=" ")
            l=l.next
            count+=1
        count=0
        while count < N and l:
            l=l.next
            count+=1
        count=0
