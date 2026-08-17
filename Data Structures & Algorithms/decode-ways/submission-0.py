class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # dp[i] will store the number of ways to decode s[:i]
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # Base case for the empty string
        dp[1] = 1  # We already checked s[0] != '0'

        for i in range(2, n + 1):
            # Single digit check: is s[i-1] valid? (1-9)
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # Two digit check: is s[i-2:i] valid? (10-26)
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]