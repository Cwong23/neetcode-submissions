class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()
        N, M = len(board), len(board[0])
        nodes = []
        coords = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(N):
            if board[i][0] == "O":
                nodes.append((i, 0))
            if board[i][M-1] == "O":
                nodes.append((i, M-1))
        for i in range(M):
            if board[0][i] == "O":
                nodes.append((0, i))
            if board[N-1][i] == "O":
                nodes.append((N-1, i))
        
        while nodes:
            x, y = nodes.pop()
            safe.add((x, y))

            for coord in coords:
                x_new = x + coord[0]
                y_new = y + coord[1]
                if (x_new, y_new) in safe or x_new < 0 or x_new >= N or y_new < 0 or y_new >= M:
                    continue
                if board[x_new][y_new] == "O":
                    nodes.append((x_new, y_new))
        for i in range(N):
            for j in range(M):
                if board[i][j] == "O" and (i, j) not in safe:
                    board[i][j] = "X"
        return