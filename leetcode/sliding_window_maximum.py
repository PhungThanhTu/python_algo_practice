# https://leetcode.com/problems/sliding-window-maximum/description/
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        l = r = 0
        while r < len(nums):
            print(f'window: {nums[l:r+1]}')
            if l >= 1 and dq and dq[0] == nums[l-1]:
                dq.popleft()
            while dq and nums[r] > dq[-1]:
                dq.pop()
            dq.append(nums[r])
            if r >= k - 1:
                result.append(dq[0])
                l += 1
            print(f'max : {dq[0]} dq: {dq}')
            r += 1
        return result






            
print(Solution().maxSlidingWindow([7,2,4], 2))