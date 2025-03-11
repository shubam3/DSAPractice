class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      pairs = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets

      for char in s:
        if char in pairs:  # If it's a closing bracket
            if not stack or stack.pop() != pairs[char]:  
                return False  # Stack is empty or brackets don't match
        else:
            stack.append(char)  # Push opening brackets

      return not stack  # Return True if stack is empty (all brackets matched)