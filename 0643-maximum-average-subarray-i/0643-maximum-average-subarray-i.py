class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = sum(nums[:k])
        max_avg = total / k

        for right in range(k, len(nums)):
            total = total - nums[right - k] + nums[right]
            max_avg = max(max_avg, total / k)

        return max_avg