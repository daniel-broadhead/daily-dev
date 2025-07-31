"""
Problem: Add two numbers (LeetCode #0002)
Link: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Approach:
- Need to iterate over each node in the linked list. A for loop won't do so use a while loop. Add the value of each node and store the carry 
for the next nodes.  

Time complexity: O(n)
Space complexity: O(?)
"""

from typing import List


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

if __name__ == "__main__":
    # Add test cases
    pass
