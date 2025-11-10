"""
Problem: min stack (LeetCode #155)
Link: https://leetcode.com/problems/min-stack/
Date: 2025-11-10

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Approach:
- Have 2 stacks. The first behaves normally. The second just tracks the minimum value found in the stack. Pop removes from both stacks so
that if the stack is popped until empty, the return min doesn't return a value that shouldn't exist.

Time complexity: O(c)
Space complexity: O(c)
"""

from typing import List

class MinStack:
 #use 2 stacks, 1 to keep the min value, and the other to function as regular stack
    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        #2 cases, value is minimum or not
        if not self.min_stack or val <= self.min_stack[-1]:#stack empty or val is min
            self.min_stack.append(val)
        # if not min, append whatever the min is to maintain same length
        else:
            self.min_stack.append(self.min_stack[-1])
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
               

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
