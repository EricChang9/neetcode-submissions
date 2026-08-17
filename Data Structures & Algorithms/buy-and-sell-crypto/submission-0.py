class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            j = i+1
            while(j<len(prices)):
                profit = prices[j] - prices[i]
                if profit > max:
                    max = profit
                j+=1
        return max    