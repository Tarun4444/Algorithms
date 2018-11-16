def maxSubArray(self, A)
        
        curr_sum = max_sum = A[0]
        
        p = 0
        for i in range(len(A))
            if(A[i]0)
                p=1
                break
            else
                curr_sum=A[i]
                if curr_sum  max_sum and curr_sum  0
                    max_sum=curr_sum
        
        if p==1
            curr_sum = max_sum = 0
            for i in range(len(A))
                curr_sum = curr_sum+A[i]
                
                if curr_sum  max_sum 
                    max_sum=curr_sum
                
                if curr_sum  0
                    curr_sum = 0