class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        maxim = -1
        minm = nums[0]
        for i in range(len(nums)):
            
            
            if nums[i] > minm:
                maxim = max(maxim , nums[i]-minm)
            else:
                minm = nums[i]
                    
        return maxim