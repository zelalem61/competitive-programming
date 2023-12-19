class Solution:
    def reverseString(self, s: List[str]) -> None:
        a = 0
        b = len(s)-1
        def reverseEnds(s,a,b):
            if a >= b:
                return 
            begin = s[a]
            end = s[b]
            s[a] = end
            s[b] = begin
            reverseEnds(s,a+1,b-1)
        reverseEnds(s, 0, len(s) - 1)
        print(s)
            
        
        