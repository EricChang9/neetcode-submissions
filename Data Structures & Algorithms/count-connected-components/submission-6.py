class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        if n == 1:
            return 1
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        res = 0
        for u in graph.keys():
            if u not in visited:
                res += 1
                print(f"res: {res} visited: {visited}")
                q = deque()
                q.append((u))
                visited.add(u)
                while q:
                    curr = q.popleft()
                    if curr in graph:
                        for v in graph[curr]:
                            if v not in visited:
                                q.append(v)
                                visited.add(v)

        return res + (n - len(visited))