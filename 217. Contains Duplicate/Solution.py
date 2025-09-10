class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1=len(set(nums))
        if set1==len(nums):
            return False
        else:
            return True
        