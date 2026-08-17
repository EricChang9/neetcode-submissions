class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
            we want to keep track of where we can go from i=0 using a dp table

            each dp[i] is true if we can reach it and false if not
            when iterating through all possible values in nums, update all reachable dp cells to 
            true if it is within the max distance, return t/f in the last index
        '''

        dp = [False] * len(nums)
        dp[0] = True

        for i, n in enumerate(nums):
            if dp[i]:
                for j in range(1, n+1):
                    if i+j < len(nums):
                        dp[i+j] = True

        return dp[-1]

