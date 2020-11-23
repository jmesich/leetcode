#Search in Rotated Sorted Array II
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        #i could also use python basic IN keyword if target in num return true
        #init the start and the end of the array
        left=0
        right=len(nums)-1
        
        while left<=right:
            #find the current mid
            mid = (left+right)/2
            #check if mid is the target
            #we will slowly whittle the array bounds down to the middle
            if nums[mid]==target:
                return True
            #if the left edge is smaller than the middle we have 2 options
            if nums[left]<nums[mid]:
                #if the left bound is smaller than the target and the target is smaller than the mid, then it must be in the left half
                if nums[left]<=target and target<nums[mid]:
                    right=mid-1
                #else its in the right half
                else:
                    left=mid+1
            #do the same but for the other side
            elif nums[left]>nums[mid]:
                if nums[mid]<target and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
                
            else:
                left=left+1   
        
 
        return False

        
