"""
Problem: merge k sorted lists (LeetCode #23)
Link: https://leetcode.com/problems/merge-k-sorted-lists
Date: 2025-10-29

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Approach:
- Use python's minheap, put all the lists in there and then remove the top(smallest value) and construct from there.

Time complexity: O(nlogk)
Space complexity: O(k)
"""

from typing import List

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq #need min heap for this, makes it easier

class Solution:
    def mergeKLists(self, lists: List):
        heap = [] 
        for i, node in enumerate(lists): #put it all in the heap, seems like cheating
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap: #while our storage exists
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
