"""
Problem: non-overlapping intervals (LeetCode #435)
Link: https://leetcode.com/problems/non-overlapping-intervals
Date: 2025-11-04

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Approach:
- Find maximum number of non-overlapping is same as removing min number of overlapping. Sort intervals by end time with goal of removing 
biggest end time overlappers. Check for overlap and incrememnt counter if overlapping

Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1]) #sort by the end time
        kept = intervals[0][1] #comparing to last end time
        count = 0 #soln
        for i in range(1, len(intervals)): 
            if intervals[i][0] < kept:
                count += 1 #remove this
            else:
                kept = intervals[i][1] #keep this

        return count
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
