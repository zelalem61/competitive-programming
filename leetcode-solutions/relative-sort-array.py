class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = Counter(arr1)
        res = []
        arr1.sort()
        for num in arr2:
            for i in range(dic[num]):
                res.append(num)
        for j in arr1:
            if j not in arr2:
                res.append(j)
        return res
        