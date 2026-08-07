class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        
        vertical_flipped = boxGrid[::-1]
        rotated = [["" for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                rotated[j][i] = vertical_flipped[i][j]
        
        for col in range(m):
            write_pos = n - 1
            for row in range(n - 1, -1, -1):
                if rotated[row][col] == "#":
                    rotated[row][col] = "."
                    rotated[write_pos][col] = "#"
                    write_pos -= 1
                elif rotated[row][col] == "*":
                    write_pos = row - 1
        return rotated
