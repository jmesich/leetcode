#4Sum II

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sums ={}
        #add every combination of A and B into the sums
        #use the total as the key and the value is the number of times it is possible
        for i in A:
            for j in B:
                if i+j not in sums:
                    sums[i+j] = 1
                else:
                    sums[i+j] +=1
                    
        sol = 0
        #do the same, every combination of C and D 
        # but multiply by 1 to see if there is a matching value
        # if there is add the value to the solution
        for i in C:
            for j in D:
                if -1 * (i+j) in sums:
                    sol+=sums[-1*(i+j)]
        return sol
        
