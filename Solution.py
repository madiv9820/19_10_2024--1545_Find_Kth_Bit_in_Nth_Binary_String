class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Start with the initial string for n=1
        current_String = '0'
        
        # Generate the string for each n from 1 to n
        for _ in range(n):
            # Create the inverted version of the current string, reversed and toggled
            inverted_String = ''.join('1' if ch == '0' else '0' for ch in current_String[::-1])
            # Form the new string by concatenating current, '1', and inverted
            new_String = current_String + '1' + inverted_String
            # Update current_String for the next iteration
            current_String = new_String

        # Return the k-th character (1-indexed) from the final string
        return current_String[k - 1]

# Time Complexity: O(2^n), since the length of the string doubles with each iteration.
# Space Complexity: O(2^n), due to the storage of the strings which grow exponentially.