class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map= {}
        for i ,nums in enumerate(nums):
            diff = target - nums
            if diff in hash_map:
                return [hash_map[diff],i]
            hash_map[nums]=i
        return []