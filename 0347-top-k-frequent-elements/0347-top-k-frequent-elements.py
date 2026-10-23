from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if not nums:
            return []
        res = []
        nums = Counter(nums)
        nums = sorted(nums.items(),key=lambda x:x[1],reverse=True)
        for index , val in enumerate(nums):
            if index < k:
                res.append(val[0])
        return res