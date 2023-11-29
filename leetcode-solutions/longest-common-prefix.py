class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans =""
        bo = True
        n = float("inf")
        for k in strs:
            if len(k) < n:
                n = len(k)
        for i in range(n):
            let = strs[0][i]
            
            for j in strs:
                if let != j[i]:
                    bo = False
            if bo:
                ans+=let
            else:
                break
        return ans