class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #dfs from the edges, if we reach a 'O', we can change it to S for safe. 
        #at the end, for everything that is not S, we change to X, and change S back to O
        def dfs(r, c):
            nonlocal board
            dir = [[1,0], [-1,0], [0,1], [0,-1]]

            if board[r][c] == 'O':
                board[r][c] = 'S'

                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]):
                        dfs(nr, nc)

        for i in range(len(board)):
            dfs(i,0)
            dfs(i,(len(board[0]) - 1))
        for i in range(len(board[0])):
            dfs(0, i)
            dfs(len(board)-1, i)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"

        