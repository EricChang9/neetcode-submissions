class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            keep track of our results in a dp table where dp[i] = the max subarray up to i while
            using i. if dp[i-1] is negative, then dp[i] = nums [i]. Keep track of the current max
            and return that

            Base is dp[0] = nums[0] => iterate through nums and update dp as appropriate
        '''

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]

        return max(dp)