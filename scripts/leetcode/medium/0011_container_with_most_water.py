"""
Problem: container with most water (LeetCode #11)
Link: https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Approach:
First approach was a for loop, like a sliding window(with a for loop) and it didn't work well when I tried to figure out when to increment the 
the left side. A while loop was much more effective. Approach is to maintain that the pointers aren't at the same index. Move the shorter
line everytime 1 inwards, maintaining the max water stored. 

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    class Solution:
        def maxArea(self, height: List[int]) -> int:
            left = 0 #init left to 0
            right = len(height) - 1 #init right to end of list
            water = 0 #init water to 0
            while left < right: #using 2 pointers, while not on same index
                h = min(height[left], height[right]) #h is always the min of the 2 heights
                w = right - left #w is the distance from r to l
                water = max(water, h * w) #area = w * h
                if height[left] > height[right]:#move pointer of limiting factor, the lower height
                    right -= 1
                else:
                    left += 1
            return water #returns max after full iteration


# Example test
if __name__ == "__main__":
    # Add test cases
    pass
