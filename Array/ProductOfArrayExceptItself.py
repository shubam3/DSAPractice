# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

class Solution:
    def productitself(self, nums: List[int]) -> List[int]:
        # n= len(nums)
        # output = [1] * n

        # for i in range(n):
        #     product = 1 #intialize product for the current index 
        #     for j in range(n):
        #         if i!=j:
        #             product *= nums[j] 
        #         output[i] = product
        # return output            

        def productExceptSelf(nums):
            n = len(nums)
            res = [1] * n

            # Left products
            prefix = 1
            for i in range(n):
                res[i] = prefix
                prefix *= nums[i]

            # Right products
            suffix = 1
            for i in range(n - 1, -1, -1):
                res[i] *= suffix
                suffix *= nums[i]

            return res