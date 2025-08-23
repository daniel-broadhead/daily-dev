"""
Problem: valid parenthesis (LeetCode #20)
Link: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Approach:
- Make a mapping dict to store what maps to what. Create a stack of the chars encountered, and check each char if it has a mapping char
assoc to it. Go on through until clear and return true if stack empty.

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(", "]" : "[", "}" : "{"}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#' #returns dummy to avoid error if stack is empty
                if mapping[char] != top: # if the char is not mapped to the top
                    return False
            else:
                stack.append(char) 
        return not stack # Return True if the stack is empty, False otherwise.

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
