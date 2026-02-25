def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """


# We simulate addition from the last digit:

# Start from the end.

# If digit < 9 → just add 1 and return.

# If digit == 9 → make it 0 and carry 1 to the left.

# If all digits are 9 → add 1 at the front.

    n = len(digits)
    
    # Start from the least significant digit and propagate the carry
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # If digit becomes 10, set it to 0 and carry over
    
    # If we exit the loop, all digits were 9. We need an additional digit at the start.
    return [1] + digits
