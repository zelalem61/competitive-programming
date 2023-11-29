class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                
                if i <= n -2 and j <= m-2:
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False
        return True
                
                
        