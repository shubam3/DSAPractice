# Time: For each pair you may sort both words ⇒ worst-case
# O(n^2 · k log k) (n = #words, k = word length).
# Space: O(n) for visited (ignoring sort buffers).


def groupAnagrams(words):
    # Step 1: Get the number of words
    n = len(words)

    # Step 2: Create a 'visited' list to track grouped words
    visited = [False] * n  # Initially, all words are unvisited

    # Step 3: This will hold the final groups of anagrams
    result = []

    # Step 4: Loop through each word to form groups
    for i in range(n):
        if not visited[i]:
            # Step 4a: Start a new group with the current word
            group = [words[i]]
            visited[i] = True  # Mark it as grouped

            # Step 4b: Compare with all remaining unvisited words
            for j in range(i + 1, n):
                # Step 4c: If they are anagrams, group them
                if not visited[j] and sorted(words[i]) == sorted(words[j]):
                    group.append(words[j])
                    visited[j] = True  # Mark this word as grouped

            # Step 4d: Add the completed group to the result
            result.append(group)

    # Step 5: Return all anagram groups
    return result