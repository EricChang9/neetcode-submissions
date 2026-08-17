class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        r,l = 0, len(heights) - 1

        while r <= l:
            curr = min(heights[r], heights[l]) * (l-r)
            res = max(res, curr)
            print(curr)
            if heights[r] < heights[l]:
                r += 1
            else:
                l -= 1
        return res