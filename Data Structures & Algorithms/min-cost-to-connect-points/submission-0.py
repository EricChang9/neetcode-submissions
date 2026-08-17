class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # find the MST using prim
        # choose a starting vertex
        # add all edges
        # process all edges. if visited, skip. Else, add edge to MST, add to visited, and add all edges from this node.

        heap = [(0,0)] # each entry is edge weight, point index in points
        visit = set()

        nodes = 0
        cost = 0

        while heap:
            curr = heapq.heappop(heap)
            weight = curr[0]
            idx = curr[1]
            if idx in visit:
                continue
            visit.add(idx)
            nodes += 1
            cost += weight
            for i in range(len(points)):
                if i != idx and i not in visit:
                    dist = ((abs(points[idx][0] - points[i][0]) + abs(points[idx][1] - points[i][1])))
                    heapq.heappush(heap, (dist, i))
                    
        return cost if nodes == len(points) else -1