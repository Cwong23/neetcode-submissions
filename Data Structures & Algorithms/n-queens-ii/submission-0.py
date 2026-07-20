class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set()
        neg_diag = set()

        res = 0
        def dfs(row: int) -> None:
            temp = 0
            for col in range(n):
                if col not in cols and (row+col) not in pos_diag and (row-col) not in neg_diag:
                    if row + 1 == n:
                        temp+=1
                    else:
                        cols.add(col)
                        pos_diag.add(row+col)
                        neg_diag.add(row-col)
                        temp+=dfs(row+1)
                        cols.remove(col)
                        pos_diag.remove(row+col)
                        neg_diag.remove(row-col)
            return temp

        res = dfs(0)
        return res