                                     def maxSpecialProduct(self, a):
                                            
                                            left_special =0 
                                            right_special =0
                                            
                                            max_special_prod=0
                                            special_prod =0
                                            
                                            for i in range(len(a)):
                                                for j in range(0,i):
                                                    #left
                                                    if a[j] > a[i]:
                                                        left_special = j
                                                        
                                                for j in range(i+1,len(a)):
                                                    #Right
                                                    if a[j] > a[i]:
                                                        right_special = j
                                                        break
                                                    
                                                special_prod = a[left_special] * a[right_special]    
                                            
                                                if special_prod > max_special_prod:
                                                    max_special_prod = special_prod
                                                
                                            return max_special_prod % 1000000007
                                                
