class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = []
        sorted_he = sorted(heights)
        
        for i in range(len(heights)):
            minimum = sorted_he[i]
            index = heights.index(minimum)
            result.append(names[index])
        return result[::-1]
            
        