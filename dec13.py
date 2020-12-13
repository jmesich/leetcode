#Burst Ballons
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        #we can add ones on each side so we can always perform the same operation
        #and it wont change the value of the coins
        nums = [1] + nums + [1]
        #create an 2d array to store all possible values
        dynProg = [[0 for x in range(n + 2)] for y in range(n + 2)]
        #iterate through the nums, but you just want the valued numbers (aka not the 1 padded sides)
        for length in range(1, n + 1): 
            for left in range(1, n-length + 2): 
                right = left + length -1
  
                # For a sub-array from indices left, right 
                # This innermost loop finds the last balloon burst 
                for last in range(left, right + 1): 
                    dynProg[left][right] = max(dynProg[left][right], dynProg[left][last-1] + nums[left-1]*nums[last]*nums[right + 1] + dynProg[last + 1][right]) 
        return(dynProg[1][n])
