"""
Problem: search a 2d matrix ii (LeetCode #240)
Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
Date: 2025-11-10

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Approach:
- Start in the top right, or bottom left, corner and move rows or columns based on if target is higher or lower than that corner box.

Time complexity: O(m + n)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0]) 
        r, c = 0, cols - 1

        while r < rows and c >= 0:
            if matrix[r][c] == target: #win
                return True
            elif matrix[r][c] > target: #look for bigger numbers
                c -= 1
            else: #look for smaller numbers
                r += 1

        return False
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
