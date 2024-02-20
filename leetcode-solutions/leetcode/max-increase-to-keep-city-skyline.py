class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res = 0
        rowMax = []
        colMax = [float('-inf')] * len(grid)
        for row in grid:
            rowMax.append(max(row))
        

        for j in range(len(grid)):
            for i in range(len(grid)):
                colMax[j] = max(colMax[j], grid[i][j])
        for i in range(len(grid)):
            for j in range(len(grid)):
                res+= min(rowMax[i],colMax[j])-grid[i][j]
        return res