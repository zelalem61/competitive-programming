class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distResult = []
        point = points.copy()
        result = []
        
        for i in points:
            dist = (i[0])**2 + (i[1])**2
            distResult.append(dist)
        while k>0:
            minimum = min(distResult)
            j = distResult.index(minimum)
            result.append(point[j])
            del point[j]
            del distResult[j]
            k-=1
            
        return result     
            
            