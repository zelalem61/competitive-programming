class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        V = set(["a","e","i","o","u"])
        arr = [1 if x in V else 0 for x in s]
        l, r = 0, k
        suma = sum(arr[0:k])
        res = suma
        while r<len(s):
            suma += (arr[r]-arr[l])
            r+=1
            l+=1
            res = max(suma,res)
            
        return res
        