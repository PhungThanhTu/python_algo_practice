# https://leetcode.com/problems/partition-array-for-maximum-sum/description/?envType=daily-question&envId=2024-02-03
from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        memo = {}
        def findMaxSum(i):
            if i in memo:
                return memo[i]
            if i == n:
                return 0
            curMax = 0
            for j in range(i, min(i + k, n)):
                cur = max(arr[i:j+1]) * (j - i + 1) + findMaxSum(j + 1)
                curMax = max(curMax, cur)
            memo[i] = curMax
            return curMax
        return findMaxSum(0)

print(Solution().maxSumAfterPartitioning([1,15,7,9,2,5,10], 3))