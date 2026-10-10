class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        normal_sum = sum(nums)
        expected_sum = len(nums)*(len(nums) + 1)//2
        
        
        return expected_sum - normal_sum