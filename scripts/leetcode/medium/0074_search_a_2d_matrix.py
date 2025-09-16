"""
Problem: search a 2d matrix (LeetCode #74)
Link: https://leetcode.com/problems/search-a-2d-matrix
Date: 2025-09-16

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Approach:
- Treat the 2d matrix as a flattened 1d array. Binary search this array. 

Time complexity: O(log m * n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #treat the 2d array as a flattened 1d array and binary search
        if not matrix or not matrix[0]: #check for empty
            return False

        m, n = len(matrix), len(matrix[0]) #m, n for left  right assign
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n) #divmod gives easier access to the row, col by doing mid // n and mid%n
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False




        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
