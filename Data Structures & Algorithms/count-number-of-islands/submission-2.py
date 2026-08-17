class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    grid[i][j] = "0"
                    self.bfs(i, j, grid)

    
        return res

    def bfs(self, i, j, grid):
        q = deque()
        q.append((i,j))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r,c = q.popleft()
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]

                if nr > -1 and nr < len(grid) and nc > -1 and nc < len(grid[0]):
                    if grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
