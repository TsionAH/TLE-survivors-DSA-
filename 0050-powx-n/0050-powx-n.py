class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)
        def rec(n):
            if n == 0:
                return 1
            temp = rec(n//2)
            if n% 2 == 0:
                return temp * temp
            else:
                return x * temp * temp
        ans = rec(N)
        return 1/ans if n<0 else ans