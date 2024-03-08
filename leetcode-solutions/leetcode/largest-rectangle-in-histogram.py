class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       
            stk = [-1]
            heights.append(0)
            ans = 0
            for i in range(len(heights)):
                while heights[i] < heights[stk[-1]]:
                    h = heights[stk.pop()]
                    w = i - stk[-1] - 1
                    ans = max(ans, h * w)
                stk.append(i)
            return ans