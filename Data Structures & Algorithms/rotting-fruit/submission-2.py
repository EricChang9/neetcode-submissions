class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dir = [[1,0], [-1,0], [0,1], [0,-1]]
        
        num_fresh = 0
        num_seen = 0
        q = deque()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        time = 0
        while q:
            if num_seen == num_fresh:
                    break
            for _ in range(len(q)):
                
                r,c = q.popleft()

                for d in dir:
                    nr, nc = r + d[0], c + d[1]

                    if nr >= 0 and nr < n and nc >= 0 and nc < m:
                        if grid[nr][nc] == 1:
                            num_seen += 1
                            grid[nr][nc] = 2
                            q.append((nr,nc))
            time += 1
        print(num_seen, num_fresh, time)
        return time if num_seen == num_fresh else -1
