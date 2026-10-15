class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda  x:x[1])
        count = 1
        left = 0
        
       # print(intervals)
        
        for i in range(1,len(intervals)):
            if intervals[i][0] >= intervals[left][1]:
                left = i
                count += 1
        return len(intervals) - count

