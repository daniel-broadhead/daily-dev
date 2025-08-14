"""
Problem: largest 3 same digit number in string (LeetCode #2264)
Link: https://leetcode.com/problems/largest-3-same-digit-number-in-string

You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.

Approach:
- Originally I tried with storing each letter in a list, and if a letter was the same as the previous I would add to that list, later comparing 
it to the max found substring(if got to 3 numbers). This errored due to data type changing and list not functioning that way. I learned that
max() can compare strings as well, which is nice. So second attempt was to store candidates as strings if 3 consecutive numbers. Then
compare that to max found candidate.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_substring = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                candidate = num[i:i + 3]
                if candidate > max_substring:
                    max_substring = candidate
        return max_substring

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
