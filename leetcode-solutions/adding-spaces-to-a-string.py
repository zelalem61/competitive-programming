class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        j= 0
        for i in range(len(s)):
            if i == spaces[j]:
                ans += " "
                if j < len(spaces)-1:
                    j+=1
            ans+=s[i]
        return ans