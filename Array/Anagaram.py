class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
         return False  # Anagrams must have the same length

        s_sorted, t_sorted = sorted(s), sorted(t)  # Sort both strings

        left, right = 0, 0  # Two pointers

        while left < len(s):  # Compare characters one by one
         if s_sorted[left] != t_sorted[right]:
            return False
         left += 1
         right += 1

        return True  # If all characters match, it's an anagram  
