"""
Problem: daily temperatures (LeetCode #739)
Link: https://leetcode.com/problems/daily-temperatures/
Date: 2025-09-04

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
 is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day 
 for which this is possible, keep answer[i] == 0 instead.

 

Approach:
- Maintain a stack of all the days that have not seen high temps. While that stack exists and the current temp is higher than the temps
of the stack's day, pop the stack and append index - stack's index to answer. Add current index to stack when no longer true. 

Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n #array of answer
        stack = [] #holds the days that havent seen higher temps
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[- 1]]: #while there is a stack, and temp is higher than at that stack index
                last = stack.pop() #index/day
                answer[last] = i - last #index/day
            stack.append(i)#index/day
        return answer

                    

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
