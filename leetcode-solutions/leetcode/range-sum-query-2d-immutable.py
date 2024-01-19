class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.pre = []

        for nums in self.matrix:
            self.pre.append(list(accumulate([0]+ nums)))
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = 0
        for i in range(row1,row2+1):
            summ += self.pre[i][col2+1] - self.pre[i][col1]
        return summ

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)