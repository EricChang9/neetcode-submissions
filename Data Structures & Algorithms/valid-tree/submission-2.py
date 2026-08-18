class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visit:
                return False
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        # Must be acyclic AND all nodes must be reachable from 0
        return dfs(0, -1) and len(visit) == n