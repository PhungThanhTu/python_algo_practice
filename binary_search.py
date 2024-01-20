# https://leetcode.com/problems/binary-search/
from typing import List

class Solution:
    def binSearch(self, nums, target, start, end):
        print(f'start {start}')
        print(f'end {end}')
        pivot = int((start + end) / 2)
        print(pivot)
        if target == nums[pivot]:
            return pivot
        if start > end:
            return -1
        if target > nums[pivot]:
            return self.binSearch(nums, target, pivot + 1, end)
        if target < nums[pivot]:
            return self.binSearch(nums, target, start, pivot - 1 )
    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, target, 0, len(nums) - 1)
    
print(Solution().search([-1,0,3,5,9,12], 9))