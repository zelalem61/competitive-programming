class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = ""
        res = 0
        index = 0
        while index < len(s):
            if s[index] not in ss:
                ss+=s[index]
            else:
                res = max(res,len(ss))
                ss = ss[ss.index(s[index])+1:] + s[index]  
            index+=1
        return max(res,len(ss))