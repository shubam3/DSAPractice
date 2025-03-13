def rotate_right(lst, k):
    """Rotate list to the right by k positions without slicing or deque."""
    if not lst or k <= 0:
        return lst

    n = len(lst)
    k %= n  # Handle cases where k > len(lst)

    for _ in range(k):
        last = lst.pop()  # Remove last element
        lst.insert(0, last)  # Insert it at the beginning

    return lst

def rotate_left(lst, k):
    """Rotate list to the left by k positions without slicing or deque."""
    if not lst or k <= 0:
        return lst

    n = len(lst)
    k %= n  # Handle cases where k > len(lst)

    for _ in range(k):
        first = lst.pop(0)  # Remove first element
        lst.append(first)  # Append it at the end

    return lst

# Example usage:
nums = [1, 2, 3, 4, 5]
print("Original List:", nums)

# Rotate right by 2
print("Right Rotate by 2:", rotate_right(nums[:], 2))  # Output: [4, 5, 1, 2, 3]

# Rotate left by 2
print("Left Rotate by 2:", rotate_left(nums[:], 2))  # Output: [3, 4, 5, 1, 2]




################################

def rotate_right(lst, k):
    """Rotate list to the right by k positions."""
    k %= len(lst)  # Handle cases where k > len(lst)
    return lst[-k:] + lst[:-k]

def rotate_left(lst, k):
    """Rotate list to the left by k positions."""
    k %= len(lst)  # Handle cases where k > len(lst)
    return lst[k:] + lst[:k]

# Example usage:
nums = [1, 2, 3, 4, 5]
print("Original List:", nums)

# Rotate right by 2
print("Right Rotate by 2:", rotate_right(nums, 2))  # Output: [4, 5, 1, 2, 3]

# Rotate left by 2
print("Left Rotate by 2:", rotate_left(nums, 2))  # Output: [3, 4, 5, 1, 2]




################################
def reverse(lst, start, end):
    """Helper function to reverse a portion of the list in place."""
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

def rotate_right(lst, k):
    """Rotate list to the right by k positions without slicing or deque."""
    if not lst or k <= 0:
        return lst

    n = len(lst)
    k %= n  # Handle cases where k > len(lst)

    reverse(lst, 0, n - 1)  # Step 1: Reverse entire list
    reverse(lst, 0, k - 1)  # Step 2: Reverse first k elements
    reverse(lst, k, n - 1)  # Step 3: Reverse remaining elements

    return lst

def rotate_left(lst, k):
    """Rotate list to the left by k positions without slicing or deque."""
    if not lst or k <= 0:
        return lst

    n = len(lst)
    k %= n  # Handle cases where k > len(lst)

    reverse(lst, 0, n - 1)  # Step 1: Reverse entire list
    reverse(lst, 0, n - k - 1)  # Step 2: Reverse first n-k elements
    reverse(lst, n - k, n - 1)  # Step 3: Reverse remaining k elements

    return lst

# Example usage:
nums = [1, 2, 3, 4, 5]
print("Original List:", nums)

# Rotate right by 2
print("Right Rotate by 2:", rotate_right(nums[:], 2))  # Output: [4, 5, 1, 2, 3]

# Rotate left by 2
print("Left Rotate by 2:", rotate_left(nums[:], 2))  # Output: [3, 4, 5, 1, 2]
