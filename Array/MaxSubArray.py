# Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray [4, -1, 2, 1] has the maximum sum 6

def max_subarray_sum(arr):
    """
    Given an array of integers, find the maximum sum of any subarray.

    Parameters:
    arr (List[int]): List of integers.

    Returns:
    int: Maximum sum of any subarray.
    """
    # Implement the function
    # if not arr:
    #     return 0
 
    # # Initialize variables
    # max_ending_here = 0
    # max_so_far = float('-inf')
 
    # # Iterate through the array
    # for x in arr:
    #     # Update max_ending_here to include current element
    #     max_ending_here = max(x, max_ending_here + x)
    #     # Update max_so_far to the maximum value found so far
    #     max_so_far = max(max_so_far, max_ending_here)
 
    # return max_so_far
    
    #Kadaen's Algorithm: Kadane’s Algorithm is an efficient dynamic programming approach to 
    #find the maximum sum of a contiguous subarray in an array.


    if not arr:  # Check if the array is empty
        return 0  
    
    maxSum = arr[0]
    currSum = 0
  
    
    for n in arr:
        if currSum <0:
           currSum = 0
          
        currSum += n
        maxSum = max(maxSum,currSum)
         
    return maxSum     