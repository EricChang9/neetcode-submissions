class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = {}
        for i in range(0,len(nums)):
            difference = target - nums[i]
            if difference in ls:
                return [ls[difference],i]
            ls[nums[i]] = i