"""
Problem: intersection of two arrays 2 (LeetCode #350)
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times 
as it shows in both arrays and you may return the result in any order.

Approach:
- Create a dictionary of the frequencies that each number appears in the arrays. Iterate through the first array and store the frequencies.
Iterate through the second array, and if a number appears that is in the frequency dict, add it to the result and subtract 1 from the frequencies
to avoid overcounting. Return the result

Time complexity: O(?)
Space complexity: O(?)
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        result = []
        for num in nums1:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        return result

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
