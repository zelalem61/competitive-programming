class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        
        i = 0
        j = 0
        k = 0
        while j < len(word1) and k < len(word2):
            if i == 0:
                res += word1[j]
                j+=1
                i = 1
            else:
                res += word2[k]
                k+=1
                i=0
        if j == len(word1) and k==len(word2):
            return res
        elif j == len(word1):
            while k < len(word2):
                res+=word2[k]
                k+=1
        elif k == len(word2):
            while j < len(word1):
                res+=word1[j]
                j+=1
        return res
        