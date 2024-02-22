class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        las={}
        for i in range(len(s)):
            las[s[i]]=i
        most=0
        res=[]
        c=0
        for i in range(len(s)):
            c=c+1
            if las[s[i]]>most:
                most=las[s[i]]
            if las[s[i]]==most and i==most:
                res.append(c)
                most=0
                c=0
        return res
        