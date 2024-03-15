# You have to pull out all of n stones.
# You can only pull out one at a time.
# The cost to pull out the ith stone is as follows(0<=i<N):

# The cost is 0 if there is no (i-1)th stone and (i+1) th stone
# The cost is A[i] if either the (i-1)th stone and (i+1)th stone is left.
# The cost is B[i] if both (i-1)th stone and (i+1) the stone are left.
# You are requested to find the minimum total sum of the necessary cost.
# Example:
# n=5
# A[i]=[1,5,3,4,3]
# B[i]=[0,2,1,5,0]
# Answer:5

# If stones are pulled out in the order of 0->2->4->1->3
# 1+1+3+0+0=5

# n=4
# a[]=[3,3,2,0]
# B[]=[0,2,3,0]
# Answer:2

# If the stones are pulled out in the order of 1->3->0->2
# 2+0+0+0=2

# Constraints

# 1<= N <= 50000
from typing import List

class Solution:
    def throwStone(self, a:List[int], b:List[int]) -> int:
        n = len(a)
        dp = [0] * n
        dp[0] = min(a[0], a[0])
        for i in range(1, n):
            dp[i] = min(dp[i-1] + a[i], dp[i-2] + b[i])

        return dp[-1]

print(Solution().throwStone([3,3,2,0], [0,2,3,0]))