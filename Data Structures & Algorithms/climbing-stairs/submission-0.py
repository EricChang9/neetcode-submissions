class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n+1)

        res[0] = 1
        
        for i in range(n+1):
            print(res)
            if i+1 < n+1:
                res[i+1] += res[i]
            if i+2 < n+1:
                res[i+2] += res[i]
        return res[-1]