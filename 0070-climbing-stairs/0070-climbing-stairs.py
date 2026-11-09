class Solution:
    def climbStairs(self, n: int) -> int:
        hash_map = {}
        def memo(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in hash_map:
                return hash_map[n]
            hash_map[n]=memo(n-1) + memo(n-2)
            return hash_map[n]
                
        return memo(n)