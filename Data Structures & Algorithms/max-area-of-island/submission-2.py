class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def find_area(i, j):
            area = 0
            dirs = [(1,0),(-1,0), (0,1), (0,-1)] #right, left, up, down
            q = deque()
            q.append((i,j))

            while q:
                row, col = q.popleft()
                grid[row][col] = 0
                area += 1
                for dir in dirs:
                    nr, nc = row + dir[0], col + dir[1]

                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            q.append((nr, nc))
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, find_area(i,j))


        return max_area