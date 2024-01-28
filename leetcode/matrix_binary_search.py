# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List

class Solution:
    def binarySearch(self, matrix, target, start, end):

        if start > end:
            return False
        pivot = int((start + end) / 2)
        pivotX = pivot % len(matrix[0])
        pivotY = int(pivot / len(matrix[0]))
        print(f'pivot {pivot}, pivotX {pivotX} pivotY {pivotY}, len X {len(matrix[0])} len Y {len(matrix)}')
        if matrix[pivotY][pivotX] == target:
            return True
        if target < matrix[pivotY][pivotX]:
            return self.binarySearch(matrix, target, start, pivot -1)
        if target > matrix[pivotY][pivotX]:
            return self.binarySearch(matrix, target, pivot + 1, end)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        return self.binarySearch(matrix, target, 0, m * n - 1)
    
print(Solution().searchMatrix([[1,3]], 3))