class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
            recursion or dp
            for each position, you can either keep the same index or increment

            dp is more efficient 
        '''
        def backtrack(i, total):
            if i ==len(nums):
                return  total == target

            return (backtrack(i + 1, total + nums[i]) +
                    backtrack(i + 1, total - nums[i]))

        return backtrack(0, 0)
