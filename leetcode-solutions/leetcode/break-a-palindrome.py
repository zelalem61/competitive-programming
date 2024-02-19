class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        if len(s) == 1:
            return ""
        for i in range(len(s)):
            if s[i] != "a" and i != len(s)//2:
                s[i] = "a"
                return "".join(s)
        s[-1] = "b"
        return "".join(s)

        