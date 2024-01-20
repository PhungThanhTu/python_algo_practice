# https://leetcode.com/problems/car-fleet/description/
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = [
                (p,s) for p,s in zip(position, speed)
        ]
        for p,s in sorted(cars)[::-1]:
            fleets.append((target - p) / s)
            if len(fleets) > 1 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)



sol = Solution()
pos = [10,8,0,5,3]
tar = 12
spd = [2,4,1,1,3]
print(sol.carFleet(tar, pos, spd))