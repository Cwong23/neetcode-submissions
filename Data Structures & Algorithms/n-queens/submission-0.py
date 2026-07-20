class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set() # stores col num
        pos_diag = set() # stores diag
        neg_diag = set()

        def create_str_pos(col: int) -> str:
            res = "." * (n - (n - col)) + "Q" + "." * (n - col - 1)
            return res

        res = []
        spots = []

        def dfs(row: int):
            for col in range(n):
                if col not in cols and (row+col) not in pos_diag and (row-col) not in neg_diag:
                    if row + 1 == n:
                        temp = []
                        spots.append(col)
                        for x in spots:
                            temp.append(create_str_pos(x))
                        res.append(temp)
                        spots.pop()
                    else:
                        cols.add(col)
                        pos_diag.add(row+col)
                        neg_diag.add(row-col)
                        spots.append(col)
                        dfs(row+1)
                        spots.pop()
                        cols.remove(col)
                        pos_diag.remove(row+col)
                        neg_diag.remove(row-col)

        dfs(0)

        return res