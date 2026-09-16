class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # empty board? verify in constraints

        m, n = len(board), len(board[0])
        
        # find + crush
        def find_and_crush() -> bool:
            complete: bool = True
            
            # Check vertical (row) candies
            for r in range(1, m-1):
                for c in range(n):
                    if board[r][c] == 0:
                        continue
                    
                    if abs(board[r-1][c]) == abs(board[r][c]) == abs(board[r+1][c]):
                        board[r-1][c] = -abs(board[r-1][c])
                        board[r][c] = -abs(board[r][c])
                        board[r+1][c] = -abs(board[r+1][c])
                        complete = False
            
            
            # Check horizontal (col) candies
            for r in range(m):
                for c in range(1, n-1):
                    if board[r][c] == 0:
                        continue
                    
                    if abs(board[r][c-1]) == abs(board[r][c]) == abs(board[r][c+1]):
                        board[r][c-1] = -abs(board[r][c-1])
                        board[r][c] = -abs(board[r][c])
                        board[r][c+1] = -abs(board[r][c+1])    
                        complete = False
            
            # crush the candies
            for r in range(m):
                for c in range(n):
                    if board[r][c] < 0:
                        board[r][c] = 0
            
            return complete
            
        def drop() -> None:

            # group by cols
            for c in range(n):
                # must reset for every column
                lowest_zero_idx: int = -1

                # go bottom to top
                for r in range(m-1, -1, -1):
                    if board[r][c] == 0:
                        lowest_zero_idx = max(lowest_zero_idx, r)
                        
                    elif lowest_zero_idx >= 0:
                        board[r][c], board[lowest_zero_idx][c] = board[lowest_zero_idx][c], board[r][c]
                        lowest_zero_idx -= 1
                    
        
        while not find_and_crush():
            drop()
            
        return board