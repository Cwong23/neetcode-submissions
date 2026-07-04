class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def convert_2D_position_to_1D(pos):
            row, col = pos
            return row * n + col
        
        def convert_1D_position_to_2D(index):
            row = index // n
            col = index % n
            return [row, col]

        left, right = [0, 0], [m - 1, n - 1]
        left_1D, right_1D = convert_2D_position_to_1D(left), convert_2D_position_to_1D(right)
        while left_1D <= right_1D:
            middle_1D = int((left_1D + right_1D) / 2)
            middle = convert_1D_position_to_2D(middle_1D)

            middle_val = matrix[middle[0]][middle[1]]
            if middle_val == target:
                return True
            elif middle_val > target:
                right = convert_1D_position_to_2D(middle_1D - 1)
            else:
                left = convert_1D_position_to_2D(middle_1D + 1)
            left_1D, right_1D = convert_2D_position_to_1D(left), convert_2D_position_to_1D(right)
        return False
