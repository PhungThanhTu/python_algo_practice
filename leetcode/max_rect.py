#https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        if len(heights) == 1:
            return heights[0]
        for i in range(len(heights)):
            print(stack)
            ans = max(heights[i], ans)
            while stack and heights[i] <= heights[stack[-1]]:
                print('popstack')
                k = stack.pop()
                w = i - k
                ans = max(ans, heights[k]*w, heights[i]*(w+1))
                print(w)
            stack.append(i)
        print(heights + [0])
        return ans 
    

print(Solution().largestRectangleArea([1,1]))