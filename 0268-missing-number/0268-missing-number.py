class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        normal_sum = sum(nums)
        expected_sum = 0
        for i in range(len(nums) + 1):
            expected_sum += i
        
        return expected_sum - normal_sum