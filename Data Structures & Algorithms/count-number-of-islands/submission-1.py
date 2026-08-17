class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        temp = grid
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # r, l, u, d
        for r in range(len(temp)):
            for c in range(len(temp[0])):
                q = deque()
                if temp[r][c] == '1':
                    res += 1
                    q.append((r,c))
                    temp[r][c] = '0'
                    while q:
                        curr = q.popleft()
                        cr, cc = curr[0], curr[1]
                        for dir in directions:
                            nr = cr + dir[0]
                            nc = cc + dir[1]

                            if nr >=0 and nr < len(temp) and nc >= 0 and nc < len(temp[0]):
                                if temp[nr][nc] == '1':
                                    q.append((nr,nc))
                                    temp[nr][nc] = '0'

        return res