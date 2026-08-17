class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1) #each dp[i] = min num of perfect squares need to get to i
        dp[0] = 0

        for i in range(1, len(dp)):
            for j in range(1,i+1):
                if i - (j**2) >= 0:
                    dp[i] = min(dp[i - (j**2)] + 1, dp[i])
                else:
                    break
        if dp[n] == float('inf'):
            return -1
        else: return dp[n]