class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        min_arr = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_arr = min(min_arr, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_arr == float('inf') else min_arr