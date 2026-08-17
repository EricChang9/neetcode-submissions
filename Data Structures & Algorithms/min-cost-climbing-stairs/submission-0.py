class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        temp = [0] * len(cost)
        temp[0] = cost[0]
        temp[1] = cost[1]

        for i in range(2, len(cost)):
            temp[i] = (min(temp[i-1], temp[i-2]) + cost[i])

        return min(temp[-1], temp[-2])