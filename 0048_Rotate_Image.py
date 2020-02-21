#------- 92#

# 1. Transpose matrix
# 2. Reverse each row
#-- Time: O(n^2)
#-- Space: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        for i in range(len(matrix)):
            matrix[i].reverse()

    