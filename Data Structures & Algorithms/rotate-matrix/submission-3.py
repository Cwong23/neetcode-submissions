class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # You must rotate the matrix in-place

        # Transpose:
        #   [1,2],
        #   [3,4]
        # ->
        #   [1,3],
        #   [2,4]
        for row_idx in range(len(matrix)):
            for col_idx in range(row_idx+1, len(matrix)):
                matrix[row_idx][col_idx], matrix[col_idx][row_idx] = matrix[col_idx][row_idx], matrix[row_idx][col_idx]
        
        # Evident we need to reverse each row
        for row_idx in range(len(matrix)):
            # list reverse given to us
            matrix[row_idx].reverse()
