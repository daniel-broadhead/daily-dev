"""
Problem: subarray sum equals k (LeetCode #560)
Link: https://leetcode.com/problems/subarray-sum-equals-k

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Approach:
- This one hurt my brain. A brute force approach timed out so I had to research other options. Using a prefix table and the relation
that a valid count : running_sum[j] - running_sum[i] = k can rearrange to running_sum - k = running_sum[i], I store the running_sum[i] as
a key, and a frequency of it in the table. When adding to the table i increase the count of valid subarrays. 

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0 #init the count
        running_sum = 0 #init the running sum
        prefix_count = {0 : 1} #init table, with a 0 so can include counting 0
        for num in nums: #for each number
            running_sum += num #increase the running sum
            if running_sum - k in prefix_count: #if running sum - k has is in table
                count += prefix_count[running_sum - k] #increase count(sometimes more than once, like if a num is 0)
                prefix_count[running_sum] = prefix_count.get(running_sum, 0) + 1 #update the table by seeing if seeing if sum is in table, or if not is 0. add 1 to the count
        return count

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
