class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0

        for _ in range(k+1):
            temp = list(cost)
            for flight in flights:
                u, v, weight = flight
                if cost[u] == float('inf'):
                    continue
                if cost[u] + weight < temp[v]:
                    temp[v] = cost[u] + weight
            cost = temp
        if cost[dst] == float('inf'):
            return -1
        return cost[dst]