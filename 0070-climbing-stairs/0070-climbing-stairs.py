class Solution:
    def climbStairs(self, n: int) -> int:
        stor = {}
        def climbNow(n):
            if n in stor:
                return stor[n]
            if n == 1 :
                return 1
            if n == 2:
                return 2
            else:
                res = climbNow(n-1) + climbNow(n-2)
            stor[n] = res
            return res
        
        return climbNow(n)
        