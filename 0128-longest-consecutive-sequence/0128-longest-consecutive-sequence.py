class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_val = set(nums)
        max_sum = 0
        for num in set_val:
            if num -1 not in set_val:
                count = 1
                while num + count  in set_val:
                    count += 1
                max_sum = max(max_sum,count)
        return max_sum