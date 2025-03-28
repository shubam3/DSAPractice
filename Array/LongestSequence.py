def longestConsecutive(nums):
   
    if not nums:   # O(n logn ) because of string
        return 0

    nums.sort()
    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

    return max(longest_streak, current_streak)



    # num_set = set(nums)  # O(n) 
    # longest_streak = 0

    # for num in num_set:
    #     # Check if it's the start of a sequence
    #     if num - 1 not in num_set:
    #         current_num = num
    #         current_streak = 1

    #         # Continue the sequence
    #         while current_num + 1 in num_set:
    #             current_num += 1
    #             current_streak += 1

    #         longest_streak = max(longest_streak, current_streak)

    # return longest_streak

