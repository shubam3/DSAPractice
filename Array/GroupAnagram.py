def group_anagrams_brute_force(strs):

    anagram_map = {}  # sorted words as keys and lists of anagrams as values

    for word in strs:
        sorted_word = ''.join(sorted(word))  # Sort letters to create a key
        
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []  # Initialize list if key is not present
        
        anagram_map[sorted_word].append(word)  # Append word to the group

    return list(anagram_map.values())  # Convert dictionary values to a list

    result = []  # Stores grouped anagrams
    visited = [False] * len(strs)  # Track visited words

    for i in range(len(strs)):
        if visited[i]:  # Skip if already grouped
            continue
        
        group = [strs[i]]  # Start a new group
        visited[i] = True

        for j in range(i + 1, len(strs)):  # Compare with every other word
            if sorted(strs[i]) == sorted(strs[j]):  # Check if anagram
                group.append(strs[j])
                visited[j] = True  # Mark as grouped

        result.append(group)  # Add the group to final result

    return result    #n2 logn