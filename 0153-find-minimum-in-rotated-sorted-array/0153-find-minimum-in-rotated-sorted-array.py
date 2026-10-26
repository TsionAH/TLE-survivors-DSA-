class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_no = float('inf')
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right - left)// 2
            min_no = min(min_no,nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return min_no


                