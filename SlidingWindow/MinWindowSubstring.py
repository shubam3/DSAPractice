# ⏱ Time Complexity:
# O(n² * m) — n for substring generation, m for checking character counts

# 🧠 Space Complexity:
# O(n + m) — for frequency counters


from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)              # Count of characters in t
    min_len = float('inf')            # To track minimum window length
    min_window = ""

    for i in range(len(s)):           # Start index of window
        window_count = Counter()
        for j in range(i, len(s)):    # End index of window
            window_count[s[j]] += 1

            # Check if current window has all required characters
            if all(window_count[char] >= t_count[char] for char in t_count):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    min_window = s[i:j+1]
                break   # No need to expand this window further
    return min_window


# ⏱ Time Complexity:
# O(n + m)

# n = len(s), m = len(t)

# Each character is visited at most twice.

# 🧠 Space:
# O(n + m) — for dictionaries


from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)  # Frequency of required characters
    window_count = {}     # Frequency of characters in current window
    required = len(t_count)  # Total unique characters to match
    formed = 0               # How many characters currently match required freq

    left = 0
    min_len = float('inf')
    min_window = ""

    # Expand window by moving right
    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        # If current char meets required count
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        # Try shrinking window from left if valid
        while formed == required:
            # Update answer if this window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right+1]

            # Shrink the window
            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                formed -= 1  # We no longer satisfy this char
            left += 1  # Move left pointer

    return min_window


# Input:
# s = "OUZODYXAZV"
# t = "XYZ"

# t_count = {'X': 1, 'Y': 1, 'Z': 1} → we need all 3 characters

# Start sliding window:

# Expand right pointer until you collect X, Y, and Z in the window

# Once formed == required (3), start moving left to shrink

# Track the smallest window

# 🔍 At window s[5:8] = "YXAZ" → it contains X, Y, Z

# Try shrinking → can’t remove any without losing required char

# It’s valid and length = 4 → ✅ update answer

# No shorter valid substring exists → ✅ final answer: "YXAZ"