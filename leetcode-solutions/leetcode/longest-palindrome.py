class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = Counter(s)
        bo = False
        count = 0
        for key in dic:
            if dic[key] >= 2:
                if dic[key] % 2 != 0:
                    count += dic[key] - 1
                    bo = True
                else:
                    count += dic[key]
            else:
                bo = True
        if bo:
            count+=1
        return count