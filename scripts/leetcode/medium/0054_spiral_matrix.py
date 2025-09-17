"""
Problem: spiral matrix (LeetCode #54)
Link: https://leetcode.com/problems/spiral-matrix
Date: 2025-09-17

Given an m x n matrix, return all elements of the matrix in spiral order.

Approach:
- Keep track of 4 dynamic parameters: top, right, bottom, left, and go through the items in each of those parameters, updating when complete.


Time complexity: O(m * n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1 #keep track of 4 parameters that change as we go
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            #first go from left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1 #shift current top 1 down

            #next go top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1 #shift right 1 to the left

            #if there is a bottom 
            if top <= bottom:
                for col in range(right, left - 1, - 1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            #if there is a left
            if left <= right:
                for row in range(bottom, top - 1, - 1):
                    result.append(matrix[row][left])
                left += 1
        return result

        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
