class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        res = [0]*len(nums)
        zeros = 0
        for num in nums:
            if num != 0:
                total *= num 
            else:
                zeros += 1
        if zeros > 1: return res

        for i,num in enumerate(nums):
            if num != 0 and zeros == 0:
                res[i] = int(total/num)
            else:
                if num == 0:
                    res[i] = total
        return res
