# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List
class Solution:
    def binarySearch(self, nums, target, start, end):
        center = int((start + end) / 2)
        if start > end:
            return -1
        if nums[center] == target:
            return center
        # center sorted
        if nums[center] >= nums[start] and nums[center] <= nums[end]:
            if target < nums[center]:
                return self.binarySearch(nums, target, start, center - 1)
            else:
                return self.binarySearch(nums, target, center + 1, end)
        # left sorted
        if nums[center] >= nums[start]:
            if target < nums[start]:
                return self.binarySearch(nums, target, center + 1, end)
            if target < nums[center]:
                return self.binarySearch(nums, target, start, center - 1)
            return self.binarySearch(nums, target, center + 1, end)
        # right sorted
        else:
            if target > nums[end]:
                return self.binarySearch(nums, target, start, center - 1)
            if target > nums[center]:
                return self.binarySearch(nums, target, center + 1, end)
            return self.binarySearch(nums, target, start, center - 1)
        
            
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        if len(nums) == 1 and nums[0] != target:
            return -1
        return self.binarySearch(nums, target, 0, len(nums) - 1)
        
print(Solution().search([4,5,6,7,0,1,2],5))