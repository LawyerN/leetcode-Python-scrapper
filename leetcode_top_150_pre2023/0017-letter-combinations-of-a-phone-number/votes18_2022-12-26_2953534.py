class Solution:
    def letterCombinations(self, n: str) -> List[str]:
        # Return an empty list if n is an empty string
        if n==\'\':
            return []
        
        # List of options for each digit on the keypad
        options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        # Initialize queue with an empty string
        queue = [""]
        
        # Loop over each digit in n
        for digit in n:
            # Convert digit to integer
            digit = int(digit)            
            # Loop over the length of queue
            for _ in range(len(queue)):
                # Remove the first element in queue and store it in curr
                curr = queue.pop(0)
                # Append the concatenation of curr and each character in the set of characters corresponding to digit in options to queue
                for letter in options[digit]:
                    queue.append(curr + letter)
        
        # Return the list of combinations stored in queue
        return queue