class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        n = 0
        for word in words:
            if len(word) > n:
                n = len(word)
        
        l = 0
        while l < n:
            arr = []
            for m in words:
                if l >= len(m):
                    arr.append(-1)
                elif l < len(m):
                    arr.append(order.index(m[l]))
            # print(arr)
            if arr != sorted(arr):
                print(arr)
                return False
            elif len(arr) == len(set(arr)):
                return True
            l += 1
        return True