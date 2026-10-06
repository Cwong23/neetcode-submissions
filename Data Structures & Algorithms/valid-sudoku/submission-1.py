class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(nums: list[str]) -> bool:
            vals = set()
            for n in nums:
                if n == ".":
                    continue
                if n in vals:
                    return False
                else:
                    vals.add(n)
            return True
        
        for i in range(len(board)):
            if not is_valid(board[i]):
                return False

        for i in range(len(board)):
            col = [row[i] for row in board]
            if not is_valid(col):
                return False

        for k in range(0, 9, 3):
            ptr1 = k % 9
            for z in range(0, 9, 3):
                ptr2 = z % 9
                square = []
                for i in range(ptr1, ptr1 + 3):
                    for j in range(ptr2, ptr2 + 3):
                        square.append(board[i][j])
                if not is_valid(square):
                    return False
        return True