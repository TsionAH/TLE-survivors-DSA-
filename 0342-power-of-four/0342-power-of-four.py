class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if log(n,4).is_integer() or n == 1:
            return True
        return False