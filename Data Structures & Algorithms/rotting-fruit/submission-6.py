class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find the number of fresh fruit
        # run a multi-source, level-order traversal of the graph. If at the end, there are oranges left, then return -1, track and return how many levels there where

        dirs  = [(1,0), (-1,0), (0,1), (0,-1)] #right, left, up, down

        num_fresh = 0
        time = 0

        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))

        while q and num_fresh:
            for _ in range(len(q)):
                i, j = q.popleft()

                for dir in dirs:
                    ni, nj = i + dir[0], j + dir[1]

                    if ni > -1 and ni < len(grid) and nj > -1 and nj < len(grid[0]):
                        if grid[ni][nj] == 1:
                            num_fresh -= 1
                            grid[ni][nj] = 2
                            q.append((ni, nj))
            time += 1            
    
        if num_fresh == 0:
            return time
        else:
            return -1


