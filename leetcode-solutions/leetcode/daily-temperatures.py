class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures: return []
        if len(temperatures) == 1: return [0]
        ret = [0] * len(temperatures)
        stack = []
        index = 0
        while index < len(temperatures):
            while index < len(temperatures) and (not stack or temperatures[index] <=    temperatures[stack[-1]]):
                stack.append(index)
                index += 1
            while index < len(temperatures) and stack and temperatures[stack[-1]] <         temperatures[index]:
                val = stack.pop()
                ret[val] = index - val
            stack.append(index)
            index += 1
        return ret