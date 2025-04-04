# ⏱ Time Complexity:
# O(n) – you might have to check every element

# 🧠 Space Complexity:
# O(1) – no extra space used

def search(nums, target):
    # Step 1: Go through each element
    for i in range(len(nums)):
        # Step 2: Check if it's equal to the target
        if nums[i] == target:
            return i  # Found the target, return its index
    return -1  # Not found



# ⏱ Time Complexity:
# O(log n) — standard binary search logic

# 🧠 Space Complexity:
# O(1) — constant space


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Step 1: Found the target
        if nums[mid] == target:
            return mid

        # Step 2: Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # target is in the left half
            else:
                left = mid + 1   # target is in the right half
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # target is in the right half
            else:
                right = mid - 1  # target is in the left half

    return -1  # Target not found

