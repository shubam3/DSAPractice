# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#      s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#      # Two-pointer approach to check for palindrome
#      left, right = 0, len(s) - 1
    
#      while left < right:
#         if s[left] != s[right]:
#          return False
#         left += 1
#         right -= 1
    
#      return True

# without using extra space o(1) and time o(n)
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():  # Skip non-alphanumeric left
            left += 1
        while left < right and not s[right].isalnum():  # Skip non-alphanumeric right
            right -= 1
        
        if s[left].lower() != s[right].lower():  # Compare lowercase characters
            return False
        
        left += 1
        right -= 1  # Move both pointers

    return True

# Example Test Cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))  # False
print(isPalindrome(" "))  # True
