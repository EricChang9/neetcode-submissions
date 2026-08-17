class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if arr[-1] >= target:
                l,r = 0,len(arr)-1
                while(l<=r):
                    m = l + (r-l//2)
                    if target > arr[m]:
                        l = m + 1
                    elif target < arr[m]:
                        r = m - 1
                    else:
                        return True
        return False