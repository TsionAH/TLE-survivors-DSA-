class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        res = []
        def rec(index):
            if index == len(s)-1:
                res.append(s[index])
                return
            
            val = rec(index + 1)
            res.append(s[index])
        rec(0)
        s[:] = res
