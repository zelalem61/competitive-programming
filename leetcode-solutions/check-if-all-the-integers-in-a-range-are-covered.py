class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            bo = False
            for j in ranges:
                if i >= j[0] and i <= j[1]:
                    
                    bo = True
                    continue
            if bo == False:
                return False
        return True