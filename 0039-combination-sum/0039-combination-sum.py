class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def backtrack(total,inputs,index):
            if total == target:
                result.append(inputs[:])
                return
            if total > target:
                return
            for i in range(index,len(candidates)):
                index = i
                inputs.append(candidates[i])
                backtrack(total + candidates[i],inputs,index)

                inputs.pop()
        backtrack(0,[],0)
        return result 