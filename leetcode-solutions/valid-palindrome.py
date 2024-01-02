class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        for i in (s):
            if i.isalpha() or i.isdigit():
                if i.isalpha():
                    i = i.lower()
                result+=i
        if result == result[::-1]:
            return True
        else:
            return False
        