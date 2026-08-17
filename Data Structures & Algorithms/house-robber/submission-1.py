class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        
        if len(nums) == 1:
            return nums[0]
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])
        for i in range(2,len(arr)):
            print(arr)
            o1 = arr[i-2] + nums[i]
            o2 = arr[i-1]
            print(f"o1:{o1}, o2:{o2}")
            arr[i] = max(o1, o2)

        return arr[-1]

        