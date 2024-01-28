# https://leetcode.com/problems/generate-parentheses/
from typing import List 

class Solution:
    def __init__(self):
        self.cache = {}
        self.cache[1] = ["()"]
    def wrapParenthesis(self, element):
        return f'({element})'
    def pushParenthesis(self, element):
        return f'{element}()'
    def shiftParenthesis(self, element):
        return f'(){element}'
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1: return self.cache[1]
        if n in self.cache:
            return self.cache[n]
        prev = self.generateParenthesis(n-1)
        current_1 = list(map(self.wrapParenthesis, prev))
        current_2 = list(map(self.pushParenthesis, prev))
        current_2.pop() # avoid duplicated ()()
        current_3 = list(map(self.shiftParenthesis, prev))
        result = current_1 + current_2 + current_3
        return result

def __main__():
    sol = Solution()
    print(sol.generateParenthesis(4))

__main__()