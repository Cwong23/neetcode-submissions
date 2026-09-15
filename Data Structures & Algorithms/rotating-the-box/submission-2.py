class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows: int = len(boxGrid)
        cols: int = len(boxGrid[0])
        
        # Apply gravity left to right first 
        # do so across the rows
        for r in range(rows):
            # maintain pointer to rightmost point at row
            i = cols - 1
            # go right to left
            for c in reversed(range(cols)):
                # handle stone
                if boxGrid[r][c] == "#":
                    # swap
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c] 
                    # set just before stone
                    i = i-1
                # handle obstacle
                elif boxGrid[r][c] == "*":
                    i = c - 1
        
        # rotate box 90deg via transpose + reverse row
        output: list[list[str]] = [list(row) for row in zip(*boxGrid)]
        
        for row_idx in range(len(output)):
            output[row_idx].reverse()
            
        return output