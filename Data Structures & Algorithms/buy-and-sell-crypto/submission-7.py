class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        res = 0

        for price in prices:
            res = max(res, price - min_p)
            min_p = min(price, min_p)

        return res