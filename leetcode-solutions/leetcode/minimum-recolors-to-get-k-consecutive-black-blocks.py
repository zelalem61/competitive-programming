class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = k-1
        ans = float("inf")
        while right < len(blocks):
            d = blocks[left:right+1].count("W")
            ans = min(ans,d)
            left+=1
            right+=1
        return ans


