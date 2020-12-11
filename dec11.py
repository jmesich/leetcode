#Remove Duplicates from Sorted Array II

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if less than three then cant be over the dup limit
        if len(nums)<3:
            return len(nums)
        
        back_pointer=2
        #only increment when you have found a number that is unique
        #start at 2 bc we can have 2 dup max
        for forward_pointer in range (2,len(nums)):
            if nums[back_pointer-2] != nums[forward_pointer]:
                nums[back_pointer] = nums[forward_pointer]
                back_pointer+=1
        
        for del_pointer in range(forward_pointer,back_pointer-1,-1):
            del nums[del_pointer]

        return len(nums)
