class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
            valid tree => no cycles
            1. dfs with cycle detection
            2. disjoin set union -> if we ever add an edge to 2 things that are in the same set already, 
            then it is false -> hard because we have to find connectivity
            3. use bfs cycle detection


            want to run a dfs. everytime we need to pass in the parent, and also keep track of what
            nodes we have already seen. 
            
            dfs method should return False if we see a cycle. If not, we check the lenght of visited
            to see if the graph is connected
        """

        adj = [[] for i in range(n)]
        seen = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(v, parent):
            if v in seen:
                return False
            seen.add(v)
            for nei in adj[v]:
                if nei == parent:
                    continue
                if not dfs(nei, v):
                    return False
            return True

        if not dfs(0, -1):
            return False
        print(seen)
        return len(seen) == n





            


        
        

            
        