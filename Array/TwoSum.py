# enumerate(nums) provides both index (i) and value (num) in nums.
# range(n) → Generates indices from 0 to n-1, allowing us to loop through the list.
# Using range(len(nums)) ensures we can access both index (i) and value (nums[i]).



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #          return [i,j]

        prevMap = {} #val : index

        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n] = i
                