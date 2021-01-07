class Subarray_560:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, sum_so_far = 0, 0
        pre_sum_count = {0: 1}
        for num in nums:
            sum_so_far += num
            res += pre_sum_count.get(sum_so_far - k, 0)
            pre_sum_count[sum_so_far] = 1 + pre_sum_count.get(sum_so_far, 0)
        return res
