class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            curr_max = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    curr_max = max(curr_max, dp[j])
            dp[i] += curr_max
        return max(dp)