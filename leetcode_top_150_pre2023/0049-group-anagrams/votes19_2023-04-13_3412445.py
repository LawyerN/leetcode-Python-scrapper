class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to act as hashmap
        res = {}
        for word in strs:
            # We want to retain the original word to add to the dictionary
            # Therefore, create a temporary variable with the sorted word
            temp = \'\'.join(sorted(word))
            # If the sorted word exists in the dictionary, 
            # append to the values list
            if temp in res:
                res[temp].append(word)
            # Else, add a new key-value pair to the dictionary
            else:
                res[temp] = [word]
        # We only require the values list to be returned
        return res.values()