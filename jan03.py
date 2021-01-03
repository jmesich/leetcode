class Solution(object):
    def countArrangement(self, N):
        """
        :type n: int
        :rtype: int
        """
        def countHelper(n, arr):
            #if the size is negative than dont continue
            if n <= 0:
                return 1
            count = 0
            #iterate through each value in the array
            for i in range(n):
                #check if the val at n is divisible by i and vice versa
                if arr[i] % n == 0 or n % arr[i] == 0:
                    arr[i] = arr[n-1]
                    arr[n-1] = arr[i]
                    count += countHelper(n - 1, arr)
                    arr[i] = arr[n-1]
                    arr[n-1] = arr[i]
            return count

        #sends it an array from 1 to N+1
        return countHelper(N, range(1, N+1))
        
