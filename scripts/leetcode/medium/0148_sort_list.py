"""
Problem: sort list (LeetCode #148)
Link: https://leetcode.com/problems/sort-list/
Date: 2025-09-11

Given the head of a linked list, return the list after sorting it in ascending order.

Approach:
- This one is dumb. I worked hard on a quick sort method, but one of the test cases is worst case for quick sort so TLE. I'll still post 
my quick sort method. But working solutions use merge sort, since that's evidently a better method for linked lists. 

Time complexity: O(logn) (O(n^2) worst case)
Space complexity: O(1)
"""

from typing import List

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if head is None or head.next is None: #if list of none or one
            return head
            
        pivot = head #variables for partitioning
        before_dummy = ListNode(0) #dummy node for start of list
        after_dummy = ListNode(0)
        before = before_dummy
        after = after_dummy

        current = head.next
        while current: #while there is a node
            if current.val < pivot.val: #current value is smaller than pivot
                before.next = current #before list next node is current node
                before = before.next #before list pointer moves forwards
            else: #current is greater than or equal to pivot
                after.next = current #same as above but for after
                after = after.next       
            current = current.next

        #close lists when loop is complete
        before.next = None
        after.next = None

         #recursively sort those lists
        before_sorted = self.sortList(before_dummy.next)
        after_sorted = self.sortList(after_dummy.next)

        #join the sorteds(will be just pivots at this point)
        pivot.next = after_sorted #after pivot is the after_sorted
        if before_sorted:
            tail = before_sorted
            while tail.next: #while another value in before_sorted
                tail = tail.next
            tail.next = pivot #complete the joining
            return before_sorted
        else:
            return pivot


# Example test
if __name__ == "__main__":
    # Add test cases
    pass
