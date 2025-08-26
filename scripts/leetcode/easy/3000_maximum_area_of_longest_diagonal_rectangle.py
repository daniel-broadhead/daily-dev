"""
Problem: maximum area of longest diagonal rectangle (LeetCode #3000)
Link: https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle

You are given a 2D 0-indexed integer array dimensions.

For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.

Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.

Approach:
- Store in memory the longest rectangle seen, and its maximum area. Calculate the longest diagonal for each dimensions, and update values when
necessary. Return the max area when complete. 

Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longest_diag = 0  #init longest_diag to 0
        max_area = 0 #init max area to 0(for if same diag)
        for i, sublist in enumerate(dimensions): #tracking index while going through dimension
            diag = ((dimensions[i][0] ** 2) + (dimensions[i][1] ** 2)) ** 0.5 #diag formula
            if diag > longest_diag: #if current diag longer than prev max
                longest_diag = diag #update longest diag
                max_area = dimensions[i][0] * dimensions[i][1] #get area of longest diag
            elif diag == longest_diag: #if diags are ==
                max_area = max(max_area, dimensions[i][0] * dimensions[i][1]) #compare max_area
        return max_area #return area when finished

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
