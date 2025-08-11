"""
Problem: median of two sorted arrays (LeetCode #4)
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Approach:
- This was hard, thus its category. My first attempt was successful but did not fall in correct time. I added the arrays together, sorted
and returned the values for the median indices. But that was too slow. So the correct approach is to set nums1 to the smaller array. Then
binary search the left array, while partitioning the right array in proportion to the left partition. Check the mins and maxes and split
again if necessary. When maxLeft1 <= minRight2 and maxLeft2 <= minRight1 we have found the correct median. 

Time complexity: O(log(min(m,n)))
Space complexity: O(1)
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): # switch nums1 and nums2 if nums1 isn't the smaller array
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        left = 0 #binary sort the smaller array
        right = m
        half_len = (m + n + 1) // 2 #want left to half half of all elements. this used to check

        while left <= right:
            i = (left + right) // 2 #find first partition on smaller array
            j = half_len - i # cut nums2 propor to nums1

            maxLeft1 = nums1[i - 1] if i > 0 else float('-inf') #max of left1 if on array
            minRight1 = nums1[i] if i < m else float('inf') #min of right1 if on array

            maxLeft2 = nums2[j - 1] if j > 0 else float('-inf')#more edge case check
            minRight2 = nums2[j] if j < n else float('inf')#more edge case check

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2: #i is too big, move right away from half_len
                right = i - 1
            else: #i is too small, move left towards half_len
                left = i + 1




# Example test
if __name__ == "__main__":
    # Add test cases
    pass
