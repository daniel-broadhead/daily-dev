"""
Problem: implement queue using stacks (LeetCode #232)
Link: https://leetcode.com/problems/implement-queue-using-stacks
Date: 2025-09-04

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the 
functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is 
empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a 
list or deque (double-ended queue) as long as you use only a stack's standard operations.

Approach:
- In python a stack is essentially a list, though lists have more functionality. So using 2 lists, like 2 cups, I can spill the contents 
of one cup into the other cup, which makes the first last and vice versa. 

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class MyQueue:

    def __init__(self):
        self.in_stack = [] #2 stacks(lists in python, but restrict to stack ops)
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x) #add to in_stack

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop() 

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self): #like turning 1 cup upside down into another cup. last is now first
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
