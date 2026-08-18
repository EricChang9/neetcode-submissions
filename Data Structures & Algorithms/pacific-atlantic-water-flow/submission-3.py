class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]


        def p_search(r, c):
            pac.add((r,c))
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr > -1 and nr < len(heights) and nc > -1 and nc < len(heights[0]):
                    if heights[nr][nc] >= heights[r][c] and (nr, nc) not in pac:
                        p_search(nr, nc)
        def a_search(r, c):
            atl.add((r,c))
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr > -1 and nr < len(heights) and nc > -1 and nc < len(heights[0]):
                    if heights[nr][nc] >= heights[r][c] and (nr, nc) not in atl:
                        a_search(nr, nc)


        for i in range(len(heights)):
            p_search(i, 0)
            a_search(i, len(heights[0]) - 1)

        for i in range(len(heights[0])):
            p_search(0, i)
            a_search(len(heights) - 1, i)


        return list(pac & atl)

