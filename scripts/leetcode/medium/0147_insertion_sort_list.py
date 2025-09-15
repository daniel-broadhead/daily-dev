"""
Problem: insertion sort list (LeetCode #147)
Link: https://leetcode.com/problems/insertion-sort-list/
Date: 2025-09-15

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.

Approach:
- The algorithm is given in the problem. Approach is to create a dummy node for simplicity. Look at each node sequentially comparing it to
the other nodes until the correct place is found, and updating the pointers accordingly. 

Time complexity: O(n)(best case)
Space complexity: O(1)
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        
        curr = head
        while curr:
            prev = dummy #start each iteration at head of list
            while prev.next and prev.next.val < curr.val: #looking for where item fits
                prev = prev.next #to find the insertion point
            next_node = curr.next #placeholder for saving space in given list

            curr.next = prev.next #put current inbetween prev and prev.next
            prev.next = curr

            curr = next_node  #move curr pointer to next in given list
        
        return dummy.next #return head of new list

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
