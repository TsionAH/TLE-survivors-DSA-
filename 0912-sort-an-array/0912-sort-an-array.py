class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        maxim = max(nums)
        minim = min(nums)
        counter = [0] *(maxim - minim + 1)
        for i in nums:
            counter[i - minim] += 1
        res = []
        for i in range(len(counter)):
            while counter[i] > 0:
                res.append(i + minim)
                counter[i] -= 1
        return res
