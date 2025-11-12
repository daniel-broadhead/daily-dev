"""
Problem: maximal rectangle (LeetCode #85)
Link: https://leetcode.com/problems/maximal-rectangle
Date: 2025-11-12

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Approach:
- This problem relies on the solution for problem 84. The difference is converting a 2d matrix into a histogram, which is done by comparing 
row by row and building rectangles off of consecutive 1's in columns. 

Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: #edge cases
            return 0
        
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        def largestRectangleArea(heights): #soln from #84
            max_area = 0
            stack = []
            heights.append(0)
    #stack top will be the tallest seen in a while, and is popped when something shorter is seen. checking valid rectangles from left to right
            for i, h in enumerate(heights): #need keep index and heights
                while stack and heights[stack[-1]] > h: #if height is less than stack top, means stack top not valid for future rectangles
                    height = heights[stack.pop()] #pop it and calculate this rectangle
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width) #store the max height
                stack.append(i)
            return max_area
        
        for row in matrix: #go through row by row to build heights, which is increased if consecutive 1's, and 0'd out when 0. find max area for each row
            for j in range(n):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
