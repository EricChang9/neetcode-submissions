class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            use dp where dp[i] contains all the possible ways to get i
            the for each possible value in i, iterate from i to target.
        """ 
        dp = [[] for _ in range(target+1)]
        dp[0] = [[]]

        for n in nums:
            for s in range(n, target+1):
                for comb in dp[s-n]:
                    dp[s].append(comb + [n])

        return dp[target]
