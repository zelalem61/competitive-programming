class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        ind = []
        ans = []
        for i in range(len(list1)):
            if list1[i] in list2:
                b = list2.index(list1[i])
                dic[list1[i]] = i + b
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        
        for key, value in dic.items():
            ind.append(value)
        mini = min(ind)
        
        for key, value in dic.items():
            if value == mini:
                ans.append(key)
        return ans
