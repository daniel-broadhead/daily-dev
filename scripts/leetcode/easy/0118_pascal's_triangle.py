"""
Problem: pascal's triangle (LeetCode #118)
Link: https://leetcode.com/problems/pascals-triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Approach:
- Below

Time complexity: O(n^2)
Space complexity: O(n^2)
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [] #init the triangle as a list
        for i in range(numRows): #for each row
            row = [1] #row starts with 1
            if i > 0: #if not in first row
                prev_row = triangle[i - 1] #the last row
                for j in range(1, i): #for each position except the first and last
                    row.append(prev_row[j - 1] + prev_row[j]) #each value is equal to last row's this position and next position summed
                row.append(1) #append 1 to end
            triangle.append(row) #append this row(list) to triangle(list)
        return triangle 

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
