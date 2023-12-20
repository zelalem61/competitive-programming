class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(list(t) for t in zip(*matrix))
    