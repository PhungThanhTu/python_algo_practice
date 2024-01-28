# https://leetcode.com/problems/daily-temperatures/
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [
            0 for i in temperatures
        ]
        for i in range(len(temperatures)):
            while(stack != [] and temperatures[i] > temperatures[stack[-1]]):
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)
        while stack != []:
            prev = stack.pop()
            result[prev] = 0
        return result

sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]

print(sol.dailyTemperatures(temperatures))