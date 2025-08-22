"""
Problem: valid sudoku (LeetCode #36)
Link: https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Approach:
- Create hashmaps for the rows, columns, and boxes. Calculate the box index for the mini boxes by // row and column by 3. Multiply row by 3
and add together. This gives box index. Check if val at spot on board is in hashmaps. Return false if so. Add value and repeat if not.

Time complexity: O(81)
Space complexity: O(81)
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #three empty hashmaps for containing if seen
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        #checking each item
        for r in range(9):
            for c in range(9):
                val = board[r][c] #compute value
                if val == ".":
                    continue
                box_index = (r // 3) * 3 + (c // 3) #compute box. 

                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_index]): #if value in hashmap
                    return False
                 #add to hashmaps
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        return True
        
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
