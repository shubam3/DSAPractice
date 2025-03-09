class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #  return False  # Anagrams must have the same length

        # s_sorted, t_sorted = sorted(s), sorted(t)  # Sort both strings

        # left, right = 0, 0  # Two pointers

        # while left < len(s):  # Compare characters one by one
        #  if s_sorted[left] != t_sorted[right]:
        #     return False
        #  left += 1
        #  right += 1
  
        # return True  # If all characters match, it's an anagram  

        # return sorted(s)== sorted(t)
        
        if len(s) != len(t):
         return False  # Anagrams must have the same length
    
        freq = [0] * 26  # Array to track letter frequencies (26 lowercase letters)

        for i in range(len(s)):
         freq[ord(s[i]) - ord('a')] += 1  # Increment for `s`
         freq[ord(t[i]) - ord('a')] -= 1  # Decrement for `t`

        return all(f == 0 for f in freq)  # If all counts are zero, it's an anagram