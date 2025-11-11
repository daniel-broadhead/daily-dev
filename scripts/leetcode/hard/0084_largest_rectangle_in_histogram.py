"""
Problem: largest rectangle in histogram (LeetCode #84)
Link: https://leetcode.com/problems/largest-rectangle-in-histogram
Date: 2025-11-11

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Approach:
- Use a stack to track the largest triangle for each height. Pop a height when something smaller found and no longer valid for calculations

Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
