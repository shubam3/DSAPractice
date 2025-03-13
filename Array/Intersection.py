# Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6]
# Output: []
 
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]
 
# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]

def intersection(nums1, nums2):
    # TODO: Implement this function
    nums1_set = set(nums1)  # Convert nums1 to a set for O(1) lookup
    visited = set()  # Track visited numbers
    result = []

    for num in nums2:
        if num in nums1_set and num not in visited:
            result.append(num)
            visited.add(num)  # Use set for O(1) lookup

    return result           #o(n)
            
    result = []  # Stores the intersection result
    visited = []  # Keeps track of already added elements


    # Iterate over nums2 to preserve its order
    for num in nums2:
        if num in nums1 and num not in visited:
            result.append(num)
            visited.append(num)

    return result           #o(n2)