class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(map(str, digits))
        num = str(int(num)+1)
        return [int(char) for char in num]