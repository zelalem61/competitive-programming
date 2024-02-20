class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        counter = 0
        res = 1
        points = sorted(points, key=lambda x:x[1])
        for i in range(1,len(points)):
            if points[i][0] <= points[counter][1] <= points[i][1]:
                continue
            else:
                res+=1
                counter = i
        return res
        