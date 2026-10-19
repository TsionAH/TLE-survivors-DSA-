class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1 or n % 4:
            return False
        x = log(n,4)

        return x >= 1 and x.is_integer()