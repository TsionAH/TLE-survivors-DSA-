class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) -1
        res = []
        found = False
        while not found:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] <  target:
                left += 1
            else:
                found = True
                res.append(left + 1)
                res.append(right + 1)
        return res