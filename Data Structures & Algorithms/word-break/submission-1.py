class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #state at i is whether or not 0:i is valid

        dp = [False] * len(s)
        MAX = 0

        for word in wordDict:
            MAX = max(len(word), MAX)

        for i in range(MAX):
            if s[:i+1] in wordDict:
                dp[i] = True

        for i in range(len(s)):
            for j in range(i):
                if dp[j] and s[j+1:i+1] in wordDict:
                    dp[i] = True
        print(dp)
        return dp[-1]
        
        