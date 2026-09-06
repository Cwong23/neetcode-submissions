class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows: int = len(boxGrid)
        cols: int = len(boxGrid[0])

        # Iterate rows --> cols
        # O(mn)
        for r in range(rows):
            i = cols-1
            # Go right to left
            for c in reversed(range(cols)):
                # Current element is stone
                if boxGrid[r][c] == "#":
                    # Swap with curr right most element
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    # Move ptr to left
                    i -= 1
                
                if boxGrid[r][c] == "*":
                    i = c-1

        # Transpose and reverse rows to achieve 90deg rotation
        transposed: List[List[str]] = [list(row) for row in zip(*boxGrid)]
        # Reverse
        # O(n)
        for row in transposed:
            # O(m)
            row.reverse()

        return transposed