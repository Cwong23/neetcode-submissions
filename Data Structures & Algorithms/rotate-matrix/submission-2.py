class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose first along diagonal

        # 1 2
        # 3 4
        # -->
        # 1 3
        # 2 4
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse all of the rows
        for row in matrix:
            row.reverse()

