# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

class Solution:
    def productitself(self, nums: List[int]) -> List[int]:
        # n= len(nums)
        # output = [1]*n

        # for i in range(n):
        #     product = 1 #intialize product for the current index 
        #     for j in range(n):
        #         if i!=j:
        #             product += nums[j] 
        #         output[j] = product
        # return output            

        n = len(nums)
        output = [1] * n
        
        # Calculate left products
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        
        # Calculate right products and finalize result
        right_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output