class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n nodes 
        # each entry of times is (source, dest, weight)
        # k = start node
        graph = defaultdict(list)
        visit = set()


        for source, dest, weight in times:
            graph[source].append((weight, dest))

        pq = [(0,k)]
        time = 0
        while pq:
            w1, node = heapq.heappop(pq)
            if node not in visit:
                visit.add(node)
                time = max(time, w1)
                for w2, dest in graph[node]:
                    if dest not in visit:
                        heapq.heappush(pq, (w2+w1, dest))
        return time if len(visit) == n else -1
