class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        query_val = [0]*len(s)
        res = ""
        for query in shifts:
            initial = query[0]
            final = query[1]
            direc = query[2]
            if direc == 0:
                query_val[initial]-=1
                if final+1 < len(s):
                    query_val[final+1]+=1

            elif direc == 1:
                query_val[initial]+=1
                if final +1 < len(s):
                    query_val[final+1]-=1
        shifterVal = list(accumulate(query_val))
        for i in range(len(s)):
            letter = s[i]
            askiVal = ord(letter)
            shiftedAski = ((askiVal - 97 + shifterVal[i]) % 26) + 97
            res = res + chr(shiftedAski)
        return res