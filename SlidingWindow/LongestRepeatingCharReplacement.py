# We want the length of the longest substring where we can replace at most k = 2 characters to make all characters the same.

# 🔑 Main Idea:
# Use a sliding window [left, right]

# Track character counts in the current window

# Keep track of max_count, the count of the most frequent character in the window

# If (window_size - max_count) > k, shrink the window from the left





def characterReplacement(s, k):
    # n = len(s)
    # max_len = 0

    # for i in range(n):
    #     count = [0] * 26  # For A-Z
    #     max_count = 0

    #     for j in range(i, n):
    #         count[ord(s[j]) - ord('A')] += 1
    #         max_count = max(max_count, count[ord(s[j]) - ord('A')])

    #         window_len = j - i + 1
    #         if window_len - max_count <= k:
    #             max_len = max(max_len, window_len)

    # return max_len
    
    
    
    from collections import defaultdict

    count = defaultdict(int)
    left = 0
    max_count = 0
    max_len = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])

        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len