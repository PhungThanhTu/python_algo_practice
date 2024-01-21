# https://leetcode.com/problems/koko-eating-bananas/
from typing import List

class Solution:
    def checkEatAllPiles(self, piles, h, k):
        sum_hour = 0
        if k == 0:
            return False
        for i in range(len(piles)):
            if piles[i] % k != 0:
                sum_hour += int(piles[i] / k) + 1
            else:
                sum_hour += int(piles[i] / k)
        print(f'sum hour for {k} speed is {sum_hour}')
        if sum_hour > h:
            return False
        return True
    def checkMinSpeed(self, piles, h, k):
        return self.checkEatAllPiles(piles, h, k) and not self.checkEatAllPiles(piles, h, k - 1)
    def binarySearch(self, piles, h, start, end):
        pivot = int((start + end) / 2)
        if start >= end:
            if self.checkEatAllPiles(piles, h, start):
                return start
            else:
                return end
        if self.checkMinSpeed(piles, h, pivot):
            return pivot
        print(f'start : {start} end : {end} pivot {pivot}')
        if self.checkEatAllPiles(piles, h, pivot):
            return self.binarySearch(piles, h, start, pivot - 1)
        else:
            return self.binarySearch(piles, h, pivot + 1, end)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        return self.binarySearch(piles, h, min_k, max_k)

print(Solution().minEatingSpeed([30,11,23,4,20],6))