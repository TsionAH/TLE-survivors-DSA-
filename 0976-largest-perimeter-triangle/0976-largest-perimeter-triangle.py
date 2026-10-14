class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort(reverse=True)
        
        max1 = 0
        for i in range(2,len(nums)):
            maxim = 0
            
            if nums[i] + nums[i-1] > nums[i-2] and nums[i] + nums[i-2] > nums[i-1]and nums[i-2] + nums[i-1] > nums[i]  :
                maxim = nums[i] + nums[i-1] + nums[i-2]
                    
                
            max1 = max(max1,maxim)
        return max1