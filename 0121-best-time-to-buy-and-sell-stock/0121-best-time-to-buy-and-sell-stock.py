class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        buying_at = prices[0]
        maxim = 0

        for i, nums in enumerate(prices):
            buying_at = min(buying_at, nums)
            profit = nums - buying_at
            maxim = max(maxim, profit)

        return maxim