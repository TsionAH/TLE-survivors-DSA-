class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        my_map = {}
        for i,nums in enumerate(numbers,1):
            count = target - nums
            if count in my_map:
                return [my_map[count],i]
            my_map[nums] = i
        return []