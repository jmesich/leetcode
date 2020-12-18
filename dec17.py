#Increasing Triplet Subsequence

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        firstNum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>firstNum:
                secondNum=nums[i]
                if len(nums)<=i+1:
                    return False
                elif nums[i+1]>secondNum:
                    return True
            firstNum=nums[i]
        return False
        
