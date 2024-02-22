class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n==0):
            return 1
        powe=1
        init=x
        while(powe<n):
            x=x*x
            powe=powe*2
        if(powe==n):
            return x
        z=self.myPow(init,powe-n)
        if(math.isnan(z)):
            return 0
        return x/z
        