# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.




# ⏱ Time Complexity:
# O(n) – you check every element once

# 🧠 Space Complexity:
# O(1) – just one variable to store the minimum

def findMin(nums):           
    # Step 1: Assume the first number is the smallest
    min_val = nums[0]

    # Step 2: Go through each number in the array
    for num in nums:
        # If we find a smaller number, update min_val
        if num < min_val:
            min_val = num

    # Step 3: Return the smallest number found
    return min_val


# ⏱ Time Complexity:
# O(log n) – binary search

# 🧠 Space Complexity:
# O(1) – constant space

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Case 1: mid element is greater than right → min is to the right
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Case 2: mid element is <= right → min is at mid or to the left
            right = mid

    # When loop ends, left == right and it's the minimum
    return nums[left]
