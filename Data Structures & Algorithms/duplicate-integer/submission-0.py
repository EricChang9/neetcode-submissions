class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map.keys():
                map[num] +=1
            else:
                map[num] = 1
        for key,val in map.items():
            if val > 1:
                return True
        return False
         