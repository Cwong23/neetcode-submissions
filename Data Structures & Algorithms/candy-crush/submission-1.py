class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m: int = len(board)
        n: int = len(board[0])

        # find + crush
        def find_and_crush() -> bool:
            complete: bool = True

            # check horizontally
            for r in range(m):
                for c in range(1, n-1):
                    if board[r][c] == 0:
                        continue

                    if abs(board[r][c-1]) == abs(board[r][c]) == abs(board[r][c+1]):
                        board[r][c-1] = -abs(board[r][c-1])
                        board[r][c] = -abs(board[r][c])
                        board[r][c+1] = -abs(board[r][c+1])
                        complete = False



            # check vertically
            for r in range(1, m-1):
                for c in range(n):
                    if board[r][c] == 0:
                        continue

                    if abs(board[r-1][c]) == abs(board[r][c]) == abs(board[r+1][c]):
                        board[r-1][c] = -abs(board[r-1][c])
                        board[r][c] = -abs(board[r][c])
                        board[r+1][c] = -abs(board[r+1][c])
                        complete = False

            # crush the candies after being marked
            for r in range(m):
                for c in range(n):
                    if board[r][c] < 0:
                        board[r][c] = 0

            return complete


        # drop
        def drop():
            for c in range(n):
                lowest_zero: int = -1

                for r in range(m-1, -1, -1):
                    if board[r][c] == 0:
                        lowest_zero = max(lowest_zero, r)
                    
                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        lowest_zero -= 1

        while not find_and_crush():
            drop()

        return board




