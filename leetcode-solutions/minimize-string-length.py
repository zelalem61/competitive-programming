class Solution:
    def minimizedStringLength(self, s: str) -> int:
        settedS = set(s)
        return len(settedS)