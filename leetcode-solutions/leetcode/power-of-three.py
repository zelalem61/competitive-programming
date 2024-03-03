class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        def checkPowerOfThree(n):
            if n == 1.0:
                return True
            elif n > 0 and n < 3:
                return False
            else:
                if n%3 == 0:
                    return checkPowerOfThree(n/3)
                else:
                    return False
        return checkPowerOfThree(n)
        
        