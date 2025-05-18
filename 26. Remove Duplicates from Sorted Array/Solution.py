class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0  # Pointer to track the position for the next unique element.
        for j in range(1, len(nums)):  # Pointer to traverse the list from the second element.
            if nums[j] != nums[i]:  # If the current element is different from the last unique element.
                i += 1  # Increment i to indicate a new position for a unique element.
                nums[i] = nums[j]  # Place the unique element at index i.
        return i + 1  # i is the last index of the unique element, so return the length as i+1.
