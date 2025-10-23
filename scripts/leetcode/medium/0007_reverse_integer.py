"""
Problem: reverse integer (LeetCode #7)
Link: https://leetcode.com/problems/reverse-integer/
Date: 2025-10-23

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Approach:
- String method, to store the negative in a boolean for later. Use string splicing to reverse the string digit by digit. Math method,
to take mod of x and add as the first number(after storing negative) and then int dividing x by 10. Repeat until x gone.

Time complexity: O(c)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0: #assign bool to save if x is negative for later
            negative = True
            
        string = str(abs(x)) #return abs value in string form
        rev = string[::-1] #reverse slice the value
        rev_int = int(rev) #now the string is an int again
        
        
        if negative: #check for negative
            rev_int = rev_int * -1

        if rev_int > 2 ** 31 - 1 or rev_int < - 2 ** 31 - 1: #return 0 if too big or too small
            return 0
        else:
            return rev_int

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
