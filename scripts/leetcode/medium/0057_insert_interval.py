"""
Problem: Insert Interval (LeetCode #57)
Link: https://leetcode.com/problems/insert-interval
Date: 2025-11-03

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Approach:
- Iterate through the list and consider three cases for each interval. The interval is less than the new one, greater than the new one, or
overlaps with the new one. React accordingly.

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new = newInterval
        for i in intervals: #3 cases to consider
            #1, interval is completely before new
            if i[1] < new[0]:
                result.append(i)
            #2, if interval is completely after new
            elif i[0] > new[1]:
                result.append(new)
                new = i
            #3, if need to merge
            else:
                new = [min(i[0], new[0]), max(i[1], new[1])]

        result.append(new)

        return result

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
