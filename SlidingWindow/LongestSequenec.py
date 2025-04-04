def lengthOfLongestSubstring(s):
    # max_len = 0
    # n = len(s)
    
    # for i in range(n):  # Start of substring
    #  seen = set()    # To store unique characters
    #  for j in range(i, n):  # End of substring
    #     if s[j] in seen:   # Repeating character? Stop this substring
    #         break
    #     seen.add(s[j])     # Add to set if not seen
    #     max_len = max(max_len, j - i + 1)  # Update max length

    # return max_len    


# Use a sliding window with two pointers (left and right).
#  Use a set to track unique characters in the current window. 
#  Move right to expand the window, and move left when duplicates are found.


    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
