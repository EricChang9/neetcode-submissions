class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            
            if goal in map:
                return [map[goal], i]
            map[nums[i]] = i