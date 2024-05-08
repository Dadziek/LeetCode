class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = max_diff = 0
        for price in reversed(prices):
            max_diff = max(max_diff, max_price - price)
            max_price = max(max_price, price)
        return max_diff