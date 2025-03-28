# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

def threeSum(nums):
    # Sort the array to make it easier to skip duplicates
    # nums.sort()
    # result = []
    # n = len(nums)

    # # Brute force: check all combinations of three numbers
    # for i in range(n - 2):  # The first number
    #     # Skip duplicate elements
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #     for j in range(i + 1, n - 1):  # The second number
    #         # Skip duplicate elements
    #         if j > i + 1 and nums[j] == nums[j - 1]:
    #             continue
    #         for k in range(j + 1, n):  # The third number
    #             # Skip duplicate elements
    #             if k > j + 1 and nums[k] == nums[k - 1]:
    #                 continue
    #             # Check if the sum is zero
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 result.append([nums[i], nums[j], nums[k]])

    # return result

    nums.sort()  # Sort the array to use the two-pointer technique
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
            continue
        left, right = i + 1, n - 1  # Initialize two pointers
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Move left and right pointers to skip duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1  # Need a larger number
            else:
                right -= 1  # Need a smaller number

    return result
