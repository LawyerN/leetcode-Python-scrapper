def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()  # Split the string into a list of words
    
    if len(pattern) != len(words):  # Check if the number of characters in the pattern and the number of words in the string are equal
        return False
    
    mapping = [-1] * 26  # Initialize an array of size 26 to store the mapping between characters and words
    for i in range(len(pattern)):
        char = ord(pattern[i]) - ord(\'a\')  # Convert the character to an integer index in the range 0-25
        word = words[i]
        
        if mapping[char] != -1:  # If the character is already in the mapping, check if it maps to the same word as before
            if mapping[char] != word:
                return False
        else:  # If the character is not in the mapping, check if the word is already mapped to a different character
            for j in range(26):
                if mapping[j] == word:
                    return False
            mapping[char] = word  # Add the mapping to the array
    
    return True  # If all checks pass, return True