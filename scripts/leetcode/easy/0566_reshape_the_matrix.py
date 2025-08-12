"""
Problem: reshape the matrix (LeetCode #566)
Link: https://leetcode.com/problems/reshape-the-matrix/

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Approach:
- First check if the number of elements in the current matrix is equal to the number of elements in the reshaped matrix. Return orig if
not. Flatten the orig matrix for extraction. Slice that flattened list into the rows and columns.

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        reshaped_elements = r * c
        flat = []
        for row in mat: #flatten each old matrix into a new list for extraction
            for val in row:
                flat.append(val)
        if len(flat) != reshaped_elements:
            return mat
        reshaped = []
        for i in range(r): #for each desired row
            new_row = flat[i * c :(i + 1) * c] #slice with c elements. 0th index to cth index. 1 *cth to 2 * cth, so on. 
            reshaped.append(new_row) #append these new rows to the reshaped matrix
        return reshaped

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
