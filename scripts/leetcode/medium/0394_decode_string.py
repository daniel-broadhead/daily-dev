"""
Problem: decode string (LeetCode #394)
Link: https://leetcode.com/problems/decode-string
Date: 2025-11-11

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.


Approach:
- Use a stack to build segments that are constructed when encountering a close bracket. 

Time complexity: O(c)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""

        for ch in s: #4 options, digit, letter, [, or ]. each handled differently
            if ch.isdigit(): 
                curr_num = curr_num * 10 + int(ch) # for multi digit numbers
            elif ch == "[": #opening bracket means add to stack
                stack.append((curr_str, curr_num))
                curr_str, curr_num = "", 0
            elif ch == "]": #closing bracket means pop and build str
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num 
            else: #if ch is letter
                curr_str += ch

        return curr_str

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
