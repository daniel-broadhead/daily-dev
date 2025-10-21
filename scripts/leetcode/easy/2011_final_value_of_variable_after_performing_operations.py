"""
Problem: Final Value of Variable After Performing Operations (LeetCode #2011)
Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description
Date: 2025-10-20

There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

Approach:
- This is helping me get back into a streak of solving these problems. The soln is really straightforward. Assign a variable to track final
value. Check each item in operations list and increment/decrement the value tracker, and when no more items in list, return variable.

Time complexity: O(c)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        var = 0
        for i in operations:
            if i == "++X" or i == "X++":
                var += 1
            elif i == "--X" or i == "X--":
                var -= 1
            else:
                print(f"That {i} is not recognized.")
        return var
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
