#  Smallest Integer Divisible by K



class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K%2 == 0 or K%5 ==0:
            return -1
        
        num = 0; 
  
        length = 1; 
        #generate numbers from 1, K+1
        for length in range(1,K+1): 
            num = num * 10 + 1; 
  
        # check divisibility
            if ((num % K == 0)): 
                return length; 
  
        return -1; 
        
