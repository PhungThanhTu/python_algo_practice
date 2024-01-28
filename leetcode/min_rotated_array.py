# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List

class Solution:
    def binarySearch(self, nums, start, end):
        pivot = int((start + end) / 2)
        left = pivot
        mid = int(len(nums)/2) + pivot
        if mid > len(nums) - 1:
            mid = mid - len(nums)
        right = pivot - 1
        print(f'left {left} mid {mid} right {right}')
        if nums[left] < nums[mid] and nums[mid] < nums[right]:
            return pivot
        if nums[left] > nums[mid] and nums[mid] < nums[right]:
            return self.binarySearch(nums, pivot + 1, end)
        if nums[left] < nums[mid] and nums[mid] > nums[right]:
            return self.binarySearch(nums, start, pivot - 1)
        
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)
        return nums[self.binarySearch(nums, 0, len(nums) - 1)]

print(Solution().findMin([11,13,15,17]))