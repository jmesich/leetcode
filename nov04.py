#The kth Factor of n

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # initialize a vector v
        factors = []
 
        p = int(sqrt(n)) + 1
        for i in range(1, p, 1):
            if (n % i == 0):
                factors.append(i)
                if (i != sqrt(n)):
                    factors.append(n / i);
                    
        #check if k is possible
        if (k > len(factors)):
            return -1 
        
        # sort the array
        factors.sort(reverse = False)
 
        # return k
        return factors[k-1]
            
