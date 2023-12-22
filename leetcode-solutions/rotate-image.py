class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for t in range(n//2):
            i = [t,t]
            j = [t,n-t-1]
            k = [n-t-1,n-t-1]
            l = [n-t-1,t]
            while i[1] < n-t-1:
                matrix[i[0]][i[1]],matrix[j[0]][j[1]],matrix[k[0]][k[1]],matrix[l[0]][l[1]] = matrix[l[0]][l[1]],matrix[i[0]][i[1]],matrix[j[0]][j[1]],matrix[k[0]][k[1]]
                i[1]+=1
                j[0]+=1
                k[1]-=1
                l[0]-=1