from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        ROWS, COLS, WORD = len(board), len(board[0]), len(word)
        def backtrack(r,c,i):
            if i == WORD:
                return True
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r,c) in path or
                board[r][c] != word[i]): return False
            path.add((r,c))
            res = (backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1))

            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c, 0): return True
        
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
