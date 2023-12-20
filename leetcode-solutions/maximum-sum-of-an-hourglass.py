class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0
        def checkSum(self,initial: List[int],grid):
            a, b = initial[0], initial[1]
            s = grid[a][b] + grid[a][b+1] + grid[a][b+2] + grid[a+1][b+1] + grid[a+2][b] + grid[a+2][b+1] + grid[a+2][b+2]

            return s
        
        for i in range(m):
            for j in range(n):
                if i + 2 < m and j + 2 < n:
                    sums = checkSum(self,[i,j],grid)
                    if sums > res:
                        res = sums
        return res