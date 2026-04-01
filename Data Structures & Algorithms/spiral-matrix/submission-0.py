class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # delete as we add to result
        # O(n + m) time since we touch every element once

        # res = []
        # while matrix:
        #     # migrate right - take the first row all the way
        #     res += matrix[0]
        #     matrix.pop(0)

        #     # migrate down - for all rows, get the last
        #     for l in matrix:
        #         res.append(l.pop(len(l) - 1))

        #     # migrate left. - for the last row, all the way reverse order
        #     res += reversed(matrix[len(matrix) - 1])
        #     matrix.pop(len(matrix) - 1)

        #     # migrate up - for all rows, get the first and in reverse
        #     for l in range(len(matrix) - 1, -1, -1):
        #         res.append(l.pop(0))
        
        # return res


        # solution
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range (top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res


