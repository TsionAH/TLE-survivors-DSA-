class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_table = {}
        result = []
        for i in range(len(nums)):
            my_table[nums[i]] = i
        for i in range(len(nums)):
            index = target - nums[i]
            if index in my_table:
                if my_table[index] != i:
                    return [i,my_table[index]]
                
        return []
        