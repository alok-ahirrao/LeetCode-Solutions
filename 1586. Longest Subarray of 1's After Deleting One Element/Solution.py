class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return(len(nums)-1)
        
        if sum(nums) == 0:
            return(0)
        
        locs = []
        for i in range(len(nums)):
            if nums[i] == 0:
                locs.append(i)
        
        if len(locs) == 1:
            return(len(nums)-1)
        
        size = locs[1] - 0 - 1
        max_size = size

        if len(locs) > 2:
            for i in range(2, len(locs)):
                size = locs[i] - locs[i-2] - 1 - 1
                max_size = max(size, max_size)
        
        if locs[-1] < len(nums)-1:
            size = len(nums)-1 - locs[-2] - 1
            max_size = max(size, max_size)
        
        return(max_size)
        