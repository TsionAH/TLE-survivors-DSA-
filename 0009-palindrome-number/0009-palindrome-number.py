class Solution:
    def isPalindrome(self, x: int) -> bool:
        start = 0
        s = str(x)
        end = len(s) -1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True