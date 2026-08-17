class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    visited = set()
                    q.append((r,c))
                    visited.add((r,c))
                    level = 0
                    while q:
                        level += 1

                        for _ in range(len(q)):
                            curr = q.popleft()

                            for d in directions:
                                nr, nc = curr[0] + d[0], curr[1] + d[1]

                                if nr >= 0 and nr < n and nc >= 0 and nc < m and (nr,nc) not in visited:
                                    if grid[nr][nc] > 0:
                                        grid[nr][nc] = min(grid[nr][nc], level)
                                        q.append((nr,nc))
                                        visited.add((nr,nc))
                            