class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # r, l, u, d
        visited = set()
        row, col = len(grid), len(grid[0])
        res = 0

        def search(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                curr = q.popleft()
                r, c = curr[0], curr[1]
                for d in directions:
                    nr, nc = r + d[0], c + d[1]  # Use temporary variables
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited:
                        if grid[nr][nc] == '1':
                            visited.add((nr, nc))
                            q.append((nr, nc))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    search(r, c)

        return res