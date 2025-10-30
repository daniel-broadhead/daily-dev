"""
Problem: merge intervals (LeetCode #56)
Link: https://leetcode.com/problems/merge-intervals
Date: 2025-10-30

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of 
the non-overlapping intervals that cover all the intervals in the input.


Approach:
- First sort the intervals by start time. Then check if each start time is greater than the interval's end time, if so that breaks up the 
merged intervals. Otherwise merge them by taking the max end time.

Time complexity: O(nlogn)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) #sort by the key lambda which is the start time
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]: #if the merged list is empty or if the last item's end time is less than the current interval start...
                merged.append(interval) #slap that bad boy onto the merged list
            else:
                merged[-1][1] = max(merged[-1][1], interval[1]) #merge the overlap

        return merged
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
