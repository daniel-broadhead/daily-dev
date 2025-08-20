"""
Problem: count square submatrices with all ones (LeetCode #1277)
Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Approach:
- NGL I needed a lot of help on this one. Still making my head spin. The approach is to create a DP table filled with 0s. Check each spot
in the original matrix. If it is a 1, check the DP table for its smallest neighbors, which tells how many squares end at that index.
Return all the squares found. Still, head spinning. 

Time complexity: O(n^2)
Space complexity: O(m * n)
"""

from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        count_squares = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i -1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    count_squares += dp[i][j]
        return count_squares

        
        
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
