class Solution:
    def mySqrt(self, x: int) -> int:
        count = 0
        diff = float('inf')
        low = 1
        high = x//2
        if x == 0 or x==1:
            return x
        while low <= high:
            mid = (low+high)//2
            if mid**2 == x:
                return mid
            if mid**2 < x:
                low = mid+1
                if (mid**2) < x and abs((mid**2)-x) < diff:
                    diff = abs((mid**2)-x)
                    count = mid
            if mid**2 > x:
                high = mid-1
                if (mid**2) < x and abs((mid**2)-x) < diff:
                    diff = abs((mid**2)-x)
                    count = mid
        return count

