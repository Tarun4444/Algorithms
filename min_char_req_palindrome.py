    def solve(self, A):
        cnt=0
        flag=0
        while(len(A) > 0):
            if A[::-1] == A:
                flag=1
                break
            else:
                cnt+=1
                A=A[:(len(A)-1)]
        
        if flag:
            return cnt
