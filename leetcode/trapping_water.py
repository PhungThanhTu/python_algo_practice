# https://leetcode.com/problems/trapping-rain-water/description/
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = height[0]
        max_right = height[len(height) - 1]
        pleft = 1
        pright = len(height) - 2
        water = 0
        while pleft <= pright :
            if height[pleft] >= max_left :
                max_left = height[pleft]
                pleft += 1
            elif height[pright] >= max_right:
                max_right = height[pright]
                pright -= 1
            elif max_left <= max_right and height[pleft] < max_left:
                water += max_left - height[pleft]
                pleft += 1
            elif max_right <= max_left  and height[pright] < max_right:
                water += max_right - height[pright]
                pright -= 1
        return water





height = [0,1,0,2,1,0,1,3,2,1,2,1]

solution = Solution()
print(solution.trap(height))
