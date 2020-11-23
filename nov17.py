#Mirror Reflection
import math
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        x = 0
        y = 0
        b = q
        a = p
        #least common multiple
        while b>0 :
            t = a % b
            a = b
            b = t
        gcd = a
        g = p * q / gcd
        y = g / p
        x = g / q
        
        mod_x = x % 2
        mod_y = y % 2
        
        if mod_x == 1 and mod_y == 0:
            return 0
        
        elif mod_x == 1 and mod_y == 1:
            return 1
        
        elif mod_x == 0 and mod_y == 1:
            return 2
        
        return 0
    

        
