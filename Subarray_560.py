"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

class Subarray_560:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, sum_so_far = 0, 0
        pre_sum_count = {0: 1}
        for num in nums:
            sum_so_far += num
            res += pre_sum_count.get(sum_so_far - k, 0)
            pre_sum_count[sum_so_far] = 1 + pre_sum_count.get(sum_so_far, 0)
        return res
