# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

class EncodeAndDecodeString:

    # def encode(self, strs: List[str]) -> str:
    #     if not strs:  # Check if the list is empty
    #         return chr(258)  # Using a non-ASCII character to denote an empty list
    #     return '|'.join(strs)  # Joining list elements with '|' as a delimiter

    # def decode(self, s: str) -> List[str]:
    #     if s == chr(258):  # Check if the encoded string represents an empty list
    #         return []
    #     return s.split('|')  # Splitting the string back into a list using '|' as the delimiter
    
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = i
            # Find the separator
            while s[j] != '#':
                j += 1
            # Get the length of the next string
            length = int(s[i:j])
            # Move j past the '#' character
            j += 1
            # Extract the string of the given length
            decoded_strings.append(s[j:j+length])
            # Move to the next string's length segment
            i = j + length
        return decoded_strings
