class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            val = matrix[m // len(matrix[0])][m % len(matrix[0])]
            if target > val:
                l = m + 1
            elif target < val:
                r = m - 1
            elif target == val:
                return True
        return False

        