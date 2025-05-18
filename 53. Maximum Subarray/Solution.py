from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=max_sum=nums[0]
        for i in nums[1:]:
            current = max(i,current + i)
            max_sum = max(current,max_sum)
        return max_sum