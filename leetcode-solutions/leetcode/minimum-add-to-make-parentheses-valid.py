class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openPar = 0
        closePar = 0
        for par in s:
            if par == "(":
                openPar+=1
            elif par == ")" and openPar > 0:
                openPar -= 1
            else:
                closePar += 1
        return openPar + closePar