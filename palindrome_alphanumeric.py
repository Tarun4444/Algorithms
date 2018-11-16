def isPalindrome(self, A):
        
        i = 0
        j = len(A) - 1
        
        A = A.lower()
        
        while i < j:
            while i < len(A) - 1 and not self.isAlphaNumeric(A[i]):
                i = i + 1
                
            while j > 0 and not self.isAlphaNumeric(A[j]):
                j = j - 1
            
            if self.isAlphaNumeric(A[i]) and self.isAlphaNumeric(A[j]) and A[i] != A[j]:
                return 0
            
            i += 1
            j -= 1
        
        return 1
                
                
                

