# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36

# Input: height = [2,2,2]
# Output: 4

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # n = len(height)
        # max_water = 0  # Initialize the maximum area as zero

        # # Nested loop to check all pairs of bars
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         # Calculate the current area between bars at index i and j
        #         current_area = min(height[i], height[j]) * (j - i)
        #         # Update the maximum area found
        #         max_water = max(max_water, current_area)

        # return max_water



        left = 0  # Initialize the left pointer at the start of the array
        right = len(height) - 1  # Initialize the right pointer at the end of the array
        max_water = 0  # To store the maximum water that can be contained

        while left < right:
            # Calculate the width of the current container
            width = right - left
            # Calculate the area with the current configuration of left and right
            current_area = min(height[left], height[right]) * width
            
            # Update the maximum area found so far
            max_water = max(max_water, current_area)

            # Move the pointer pointing to the shorter bar inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water