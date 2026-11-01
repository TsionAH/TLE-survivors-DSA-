class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtracking(index, path):
            if index == len(nums):
                result.append(path[:])
                return

            # Choice 1: Include
            path.append(nums[index])
            backtracking(index + 1, path)

            # Undo
            path.pop()

            # Choice 2: Exclude
            backtracking(index + 1, path)

        backtracking(0, [])
        return result