#   Consecutive Characters

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=1
        counter=1
        for char in range(1, len(s)): 
            
            if(s[char-1] == s[char]):
                counter=counter+1
                if(counter>max):
                    max=counter
            else:
                
                counter=1
        
        
        return max
            
        
