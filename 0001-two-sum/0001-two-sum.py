class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map={}
        for i,num in enumerate(nums):
            result=target-num
            if result in num_map:
                return num_map[result],i
            num_map[num]=i