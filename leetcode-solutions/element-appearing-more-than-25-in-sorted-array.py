class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = {}
        
        for i in arr:
            dic[i] = dic.get(i,0)+1
        for keys, values in dic.items():
            if values/len(arr) > 0.25:
                return keys
            