class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # traverse in spiral order
        # graph problem
        # row and col pointers where we shrink it each time it reaches a spot
        # 2nd example given
        # row and col pointers resulting in 4 pointers for top, bottom, left, and right
        # these pointers shrink each time a row is traversed
        # to first top pointer shrinks, then right pointer, then bottom pointer, then left pointer

        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        res = []

        while left < right and top < bottom:
            # traversing the top
            for i in range(left, right):
                res.append(matrix[top][i])
            top+=1

            # traversing right side
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right-=1

            if not (left < right and top < bottom):
                break


            # traversing the bottom
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom-=1

            # traversing left side
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left+=1

        return res