"""
Problem: k closest points to origin (LeetCode #973)
Link: https://leetcode.com/problems/k-closest-points-to-origin
Date: 2025-11-15

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Approach:
- Use a heap yo. Heappop removes the root. So negate the distances so that the largest distance is the most negative => smallest, so it gets 
removed with pop. Go through all the points and keep the k closest

Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points: 
            dist = x*x + y*y #dont need to sqrt for comparison
            heapq.heappush(heap, (-dist, (x, y))) #uses negative distance so largest points are on top. pushes -dist before point for comparing -dist

            if len(heap) > k:
                heapq.heappop(heap) #as used before, this maintains the k closest points

        return [point for (_, point) in heap] #don't care about the distance so just return the points from the tuple

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
