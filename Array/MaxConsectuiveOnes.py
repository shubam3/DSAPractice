# Input: nums = [0, 0, 0, 0]
# Output: 0
 
# Input: nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
# Output: 4
 
# Input: nums = [1, 1, 0, 1, 1, 1]
# Output: 3

def find_max_consecutive_ones(nums):
    # TODO: Implement this function

    max_count = 0  # Keeps track of the maximum sequence of consecutive 1s.
    current_count = 0  # Current streak of consecutive 1s

    for num in nums:
        if num == 1:
            current_count += 1  # Increment the streak
            max_count = max(max_count, current_count)  # Update max_count if needed
        else:
            current_count = 0  # Reset the streak if a 0 is encountered

    return max_count