class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
     nums.sort()  # Sort the list first
     for i in range(len(nums) - 1):  # Compare adjacent elements
        if nums[i] == nums[i + 1]:
            return True
     return False  