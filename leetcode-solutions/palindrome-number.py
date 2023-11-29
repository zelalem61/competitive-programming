class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        strin = str(x)
        if strin == strin[::-1]:
            return True
        return False
        