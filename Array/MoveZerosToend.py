def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    # TODO: Implement this function
    n = len(nums)  # Length of the list
    i = 0  # Pointer for iteration
    
    while i < n:  # Iterate through the list
        if nums[i] == 0:
            nums.pop(i)  # Remove the zero
            nums.append(0)  # Append zero at the end
            n -= 1  # Reduce length to avoid processing appended zeros
        else:
            i += 1  # Only move forward if current element is non-zero
    
    return nums   


#########################
def move_zeroes(nums):
    n = len(nums)
    non_zero_index = 0  # Pointer to Keep track of where the next non-zero number should go

    # Move non-zero elements forward
    for i in range(n):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

    return nums  # Only needed for displaying output, function modifies list in-place

# Example usage:
print(move_zeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(move_zeroes([0, 0, 1]))         # Output: [1, 0, 0]
print(move_zeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))  # Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]

