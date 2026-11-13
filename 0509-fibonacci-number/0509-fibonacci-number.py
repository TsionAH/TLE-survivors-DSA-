class Solution:
    def fib(self, n: int) -> int:
        # dp bottom up 
        # Time O(n) and Space O(1)
        if n == 0 or n == 1:
            return n
        prev , curr = 0 , 1
        for i in range(n - 1):
            prev , curr = curr , prev + curr
        return curr