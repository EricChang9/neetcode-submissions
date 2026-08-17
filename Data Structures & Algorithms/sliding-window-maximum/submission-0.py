class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            maintain a sliding window and keep track of the max of the sliding window
            for each update step- check if the leftmost is the max, if not, the new max is 
            the max of the current max and the new right element. If the left most is the max,
            find the new max again 

        '''
        if not nums or k == 0:
            return []
        if k == 1:
            return nums

        res = []
        l, r = 0, k - 1  # make r inclusive
        curr_max = max(nums[0:k])
        res.append(curr_max)

        while r < len(nums) - 1:
            outgoing = nums[l]
            l += 1
            r += 1

            if outgoing == curr_max:
                curr_max = max(nums[l:r+1])   # include r
            else:
                curr_max = max(curr_max, nums[r])

            res.append(curr_max)

        return res