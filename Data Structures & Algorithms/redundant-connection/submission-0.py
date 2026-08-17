class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
            find a cycle, and remove one of the edges(edge that appears last())

            keep track of edges that we are able to be connected to
            if there is a new vertex that we are able to be connected to, we add it
            -> us union find. remove an edge that comes after all the nodes are in one

            dfs to find a cyle. when we find the cycle, remove the edge that causes the cycle

            go with union find for practice
        """

        parent = [n for n in range(len(edges) + 1)]

        def find(v):
            print(v)
            if parent[v] != v:
                return find(parent[v])
            else:
                return v

        def union(u, v):
            parent[find(v)] = find(u)

        for u, v in edges:
            if find(u) == find(v):
                return [u,v]
            else:
                union(u, v)
