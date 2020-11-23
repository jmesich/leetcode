#Longest Mountain in Array
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        if size <3: 
            return 0
        i = 0
        j = 0
        ans = 0
        
        while i<size:
            j = i
            while j+1<size and A[j]<A[j+1]:
                j=j+1
            mid = j
            while j+1<size and A[j]>A[j+1]: 
                j=j+1
            if i<mid and mid<j:
                ans = max(ans,j-i+1)
            if i == j:
                i=i+1
            else: 
                i = j

        return ans;
