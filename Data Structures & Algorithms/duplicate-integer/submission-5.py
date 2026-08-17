class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        for k, v in cnt.items():
            if v > 1:
                return True

        return False