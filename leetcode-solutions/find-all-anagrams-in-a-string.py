class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = len(p)
        res = []
        p = sorted(list(p))
        s = list(s)
        while right <= len(s):
            if sorted(s[left:right]) == p:
                res.append(left)
            left+=1
            right+=1
        return res