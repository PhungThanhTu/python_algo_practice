#https://leetcode.com/problems/largest-divisible-subset/
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        sorted_nums = sorted(nums)

        max_len = 0
        max_index = -1
        path = [-1] * n
        len_path = [1] * n
        for i in range(1, n):
            print(f'check {i}')
            for j in range(i - 1, -1, -1):
                if sorted_nums[i] % sorted_nums[j] == 0:
                    curr_len = 1  + len_path[j]
                    if curr_len > len_path[i]:
                        len_path[i] = curr_len
                        path[i] = j
                    if curr_len > max_len:
                        max_len = curr_len
                        max_index = i
                else:
                    if max_index == -1:
                        max_index = i
        ans = []
        while max_index != -1:
            ans.append(sorted_nums[max_index])
            max_index = path[max_index]
        return ans[::-1]

print(Solution().largestDivisibleSubset([3,4,6,8,12,16,32]))