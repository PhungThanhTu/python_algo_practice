# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/?envType=daily-question&envId=2024-02-01
from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        result_arr = []
        sorted_arr = sorted(nums)
        for i in range(0,len(nums), 3):
            if sorted_arr[i+2] - sorted_arr[i] > k:
                return []
            result_arr.append(sorted_arr[i:i+3])
        return result_arr


print(Solution().divideArray([1,3,3,2,7,3], 3))