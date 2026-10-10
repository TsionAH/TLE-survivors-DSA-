class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sort = sorted(nums)
        first = 0
        for i in range(len(sort)):
            if sort[i] != first :
                return first
            first += 1
        return len(sort)

        