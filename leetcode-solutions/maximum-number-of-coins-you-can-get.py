class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = piles[len(piles)//3::]
        piles = piles[0::2]
        return sum(piles)
        