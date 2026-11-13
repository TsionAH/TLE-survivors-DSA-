class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # top _ down dp approach 
        # time o(n) and space o(n)
        if n == 1:
            return True
        temp = {}
        def power(n):
            if n in temp:
                return temp[n]
            if n == 1:
                return True
            if n < 1 or n % 2 != 0:
                return False
            else:
                temp[n] = power(n//2)
                return temp[n]
        return power(n)
            