#Merge Intervals
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #sort by increasing order of start interval
        intervals.sort(key=lambda x: x[0])
        sol = []
        start = -10000
        max = -100000
        for i in range(len(intervals)): 
            a = intervals[i] 
            if a[0] > max: 
                if i != 0: 
                    sol.append([start,max]) 
                max = a[1] 
                start = a[0] 
            else: 
                if a[1] >= max: 
                    max = a[1] 
          
        #'max' value gives the last point of  
        # that particular interval 
        # 's' gives the starting point of that interval 
        # 'm' array contains the list of all merged intervals 
  
        if max != -100000 and [start, max] not in sol: 
            sol.append([start, max]) 
            
        return sol
        
