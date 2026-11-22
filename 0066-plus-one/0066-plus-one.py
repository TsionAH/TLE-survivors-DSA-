class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        store = ''
        for i in digits:
            store += str(i)
        ans = int(store) + 1
        ans =str(ans)
        res = []
        for i in ans:
            res.append(int(i))
        return res
