class Solution:
    def countGoodNumbers(self, n: int) -> int:
        num = 10**9 + 7
        
        def power(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % num
                base = (base * base) % num
                exp //= 2
            return result
        
        if n % 2 == 0:
            ans = power(5, n//2) * power(4, n//2)
        else:
            ans = power(5, (n//2)+1) * power(4, n//2)
        return ans % num
