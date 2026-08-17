class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #use bfs to find islands, and keep track of the max size of an island 
        #everytime we process a piece of land as island, set it to. 0 so that we dont have to process it again 
        if not grid: 
            return 0

        m = len(grid)
        n = len(grid[0])
        max_area = 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr_area = 1
                    q = deque()
                    grid[i][j] = 0
                    q.append((i,j))

                    while q:
                        r, c = q.popleft()
                        for d in directions:
                            nr, nc = r + d[0], c + d[1]

                            if nr > -1 and nr < m and nc > -1 and nc < n and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                curr_area += 1
                                q.append((nr,nc))

                    max_area = max(max_area, curr_area)


        return max_area