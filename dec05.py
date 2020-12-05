#can place flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        
        num_spots=0
        
        for spot in range(len(flowerbed)):
            if flowerbed[spot] == 0 and (spot==0 or flowerbed[spot-1] == 0 ) and (spot == len(flowerbed)-1 or flowerbed[spot+1] == 0):
                
                flowerbed[spot] = 1
                num_spots+=1
                if num_spots>=n:
                    return True
            
        if num_spots < n:
            return False
        
        return True
        
