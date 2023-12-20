class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        down = False
        dic = {}
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if i + j in dic:
                    dic[i+j].append([i,j])
                else:
                    dic[i+j] = [[i,j]]
        for arr in dic.values():
            if down:
                for ind in list(arr):
                    res.append(mat[ind[0]][ind[1]])
                down = False
            else:
                for i in range(len(list(arr))-1,-1,-1):
                    res.append(mat[arr[i][0]][arr[i][1]])
                down = True
        return res

    
