class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in flights:
            edges[u].append((v, w))

        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            prev = dist[:]
            for u in edges:
                if prev[u] == INF:
                    continue
                for v, w in edges[u]:
                    if prev[u] + w < dist[v]:
                        dist[v] = prev[u] + w

        return -1 if dist[dst] == INF else dist[dst]